#! /usr/bin/env python
import rospy
from reflex_sf_hand import ReflexSFHand
import sys

if __name__ == '__main__':    

    if len(sys.argv) <= 1:
        print "USAGE: rosrun reflex_sf calibrate.py NAME"
        exit(0)
    
    rospy.sleep(4.0)  # To allow services and parameters to load
    hand = ReflexSFHand(sys.argv[1])
    rospy.on_shutdown(hand.disable_torque)
    hand.gui_auto_calibrate()