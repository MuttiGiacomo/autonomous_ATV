#!/bin/bash
sleep 5s
mate-terminal -- bash /home/atv-remote/movements/start_up/roscore.sh
sleep 10s
mate-terminal -- bash /home/atv-remote/movements/start_up/i2c_fifo.sh
sleep 5s
mate-terminal -- bash /home/atv-remote/movements/start_up/screen.sh
sleep 5s
mate-terminal -- bash /home/atv-remote/movements/start_up/direction.sh
sleep 5s
mate-terminal -- bash /home/atv-remote/movements/start_up/speed.sh
sleep 5s
mate-terminal -- bash /home/atv-remote/movements/start_up/api_move.sh

