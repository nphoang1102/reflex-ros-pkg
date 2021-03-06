import rospy
from python_qt_binding.QtWidgets import * #QWidget, QToolTip,QPushButton,QLabel,QGridLayout,QLineEdit
from python_qt_binding.QtGui import * #QFont,QPalette, QColor

from std_msgs.msg import String
from std_msgs.msg import Int16MultiArray

from reflex_msgs.msg import PoseCommand
from rqt_service.srv import SendTwoInt
from reflex_msgs.msg import Hand

class MyWidgetWC(QWidget):
    
    def __init__(self):
        super(MyWidgetWC, self).__init__()
        self.command_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
        self.command_pub_sim = rospy.Publisher('/reflex_sf/hand_state', Hand, queue_size=1)
        # Constantly capture the current hand state
        rospy.Subscriber('/reflex_sf/hand_state', Hand, self.hand_state_cb)
        rospy.Subscriber('/chatter',Int16MultiArray, self.received_int)
        #rospy.init_node('listener', anonymous=True)

        self.initUI()
        
    def initUI(self):

################## Position Control GUI ########################################################################
        #Finger 1 row
        self.finger_label_1 = QLabel("Goal for f1")
        #finger_slider_1 = QLineEdit()
        self.finger_slider_1 = QSlider(1)
        self.finger_slider_1.setMinimum(0)
        self.finger_slider_1.setMaximum(400)
        self.finger_slider_1.setValue(200)
        self.value_slider_1 = QTextEdit("2.00")
        self.value_slider_1.setMaximumSize(80,20)
        self.hbox_f1 = QHBoxLayout()
        self.hbox_f1.addWidget(self.finger_slider_1)
        self.hbox_f1.addWidget(self.value_slider_1)

        #Finger 2 row
        self.finger_label_2 = QLabel("Goal for f2")
        #finger_slider_2 = QLineEdit()
        self.finger_slider_2 = QSlider(1)
        self.finger_slider_2.setMinimum(0)
        self.finger_slider_2.setMaximum(400)
        self.finger_slider_2.setValue(300)

        self.value_slider_2 = QTextEdit("3.00")
        self.value_slider_2.setMaximumSize(80,20)
        self.hbox_f2 = QHBoxLayout()
        self.hbox_f2.addWidget(self.finger_slider_2)
        self.hbox_f2.addWidget(self.value_slider_2)
        #add1 = QLineEdit()
        #add2 = QLineEdit()

        #Finger 3 row
        self.finger_label_3 = QLabel("Goal for f3")
        #finger_slider_3 = QLineEdit()
        self.finger_slider_3 = QSlider(1)
        self.finger_slider_3.setMinimum(0)
        self.finger_slider_3.setMaximum(400)
        self.finger_slider_3.setValue(100)

        self.value_slider_3 = QTextEdit("1.00")
        self.value_slider_3.setMaximumSize(80,20)
        self.hbox_f3 = QHBoxLayout()
        self.hbox_f3.addWidget(self.finger_slider_3)
        self.hbox_f3.addWidget(self.value_slider_3)

        #Preshape k1
        self.finger_label_4 = QLabel("Goal for f_preshape k1")
        #finger_slider_4 = QLineEdit()
        self.finger_slider_4 = QSlider(1)
        self.finger_slider_4.setMinimum(0)
        self.finger_slider_4.setMaximum(400)
        self.finger_slider_4.setValue(0)

        self.value_slider_4 = QTextEdit("0.00")
        self.value_slider_4.setMaximumSize(80,20)
        self.hbox_f4 = QHBoxLayout()
        self.hbox_f4.addWidget(self.finger_slider_4)
        self.hbox_f4.addWidget(self.value_slider_4)

        #Preshape k2
        self.finger_label_5 = QLabel("Goal for f_preshape")
        #finger_slider_4 = QLineEdit()
        self.finger_slider_5 = QSlider(1)
        self.finger_slider_5.setMinimum(0)
        self.finger_slider_5.setMaximum(400)
        self.finger_slider_5.setValue(0)

        self.value_slider_5 = QTextEdit("0.00")
        self.value_slider_5.setMaximumSize(80,20)
        self.hbox_f5 = QHBoxLayout()
        self.hbox_f5.addWidget(self.finger_slider_5)
        self.hbox_f5.addWidget(self.value_slider_5)

###########################################################################################################
        # Testing
        # Box Layout for grouping vertical or horizontal
        # vbox = QVBoxLayout()

        # vbox.addWidget(add1)
        # vbox.addWidget(add2)
        # fbox.addRow(l2,vbox)
########## Coupling Row ###################################################################################
        #Tick line row, choosing coupling motor
        self.coupling_label = QLabel("Coupling")
        self.hbox_tick = QHBoxLayout()

        self.tick_f1 = QCheckBox("F1")
        self.tick_f2 = QCheckBox("F2")
        self.tick_f3 = QCheckBox("F3")
        self.tick_f4 = QCheckBox("Preshape")
        
        self.hbox_tick.addWidget(self.tick_f1)
        self.hbox_tick.addWidget(self.tick_f2)
        self.hbox_tick.addWidget(self.tick_f3)
        self.hbox_tick.addWidget(self.tick_f4)
        self.hbox_tick.addStretch()

        self.tick_f1_state = 0
        self.tick_f2_state = 0
        self.tick_f3_state = 0
        self.tick_f4_state = 0
        self.tick_f1.stateChanged.connect(lambda:self.tickchange(self.tick_f1))
        self.tick_f2.stateChanged.connect(lambda:self.tickchange(self.tick_f2))
        self.tick_f3.stateChanged.connect(lambda:self.tickchange(self.tick_f3))
        self.tick_f4.stateChanged.connect(lambda:self.tickchange(self.tick_f4))

########### Command Row Button ############################################################################
        # Command row
        self.command_label = QLabel("Command")
        self.go_button = QPushButton("Go Go Go !!!")
        self.home_button = QPushButton("Go Home boys !!!")
        self.re_button = QPushButton("Reset Goal")

        self.hbox_command = QHBoxLayout()
        self.hbox_command.addWidget(self.go_button)
        self.hbox_command.addWidget(self.home_button)
        self.hbox_command.addWidget(self.re_button)
########### Combo section ############################################################################
        self.combo_label = QLabel("Targeted Device")
        self.combo = QComboBox(self)
        self.combo.addItem("ReflexSF")
        self.combo.addItem("MQP Hand")
        self.combo.addItem("Rviz/Gazebo Simulation")
############ Glove Section #############################################################################
        self.glove_label = QLabel("Glove Interface")


        self.tick_glove = QCheckBox("ON/OFF")
        self.tick_glove_state = 0
        self.tick_glove.stateChanged.connect(lambda:self.tickchange(self.tick_glove))

        self.value_glove_1 = QLabel("x")
        self.value_glove_1.setMaximumSize(80,20)

        self.value_glove_2 = QLabel("x")
        self.value_glove_2.setMaximumSize(80,20)

        self.value_glove_3 = QLabel("x")
        self.value_glove_3.setMaximumSize(80,20)

        self.hbox_glove = QHBoxLayout()
        self.hbox_glove.addWidget(self.tick_glove)
        self.hbox_glove.addWidget(self.value_glove_1)
        self.hbox_glove.addWidget(self.value_glove_2)
        self.hbox_glove.addWidget(self.value_glove_3)
        
########### Calibrate section ############################################################################
        # # Calibrate f1 row
        # self.cali_f1_label = QLabel("Calibrate f1")
        # self.cali_f1_tight_button = QPushButton("Tightening f1")
        # self.cali_f1_loosen_button = QPushButton("Loosensing f1")
        # self.hbox_cali_f1 = QHBoxLayout()
        # self.hbox_cali_f1.addWidget(self.cali_f1_tight_button)
        # self.hbox_cali_f1.addWidget(self.cali_f1_loosen_button)

        # # Calibrate f2 row
        # self.cali_f2_label = QLabel("Calibrate f2")
        # self.cali_f2_tight_button = QPushButton("Tightening f2")
        # self.cali_f2_loosen_button = QPushButton("Loosensing f2")
        # self.hbox_cali_f2 = QHBoxLayout()
        # self.hbox_cali_f2.addWidget(self.cali_f2_tight_button)
        # self.hbox_cali_f2.addWidget(self.cali_f2_loosen_button)

        # # Calibrate f3 row
        # self.cali_f3_label = QLabel("Calibrate f3")
        # self.cali_f3_tight_button = QPushButton("Tightening f3")
        # self.cali_f3_loosen_button = QPushButton("Loosensing f3")
        # self.hbox_cali_f3 = QHBoxLayout()
        # self.hbox_cali_f3.addWidget(self.cali_f3_tight_button)
        # self.hbox_cali_f3.addWidget(self.cali_f3_loosen_button)

        # # Calibrate preshape row
        # self.cali_f4_label = QLabel("Calibrate preshape")
        # self.cali_f4_tight_button = QPushButton("Tightening preshape")
        # self.cali_f4_loosen_button = QPushButton("Loosensing preshape")
        # self.hbox_cali_f4 = QHBoxLayout()
        # self.hbox_cali_f4.addWidget(self.cali_f4_tight_button)
        # self.hbox_cali_f4.addWidget(self.cali_f4_loosen_button)
##########################################################################################################
        self.listPose = []
        pose0 = PoseCommand(f1=0.0,f2=0.0,f3=0.0,k1=0.0,k2=0.0)
        self.listPose.append(pose0)
        #Test List view
        self.listWidget = QListWidget()
        
        item = QListWidgetItem("Pos(  '%2.2f'  ,  '%2.2f'  ,  '%2.2f'  ,  '%2.2f',  '%2.2f'  )" % (pose0.f1,pose0.f2,pose0.f3,pose0.k1,pose0.k2))
        self.listWidget.addItem(item)

        self.listlabel = QLabel("List waypoint")

        #List Control
        self.list_control_label = QLabel("Waypoint Control")
        self.list_control_save_button = QPushButton("Save")
        self.list_control_delete_button = QPushButton("Remove")
        self.list_control_go_button = QPushButton("Go waypoints")
        self.list_control = QHBoxLayout()
        self.list_control.addWidget(self.list_control_save_button)
        self.list_control.addWidget(self.list_control_delete_button)
        self.list_control.addWidget(self.list_control_go_button)
############ Adding rows and set up singal for button ####################################################
        #QFormLayout similar to HBox but you know it look like form, add everything to FormLayout
        self.fbox = QFormLayout()
        self.fbox.addRow(self.finger_label_1,self.hbox_f1)
        self.fbox.addRow(self.finger_label_2,self.hbox_f2)
        self.fbox.addRow(self.finger_label_3,self.hbox_f3)
        self.fbox.addRow(self.finger_label_4,self.hbox_f4)
        self.fbox.addRow(self.finger_label_5,self.hbox_f5)
        self.fbox.addRow(self.coupling_label,self.hbox_tick)
        self.fbox.addRow(self.command_label,self.hbox_command)
        # self.fbox.addRow(self.cali_f1_label,self.hbox_cali_f1)
        # self.fbox.addRow(self.cali_f2_label,self.hbox_cali_f2)
        # self.fbox.addRow(self.cali_f3_label,self.hbox_cali_f3)
        # self.fbox.addRow(self.cali_f4_label,self.hbox_cali_f4)
        self.fbox.addRow(self.listlabel,self.listWidget)
        self.fbox.addRow(self.list_control_label,self.list_control)
        self.fbox.addRow(self.combo_label,self.combo)
        self.fbox.addRow(self.glove_label,self.hbox_glove)

        # Connect singal when slider change to function respectively to change value of label
        self.finger_slider_1.valueChanged.connect(self.valuechange1)
        self.finger_slider_2.valueChanged.connect(self.valuechange2)
        self.finger_slider_3.valueChanged.connect(self.valuechange3)
        self.finger_slider_4.valueChanged.connect(self.valuechange4)
        self.finger_slider_5.valueChanged.connect(self.valuechange5)
        # Add connect signal to Button Go, Cancel and Reset
        self.go_button.clicked.connect(self.handleButtonGo)
        self.home_button.clicked.connect(self.handleButtonHome)
        self.re_button.clicked.connect(self.handleButtonReset)

        # Add connect signal to f1 tight and loosen button
        # self.cali_f1_tight_button.clicked.connect(self.handle_cali_f1_tight)
        # self.cali_f1_loosen_button.clicked.connect(self.handle_cali_f1_loosen)

        # # Add connect signal to f1 tight and loosen button
        # self.cali_f2_tight_button.clicked.connect(self.handle_cali_f2_tight)
        # self.cali_f2_loosen_button.clicked.connect(self.handle_cali_f2_loosen)

        # # Add connect signal to f1 tight and loosen button
        # self.cali_f3_tight_button.clicked.connect(self.handle_cali_f3_tight)
        # self.cali_f3_loosen_button.clicked.connect(self.handle_cali_f3_loosen)

        # # Add connect signal to f1 tight and loosen button
        # self.cali_f4_tight_button.clicked.connect(self.handle_cali_f4_tight)
        # self.cali_f4_loosen_button.clicked.connect(self.handle_cali_f4_loosen)

        self.list_control_save_button.clicked.connect(self.handle_list_control_save_button)
        self.list_control_delete_button.clicked.connect(self.handle_list_control_delete_button)
        self.list_control_go_button.clicked.connect(self.handle_list_control_go_button)

######### Set up window ###################################################################################
        #Set the widget to layout and show the widget
        self.setLayout(self.fbox)
   
        self.setWindowTitle("Test QT Layout")
        self.resize(640,480)
        self.dumbnum = 0
        self.show()
        self.current_angle = [0.0,0.0,0.0,0.0]
########## Tighten and Loosen Button Function for all four motor ##########################################
######## These handler function does not let me have any other input !!!!!!!!!!!! so i cant change 
######## a, b when calling the function, so I have to make each handler for each button, need some refine
########## Tighten and Loosen for f1 ######################################################################    
#     def handle_cali_f1_tight(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 1 # 1 is motor f1
#         b = 0 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

#     def handle_cali_f1_loosen(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 1 # 1 is motor f1
#         b = 1 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e
# ########## Tighten and Loosen for f2 ######################################################################
#     def handle_cali_f2_tight(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 2 # 1 is motor f1
#         b = 0 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

#     def handle_cali_f2_loosen(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 2 # 1 is motor f1
#         b = 1 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

# ########## Tighten and Loosen for f3 ######################################################################
#     def handle_cali_f3_tight(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 3 # 1 is motor f1
#         b = 0 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

#     def handle_cali_f3_loosen(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 3 # 1 is motor f1
#         b = 1 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

# ########## Tighten and Loosen for f4 ######################################################################
#     def handle_cali_f4_tight(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 4 # 1 is motor f1
#         b = 0 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e

#     def handle_cali_f4_loosen(self):
#         rospy.wait_for_service('/send_two_int')
#         a = 4 # 1 is motor f1
#         b = 1 # 0 is tight, 1 is loosen
#         try:
#             send_two_int = rospy.ServiceProxy('/send_two_int', SendTwoInt)
#             resp1 = send_two_int(a, b)
#             print resp1
#         except rospy.ServiceException, e:
#             print "Service call failed: %s"%e
#############################################################################################################
    def handle_list_control_save_button(self):
        float_value_1 = float(self.value_slider_1.toPlainText())
        float_value_2 = float(self.value_slider_2.toPlainText())
        float_value_3 = float(self.value_slider_3.toPlainText())
        float_value_4 = float(self.value_slider_4.toPlainText())
        float_value_5 = float(self.value_slider_5.toPlainText())
        pose0 = PoseCommand(f1=float_value_1,f2=float_value_2,f3=float_value_3,k1=float_value_4,k2=float_value_5)
        self.listPose.append(pose0)

        item = QListWidgetItem("Pos(  '%2.2f'  ,  '%2.2f'  ,  '%2.2f'  ,  '%2.2f',  '%2.2f'  )" % (pose0.f1, pose0.f2, pose0.f3, pose0.k1, pose0.k2))
        self.listWidget.addItem(item)

    def handle_list_control_delete_button(self):
        print "remove button click"
        #print self.listWidget.currentRow()
        dummy = self.listPose.pop(self.listWidget.currentRow())
        #print dummy.f1
        dummyItem = self.listWidget.takeItem(self.listWidget.currentRow())


    def handle_list_control_go_button(self):
        scaled_float_1 = 1.0
        scaled_float_2 = 1.0
        scaled_float_3 = 1.0
        

        if (self.tick_glove_state == 1):
            # Scale raw value into readable value
            #print(scaled_float_1)
            self.value_glove_1.setText("%2.2f" % scaled_float_1)
            self.value_glove_2.setText("%2.2f" % scaled_float_2)
            self.value_glove_3.setText("%2.2f" % scaled_float_3)
            data = str(scaled_float_1) + ";" +str(scaled_float_2) + ";" + str(scaled_float_3) + "\n"  
            filename = "data/grasp1.txt"
            file = open(filename, "a")
            file.write(data)
            file.close()
            #rospy.sleep(2.)
######### tickchange for updating tick ###############################################################

######### valuechange for updating goal label ###############################################################
    def valuechange1(self):
        #self.dumbnum = self.dumbnum + 1;
        float_value = float(self.finger_slider_1.value())/100.0
        self.value_slider_1.setText("%2.2f" % float_value)
        if self.tick_f1_state:
            if self.tick_f2_state:
                self.value_slider_2.setText("%2.2f" % float_value)
                self.finger_slider_2.setValue(self.finger_slider_1.value())
            if self.tick_f3_state:
                self.value_slider_3.setText("%2.2f" % float_value)
                self.finger_slider_3.setValue(self.finger_slider_1.value())
            if self.tick_f4_state:
                self.value_slider_4.setText("%2.2f" % float_value)
                self.finger_slider_4.setValue(self.finger_slider_1.value())

        #print "test time" + str(self.dumbnum)

    def valuechange2(self):
        float_value = float(self.finger_slider_2.value())/100.0
        self.value_slider_2.setText("%2.2f" % float_value)
        
    def valuechange3(self):
        float_value = float(self.finger_slider_3.value())/100.0
        self.value_slider_3.setText("%2.2f" % float_value)

    def valuechange4(self):
        float_value = float(self.finger_slider_4.value())/100.0
        self.value_slider_4.setText("%2.2f" % float_value)

    def valuechange5(self):
        float_value = float(self.finger_slider_5.value())/100.0 - 2.0
        self.value_slider_5.setText("%2.2f" % float_value)

#############################################################################################################
    def tickchange(self,b):
        if b.text() == "F1":
            if b.isChecked() == True:
                self.tick_f1_state = 1
            else:
                self.tick_f1_state = 0
        if b.text() == "F2":
            if b.isChecked() == True:
                self.tick_f2_state = 1
            else:
                self.tick_f2_state = 0
        if b.text() == "F3":
            if b.isChecked() == True:
                self.tick_f3_state = 1
            else:
                self.tick_f3_state = 0
        if b.text() == "Preshape":
            if b.isChecked() == True:
                self.tick_f4_state = 1
            else:
                self.tick_f4_state = 0
        if b.text() == "ON/OFF":
            if b.isChecked() == True:
                self.tick_glove_state = 1
            else:
                self.tick_glove_state = 0 
                self.value_glove_1.setText("x")
                self.value_glove_2.setText("x")
                self.value_glove_3.setText("x")
        #print(self.tick_f1_state)

######### Command Button handler ############################################################################
    def handleButtonGo(self):
        # tar_f1 = float(self.finger_slider_1.value())/100.0
        # tar_f2 = float(self.finger_slider_2.value())/100.0
        # tar_f3 = float(self.finger_slider_3.value())/100.0
        # tar_f4 = float(self.finger_slider_4.value())/100.0
        # poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,preshape=tar_f4)
        # self.command_pub.publish(poseTarget)
        # print "Go Button Click"
        if self.combo.currentText() == "Rviz/Gazebo Simulation":
            tar_f1 = float(self.value_slider_1.toPlainText())
            tar_f2 = float(self.value_slider_2.toPlainText())
            tar_f3 = float(self.value_slider_3.toPlainText())
            tar_f4 = float(self.value_slider_4.toPlainText())
             
            print "Go Button Click Simluation"
            print(tar_f1,tar_f2,tar_f3,tar_f4)
            hand = Hand()
            hand.motor[0].joint_angle = tar_f1
            hand.motor[1].joint_angle = tar_f2
            hand.motor[2].joint_angle = tar_f3
            hand.motor[3].joint_angle = tar_f4
            self.command_pub_sim.publish(hand)
        elif (self.combo.currentText() == "MQP Hand"):
                tar_f1 = float(self.value_slider_1.toPlainText())
                tar_f2 = float(self.value_slider_2.toPlainText())
                tar_f3 = float(self.value_slider_3.toPlainText())
                tar_f4 = float(self.value_slider_4.toPlainText())
                tar_f5 = float(self.value_slider_5.toPlainText())
                #print "Go Button Click with target"
                #print(tar_f1,tar_f2,tar_f3,tar_f4)
                poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,k1=tar_f4,k2=tar_f5)
                self.command_pub.publish(poseTarget)


        else:
            tar_f1 = float(self.value_slider_1.toPlainText())
            tar_f2 = float(self.value_slider_2.toPlainText())
            tar_f3 = float(self.value_slider_3.toPlainText())
            tar_f4 = float(self.value_slider_4.toPlainText())
            print "Go Button Click with target"
            print(tar_f1,tar_f2,tar_f3,tar_f4)
            poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,preshape=tar_f4)
            self.command_pub.publish(poseTarget)
            #print "Go Button Click"

    def handleButtonHome(self):
        poseTarget = PoseCommand(f1=0.0,f2=0.0,f3=0.0,k1=0.0,k2=0.0)
        self.command_pub.publish(poseTarget)
        print "Home Button Click"

    def handleButtonReset(self):
        self.finger_slider_1.setValue(0)
        self.value_slider_1.setText("0.00")
        self.finger_slider_2.setValue(0)
        self.value_slider_2.setText("0.00")
        self.finger_slider_3.setValue(0)
        self.value_slider_3.setText("0.00")
        self.finger_slider_4.setValue(0)
        self.value_slider_4.setText("0.00")
        print "Reset Button Click"
    ## Update Value of the hand for checking for waypoint
    def hand_state_cb(self, hand):
        self.current_angle[0] = hand.motor[0].joint_angle
        self.current_angle[1] = hand.motor[1].joint_angle
        self.current_angle[2] = hand.motor[2].joint_angle
        self.current_angle[3] = hand.motor[3].joint_angle

    # Receive messages from 
    def received_int(self, value_received):
        scaled_float_1 = 2.0-(float(value_received.data[0])-450.0)/100.0
        scaled_float_2 = 2.0-(float(value_received.data[1])-500.0)/80.0  
        scaled_float_3 = 2.0 - (float(value_received.data[2])-440)/80.0  
        

        if (self.tick_glove_state == 1):
            # Scale raw value into readable value
            #print(scaled_float_1)
            self.value_glove_1.setText("%2.2f" % scaled_float_1)
            self.value_glove_2.setText("%2.2f" % scaled_float_2)
            self.value_glove_3.setText("%2.2f" % scaled_float_3)
            data = str(scaled_float_1) + ";" +str(scaled_float_2) + ";" + str(scaled_float_3) + "\n"  
            filename = "data/grasp1.txt"
            file = open(filename, "a")
            file.write(data)
            file.close()
            # Based on the Combo box decided what to do with the value
            if (self.combo.currentText() == "Rviz/Gazebo Simulation"):
                #print(scaled_float_1)
                tar_f1 = scaled_float_2
                tar_f2 = scaled_float_2
                tar_f3 = scaled_float_1
                tar_f4 = scaled_float_3
                #print "Go Button Click Simluation"
                #print(tar_f1,tar_f2,tar_f3,tar_f4)
                hand = Hand()
                hand.motor[0].joint_angle = tar_f1
                hand.motor[1].joint_angle = tar_f2
                hand.motor[2].joint_angle = tar_f3
                hand.motor[3].joint_angle = tar_f4
                self.command_pub_sim.publish(hand)
            elif (self.combo.currentText() == "MQP Hand"):
                tar_f1 = scaled_float_3
                tar_f2 = scaled_float_2
                tar_f3 = scaled_float_1
                tar_f4 = float(self.value_slider_4.toPlainText())
                tar_f5 = float(self.value_slider_5.toPlainText())
                #print "Go Button Click with target"
                #print(tar_f1,tar_f2,tar_f3,tar_f4)
                poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,k1=tar_f4,k2=tar_f5)
                self.command_pub.publish(poseTarget)
            else: 
                tar_f1 = scaled_float_2
                tar_f2 = scaled_float_3
                tar_f3 = scaled_float_1
                tar_f4 = float(self.value_slider_4.toPlainText())
                #print "Go Button Click with target"
                #print(tar_f1,tar_f2,tar_f3,tar_f4)
                poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,preshape=tar_f4)
                self.command_pub.publish(poseTarget)
                



