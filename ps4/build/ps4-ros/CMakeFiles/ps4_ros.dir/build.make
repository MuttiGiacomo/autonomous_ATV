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
CMAKE_SOURCE_DIR = /home/atv-remote/ps4/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/atv-remote/ps4/build

# Include any dependencies generated for this target.
include ps4-ros/CMakeFiles/ps4_ros.dir/depend.make

# Include the progress variables for this target.
include ps4-ros/CMakeFiles/ps4_ros.dir/progress.make

# Include the compile flags for this target's objects.
include ps4-ros/CMakeFiles/ps4_ros.dir/flags.make

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o: ps4-ros/CMakeFiles/ps4_ros.dir/flags.make
ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o: /home/atv-remote/ps4/src/ps4-ros/src/ps4_ros.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/atv-remote/ps4/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o"
	cd /home/atv-remote/ps4/build/ps4-ros && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o -c /home/atv-remote/ps4/src/ps4-ros/src/ps4_ros.cpp

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.i"
	cd /home/atv-remote/ps4/build/ps4-ros && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/atv-remote/ps4/src/ps4-ros/src/ps4_ros.cpp > CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.i

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.s"
	cd /home/atv-remote/ps4/build/ps4-ros && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/atv-remote/ps4/src/ps4-ros/src/ps4_ros.cpp -o CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.s

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.requires:

.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.requires

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.provides: ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.requires
	$(MAKE) -f ps4-ros/CMakeFiles/ps4_ros.dir/build.make ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.provides.build
.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.provides

ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.provides.build: ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o


# Object files for target ps4_ros
ps4_ros_OBJECTS = \
"CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o"

# External object files for target ps4_ros
ps4_ros_EXTERNAL_OBJECTS =

/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: ps4-ros/CMakeFiles/ps4_ros.dir/build.make
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/libroscpp.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_signals.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/librosconsole.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/liblog4cxx.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_regex.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/librostime.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /opt/ros/melodic/lib/libcpp_common.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_system.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_thread.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_chrono.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_date_time.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libboost_atomic.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libpthread.so
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: /usr/lib/arm-linux-gnueabihf/libconsole_bridge.so.0.4
/home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros: ps4-ros/CMakeFiles/ps4_ros.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/atv-remote/ps4/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros"
	cd /home/atv-remote/ps4/build/ps4-ros && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ps4_ros.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
ps4-ros/CMakeFiles/ps4_ros.dir/build: /home/atv-remote/ps4/devel/lib/ps4_ros/ps4_ros

.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/build

ps4-ros/CMakeFiles/ps4_ros.dir/requires: ps4-ros/CMakeFiles/ps4_ros.dir/src/ps4_ros.cpp.o.requires

.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/requires

ps4-ros/CMakeFiles/ps4_ros.dir/clean:
	cd /home/atv-remote/ps4/build/ps4-ros && $(CMAKE_COMMAND) -P CMakeFiles/ps4_ros.dir/cmake_clean.cmake
.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/clean

ps4-ros/CMakeFiles/ps4_ros.dir/depend:
	cd /home/atv-remote/ps4/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/atv-remote/ps4/src /home/atv-remote/ps4/src/ps4-ros /home/atv-remote/ps4/build /home/atv-remote/ps4/build/ps4-ros /home/atv-remote/ps4/build/ps4-ros/CMakeFiles/ps4_ros.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ps4-ros/CMakeFiles/ps4_ros.dir/depend

