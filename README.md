# autonomous ATV
## atv_onboard branch
These are the folders and files currently installed on the ATV's Raspberry Pi.
With the current layout all these folders must be in the home directory.
This means that once the repo has been cloned all the folders must be placed in the home directory.
In the future this should be changed in order to have some automation 
(
  for example:
- changing the paths in the startup execution app on the Raspberry 
- reorganizing the ROS ws, because now every folder is ws. In my opinion tt would be better to have them as packages in a unique ws
).
