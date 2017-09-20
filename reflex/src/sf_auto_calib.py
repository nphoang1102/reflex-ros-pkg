# 
# Script for autocalibration of the reflex SF hand
# 

__author__ = 'Hoang Nguyen'
__maintainer__ = 'Hoang Nguyen'
__email__ = 'nphoang1102@gmail.com'


from math import pi, cos

import rospy
from std_srvs.srv import Empty

from reflex_msgs.msg import Command
from reflex_msgs.msg import PoseCommand
from reflex_msgs.msg import VelocityCommand
# from reflex_msgs.msg import ForceCommand
from reflex_msgs.msg import Hand

# Class for Reflex SF hand autocalibration
class AutoCalibrate(object):

    # Initialize class method
    def __init__(self):

        # First thing first, this needs a node name
        rospy.init_node('SFautoCalibration')

        # Overload tracking dictionary
        self.motors = {
            0 : None, # Finger 1
            1 : None, # Finger 2
            2 : None, # Finger 3
            3 : None # Preshape
        }

        # Start with not updated load value on motors
        self.load_updated = False

        # Fetching user config params from .yaml file
        self.threshold = {
            0: rospy.get_param("reflex_sf_f1/overload_threshold")
            1: rospy.get_param("reflex_sf_f2/overload_threshold")
            2: rospy.get_param("reflex_sf_f3/overload_threshold")
            3: rospy.get_param("reflex_sf_f4/overload_threshold")
        }

        # Subscribe to the hand_state topic and update the load reading
        rospy.Subscriber('/reflex_sf/hand_state', Hand, self._loadupdate_cb)

        # Initialize all of the topics to publish to
        self.command_pub = rospy.Publisher('/reflex_sf/command', Command, queue_size=1)
        self.pos_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
        self.vel_pub = rospy.Publisher('/reflex_sf/command_velocity', VelocityCommand, queue_size=1)

        # Wait for updated motor value then start autocalibration process
        while(not self.load_updated):    
        self._auto_calib()

    # Callback for updating the load on each motors
    def _loadupdate_cb(data):
        self.motors[0] = data.motor[0].load
        self.motors[1] = data.motor[1].load
        self.motors[2] = data.motor[2].load
        self.motors[3] = data.motor[3].load

        # Inform that we have updated the new load value for each motors
        if (not self.load_updated):
            self.load_updated = True

    # Autocalibration process here
    def _auto_calib():

# Run the calibration process in main
if __name__ == '__main__':
    calibration_process = AutoCalibrate()
    rospy.spin()