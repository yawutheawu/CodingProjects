@ECHO OFF
:: Loops through all folders in a folder full of git repos and pulls latest updates
TITLE Repo Updater
ECHO Updating All repos through git pull

for /D %%i in (*) do (
    ECHO in folder %%i
    cd "%%i"
    git pull
    cd ..
)
ECHO Done
TIMEOUT 2