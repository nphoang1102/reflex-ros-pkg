from python_qt_binding.QtWidgets import * #QWidget, QToolTip,QPushButton,QLabel,QGridLayout,QLineEdit
from python_qt_binding.QtGui import * #QFont,QPalette, QColor

class MyWidgetWC(QWidget):
    
    def __init__(self):
        super(MyWidgetWC, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        #Finger 1 row
        finger_label_1 = QLabel("Goal for f1")
        finger_slider_1 = QLineEdit()
        value_slider_1 = QLabel("0.1")
        hbox_f1 = QHBoxLayout()
        hbox_f1.addWidget(finger_slider_1)
        hbox_f1.addWidget(value_slider_1)

        #Finger 2 row
        finger_label_2 = QLabel("Goal for f2")
        finger_slider_2 = QLineEdit()
        value_slider_2 = QLabel("0.2")
        hbox_f2 = QHBoxLayout()
        hbox_f2.addWidget(finger_slider_2)
        hbox_f2.addWidget(value_slider_2)
        #add1 = QLineEdit()
        #add2 = QLineEdit()

        #Finger 3 row
        finger_label_3 = QLabel("Goal for f3")
        finger_slider_3 = QLineEdit()
        value_slider_3 = QLabel("0.3")
        hbox_f3 = QHBoxLayout()
        hbox_f3.addWidget(finger_slider_3)
        hbox_f3.addWidget(value_slider_3)

        #Finger 4
        finger_label_4 = QLabel("Goal for f_preshape")
        finger_slider_4 = QLineEdit()
        value_slider_4 = QLabel("0.4")
        hbox_f4 = QHBoxLayout()
        hbox_f4.addWidget(finger_slider_4)
        hbox_f4.addWidget(value_slider_4)


        
        # Box Layout for grouping vertical or horizontal
        # vbox = QVBoxLayout()

        # vbox.addWidget(add1)
        # vbox.addWidget(add2)
        # fbox.addRow(l2,vbox)

        #Tick line row, choosing coupling motor
        coupling_label = QLabel("Coupling")
        hbox_tick = QHBoxLayout()

        tick_f1 = QRadioButton("F1")
        tick_f2 = QRadioButton("F2")
        tick_f3 = QRadioButton("F3")
        tick_f4 = QRadioButton("Preshape")
        
        hbox_tick.addWidget(tick_f1)
        hbox_tick.addWidget(tick_f2)
        hbox_tick.addWidget(tick_f3)
        hbox_tick.addWidget(tick_f4)
        hbox_tick.addStretch()

        # Command row
        command_label = QLabel("Command")
        go_button = QPushButton("Go Go Go !!!")
        home_button = QPushButton("Home run boys !!!")
        re_button = QPushButton("Reset Goal")

        hbox_command = QHBoxLayout()
        hbox_command.addWidget(go_button)
        hbox_command.addWidget(home_button)
        hbox_command.addWidget(re_button)

        #QFormLayout similar to HBox but you know it look like form, add everything to FormLayout
        fbox = QFormLayout()
        fbox.addRow(finger_label_1,hbox_f1)
        fbox.addRow(finger_label_2,hbox_f2)
        fbox.addRow(finger_label_3,hbox_f3)
        fbox.addRow(finger_label_4,hbox_f4)
        fbox.addRow(coupling_label,hbox_tick)
        fbox.addRow(command_label,hbox_command)

        self.setLayout(fbox)
   
        self.setWindowTitle("Test QT Layout")
        self.resize(640,480)

        self.show()