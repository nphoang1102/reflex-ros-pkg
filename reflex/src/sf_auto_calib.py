#!/usr/bin/env python


from math import pi, cos

import rospy
from std_srvs.srv import Empty

from reflex_msgs.msg import Command
from reflex_msgs.msg import PoseCommand
from reflex_msgs.msg import VelocityCommand
# from reflex_msgs.msg import ForceCommand
from reflex_msgs.msg import Hand


hand_state = Hand()

def main():

    rospy.init_node('SFautoCalibration')

    # This collection of publishers can be used to command the hand
    command_pub = rospy.Publisher('/reflex_sf/command', Command, queue_size=1)
    pos_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
    vel_pub = rospy.Publisher('/reflex_sf/command_velocity', VelocityCommand, queue_size=1)
    # force_pub = rospy.Publisher('/reflex_sf/command_motor_force', ForceCommand, queue_size=1)

    # Constantly capture the current hand state
    rospy.Subscriber('/reflex_sf/hand_state', Hand, hand_state_cb)

    # Demonstration of velocity control - variable closing speed
    raw_input("== When ready to open and close fingers with velocity control, hit [Enter]\n")
    for i in range(3):
        pos_pub.publish(PoseCommand(f1=i, f2=i, f3=i, preshape=0.0))
        rospy.sleep(2.0)
        setpoint = 5.0 - (i * 2.25)
        vel_pub.publish(VelocityCommand(f1=setpoint, f2=setpoint, f3=setpoint, preshape=0.0))
        rospy.sleep(7.0 - setpoint)
    raw_input("...\n")
    pos_pub.publish(PoseCommand())

def hand_state_cb(data):
    global hand_state
    hand_state = data
    # rospy.loginfo(hand_state.motor)

if __name__ == '__main__':
    main()