# Implementation on the ATV hardware

The current branch focuses on the simulation of an ATV that can be controlled either by a PS4 controller or keyboard inputs. The code is divided into 3 layers:
- Inner layer: composed of the ATV model dynamics and mechanics.
- Mid-layer: composed of the "action_control_unit" package that translates the custom "movement" messages to "ackermann_drive" messages used in the inner layer.
- Outer layer: made of different types of input (currently only PS4 controller and keyboard inputs, but other forms of control can be added).

ROS version: Melodic
dev_ws: "ATV_ws"

Current packages: 
- action_control_unit -> translates the custom "movement" messages to "ackermann_drive" messages
- ATV_control -> for actuator implementation, needed for wheel steering and spinning
- atv_description -> dedicated to ATV models and representation
- atv_gazebo -> dedicated to different worlds and gazebo/rviz representation
- teleop_key -> command ATV from keyboard input
- teleop_joy -> command ATV from joystick input

--------------

### Nodes and topics graph

![rqt_graph](full_sim_graph.png)

The image, generated using `rqt_graph`, shows the active nodes and topics: the `/teleop_key` node sends the keyboard inputs through the `/command_move` topic to the `/custom_to_ackermann` node that translates the custom `/movement` message into the more common `/ackermann_drive` message. From this point onwards, the structure is the same as the atv_playground branch.

In the background, `joint_state_publisher` and `robot_state_publisher` are always publishing through `/tf`, allowing visualization in RViz.

(This is the simple version without any additional sensors and using the keyboard teleoperation. You can have the actual graph at your current state by running `rqt_graph` at any point in a new terminal while the simulation is running.)

--------------

### Launch command

```sh
cd autonomous_ATV/ATV_ws
catkin_make
source devel/setup.bash # Remember to source the environment in every command window
```

### Spawn the ATV in a specific world:

launch empty world with ATV in the origin:
  ```sh
roslaunch ATV_description launch_ATV.launch
  ```
launch agribot world with ATV in it:
  ```sh
roslaunch ATV_gazebo agriculture_world.launch
  ```

### Connect a teleoperation device:

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
