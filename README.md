# implementation on the ATV hardware

The current branch focusses on the simulation of an ATV that can be controlled either by a PS4 controller or keyboard inouts.
The code is devided in 3 layers:
- inner layer: composed of the ATV model dinamics and mechanics
- mid-layer: composed of the "action_control_unit" package that translates the custom "movement" messages to "ackermann_drive" messages, used in the inner layer
- outer layer: made of different types of input (currently only PS4 controller and keyboard inputs, but other form of control can be added)


ROS version: Melodic 
dev_ws: "ATV_ws"

current packages:
- action_control_unit -> translates the custom "movement" messages to "ackermann_drive" messages
- ATV_control -> for actuator implementation, needed for wheel steering and spinning
- ATV_description -> dedicated to ATV models and representation
- ATV_gazebo -> dedicated to different worlds and gazebo/rviz representation
- teleop_key -> command ATV from keyboard input
- teleop_joy -> command ATV from joystick input


build and source of the enviroment
  ```sh
cd autonomous_ATV/ATV_ws
catkin_make
source devel/setup.bash #remember to source the enviroment in every cmd window
  ```
LOAD A WORLD AND ATV:

launch empty world with ATV in the origin:
  ```sh
roslaunch ATV_description launch_ATV.launch
  ```
launch agribot world with ATV in it:
  ```sh
roslaunch ATV_gazebo agriculture_world.launch
  ```

LOAD A TELEOP DEVICE:

teleoperating with keyboard:
```sh
launch ATV_control teleop_key.launch 
#launch ATV_control teleop_key_sim_only.launch  if you want to control emergency stop and stepper motor signals
  ```
teleoperating with PS4 controller:
```sh
rosrun ATV_control teleop_joy.launch
#rosrun ATV_control teleop_joy_sim_only.launch if you want to control emergency stop and stepper motor signals
  ```
