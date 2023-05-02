#!/bin/bash
sleep 10s
mate-terminal -- bash /home/autonomous_ATV/movements/startup_scripts/main.sh
sleep 25s
mate-terminal -- bash /home/autonomous_ATV/startup_scripts/remote.sh 
sleep 5s
mate-terminal -- bash /home/autonomous_ATV/startup_scripts/emergency.sh 
sleep 2s
mate-terminal -- bash /home/autonomous_ATV/startup_scripts/wireless_remote.sh 
