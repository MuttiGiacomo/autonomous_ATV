# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/atv-remote/wireless_remote/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/atv-remote/wireless_remote/build

# Utility rule file for wireless_remote_controller_gencpp.

# Include the progress variables for this target.
include joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/progress.make

wireless_remote_controller_gencpp: joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/build.make

.PHONY : wireless_remote_controller_gencpp

# Rule to build all files generated by this target.
joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/build: wireless_remote_controller_gencpp

.PHONY : joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/build

joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/clean:
	cd /home/atv-remote/wireless_remote/build/joystick_drivers/wireless_remote_controller && $(CMAKE_COMMAND) -P CMakeFiles/wireless_remote_controller_gencpp.dir/cmake_clean.cmake
.PHONY : joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/clean

joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/depend:
	cd /home/atv-remote/wireless_remote/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/atv-remote/wireless_remote/src /home/atv-remote/wireless_remote/src/joystick_drivers/wireless_remote_controller /home/atv-remote/wireless_remote/build /home/atv-remote/wireless_remote/build/joystick_drivers/wireless_remote_controller /home/atv-remote/wireless_remote/build/joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : joystick_drivers/wireless_remote_controller/CMakeFiles/wireless_remote_controller_gencpp.dir/depend

