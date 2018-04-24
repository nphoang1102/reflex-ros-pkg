import rospy
from python_qt_binding.QtWidgets import * #QWidget, QToolTip,QPushButton,QLabel,QGridLayout,QLineEdit
from python_qt_binding.QtGui import * #QFont,QPalette, QColor

from std_msgs.msg import String
from reflex_msgs.msg import PoseCommand
from std_srvs.srv import Empty
from rqt_service.srv import SendTwoInt
class MyWidgetCali(QWidget):
    
    def __init__(self):
        super(MyWidgetCali, self).__init__()
        #self.command_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
        #rospy.init_node('listener', anonymous=True)

        self.initUI()
        
    def initUI(self):

################## Position Control GUI ########################################################################
#         #Finger 1 row
#         self.finger_label_1 = QLabel("Goal for f1")
#         #finger_slider_1 = QLineEdit()
#         self.finger_slider_1 = QSlider(1)
#         self.finger_slider_1.setMinimum(0)
#         self.finger_slider_1.setMaximum(400)
#         self.finger_slider_1.setValue(200)
#         self.value_slider_1 = QLabel("2.00")
#         self.hbox_f1 = QHBoxLayout()
#         self.hbox_f1.addWidget(self.finger_slider_1)
#         self.hbox_f1.addWidget(self.value_slider_1)

#         #Finger 2 row
#         self.finger_label_2 = QLabel("Goal for f2")
#         #finger_slider_2 = QLineEdit()
#         self.finger_slider_2 = QSlider(1)
#         self.finger_slider_2.setMinimum(0)
#         self.finger_slider_2.setMaximum(400)
#         self.finger_slider_2.setValue(300)

#         self.value_slider_2 = QLabel("3.00")
#         self.hbox_f2 = QHBoxLayout()
#         self.hbox_f2.addWidget(self.finger_slider_2)
#         self.hbox_f2.addWidget(self.value_slider_2)
#         #add1 = QLineEdit()
#         #add2 = QLineEdit()

#         #Finger 3 row
#         self.finger_label_3 = QLabel("Goal for f3")
#         #finger_slider_3 = QLineEdit()
#         self.finger_slider_3 = QSlider(1)
#         self.finger_slider_3.setMinimum(0)
#         self.finger_slider_3.setMaximum(400)
#         self.finger_slider_3.setValue(100)

#         self.value_slider_3 = QLabel("1.00")
#         self.hbox_f3 = QHBoxLayout()
#         self.hbox_f3.addWidget(self.finger_slider_3)
#         self.hbox_f3.addWidget(self.value_slider_3)

#         #Finger 4
#         self.finger_label_4 = QLabel("Goal for f_preshape")
#         #finger_slider_4 = QLineEdit()
#         self.finger_slider_4 = QSlider(1)
#         self.finger_slider_4.setMinimum(0)
#         self.finger_slider_4.setMaximum(400)
#         self.finger_slider_4.setValue(0)

#         self.value_slider_4 = QLabel("0.00")
#         self.hbox_f4 = QHBoxLayout()
#         self.hbox_f4.addWidget(self.finger_slider_4)
#         self.hbox_f4.addWidget(self.value_slider_4)

# ###########################################################################################################
#         # Testing
#         # Box Layout for grouping vertical or horizontal
#         # vbox = QVBoxLayout()

#         # vbox.addWidget(add1)
#         # vbox.addWidget(add2)
#         # fbox.addRow(l2,vbox)
# ########## Coupling Row ###################################################################################
#         #Tick line row, choosing coupling motor
#         self.coupling_label = QLabel("Coupling")
#         self.hbox_tick = QHBoxLayout()

#         self.tick_f1 = QCheckBox("F1")
#         self.tick_f2 = QCheckBox("F2")
#         self.tick_f3 = QCheckBox("F3")
#         self.tick_f4 = QCheckBox("Preshape")
        
#         self.hbox_tick.addWidget(self.tick_f1)
#         self.hbox_tick.addWidget(self.tick_f2)
#         self.hbox_tick.addWidget(self.tick_f3)
#         self.hbox_tick.addWidget(self.tick_f4)
#         self.hbox_tick.addStretch()


# ########### Command Row Button ############################################################################
#         # Command row
#         self.command_label = QLabel("Command")
#         self.go_button = QPushButton("Go Go Go !!!")
#         self.home_button = QPushButton("Go Home boys !!!")
#         self.re_button = QPushButton("Reset Goal")

#         self.hbox_command = QHBoxLayout()
#         self.hbox_command.addWidget(self.go_button)
#         self.hbox_command.addWidget(self.home_button)
#         self.hbox_command.addWidget(self.re_button)
########### Calibrate section ############################################################################
        # Calibrate f1 row
        self.cali_f1_label = QLabel("Calibrate f1")
        self.cali_f1_tight_button = QPushButton("Tightening f1")
        self.cali_f1_loosen_button = QPushButton("Loosensing f1")
        self.hbox_cali_f1 = QHBoxLayout()
        self.hbox_cali_f1.addWidget(self.cali_f1_tight_button)
        self.hbox_cali_f1.addWidget(self.cali_f1_loosen_button)

        # Calibrate f2 row
        self.cali_f2_label = QLabel("Calibrate f2")
        self.cali_f2_tight_button = QPushButton("Tightening f2")
        self.cali_f2_loosen_button = QPushButton("Loosensing f2")
        self.hbox_cali_f2 = QHBoxLayout()
        self.hbox_cali_f2.addWidget(self.cali_f2_tight_button)
        self.hbox_cali_f2.addWidget(self.cali_f2_loosen_button)

        # Calibrate f3 row
        self.cali_f3_label = QLabel("Calibrate f3")
        self.cali_f3_tight_button = QPushButton("Tightening f3")
        self.cali_f3_loosen_button = QPushButton("Loosensing f3")
        self.hbox_cali_f3 = QHBoxLayout()
        self.hbox_cali_f3.addWidget(self.cali_f3_tight_button)
        self.hbox_cali_f3.addWidget(self.cali_f3_loosen_button)

        # Calibrate preshape row
        self.cali_f4_label = QLabel("Calibrate preshape")
        self.cali_f4_tight_button = QPushButton("Tightening preshape")
        self.cali_f4_loosen_button = QPushButton("Loosensing preshape")
        self.hbox_cali_f4 = QHBoxLayout()
        self.hbox_cali_f4.addWidget(self.cali_f4_tight_button)
        self.hbox_cali_f4.addWidget(self.cali_f4_loosen_button)

        # Auto Calibration
        self.cali_f5_label = QLabel("Auto-Calibration")
        self.cali_f5_button = QPushButton("Auto-Calibration")
##########################################################################################################
        # self.listPose = []
        # pose0 = PoseCommand(f1=0.0,f2=0.0,f3=0.0,preshape=0.0)
        # self.listPose.append(pose0)
        # #Test List view
        # self.listWidget = QListWidget()
        
        # item = QListWidgetItem("Pos('%2.2f','%2.2f','%2.2f','%2.2f')" % (pose0.f1,pose0.f2,pose0.f3,pose0.preshape))
        # self.listWidget.addItem(item)

        # self.listlabel = QLabel("List waypoint")

        # #List Control
        # self.list_control_label = QLabel("Waypoint Control")
        # self.list_control_save_button = QPushButton("Save")
        # self.list_control_delete_button = QPushButton("Remove")
        # self.list_control_go_button = QPushButton("Go waypoints")
        # self.list_control = QHBoxLayout()
        # self.list_control.addWidget(self.list_control_save_button)
        # self.list_control.addWidget(self.list_control_delete_button)
        # self.list_control.addWidget(self.list_control_go_button)
############ Adding rows and set up singal for button ####################################################
        #QFormLayout similar to HBox but you know it look like form, add everything to FormLayout
        self.fbox = QFormLayout()
        # self.fbox.addRow(self.finger_label_1,self.hbox_f1)
        # self.fbox.addRow(self.finger_label_2,self.hbox_f2)
        # self.fbox.addRow(self.finger_label_3,self.hbox_f3)
        # self.fbox.addRow(self.finger_label_4,self.hbox_f4)
        # self.fbox.addRow(self.coupling_label,self.hbox_tick)
        # self.fbox.addRow(self.command_label,self.hbox_command)
        self.fbox.addRow(self.cali_f1_label,self.hbox_cali_f1)
        self.fbox.addRow(self.cali_f2_label,self.hbox_cali_f2)
        self.fbox.addRow(self.cali_f3_label,self.hbox_cali_f3)
        self.fbox.addRow(self.cali_f4_label,self.hbox_cali_f4)
        self.fbox.addRow(self.cali_f5_label,self.cali_f5_button)
        # self.fbox.addRow(self.listlabel,self.listWidget)
        # self.fbox.addRow(self.list_control_label,self.list_control)

        # # Connect singal when slider change to function respectively to change value of label
        # self.finger_slider_1.valueChanged.connect(self.valuechange1)
        # self.finger_slider_2.valueChanged.connect(self.valuechange2)
        # self.finger_slider_3.valueChanged.connect(self.valuechange3)
        # self.finger_slider_4.valueChanged.connect(self.valuechange4)
        
        # # Add connect signal to Button Go, Cancel and Reset
        # self.go_button.clicked.connect(self.handleButtonGo)
        # self.home_button.clicked.connect(self.handleButtonHome)
        # self.re_button.clicked.connect(self.handleButtonReset)

        # Add connect signal to f1 tight and loosen button
        self.cali_f1_tight_button.clicked.connect(self.handle_cali_f1_tight)
        self.cali_f1_loosen_button.clicked.connect(self.handle_cali_f1_loosen)

        # Add connect signal to f1 tight and loosen button
        self.cali_f2_tight_button.clicked.connect(self.handle_cali_f2_tight)
        self.cali_f2_loosen_button.clicked.connect(self.handle_cali_f2_loosen)

        # Add connect signal to f1 tight and loosen button
        self.cali_f3_tight_button.clicked.connect(self.handle_cali_f3_tight)
        self.cali_f3_loosen_button.clicked.connect(self.handle_cali_f3_loosen)

        # Add connect signal to f1 tight and loosen button
        self.cali_f4_tight_button.clicked.connect(self.handle_cali_f4_tight)
        self.cali_f4_loosen_button.clicked.connect(self.handle_cali_f4_loosen)

        self.cali_f5_button.clicked.connect(self.handle_cali_f5)

        # self.list_control_save_button.clicked.connect(self.handle_list_control_save_button)
        # self.list_control_delete_button.clicked.connect(self.handle_list_control_delete_button)
        # self.list_control_go_button.clicked.connect(self.handle_list_control_go_button)

######### Set up window ###################################################################################
        #Set the widget to layout and show the widget
        self.setLayout(self.fbox)
   
        self.setWindowTitle("Test QT Layout")
        self.resize(640,480)
        self.dumbnum = 0
        self.show()

########## Tighten and Loosen Button Function for all four motor ##########################################
######## These handler function does not let me have any other input !!!!!!!!!!!! so i cant change 
######## a, b when calling the function, so I have to make each handler for each button, need some refine
########## Tighten and Loosen for f1 ######################################################################    
    def handle_cali_f1_tight(self):
        rospy.wait_for_service('/send_two_int')
        a = 1 # 1 is motor f1
        b = 0 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def handle_cali_f1_loosen(self):
        rospy.wait_for_service('/send_two_int')
        a = 1 # 1 is motor f1
        b = 1 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
########## Tighten and Loosen for f2 ######################################################################
    def handle_cali_f2_tight(self):
        rospy.wait_for_service('/send_two_int')
        a = 2 # 1 is motor f1
        b = 0 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def handle_cali_f2_loosen(self):
        rospy.wait_for_service('/send_two_int')
        a = 2 # 1 is motor f1
        b = 1 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

########## Tighten and Loosen for f3 ######################################################################
    def handle_cali_f3_tight(self):
        rospy.wait_for_service('/send_two_int')
        a = 3 # 1 is motor f1
        b = 0 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def handle_cali_f3_loosen(self):
        rospy.wait_for_service('/send_two_int')
        a = 3 # 1 is motor f1
        b = 1 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

########## Tighten and Loosen for f4 ######################################################################
    def handle_cali_f4_tight(self):
        rospy.wait_for_service('/send_two_int')
        a = 4 # 1 is motor f1
        b = 0 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def handle_cali_f4_loosen(self):
        rospy.wait_for_service('/send_two_int')
        a = 4 # 1 is motor f1
        b = 1 # 0 is tight, 1 is loosen
        try:
            send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
            resp1 = send_two_int(a, b)
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
#############################################################################################################
    def handle_cali_f5(self):
        try:
            auto_calibrate = rospy.ServiceProxy('/reflex_sf/auto_calibrate', Empty)
            resp1 = auto_calibrate()
            print resp1
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
#     def handle_list_control_save_button(self):
#         float_value_1 = float(self.finger_slider_1.value())/100.0
#         float_value_2 = float(self.finger_slider_2.value())/100.0
#         float_value_3 = float(self.finger_slider_3.value())/100.0
#         float_value_4 = float(self.finger_slider_4.value())/100.0
#         pose0 = PoseCommand(f1=float_value_1,f2=float_value_2,f3=float_value_3,preshape=float_value_4)
#         self.listPose.append(pose0)

#         item = QListWidgetItem("Pos('%2.2f','%2.2f','%2.2f','%2.2f')" % (pose0.f1, pose0.f2, pose0.f3, pose0.preshape))
#         self.listWidget.addItem(item)

#     def handle_list_control_delete_button(self):
#         print "remove button click"
#         #print self.listWidget.currentRow()
#         dummy = self.listPose.pop(self.listWidget.currentRow())
#         #print dummy.f1
#         dummyItem = self.listWidget.takeItem(self.listWidget.currentRow())


#     def handle_list_control_go_button(self):
#         print "go waypoints click"

#         for pose in self.listPose:
#             print "Go to Pos('%2.2f','%2.2f','%2.2f','%2.2f')" % (pose.f1, pose.f2, pose.f3, pose.preshape)
#             self.command_pub.publish(pose)
#             rospy.sleep(2.)

# ######### valuechange for updating goal label ###############################################################
#     def valuechange1(self):
#         self.dumbnum = self.dumbnum + 1;
#         float_value = float(self.finger_slider_1.value())/100.0
#         self.value_slider_1.setText("%2.2f" % float_value)
#         #print "test time" + str(self.dumbnum)

#     def valuechange2(self):
#         float_value = float(self.finger_slider_2.value())/100.0
#         self.value_slider_2.setText("%2.2f" % float_value)
        
#     def valuechange3(self):
#         float_value = float(self.finger_slider_3.value())/100.0
#         self.value_slider_3.setText("%2.2f" % float_value)

#     def valuechange4(self):
#         float_value = float(self.finger_slider_4.value())/100.0
#         self.value_slider_4.setText("%2.2f" % float_value)

# #############################################################################################################


# ######### Command Button handler ############################################################################
#     def handleButtonGo(self):
#         tar_f1 = float(self.finger_slider_1.value())/100.0
#         tar_f2 = float(self.finger_slider_2.value())/100.0
#         tar_f3 = float(self.finger_slider_3.value())/100.0
#         tar_f4 = float(self.finger_slider_4.value())/100.0
#         poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,preshape=tar_f4)
#         self.command_pub.publish(poseTarget)
#         print "Go Button Click"

#     def handleButtonHome(self):
#         poseTarget = PoseCommand(f1=0.0,f2=0.0,f3=0.0,preshape=0.0)
#         self.command_pub.publish(poseTarget)
#         print "Home Button Click"

#     def handleButtonReset(self):
#         self.finger_slider_1.setValue(0)
#         self.value_slider_1.setText("0.00")
#         self.finger_slider_2.setValue(0)
#         self.value_slider_2.setText("0.00")
#         self.finger_slider_3.setValue(0)
#         self.value_slider_3.setText("0.00")
#         self.finger_slider_4.setValue(0)
#         self.value_slider_4.setText("0.00")
#         print "Reset Button Click"