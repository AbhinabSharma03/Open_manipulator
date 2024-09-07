4#! /usr/bin/env python3

# This code exapnds on the code single_movement.py to include 4 movements,
# it will move from home, pick and place. There is a 5 second delay to stop 
# code skipping ahead to the next section until movement has been completed

import rospy
import sys
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest

rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_joint_space_path')
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition) #allows the script to call the service and and send requests to it
goal_joint_space_path_request_object = SetJointPositionRequest()

# 1st Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['gripper','joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0028429778416951498,1.497165322303772,-0.05522330850362778,0.3067961633205414, 1.2701361179351807]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 1...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(5)

# 2nd Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['gripper', 'joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0028429778416951498, 1.497165322303772, -0.4448544383049011, 0.28685441613197327, 1.2302526235580444]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 2...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(5)

# 3rd Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['gripper' 'joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0028327512741088867, -0.07669904083013535, 0.023009711876511574, 0.30833014845848083, 0.9203885197639465]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 3...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(5)

# 4th Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['gripper' 'joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [-0.005593916575113932, -0.04141748324036598, 0.01840776950120926, 0.25003886222839355, 0.9602720141410828]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 4...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print (result)
rospy.sleep(5)
