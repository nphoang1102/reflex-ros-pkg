import rospy
from python_qt_binding.QtWidgets import * #QWidget, QToolTip,QPushButton,QLabel,QGridLayout,QLineEdit
from python_qt_binding.QtGui import * #QFont,QPalette, QColor

from std_msgs.msg import String
from reflex_msgs.msg import PoseCommand
from rqt_service.srv import SendTwoInt
class MyWidgetWC(QWidget):
    
    def __init__(self):
        super(MyWidgetWC, self).__init__()
        self.command_pub = rospy.Publisher('/reflex_sf/command_position', PoseCommand, queue_size=1)
        #rospy.init_node('listener', anonymous=True)

        self.initUI()
        
    def initUI(self):
        #Finger 1 row
        self.finger_label_1 = QLabel("Goal for f1")
        #finger_slider_1 = QLineEdit()
        self.finger_slider_1 = QSlider(1)
        self.finger_slider_1.setMinimum(0)
        self.finger_slider_1.setMaximum(400)
        self.finger_slider_1.setValue(200)
        self.value_slider_1 = QLabel("2.00")
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

        self.value_slider_2 = QLabel("3.00")
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

        self.value_slider_3 = QLabel("1.00")
        self.hbox_f3 = QHBoxLayout()
        self.hbox_f3.addWidget(self.finger_slider_3)
        self.hbox_f3.addWidget(self.value_slider_3)

        #Finger 4
        self.finger_label_4 = QLabel("Goal for f_preshape")
        #finger_slider_4 = QLineEdit()
        self.finger_slider_4 = QSlider(1)
        self.finger_slider_4.setMinimum(0)
        self.finger_slider_4.setMaximum(400)
        self.finger_slider_4.setValue(0)

        self.value_slider_4 = QLabel("0.00")
        self.hbox_f4 = QHBoxLayout()
        self.hbox_f4.addWidget(self.finger_slider_4)
        self.hbox_f4.addWidget(self.value_slider_4)


        
        # Box Layout for grouping vertical or horizontal
        # vbox = QVBoxLayout()

        # vbox.addWidget(add1)
        # vbox.addWidget(add2)
        # fbox.addRow(l2,vbox)

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

        # Command row
        self.command_label = QLabel("Command")
        self.go_button = QPushButton("Go Go Go !!!")
        self.home_button = QPushButton("Go Home boys !!!")
        self.re_button = QPushButton("Reset Goal")

        self.hbox_command = QHBoxLayout()
        self.hbox_command.addWidget(self.go_button)
        self.hbox_command.addWidget(self.home_button)
        self.hbox_command.addWidget(self.re_button)

        # Calibrate row
        self.cali_f1_label = QLabel("Calibrate f1")
        self.cali_f1_tight_button = QPushButton("Tightening")
        self.cali_f1_loosen_button = QPushButton("Loosensing")

        self.hbox_cali_f1 = QHBoxLayout()
        self.hbox_cali_f1.addWidget(self.cali_f1_tight_button)
        self.hbox_cali_f1.addWidget(self.cali_f1_loosen_button)

        #QFormLayout similar to HBox but you know it look like form, add everything to FormLayout
        self.fbox = QFormLayout()
        self.fbox.addRow(self.finger_label_1,self.hbox_f1)
        self.fbox.addRow(self.finger_label_2,self.hbox_f2)
        self.fbox.addRow(self.finger_label_3,self.hbox_f3)
        self.fbox.addRow(self.finger_label_4,self.hbox_f4)
        self.fbox.addRow(self.coupling_label,self.hbox_tick)
        self.fbox.addRow(self.command_label,self.hbox_command)
        self.fbox.addRow(self.cali_f1_label,self.hbox_cali_f1)

        # Connect singal when slider change to function respectively to change value of label
        self.finger_slider_1.valueChanged.connect(self.valuechange1)
        self.finger_slider_2.valueChanged.connect(self.valuechange2)
        self.finger_slider_3.valueChanged.connect(self.valuechange3)
        self.finger_slider_4.valueChanged.connect(self.valuechange4)
        
        # Add connect signal to Button Go, Cancel and Reset
        self.go_button.clicked.connect(self.handleButtonGo)
        self.home_button.clicked.connect(self.handleButtonHome)
        self.re_button.clicked.connect(self.handleButtonReset)
        # Add connect signal to f1 tight and loosen button
        self.cali_f1_tight_button.clicked.connect(self.handle_cali_f1_tight)
        self.cali_f1_loosen_button.clicked.connect(self.handle_cali_f1_loosen)
        #Set the widget to layout and show the widget
        self.setLayout(self.fbox)
   
        self.setWindowTitle("Test QT Layout")
        self.resize(640,480)

        self.show()

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

    def valuechange1(self):
        float_value = float(self.finger_slider_1.value())/100.0
        self.value_slider_1.setText("%3.2f" % float_value)

    def valuechange2(self):
        float_value = float(self.finger_slider_2.value())/100.0
        self.value_slider_2.setText("%3.2f" % float_value)
        
    def valuechange3(self):
        float_value = float(self.finger_slider_3.value())/100.0
        self.value_slider_3.setText("%3.2f" % float_value)

    def valuechange4(self):
        float_value = float(self.finger_slider_4.value())/100.0
        self.value_slider_4.setText("%3.2f" % float_value)

    def handleButtonGo(self):
        tar_f1 = float(self.finger_slider_1.value())/100.0
        tar_f2 = float(self.finger_slider_2.value())/100.0
        tar_f3 = float(self.finger_slider_3.value())/100.0
        tar_f4 = float(self.finger_slider_4.value())/100.0
        poseTarget = PoseCommand(f1=tar_f1,f2=tar_f2,f3=tar_f3,preshape=tar_f4)
        self.command_pub.publish(poseTarget)
        print "Go Button Click"

    def handleButtonHome(self):
        poseTarget = PoseCommand(f1=0.0,f2=0.0,f3=0.0,preshape=0.0)
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