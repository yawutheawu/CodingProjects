# powershell -ExecutionPolicy Bypass -File jiggler.ps1


# Imports
Add-Type -AssemblyName System.Windows.Forms
# P/Invoke for reliable key simulation (SendKeys can be flaky depending on focus)
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class KeyboardSim {
    [DllImport("user32.dll")]
    public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);
    public const int VK_NUMLOCK = 0x90;
    public const uint KEYEVENTF_KEYUP = 0x0002;

    public static void ToggleNumLock() {
        keybd_event(VK_NUMLOCK, 0x45, 0, UIntPtr.Zero);
        keybd_event(VK_NUMLOCK, 0x45, KEYEVENTF_KEYUP, UIntPtr.Zero);
    }
}
"@

# Globals 
$IntervalSeconds = 15
$ActionIntervalMax = 2
$ActionIntervalMin = 0.1
$DragMSMin = 50
$DragMSMax = 120
$MoveLarge = 100
$MoveSmall = -1 * $MoveLarge

# Live Vars
$expectedPos   = [System.Windows.Forms.Cursor]::Position
$lastMoveTime  = Get-Date
$paused        = $false
$nextActionTime = Get-Date

# Extract individual coordinates
$X = [System.Windows.Forms.Cursor]::Position.X
$Y = [System.Windows.Forms.Cursor]::Position.Y

# Print a clean string output
Write-Host "Mouse jiggler running. Press Ctrl+C to stop."
Write-Host "Pauses automatically if you move the mouse; resumes after IntervalSecondsMin - IntervalSecondsMax of inactivity."
Write-Output "Current Mouse Location -> X: $X , Y: $Y"


function Move-Smoothly {
    param(
        [System.Drawing.Point]$From,
        [System.Drawing.Point]$To,
        [int]$Steps = 20,
        [int]$DelayMs = 15
    )

    $StepPause = $DelayMs/$Steps

    for ($i = 1; $i -le $Steps; $i++) {
        $t = $i / [double]$Steps
        # Ease in/out (smoothstep) so it doesn't move at constant robotic speed
        $ease = $t * $t * (3 - 2 * $t)

        $x = [int]($From.X + ($To.X - $From.X) * $ease)
        $y = [int]($From.Y + ($To.Y - $From.Y) * $ease)

        $stepPos = New-Object System.Drawing.Point($x, $y)
        [System.Windows.Forms.Cursor]::Position = $stepPos

        Start-Sleep -Milliseconds $StepPause
    }
}


while ($true) {
    $X = [System.Windows.Forms.Cursor]::Position.X
    $Y = [System.Windows.Forms.Cursor]::Position.Y
    Write-Output "Current Mouse Location -> X: $X , Y: $Y"
    $currentPos = [System.Windows.Forms.Cursor]::Position

    # Did the mouse move since we last set/checked its position?
    if ($currentPos -ne $expectedPos) {
        $lastMoveTime = Get-Date
        $expectedPos  = $currentPos
        if (-not $paused) {
            $paused = $true
            Write-Host "$(Get-Date -Format 'HH:mm:ss') - User activity detected, pausing jiggler."
        }
    }

    if ($paused) {
        $idleSeconds = ((Get-Date) - $lastMoveTime).TotalSeconds
        if ($idleSeconds -ge $IntervalSeconds) {
            $paused = $false
            $nextActionTime = Get-Date  # act soon after resuming
            Write-Host "$(Get-Date -Format 'HH:mm:ss') - No movement for $IntervalSeconds, resuming jiggler."
        }
        Start-Sleep -Seconds 1
        continue
    }

    # Time to jiggle / toggle NumLock?
    if ((Get-Date) -ge $nextActionTime) {

        $start  = [System.Windows.Forms.Cursor]::Position
        $target = New-Object System.Drawing.Point(
                ($start.X + (Get-Random -Minimum $MoveSmall -Maximum $MoveLarge)),
                ($start.Y + (Get-Random -Minimum $MoveSmall -Maximum $MoveLarge))
        )
        Move-Smoothly -From $start -To $target -Steps (Get-Random -Minimum $DragMSMin -Maximum $DragMSMax) -DelayMs (Get-Random -Minimum $DragMSMin -Maximum $DragMSMax)
        $expectedPos = $target   # so we don't mistake our own move for user activity
        Write-Host "$(Get-Date -Format 'HH:mm:ss') - Jiggled mouse."

        [KeyboardSim]::ToggleNumLock()
        Start-Sleep -Milliseconds 300
        [KeyboardSim]::ToggleNumLock()
        Write-Host "$(Get-Date -Format 'HH:mm:ss') - Toggled NumLock."

        $nextActionTime = (Get-Date).AddSeconds((Get-Random -Minimum $ActionIntervalMin -Maximum $ActionIntervalMax))
    }

    Start-Sleep -Seconds 1
}