#!/bin/bash
sleep 10s
mate-terminal -- bash /home/atv-remote/movements/start_up/main.sh
sleep 25s
mate-terminal -- bash /home/atv-remote/start_up/remote.sh 
sleep 5s
mate-terminal -- bash /home/atv-remote/start_up/emergency.sh 
sleep 2s
mate-terminal -- bash /home/atv-remote/start_up/wireless_remote.sh 
