#!/usr/bin/env python

# 
# Script for autocalibration of the reflex SF hand
# 

__author__ = 'Hoang Nguyen'
__maintainer__ = 'WPI MQP Yale Open Hand team'
__email__ = 'nphoang1102@gmail.com'


import rospy

from reflex_msgs.msg import Command
from reflex_msgs.msg import PoseCommand
from reflex_msgs.msg import VelocityCommand
from reflex_msgs.msg import Hand

# Class for Reflex SF hand autocalibration
class AutoCalibrate(object):

    # Initialize class method
    def __init__(self):

        # Print out something to the terminal
        print("Initializing autocalibration node for Reflex SF")

        # First thing first, this needs a node name
        rospy.init_node('SFautoCalibration')

        # Overload tracking dictionary
        self.motorsdata = None

        # Fetching user config params from .yaml file
        self.threshold = {
            0: rospy.get_param("reflex_sf_f1/overload_threshold"),
            1: rospy.get_param("reflex_sf_f2/overload_threshold"),
            2: rospy.get_param("reflex_sf_f3/overload_threshold"),
            3: rospy.get_param("reflex_sf_preshape/overload_threshold")
        }

        # Calibration motor angle
        self.zero_angles = {
            0: None,
            1: None,
            2: None,
            3: None
        }

        # Dictionary for storing velocity command
        self.vel_command = {
            0: VelocityCommand(f1 = 2.0, f2 = 0.0, f3 = 0.0, preshape = 0.0),
            1: VelocityCommand(f1 = 0.0, f2 = 2.0, f3 = 0.0, preshape = 0.0),
            2: VelocityCommand(f1 = 0.0, f2 = 0.0, f3 = 2.0, preshape = 0.0),
            3: VelocityCommand(f1 = 0.0, f2 = 0.0, f3 = 0.0, preshape = 2.0)
        }

        # Subscribe to the hand_state topic and update the load reading
        rospy.Subscriber('/reflex_sf/hand_state', Hand, self._loadupdate_cb)

        # Initialize all of the topics to publish to
        self.command_pub = rospy.Publisher('/reflex_sf/command', Command, queue_size=1)
        self.pos_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
        self.vel_pub = rospy.Publisher('/reflex_sf/command_velocity', VelocityCommand, queue_size=1)

        # Wait for updated motor value
        while(self.motorsdata == None):
            pass

        # Motor value updated, start autocalibration process
        print("Initializing complete, start auto calibration process")
        self._auto_calib()

    # Callback for updating the load on each motors
    def _loadupdate_cb(self, data):
        self.motorsdata = data.motor

    # Autocalibration process here
    def _auto_calib(self):
        # Start closing the fingers to find overload angles
        for finger in range(0,3):
            self._find_loadpont(finger)
            print("Finger", finger, "overload position recorded. Moving on")
            rospy.sleep(0.5)

        # Open back the fingers
        self.vel_pub.publish(VelocityCommand(f1 = -2.0, f2 = -2.0, f3 = -2.0, preshape = 0.0))
        print("Recorded overload position", self.zero_angles)

    # Helper function to drive the finger to overload point and record
    def _find_loadpont(self, finger):

        # Close the finger
        self.vel_pub.publish(self.vel_command[finger])

        # Waiting for hand to reach overload position
        while (self.motorsdata[finger].load < self.threshold[finger]):
            pass

        # Overload threshold reached, stop moving and take reading
        self.vel_pub.publish(VelocityCommand(f1 = 0.0, f2 = 0.0, f3 = 0.0, preshape = 0.0))
        self.zero_angles[finger] = self.motorsdata[finger].raw_angle



# Our main process here
def main():
    calibration_process = AutoCalibrate()
    rospy.spin()



    
# Run the calibration process in main
if __name__ == '__main__':
    main()