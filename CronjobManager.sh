#!/bin/sh

echo "Activating environment"
source /home/burneds/crontabGUI/bin/activate
# source /home/shinthantaun/crontabGUI/bin/activate

echo "Launching app.."
python3 /home/burneds/crontabGUI/src/app.py
# python3 /home/shinthantaun/crontabGUI/src/app.py

deactivate