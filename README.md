# Open_manipulator

OpenManipulator X Pick and Place Operation

You have two options: Either clone the entire open manipulator x into your pc using:

bash
> cd ~/catkin_ws/src
> git clone https://github.com/AbhinabSharma03/Open_manipulator.git
and start from 2nd part of step 3 i.e. giving execute permissions to the scripts

"or" follow this from point 1, if you want to DIY but need some assistance

This README provides instructions for setting up and running a pick-and-place operation with the OpenManipulator X hardware using ROS. Follow these steps to get everything set up correctly.
Prerequisites

Ensure you have ROS installed and properly configured. You should also have a catkin workspace set up. If not, please refer to the ROS installation guide.
Setup Instructions
1. Clone the OpenManipulator X Repository

First, clone the OpenManipulator X packages into your catkin workspace's src directory:

bash
> cd ~/catkin_ws/src
> git clone https://github.com/ROBOTIS-GIT/open_manipulator.git

This repository includes the necessary controller launch files, Gazebo launch files, robot URDF, and Xacro files.

2. Create a Python Scripts Package

Create a new package named scripts to keep your Python files, such as publishers, subscribers, and other utilities:

bash
> cd ~/catkin_ws/src
> catkin_create_pkg scripts rospy std_msgs

3. Add Python Scripts

Download the Python script files named newpp.py or p_p.py from this repository and place them in the scripts package. For example:

bash
> cd ~/catkin_ws/src/scripts
# Assuming you have the raw URL for the scripts
wget http://example.com/path/to/newpp.py
wget http://example.com/path/to/p_p.py

Make sure to give execute permissions to your scripts:

bash
> chmod +x newpp.py
> chmod +x p_p.py

4. Build Your Workspace

Navigate to your catkin workspace and build it to include the new package and scripts:

bash
> cd ~/catkin_ws
> catkin_make

5. Launch the Controller

Start the controller for the OpenManipulator X. This step initializes the robot and sets up the necessary nodes:

bash
> roslaunch open_manipulator_controller open_manipulator_controller.launch

6. Run the Python Script

Run the Python script you downloaded to perform the pick-and-place operation. For example:

bash
> rosrun scripts newpp.py
or
> rosrun scripts p_p.py

7. Adjust Joint Angles and Gripper Positions

Modify the joint angles and gripper open/close positions in your Python script according to your specific requirements. The script contains parameters for setting the joint positions and gripper actions.
Recommendation

Always test your code in Gazebo before running it on the actual hardware. This helps ensure that your code behaves as expected and prevents potential damage to the hardware.

For more detailed instructions or troubleshooting, refer to the OpenManipulator X documentation.
