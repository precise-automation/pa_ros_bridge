# pa_tcs_bridge
A bridge between the ROS world and a Precise Automation controller running TCS. Provides a simple pass-through for string commands and replies.

### Install
??
If no catkin workspace,
1. Create catkin workspace
   - `cd ~`
   - `mkdir my_workspace`
   - `cd my_workspace`
   - `catkin_make`
2. Navigate to src: `cd src` 
3. Clone project: `git clone .....`
4. Make
   - `cd ~/my_workspace.`
   - `catkin_make`

### Run
1. `source ./devel/setup.bash`
2. `roslaunch pa_tcs_bridge bridge.launch ip:="192.168.0.1" port:=10100`
