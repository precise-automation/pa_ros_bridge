# pa_tcs_bridge
A bridge between the ROS world and a Precise Automation controller running TCS. Provides a simple pass-through for string commands and replies.

### Install
Requires ROS.
If you already have a catkin workspace, skip to step 2.
1. Create catkin workspace
   - `cd ~`
   - `mkdir my_workspace`
   - `cd my_workspace`
   - `catkin_make`
2. Navigate to src: `cd src` 
3. Clone project: `git clone .....`
4. Make
   - `cd ~/my_workspace`
   - `catkin_make`

### Run
1. Setup TCS on the controller
2. `source ./devel/setup.bash`
3. `roslaunch pa_tcs_bridge bridge.launch ip:="192.168.0.1" port:=10100`
4. In a new terminal, `rosservice list` to verify the bridge is running
5. Send commands like so: `rosservice call /TCS/CommandService "wherej"`
