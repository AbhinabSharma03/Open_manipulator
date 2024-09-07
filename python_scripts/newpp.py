#! /usr/bin/env python3

import rospy
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest

# Initialize the node
rospy.init_node('pick_and_place_node')

# Wait for services to be available
rospy.wait_for_service('/goal_joint_space_path')
rospy.wait_for_service('/goal_tool_control')

# Create service clients for arm and gripper
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
goal_tool_control_service_client = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)

# Create request objects
arm_request = SetJointPositionRequest()
gripper_request = SetJointPositionRequest()

# 1. Move to "Pick" Position (above the object)
arm_request.planning_group = 'arm'
arm_request.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
# Example coordinates for "Pick" position (adjust as needed)
arm_request.joint_position.position = [1.497165322303772,-0.05522330850362778,0.3067961633205414, 1.2701361179351807] # Arm above the object
arm_request.joint_position.max_accelerations_scaling_factor = 1.0
arm_request.joint_position.max_velocity_scaling_factor = 1.0
arm_request.path_time = 2.0

rospy.loginfo("Moving to pick position...")
goal_joint_space_path_service_client(arm_request)
rospy.sleep(3) # Give time to move


# 3. Gripper - Close to grasp the object
gripper_request.planning_group = 'gripper'
gripper_request.joint_position.joint_name = ['gripper']
gripper_request.joint_position.position = [-0.01] # Close gripper
gripper_request.joint_position.max_accelerations_scaling_factor = 1.0
gripper_request.joint_position.max_velocity_scaling_factor = 1.0
gripper_request.path_time = 1.0

rospy.loginfo("Closing gripper to grasp object...")
goal_tool_control_service_client(gripper_request)
rospy.sleep(2)

# 2. Lower the arm slightly to "grasp" the object
arm_request.joint_position.position = [ 1.497165322303772, -0.4448544383049011, 0.28685441613197327, 1.2302526235580444] # Slightly lower to pick object
rospy.loginfo("Lowering arm to grasp object...")
goal_joint_space_path_service_client(arm_request)
rospy.sleep(2)


# 4. Lift the object (move the arm upwards)
arm_request.joint_position.position = [-0.07669904083013535, 0.023009711876511574, 0.30833014845848083, 0.9203885197639465] # Lift object after grasping
rospy.loginfo("Lifting the object...")
goal_joint_space_path_service_client(arm_request)
rospy.sleep(3)

# 5. Move to the "Place" position (above the drop location)
arm_request.joint_position.position = [-0.04141748324036598, 0.01840776950120926, 0.25003886222839355, 0.9602720141410828] # Move to place position
rospy.loginfo("Moving to place position...")
goal_joint_space_path_service_client(arm_request)
rospy.sleep(3)

# 7. Gripper - Open to release the object
gripper_request.joint_position.position = [0.01] # Open gripper to release object
rospy.loginfo("Opening gripper to release object...")
goal_tool_control_service_client(gripper_request)
rospy.sleep(2)

# 8. Retract the arm (back to "Home" position)
arm_request.joint_position.position = [0.0, -0.5, 0.3, 0.7] # Retract to home
rospy.loginfo("Retracting the arm to home position...")
goal_joint_space_path_service_client(arm_request)
rospy.sleep(3)
