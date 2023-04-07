# autonomous_ATV
Development of autonomous driving capabilities for an ATV, in collaboration with the department of Agricultural Science of the Helsinki University


Roadmap:

- enviroment setup (ros workspace + gazebo)  :white_check_mark: DONE
- URDF model of the atv (needed for a proper Gazebo/Rviz/ROS simulation)  :white_check_mark: DONE
- create a proper .launch file :white_check_mark: DONE
- anable moovement using scrips :white_check_mark: DONE
- definition of steering mechanism :white_check_mark: DONE
- driving ATV from keyboard :white_check_mark: DONE
- driving ATV from PS4 controller :white_check_mark: DONE
- creation of world :eight_pointed_black_star: DONE (but can be done better)
- connect Rviz and gazebo :eight_pointed_black_star: ONGOING
- sensor implementation in URDF :eight_pointed_black_star: ONGOING
- check for needed sensor plugins
- wrapper for sensors
- calman filter (sort of)




ROS version: Melodic 

dev_ws: "ATV_ws"

current packages:
- ATV_description -> for ATV model and world visualization
- ATV_control -> for actuator implementation
- ATV_gazebo -> for launching everything in a specific complex world 
- teleop_key -> command ATV from keyboard input
- teleop_joy -> command ATV from joystick input


launch command
  ```sh
cd autonomous_ATV/ATV_ws
catkin_make
source devel/setup.bash
  ```
LOAD A WORLD AND ATV:

launch empty world with ATV in the origin:
  ```sh
roslaunch ATV_description launch_ATV.launch
  ```
launch agribot world with ATV in it:
  ```sh
launch ATV_gazebo agribot_farm.launch
  ```

LOAD A TELEOP DEVICE:
teleoperating with keyboard:
```sh
launch ATV_control teleop_key.launch
  ```
teleoperating with PS4 controller:
```sh
rosrun ATV_control teleop_joy_ps4.launch
  ```
