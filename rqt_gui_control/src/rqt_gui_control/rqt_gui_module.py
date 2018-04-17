import os
import rospy
import rospkg

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
from my_widget import MyWidgetWC
from my_widget_vel_pos import MyWidgetVelPos
from my_widget_vel import MyWidgetVel
from my_cali_widget import MyWidgetCali
from server_gui import ServerGui
from glove_gui import GloveWidget

import socket               # Import socket module

class MyPlugin(Plugin):

    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin Noob')

        # Process standalone plugin command-line arguments
        # from argparse import ArgumentParser
        # parser = ArgumentParser()
        # # Add argument(s) to the parser.
        # parser.add_argument("-q", "--quiet", action="store_true",
        #               dest="quiet",
        #               help="Put plugin in silent mode")
        # args, unknowns = parser.parse_known_args(context.argv())
        # if not args.quiet:
        #     print 'arguments: ', args
        #     print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = MyWidgetWC()
        self._widget.setObjectName('MyPosUI')
        # self._widget2 = MyWidgetVel()
        # self._widget2.setObjectName('MyVelUI')
        # self._widget3 = MyWidgetVelPos()
        # self._widget3.setObjectName('MyPosVelUI')
        self._widget4 = MyWidgetCali()
        self._widget4.setObjectName('MyCali')
        self._widget5 = GloveWidget()
        self._widget5.setObjectName('Glove Interface')

        # self._widget.setWindowTitle("Position Control")
        # self._widget2.setWindowTitle("Velocity Control")
        # self._widget3.setWindowTitle("Position and Velocity Control")
        # self._widget4.setWindowTitle('Calibration')
        self._widget5.setWindowTitle('Server')
        

        #self._widget.move(0,0)
        # Get path to UI file which should be in the "resource" folder of this package
        #ui_file = os.path.join(rospkg.RosPack().get_path('rqt_mypkg'), 'resource', 'MyPlugin.ui')
        # Extend the widget with all attributes and children from UI file
        #loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        
        #self._widget.setStyleSheet("background-color:red;");
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        

        # Second Tab for Controling slider and Button
        #self._widget2 = MyWidget()
        #self._widget2.setObjectName("MyNoobTest")
        #self._widget2.setWindowTitle("Simple2")
        #self._widget2.setStyleSheet("background-color:green;");
        # tell from pane to pane.
        
        #self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        #self._widget2.setWindowTitle(self._widget2.windowTitle() + (' (%d)' % context.serial_number()))

        # Add widget to the user interface
        
        context.add_widget(self._widget)
        # context.add_widget(self._widget2)
        # context.add_widget(self._widget3)
        context.add_widget(self._widget4)
        context.add_widget(self._widget5)

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog