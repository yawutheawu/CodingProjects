
extends CharacterBody3D
# Character movement constants
const SPEED = 5.0
const JUMP_VELOCITY = 4.5
# Track mouse capture state
var is_mouse_captured = false  # Set this to false by default
var lastMouse = 0
# Sensitivity for mouse movement
var sensitivity = 0.1

signal Jumped

'''
https://www.youtube.com/@Bonkahe/playlists
'''
func _ready():
	$"Camera Controller".rotation_degrees.y = rotation_degrees.y

# Physics process (Character movement)
func _physics_process(delta: float) -> void:
	# Add gravity if not on the floor
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump input
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY
		Jumped.emit()

	# Get input direction and handle movement
	var input_dir := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		rotation_degrees.x = $"Camera Controller".rotation_degrees.y
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()

	# Check every frame if mouse capture/release worked
	_capture_release_mouse_button()

# Mouse capture/release handling
func _capture_release_mouse_button():
	if Time.get_ticks_msec() > lastMouse + 100:
		if Input.is_action_just_pressed("mouse_middle") and is_mouse_captured == false:
			lastMouse = Time.get_ticks_msec()
			capture_mouse()
		elif Input.is_action_just_pressed("mouse_middle") and is_mouse_captured == true:
			lastMouse = Time.get_ticks_msec()
			release_mouse()

# Function to release mouse capture
func release_mouse():
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	is_mouse_captured = false
	print("Mouse Released: ", is_mouse_captured)

# Function to capture the mouse
func capture_mouse():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	is_mouse_captured = true
	print("Mouse Captured: ", is_mouse_captured)

# Mouse movement handling (Rotation)
func _mouse_movement(event: InputEvent) -> void:
	#https://www.youtube.com/watch?v=EP5AYllgHy8
	if event is InputEventMouseMotion and is_mouse_captured == true:
		rotate_y(deg_to_rad(-event.relative.x*sensitivity))  # Limit vertical rotation to avoid flipping
		$"Camera Controller".rotate_x(deg_to_rad(-event.relative.y*sensitivity))

# Function to process input events
func _input(event: InputEvent) -> void:
	# Also check for mouse capture/release
	_capture_release_mouse_button()
	# Call mouse movement handler
	_mouse_movement(event)
