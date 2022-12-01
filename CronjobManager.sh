#!/bin/sh

echo "Activating environment"
# Put your env file path here
source /home/shinthantaun/crontabGUI/bin/activate

echo "Launching app.."
# Put your source file path here
python3 /home/shinthantaun/crontabGUI/src/app.py

deactivate