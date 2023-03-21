# autonomous_ATV
Development of autonomous driving capabilities for an ATV, in collaboration with the department of Agricultural Science of the Helsinki University


Roadmap:

- enviroment setup (ros workspace + gazebo)  :white_check_mark: DONE
- URDF model of the atv (needed for a proper Gazebo/Rviz/ROS simulation)  :white_check_mark: DONE
- create a proper .launch file :white_check_mark: DONE
- anable moovement using scrips :white_check_mark: DONE
- definition of steering mechanism :white_check_mark: DONE
- driving ATV from script :white_check_mark: DONE
- creation of world :eight_pointed_black_star: ONGOING
- identification of the needed/existing sensors :eight_pointed_black_star: ONGOING
- start dealing with sensors and topics 
- check for needed sensor plugins
- wrapper for sensors
- calman filter (sort of)




ROS version: Melodic 

dev_ws: "ATV_ws"

current packages:
- ATV_description -> for ATV model and world visualization
- ATV_control -> for actuator implementation
- teleop_twist_keyboard -> command ATV from keyboard input
- teleop_twist_joy -> command ATV from joystick input


launch command
  ```sh
cd autonomous_ATV/ATV_ws
catkin_make
source devel/setup.bash
  ```
launch empty world with ATV in the origin:
  ```sh
roslaunch ATV_description launch_ATV.launch
  ```
launch Rviz and link_state_publisher:
  ```sh
launch ATV_description display_rviz.launch
  ```
