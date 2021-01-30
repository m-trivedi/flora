# Import required modules ---

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import pandas as pd
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

#---

# Connecting to MySQL ---

mycon=mc.connect(host="localhost", user="root", passwd="", database="mihir", charset="utf8")
if mycon.is_connected():
    print("Connection Successful")
    cursor=mycon.cursor()
else:
    print("Connection Unsuccessful")

#---
    
butstyle = "QPushButton::hover{ background-color: white; color: #0278ae;}"
bigstyle = """QPushButton{ background-color:#0278ae; color:white; border-radius:25px; border: 1px solid #0278ae; }
QPushButton::hover{ background-color: white; color: #0278ae; border: 1px solid grey; }"""
impstyle = "QLineEdit{ padding: 0px 10px; border:1px solid black; border-radius:10px; } QLineEdit::hover{ border: 1px solid blue; }"
normalButton = "QPushButton{ background-color:#0278ae; color:white; border-radius:10px; border: 1px solid #0278ae; } QPushButton::hover{ background-color: white; color: #0278ae; border: 1px solid grey; }"
tablab = "QLabel{border: 1px solid black;padding:10px; border-left: none; border-top: none;background-color:white;} QLabel::hover {background-color:lightblue;}"

# Main font ---

mfont = QtGui.QFont()
mfont.setFamily("Tahoma")
mfont.setPointSize(10)

# Heading font ---

hfont = QtGui.QFont()
hfont.setFamily("Tahoma")
hfont.setPointSize(20)

# Spacer ---

spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

# Class for drawing graphs, pie charts ---

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

# ---

# Ui Class ---
    
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("flora")
        MainWindow.resize(845, 495)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        # Subheading font ---
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        
        # Side Menu ---
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_4.setStyleSheet("color: white; background-color: #0278ae; border: none; border-right:1px solid black;")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.home = QtWidgets.QPushButton(self.frame_4)
        self.meetups = QtWidgets.QPushButton(self.frame_4)
        #self.request = QtWidgets.QPushButton(self.frame_4)
        self.people = QtWidgets.QPushButton(self.frame_4)
        #self.admin = QtWidgets.QPushButton(self.frame_4)
        self.stats = QtWidgets.QPushButton(self.frame_4)
        self.help = QtWidgets.QPushButton(self.frame_4)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settings = QtWidgets.QPushButton(self.frame_4)
        self.logout = QtWidgets.QPushButton(self.frame_4)
        
        ndic = {self.home:"Home", self.meetups:"Meetups", self.people:"People", self.stats:"Stats", self.help:"Help", spacerItem:"Spacer", self.settings:"Settings", self.logout:"Logout"}

        for element in ndic.keys():
            if element == spacerItem:
                self.verticalLayout.addItem(element)
                continue
            element.setMinimumSize(QtCore.QSize(70, 40))
            element.setMaximumSize(QtCore.QSize(70, 40))
            element.setFont(mfont)
            element.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            element.setStyleSheet(butstyle)
            element.setText(ndic[element])
            self.verticalLayout.addWidget(element)
            
        
        #self.horizontalLayout.addWidget(self.frame_4)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color:#0278ae;")#eeeeee
        self.stackedWidget.setObjectName("stackedWidget")

        # Start Page
        self.startPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.startPage)
        frame = QtWidgets.QFrame(self.startPage)
        frame.setMinimumSize(QtCore.QSize(600, 300))
        frame.setMaximumSize(QtCore.QSize(600, 300))
        frame.setStyleSheet("background-color:white; border:1px solid grey; border-radius:25px;")

        # Title Label
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 30, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(36)
        label.setFont(font)
        label.setStyleSheet("border:none;")
        label.setText("Flora")

        # Description
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 70, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Student Counselling Services")
        
        # Login Button - 1
        self.login1 = QtWidgets.QPushButton(frame)
        self.login1.setGeometry(QtCore.QRect(20, 230, 221, 30))
        self.login1.setFont(mfont)
        self.login1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login1.setStyleSheet(normalButton)
        self.login1.setText("Log In")

        # Image
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(250, 60, 341, 231))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap("Images/twoPeople.jpg"))
        label.setScaledContents(True)

        # Register Button - 1
        self.register1 = QtWidgets.QPushButton(frame)
        self.register1.setGeometry(QtCore.QRect(20, 190, 220, 30))
        self.register1.setFont(mfont)
        self.register1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register1.setStyleSheet(normalButton + "QPushButton{ background-color: #ff7e67; border: 1px solid #ff7e67; } QPushButton::hover{ color: #ff7e67; }")
        self.register1.setText("Register")

        hlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.startPage)

        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Register Page
        self.registerPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.registerPage)
        frame = QtWidgets.QFrame(self.registerPage)
        frame.setMinimumSize(QtCore.QSize(600, 300))
        frame.setMaximumSize(QtCore.QSize(600, 300))
        frame.setStyleSheet("background-color:white; border:1px solid grey; border-radius:25px;")

        # Title Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 30, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(36)
        label.setFont(font)
        label.setStyleSheet("border:none;")
        label.setText("Flora")

        # Subtitle Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 70, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Student Counselling Services")

        # Subsubtitle Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(50, 110, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Register for Flora")

        self.backToHome = QtWidgets.QPushButton(frame)
        self.backToHome.setGeometry(QtCore.QRect(20, 115, 20, 20))
        self.backToHome.setFont(mfont)
        self.backToHome.setStyleSheet("QPushButton{border:none;border-radius:10px;} QPushButton::hover{border:1px solid blue;color:blue;}")
        self.backToHome.setText("<")
        
        # Name Input
        self.nam = QtWidgets.QLineEdit(frame)
        self.nam.setGeometry(QtCore.QRect(20, 150, 221, 30))
        self.nam.setFont(mfont)
        self.nam.setStyleSheet(impstyle)
        self.nam.setClearButtonEnabled(True)
        self.nam.setPlaceholderText("Full Name of Admin")

        # Institution Input
        self.ins = QtWidgets.QLineEdit(frame)
        self.ins.setGeometry(QtCore.QRect(20, 190, 221, 30))
        self.ins.setFont(mfont)
        self.ins.setStyleSheet(impstyle)
        self.ins.setClearButtonEnabled(True)
        self.ins.setPlaceholderText("Name of Institution")

        # Register Button - 2 
        self.register2 = QtWidgets.QPushButton(frame)
        self.register2.setGeometry(QtCore.QRect(20, 230, 221, 30))
        self.register2.setFont(mfont)
        self.register2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register2.setStyleSheet(normalButton)
        self.register2.setText("Continue")

        # Image
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(250, 50, 341, 221))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap("Images/psychologist-communicates-with-client-vector_82574-7018.jpg"))
        label.setScaledContents(True)
        
        hlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.registerPage)

        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Registerr Page
        self.registerrPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.registerrPage)
        frame = QtWidgets.QFrame(self.registerrPage)
        frame.setMinimumSize(QtCore.QSize(600, 300))
        frame.setMaximumSize(QtCore.QSize(600, 300))
        frame.setStyleSheet("background-color:white; border:1px solid grey; border-radius:25px;")

        # Title Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 30, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(36)
        label.setFont(font)
        label.setStyleSheet("border:none;")
        label.setText("Flora")

        # Subtitle Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(20, 70, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Student Counselling Services")

        # Subsubtitle Text
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(50, 110, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Chose a Username and Password")

        self.backToHome2 = QtWidgets.QPushButton(frame)
        self.backToHome2.setGeometry(QtCore.QRect(20, 115, 20, 20))
        self.backToHome2.setFont(mfont)
        self.backToHome2.setStyleSheet("QPushButton{border:none;border-radius:10px;} QPushButton::hover{border:1px solid blue;color:blue;}")
        self.backToHome2.setText("<")
        
        # Username Input
        self.use_r = QtWidgets.QLineEdit(frame)
        self.use_r.setGeometry(QtCore.QRect(20, 150, 221, 30))
        self.use_r.setFont(mfont)
        self.use_r.setStyleSheet(impstyle)
        self.use_r.setClearButtonEnabled(True)
        self.use_r.setPlaceholderText("Username")

        # Password Input
        self.pas_r = QtWidgets.QLineEdit(frame)
        self.pas_r.setGeometry(QtCore.QRect(20, 190, 221, 30))
        self.pas_r.setFont(mfont)
        self.pas_r.setStyleSheet(impstyle)
        self.pas_r.setClearButtonEnabled(True)
        self.pas_r.setPlaceholderText("Password")

        # Register Button - 3
        self.register3 = QtWidgets.QPushButton(frame)
        self.register3.setGeometry(QtCore.QRect(20, 230, 221, 30))
        self.register3.setFont(mfont)
        self.register3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register3.setStyleSheet(normalButton)
        self.register3.setText("Register")

        # Image
        label = QtWidgets.QLabel(frame)
        label.setGeometry(QtCore.QRect(250, 50, 341, 221))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap("Images/psychologist-communicates-with-client-vector_82574-7018.jpg"))
        label.setScaledContents(True)
        
        hlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.registerrPage)

        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Log In Page
        self.loginPage = QtWidgets.QWidget()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loginPage)
        self.frame_3 = QtWidgets.QFrame(self.loginPage)
        self.frame_3.setMinimumSize(QtCore.QSize(600, 300))
        self.frame_3.setMaximumSize(QtCore.QSize(600, 300))
        self.frame_3.setStyleSheet("background-color:white; border:1px solid grey; border-radius:25px;")

        # Title Text
        label = QtWidgets.QLabel(self.frame_3)
        label.setGeometry(QtCore.QRect(20, 30, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(36)
        label.setFont(font)
        label.setStyleSheet("border:none;")
        label.setText("Flora")

        # Subtitle Text
        label = QtWidgets.QLabel(self.frame_3)
        label.setGeometry(QtCore.QRect(20, 70, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Student Counselling Services")

        # Subsubtitle Text
        label = QtWidgets.QLabel(self.frame_3)
        label.setGeometry(QtCore.QRect(50, 110, 221, 30))
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setText("Log Into Flora")

        self.backToHome3 = QtWidgets.QPushButton(self.frame_3)
        self.backToHome3.setGeometry(QtCore.QRect(20, 115, 20, 20))
        self.backToHome3.setFont(mfont)
        self.backToHome3.setStyleSheet("QPushButton{border:none;border-radius:10px;} QPushButton::hover{border:1px solid blue;color:blue;}")
        self.backToHome3.setText("<")
        
        # Username Input
        self.una = QtWidgets.QLineEdit(self.frame_3)
        self.una.setGeometry(QtCore.QRect(20, 150, 221, 30))
        self.una.setFont(mfont)
        self.una.setStyleSheet(impstyle)
        self.una.setClearButtonEnabled(True)
        self.una.setPlaceholderText("Username")

        # Password Input
        self.pas = QtWidgets.QLineEdit(self.frame_3)
        self.pas.setGeometry(QtCore.QRect(20, 190, 221, 30))
        self.pas.setFont(mfont)
        self.pas.setStyleSheet(impstyle)
        self.pas.setClearButtonEnabled(True)
        self.pas.setPlaceholderText("Password")

        # Login Button - 2 
        self.login2 = QtWidgets.QPushButton(self.frame_3)
        self.login2.setGeometry(QtCore.QRect(20, 230, 221, 30))
        self.login2.setFont(mfont)
        self.login2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login2.setStyleSheet(normalButton)
        self.login2.setText("Log In")

        # Indicator
        self.indicator = QtWidgets.QLabel(self.frame_3)
        self.indicator.setGeometry(QtCore.QRect(20, 265, 231, 30))
        self.indicator.setFont(mfont)
        self.indicator.setStyleSheet("border:none;")
        self.indicator.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Image
        label = QtWidgets.QLabel(self.frame_3)
        label.setGeometry(QtCore.QRect(250, 50, 341, 221))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap("Images/psychologist-communicates-with-client-vector_82574-7018.jpg"))
        label.setScaledContents(True)
        
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.loginPage)

        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Home Page 
        self.homePage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.homePage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)
        
        self.frame_5 = QtWidgets.QFrame(self.homePage)
        hlayout_1 = QtWidgets.QHBoxLayout(self.frame_5)
        
        self.frame_21 = QtWidgets.QFrame(self.frame_5)
        self.frame_21.setMinimumSize(QtCore.QSize(311, 211))
        self.frame_21.setMaximumSize(QtCore.QSize(311, 211))

        self.peopleButton = QtWidgets.QPushButton(self.frame_21)
        self.meetupsButton = QtWidgets.QPushButton(self.frame_21)
        self.settingsButton = QtWidgets.QPushButton(self.frame_21)
        
        self.makeHButton(mfont, self.peopleButton, "People", 20, 120, bigstyle)
        self.makeHButton(mfont, self.meetupsButton, "All Meetups", 170, 0, bigstyle)
        self.makeHButton(mfont, self.settingsButton, "Settings", 170, 120, bigstyle)
        
        hlayout_1.addWidget(self.frame_21)
        hlayout.addWidget(self.frame_5)

        # Right Frame
        self.rinfo(self.homePage, hlayout, "No upcoming meetups today", "Images/twoPeople.jpg", 280, 160)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Settings Page
        self.settingsPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.settingsPage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)
        
        frame = QtWidgets.QFrame(self.settingsPage)
        gridLayout = QtWidgets.QGridLayout(frame)
        
        self.frame_2 = QtWidgets.QFrame(frame)
        self.frame_2.setMinimumSize(QtCore.QSize(280, 370))
        self.frame_2.setMaximumSize(QtCore.QSize(280, 370))
        self.frame_2.setStyleSheet("border: 1px solid grey; border-radius:25px;background-color:white;")

        label = QtWidgets.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(20, 20, 150, 30))
        label.setFont(sfont)
        label.setStyleSheet("border: none;")
        label.setText("Account Information")
        
        # Labels for acc info ---
        alst = ["Name", "Username", "Type", "Institution"]
        i = 60
        for element in alst:
            label = QtWidgets.QLabel(self.frame_2)
            label.setGeometry(QtCore.QRect(20, i, 80, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;")
            label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            label.setText(element)
            i += 30

        self.name = QtWidgets.QLabel(self.frame_2)
        self.uname = QtWidgets.QLabel(self.frame_2)
        self.type = QtWidgets.QLabel(self.frame_2)
        self.inst = QtWidgets.QLabel(self.frame_2)
        
        blst = [self.name, self.uname, self.type, self.inst]
        i = 60
        for element in blst:
            element.setGeometry(QtCore.QRect(100, i, 170, 30))
            element.setFont(mfont)
            element.setStyleSheet("border: none;")
            element.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            i += 30
        
        label = QtWidgets.QLabel(self.frame_2)
        label.setGeometry(QtCore.QRect(20, 200, 240, 30))
        label.setFont(sfont)
        label.setStyleSheet("border:none;")
        label.setText("Change Password")
        
        self.opas = QtWidgets.QLineEdit(self.frame_2)
        self.opas.setGeometry(QtCore.QRect(20, 240, 240, 30))
        self.opas.setFont(mfont)
        self.opas.setStyleSheet(impstyle)
        self.opas.setClearButtonEnabled(True)
        self.opas.setPlaceholderText("Old Password")
        
        self.npas = QtWidgets.QLineEdit(self.frame_2)
        self.npas.setGeometry(QtCore.QRect(20, 280, 240, 30))
        self.npas.setFont(mfont)
        self.npas.setStyleSheet(impstyle)
        self.npas.setClearButtonEnabled(True)
        self.npas.setPlaceholderText("New Password")
        
        self.cpasButton = QtWidgets.QPushButton(self.frame_2)
        self.cpasButton.setGeometry(QtCore.QRect(20, 320, 240, 30))
        self.cpasButton.setFont(mfont)
        self.cpasButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cpasButton.setStyleSheet(normalButton)
        self.cpasButton.setText("Change Password")
        
        gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        
        hlayout.addWidget(frame)
        
        # Image, Info Text & Spacers
        text = "\nContact your admin, if you find your\naccount information to be incorrect"
        self.rinfo(self.settingsPage, hlayout, text, "Images/fourPeople.jpg", 240, 160)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Request Page
        self.requestPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.requestPage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)

        # Frames
        frame = QtWidgets.QFrame(self.requestPage)
        gridLayout = QtWidgets.QGridLayout(frame)

        self.frame_10 = QtWidgets.QFrame(frame)
        self.frame_10.setMinimumSize(QtCore.QSize(280, 370))
        self.frame_10.setMaximumSize(QtCore.QSize(280, 370))
        self.frame_10.setStyleSheet("border: 1px solid grey; border-radius:25px;background-color:white;")

        label = QtWidgets.QLabel(self.frame_10)
        label.setGeometry(QtCore.QRect(20, 20, 240, 30))
        label.setFont(sfont)
        label.setStyleSheet("border: none;")
        label.setText("Request Meetup")

        # Meetup for current user
        self.mlabel = QtWidgets.QLabel(self.frame_10)
        self.mlabel.setGeometry(QtCore.QRect(20, 60, 240, 30))
        self.mlabel.setFont(mfont)
        self.mlabel.setStyleSheet("padding:0px 10px; background-color:white; border:1px solid black; border-radius:10px;")

        # Meetup Regarding
        self.regarding1 = QtWidgets.QPlainTextEdit(self.frame_10)
        self.regarding1.setGeometry(QtCore.QRect(20, 100, 240, 80))
        self.regarding1.setFont(mfont)
        self.regarding1.setStyleSheet("padding:10px; background-color:white; border:1px solid black; border-radius:10px;")
        self.regarding1.setPlaceholderText("Regarding")

        # Button for requesting meetup
        self.requestButton1 = QtWidgets.QPushButton(self.frame_10)
        self.requestButton1.setGeometry(QtCore.QRect(20, 190, 240, 30))
        self.requestButton1.setFont(mfont)
        self.requestButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.requestButton1.setStyleSheet(normalButton)
        self.requestButton1.setText("Request Meetup")

        label = QtWidgets.QLabel(self.frame_10)
        label.setGeometry(QtCore.QRect(20, 240, 240, 120))
        label.setFont(mfont)
        label.setStyleSheet("border: none;")
        label.setText("Note:\nIn order to request a meetup for yourself\nprovide your own username. You can only\nrequest a meetup twice a week. You will\nremain anonymous even if you request a\nmeetup for someone else.")

        gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)

        hlayout.addWidget(frame)
        
        # Image, Info Text and Spacers
        text = "\nYou can only make two requests per week\n\nThe date and time of your requested meetups\nare set by your counsellor"
        self.rinfo(self.requestPage, hlayout, text, "Images/psychologist-communicates-with-client-vector_82574-7018.jpg", 240, 160)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Edit Page
        self.editPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.editPage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)

        # Frames
        frame = QtWidgets.QFrame(self.requestPage)
        gridLayout = QtWidgets.QGridLayout(frame)

        self.frame_e = QtWidgets.QFrame(frame)
        self.frame_e.setMinimumSize(QtCore.QSize(280, 370))
        self.frame_e.setMaximumSize(QtCore.QSize(280, 370))
        self.frame_e.setStyleSheet("border: 1px solid grey; border-radius:25px;background-color:white;")

        label = QtWidgets.QLabel(self.frame_e)
        label.setGeometry(QtCore.QRect(20, 20, 240, 30))
        label.setFont(sfont)
        label.setStyleSheet("border: none;")
        label.setText("Edit Meetup")

        # Meetup Id
        self.mid = QtWidgets.QLineEdit(self.frame_e)
        self.mid.setGeometry(QtCore.QRect(20, 60, 240, 30))
        self.mid.setFont(mfont)
        self.mid.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.mid.setPlaceholderText("Meetup Id")

        # Date
        self.date_e = QtWidgets.QDateEdit(self.frame_e)
        self.date_e.setGeometry(QtCore.QRect(20, 100, 240, 30))
        self.date_e.setFont(mfont)
        self.date_e.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")

        # Time
        self.time_e = QtWidgets.QLineEdit(self.frame_e)
        self.time_e.setGeometry(QtCore.QRect(20, 140, 240, 30))
        self.time_e.setFont(mfont)
        self.time_e.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.time_e.setPlaceholderText("Time of Meetup")

        # Button
        self.button_e = QtWidgets.QPushButton(self.frame_e)
        self.button_e.setGeometry(QtCore.QRect(20, 180, 240, 30))
        self.button_e.setFont(mfont)
        self.button_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_e.setStyleSheet(normalButton)
        self.button_e.setText("Edit Meetup")

        gridLayout.addWidget(self.frame_e, 0, 0, 1, 1)
        hlayout.addWidget(frame)

        # Image, Info Text and Spacers
        text = "\nYou can only make two requests per week\n\nThe date and time of your requested meetups\nare set by your counsellor"
        self.rinfo(self.editPage, hlayout, text, "Images/psychologist-communicates-with-client-vector_82574-7018.jpg", 240, 160)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Schedule Page
        self.schedulePage = QtWidgets.QWidget()
        
        hlayout = QtWidgets.QHBoxLayout(self.schedulePage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)

        # Frames
        frame = QtWidgets.QFrame(self.schedulePage)
        gridLayout = QtWidgets.QGridLayout(frame)

        self.frame_s = QtWidgets.QFrame(frame)
        self.frame_s.setMinimumSize(QtCore.QSize(280, 370))
        self.frame_s.setMaximumSize(QtCore.QSize(280, 370))
        self.frame_s.setStyleSheet("border: 1px solid grey; border-radius:25px;background-color:white;")

        label = QtWidgets.QLabel(self.frame_s)
        label.setGeometry(QtCore.QRect(20, 20, 240, 30))
        label.setFont(sfont)
        label.setStyleSheet("border: none;")
        label.setText("Schedule Meetup")

        # Username
        self.uname_s = QtWidgets.QLineEdit(self.frame_s)
        self.uname_s.setGeometry(QtCore.QRect(20, 60, 240, 30))
        self.uname_s.setFont(mfont)
        self.uname_s.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.uname_s.setPlaceholderText("Username of Student")

        # Date
        self.date_s = QtWidgets.QDateEdit(self.frame_s)
        self.date_s.setGeometry(QtCore.QRect(20, 100, 240, 30))
        self.date_s.setFont(mfont)
        self.date_s.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")

        # Time
        self.time_s = QtWidgets.QLineEdit(self.frame_s)
        self.time_s.setGeometry(QtCore.QRect(20, 140, 240, 30))
        self.time_s.setFont(mfont)
        self.time_s.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.time_s.setPlaceholderText("Time of Meetup")

        # Regarding
        self.regarding_s = QtWidgets.QPlainTextEdit(self.frame_s)
        self.regarding_s.setGeometry(QtCore.QRect(20, 180, 240, 80))
        self.regarding_s.setFont(mfont)
        self.regarding_s.setStyleSheet("padding:10px; background-color:white; border:1px solid black; border-radius:10px;")
        self.regarding_s.setPlaceholderText("Regarding")

        # Button
        self.button_s = QtWidgets.QPushButton(self.frame_s)
        self.button_s.setGeometry(QtCore.QRect(20, 270, 240, 30))
        self.button_s.setFont(mfont)
        self.button_s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_s.setStyleSheet(normalButton)
        self.button_s.setText("Schedule Meetup")

        gridLayout.addWidget(self.frame_s, 0, 0, 1, 1)
        hlayout.addWidget(frame)

        # Right Frame
        text = "\nYou can only make two requests per week\n\nThe date and time of your requested meetups\nare set by your counsellor"
        self.rinfo(self.schedulePage, hlayout, text, "Images/psychologist-communicates-with-client-vector_82574-7018.jpg", 240, 160)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Admin Page
        self.adminPage = QtWidgets.QWidget()
        hlayout = QtWidgets.QHBoxLayout(self.adminPage)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)

        # Frames
        frame = QtWidgets.QFrame(self.adminPage)
        gridLayout = QtWidgets.QGridLayout(frame)

        self.frame_a = QtWidgets.QFrame(frame)
        self.frame_a.setMinimumSize(QtCore.QSize(280, 370))
        self.frame_a.setMaximumSize(QtCore.QSize(280, 370))
        self.frame_a.setStyleSheet("border: 1px solid grey; border-radius:25px;background-color:white;")

        label = QtWidgets.QLabel(self.frame_a)
        label.setGeometry(QtCore.QRect(20, 20, 240, 30))
        label.setFont(sfont)
        label.setStyleSheet("border: none;")
        label.setText("Admin Panel")

        label = QtWidgets.QLabel(self.frame_a)
        label.setGeometry(QtCore.QRect(20, 60, 240, 30))
        label.setFont(mfont)
        label.setStyleSheet("border: none;")
        label.setText("Create an account")        

        # Name
        self.name_a = QtWidgets.QLineEdit(self.frame_a)
        self.name_a.setGeometry(QtCore.QRect(20, 100, 240, 30))
        self.name_a.setFont(mfont)
        self.name_a.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.name_a.setPlaceholderText("Name")

        # Username
        self.uname_a = QtWidgets.QLineEdit(self.frame_a)
        self.uname_a.setGeometry(QtCore.QRect(20, 140, 240, 30))
        self.uname_a.setFont(mfont)
        self.uname_a.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.uname_a.setPlaceholderText("Username")

        # Password
        self.passw_a = QtWidgets.QLineEdit(self.frame_a)
        self.passw_a.setGeometry(QtCore.QRect(20, 180, 240, 30))
        self.passw_a.setFont(mfont)
        self.passw_a.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.passw_a.setPlaceholderText("Password")

        # Type
        self.type_a = QtWidgets.QComboBox(self.frame_a)
        self.type_a.setGeometry(QtCore.QRect(20, 220, 240, 30))
        self.type_a.setFont(mfont)
        self.type_a.setStyleSheet("background-color:white;padding: 0px 10px; border:1px solid black; border-radius: 10px;")
        self.type_a.addItems(["Counsellor", "Student", "Teacher"])

        # Button
        self.button_a = QtWidgets.QPushButton(self.frame_a)
        self.button_a.setGeometry(QtCore.QRect(20, 260, 240, 30))
        self.button_a.setFont(mfont)
        self.button_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_a.setStyleSheet(normalButton)
        self.button_a.setText("Create Account")

        # CSV Button
        self.button_csv = QtWidgets.QPushButton(self.frame_a)
        self.button_csv.setGeometry(QtCore.QRect(20, 300, 240, 30))
        self.button_csv.setFont(mfont)
        self.button_csv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_csv.setStyleSheet(normalButton)
        self.button_csv.setText("Create Accounts via CSV")

        self.indicator_a = QtWidgets.QLabel(self.frame_a)
        self.indicator_a.setGeometry(QtCore.QRect(20, 339, 240, 30))
        self.indicator_a.setFont(mfont)
        self.indicator_a.setStyleSheet("border: none;")

        gridLayout.addWidget(self.frame_a, 0, 0, 1, 1)
        hlayout.addWidget(frame)

        # Right Frame
        text = "\nYou can only make two requests per week\n\nThe date and time of your requested meetups\nare set by your counsellor"
        self.rinfo(self.schedulePage, hlayout, text, "Images/sevenPeople.jpg", 240, 190)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # Add all the pages to the stacked widget
        self.stackedWidget.addWidget(self.homePage)
        self.stackedWidget.addWidget(self.settingsPage)
        self.stackedWidget.addWidget(self.requestPage)
        self.stackedWidget.addWidget(self.editPage)
        self.stackedWidget.addWidget(self.schedulePage)
        self.stackedWidget.addWidget(self.adminPage)
        #---------------------------------------------------------------------------------------------------------------------------------------------
        
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##############################################################################################################################################

        # Button Click Functions ---
        self.home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.meetups.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.meetupsPage))
        self.people.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.counsellorPage))
        self.stats.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.linePage))
        self.settings.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))
        self.logout.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.loginPage))

        self.login1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.loginPage))
        self.register1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.registerPage))
        self.register2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.registerrPage))
        self.meetupsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.meetupsPage))
        self.peopleButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.counsellorPage))
        self.settingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))
        self.backToHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.startPage))
        self.backToHome3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.startPage))

        self.register3.clicked.connect(self.registerAccount)
        self.login2.clicked.connect(self.checkCredentials)
        self.requestButton1.clicked.connect(self.requestMeetupForMyself)
        self.button_s.clicked.connect(self.scheduleMeetup)
        self.button_e.clicked.connect(self.editMeetup)
        self.cpasButton.clicked.connect(self.changePassword)
        self.button_a.clicked.connect(self.createAccount)
        self.button_csv.clicked.connect(self.createAccountsViaCSV)

        ##############################################################################################################################################

    def infoText(self, frame, text, image, ximg, yimg):
        
        glayout = QtWidgets.QGridLayout(frame)
        # Image
        label = QtWidgets.QLabel(frame)
        label.setMinimumSize(QtCore.QSize(ximg, yimg))
        label.setMaximumSize(QtCore.QSize(ximg, yimg))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap(image))
        label.setScaledContents(True)
        glayout.addWidget(label, 1, 0, 1, 1)
        
        # Info Text
        label = QtWidgets.QLabel(frame)
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)
        glayout.addWidget(label, 2, 0, 1, 1)

        # Spacers
        glayout.addItem(spacer, 0, 0, 1, 1)
        glayout.addItem(spacer, 3, 0, 1, 1)

    def rinfo(self, pageName, hlayout, text, image, ximg, yimg):
        
        # rframe contains image, info text and spacers
        rframe = QtWidgets.QFrame(pageName)
        rframe.setMinimumSize(QtCore.QSize(300, 400))
        rframe.setStyleSheet("background-color: white; border-left: 1px solid grey;")
        
        glayout = QtWidgets.QGridLayout(rframe)
        
        # Image
        label = QtWidgets.QLabel(rframe)
        label.setMinimumSize(QtCore.QSize(ximg, yimg))
        label.setMaximumSize(QtCore.QSize(ximg, yimg))
        label.setStyleSheet("border:none;")
        label.setPixmap(QtGui.QPixmap(image))
        label.setScaledContents(True)
        glayout.addWidget(label, 1, 0, 1, 1)
        
        # Info Text
        label = QtWidgets.QLabel(rframe)
        label.setFont(mfont)
        label.setStyleSheet("border:none;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)
        glayout.addWidget(label, 2, 0, 1, 1)

        # Spacers
        glayout.addItem(spacer, 0, 0, 1, 1)
        glayout.addItem(spacer, 3, 0, 1, 1)

        hlayout.addWidget(rframe)
 
    def makeHeading(self, heading, page, layout):
        hlabel = QtWidgets.QLabel(page)
        hlabel.setFont(hfont)
        hlabel.setMinimumSize(QtCore.QSize(0, 60))
        hlabel.setMaximumSize(QtCore.QSize(10000, 60))
        hlabel.setStyleSheet("border:none;background-color:white;padding:15px;border-bottom:1px solid grey;color:#0278ae;")
        hlabel.setText(heading)
        layout.addWidget(hlabel)

    def makeHButton(self, mfont, button, name, x, y, bigstyle):
        button.setGeometry(QtCore.QRect(x, y, 121, 91))
        button.setFont(mfont)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(bigstyle)
        button.setText(name)
        
    def makeTableLabel(self, frame, glayout, text, x, y):
        label = QtWidgets.QLabel(frame)
        label.setMinimumSize(QtCore.QSize(0, 35))
        label.setFont(mfont)
        label.setStyleSheet("border:none;border-bottom:2px solid #eeeeee; background-color:white;padding:15px;")
        label.setText(text)
        glayout.addWidget(label, x, y, 1, 1)

    def checkCredentials(self, MainWindow):
        un = self.una.text()
        pa = self.pas.text()
        if un!="" and pa!="":
            gsql = "SELECT Id, Name, Type, Inst, Uname, Passw FROM USERS WHERE Uname='" + un + "' AND Passw='" + pa + "';"
            cursor.execute(gsql)
            global gdata
            gdata=cursor.fetchone()
            if gdata!=None:
                gsql = "SELECT Name FROM INSTITUTIONS WHERE Id="+str(gdata[3])+";"
                cursor.execute(gsql)
                global ginst
                ginst=cursor.fetchone()
                
                self.name.setText(gdata[1]) 
                self.uname.setText(gdata[4])
                self.type.setText(gdata[2])
                self.inst.setText(ginst[0])
                self.mlabel.setText(gdata[4])
                self.horizontalLayout.insertWidget(0, self.frame_4)

                # Assigned Meetups Page
                self.getMeetupInfo()
                # Requested Meetups Page
                self.requestedMeetupsPage()
                # Counsellor People Page
                self.counsellorPeoplePage()
                # Student People Page
                self.studentPeoplePage()
                # Teacher People Page
                self.teacherPeoplePage()
                # Line Stats Page
                self.lineStatsPage()
                # Pie Stats Page
                self.pieStatsPage()
                
                if gdata[2] == "Admin":
                    self.admin = QtWidgets.QPushButton(self.frame_4)
                    self.admin.setMinimumSize(QtCore.QSize(70, 40))
                    self.admin.setMaximumSize(QtCore.QSize(70, 40))
                    self.admin.setFont(mfont)
                    self.admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.admin.setStyleSheet(butstyle)
                    self.admin.setText("Admin")
                    self.verticalLayout.insertWidget(2, self.admin)
                    self.admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.adminPage))

                    self.adminButton = QtWidgets.QPushButton(self.frame_21)
                    self.makeHButton(mfont, self.adminButton, "Admin Panel", 20, 0, bigstyle + "QPushButton{ background-color:#ff7e67; border: 1px solid #ff7e67; } QPushButton::hover{ background-color: white; color: #ff7e67; }")
                    self.adminButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.adminPage))
                    
                elif gdata[2] == "Student" or gdata[2]=="Teacher":
                    self.request = QtWidgets.QPushButton(self.frame_4)
                    self.request.setMinimumSize(QtCore.QSize(70, 40))
                    self.request.setMaximumSize(QtCore.QSize(70, 40))
                    self.request.setFont(mfont)
                    self.request.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.request.setStyleSheet(butstyle)
                    self.request.setText("Request")
                    self.verticalLayout.insertWidget(2, self.request)
                    self.request.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestPage))

                    self.requestButton = QtWidgets.QPushButton(self.frame_21)
                    self.makeHButton(mfont, self.requestButton, "Request Meetup", 20, 0, bigstyle + "QPushButton{ background-color:#ff7e67; border: 1px solid #ff7e67; } QPushButton::hover{ background-color: white; color: #ff7e67; }")
                    self.requestButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestPage))

                elif gdata[2] == "Counsellor":
                    self.schedule = QtWidgets.QPushButton(self.frame_4)
                    self.schedule.setMinimumSize(QtCore.QSize(70, 40))
                    self.schedule.setMaximumSize(QtCore.QSize(70, 40))
                    self.schedule.setFont(mfont)
                    self.schedule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.schedule.setStyleSheet(butstyle)
                    self.schedule.setText("Schedule")
                    self.verticalLayout.insertWidget(2, self.schedule)
                    self.schedule.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.schedulePage))

                    self.edit = QtWidgets.QPushButton(self.frame_4)
                    self.edit.setMinimumSize(QtCore.QSize(70, 40))
                    self.edit.setMaximumSize(QtCore.QSize(70, 40))
                    self.edit.setFont(mfont)
                    self.edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.edit.setStyleSheet(butstyle)
                    self.edit.setText("Edit")
                    self.verticalLayout.insertWidget(3, self.edit)
                    self.edit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editPage))

                    self.scheduleButton = QtWidgets.QPushButton(self.frame_21)
                    self.makeHButton(mfont, self.scheduleButton, "Schedule Meetup", 20, 0, bigstyle + "QPushButton{ background-color:#ff7e67; border: 1px solid #ff7e67; } QPushButton::hover{ background-color: white; color: #ff7e67; }")
                    self.scheduleButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.schedulePage))
                    
            
                self.stackedWidget.setStyleSheet("background-color:#eeeeee;")
                self.stackedWidget.setCurrentIndex(4)
                print("Id:", gdata[0], "\nName:", gdata[1], "\nType:", gdata[2], "\nInst. No.:", gdata[3], "\nUsername:", gdata[4], "\nPasssword:", gdata[5], "\nInst. Name:", ginst[0])
            else:
                self.indicator.setText("Login Credentials Incorrect")
        else:
            self.indicator.setText("Username/Password cannot be empty")

    def getMeetupInfo(self):
        self.meetupsPage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.meetupsPage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.meetupsPage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Assigned Button
        self.assigned = QtWidgets.QPushButton(tframe)
        self.assigned.setGeometry(QtCore.QRect(20, 0, 65, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.assigned.setFont(sfont)
        self.assigned.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.assigned.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.assigned.setText('Assigned')
        self.assigned.clicked.connect(self.getMeetupInfo)
        # Open Button
        self.open = QtWidgets.QPushButton(tframe)
        self.open.setGeometry(QtCore.QRect(100, 0, 40, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.open.setFont(sfont)
        self.open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.open.setText('Open')
        self.open.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        # Closed Button
        self.closed = QtWidgets.QPushButton(tframe)
        self.closed.setGeometry(QtCore.QRect(155, 0, 50, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.closed.setFont(sfont)
        self.closed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closed.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.closed.setText('Closed')
        self.closed.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.meetupsPage)
        frame.setStyleSheet('padding:20px;')
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        # Fill up the table
        if gdata[2] == "Admin":
            df = pd.read_sql("SELECT Id, MeetupFor, Date, Time, Regarding, Status FROM Meetups WHERE Status='Assigned' ORDER BY Date;", mycon)
            df.rename(columns = {'Id':'Meetup Id', 'MeetupFor':'Meetup For'}, inplace = True)
        elif gdata[2] == "Counsellor":
            df = pd.read_sql("SELECT Id, MeetupFor, Date, Time, Regarding, Status FROM Meetups WHERE MeetupBy = " + str(gdata[0]) + " AND Status='Assigned' ORDER BY Date;", mycon)
            df.rename(columns = {'Id':'Meetup Id', 'MeetupFor':'Meetup For'}, inplace = True)
        else:
            df = pd.read_sql("SELECT Id, MeetupBy, Date, Time, Regarding, Status FROM Meetups WHERE MeetupFor = " + str(gdata[0]) + " AND Status='Assigned' ORDER BY Date;", mycon)
            df.rename(columns = {'Id':'Meetup Id', 'MeetupBy':'Meetup By'}, inplace = True)
        print(df)
        j = 0
        for row in df.iteritems():
            i = 1
            label = QtWidgets.QLabel(frame)
            label.setMinimumSize(QtCore.QSize(0, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;padding:15px;")
            label.setText(row[0])
            glayout.addWidget(label, 0, j, 1, 1)
            import numpy as np
            for element in row[1]:
                if j == 1:
                    sql = "SELECT Name FROM USERS WHERE Id = " + str(element)
                    cursor.execute(sql)
                    nam = cursor.fetchone()
                    self.makeTableLabel(frame, glayout, nam[0], i, j)
                else:
                    self.makeTableLabel(frame, glayout, str(element), i, j)
                i += 1
            j += 1

        glayout.addItem(spacer, 10, 0, 1, 1)
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.meetupsPage)

    # Requested Meetups Page   
    def requestedMeetupsPage(self):
        self.requestedPage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.requestedPage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.meetupsPage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Assigned Button
        self.assigned = QtWidgets.QPushButton(tframe)
        self.assigned.setGeometry(QtCore.QRect(20, 0, 65, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.assigned.setFont(sfont)
        self.assigned.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.assigned.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.assigned.setText('Assigned')
        self.assigned.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.meetupsPage))
        # Open Button
        self.open = QtWidgets.QPushButton(tframe)
        self.open.setGeometry(QtCore.QRect(100, 0, 40, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.open.setFont(sfont)
        self.open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.open.setText('Open')
        self.open.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        # Closed Button
        self.closed = QtWidgets.QPushButton(tframe)
        self.closed.setGeometry(QtCore.QRect(155, 0, 50, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.closed.setFont(sfont)
        self.closed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closed.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.closed.setText('Closed')
        self.closed.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.requestedPage)
        frame.setStyleSheet('padding:20px;')
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        # Fill up the table
        if gdata[2]=="Admin" or gdata[2]=="Counsellor":
            df = pd.read_sql("SELECT Id, MeetupFor, Date, Time, Regarding, Status FROM Meetups WHERE Status='Open';", mycon)
        else:
            df = pd.read_sql("SELECT Id, MeetupFor, Date, Time, Regarding, Status FROM Meetups WHERE Status='Open' AND MeetupFor='"+str(gdata[0])+"';", mycon)
        j = 0
        df.rename(columns = {'Id':'Meetup Id', 'MeetupFor':'Meetup For'}, inplace = True)
        print(df)
        for row in df.iteritems():
            i = 1
            label = QtWidgets.QLabel(frame)
            label.setMinimumSize(QtCore.QSize(0, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;padding:15px;")
            label.setText(row[0])
            glayout.addWidget(label, 0, j, 1, 1)
            
            for element in row[1]:
                if j == 1:
                    sql = "SELECT Name FROM USERS WHERE Id = " + str(element)
                    cursor.execute(sql)
                    nam = cursor.fetchone()
                    self.makeTableLabel(frame, glayout, nam[0], i, j)
                else:
                    self.makeTableLabel(frame, glayout, str(element), i, j)
                i += 1
            j += 1

        glayout.addItem(spacer, 10, 0, 1, 1)
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.requestedPage)

    # Counsellors Page   
    def counsellorPeoplePage(self):
        self.counsellorPage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.counsellorPage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.counsellorPage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Counsellors Button
        self.counsellors = QtWidgets.QPushButton(tframe)
        self.counsellors.setGeometry(QtCore.QRect(20, 0, 80, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.counsellors.setFont(sfont)
        self.counsellors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.counsellors.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.counsellors.setText('Counsellors')
        self.counsellors.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.counsellorPage))
        # Students Button
        self.students = QtWidgets.QPushButton(tframe)
        self.students.setGeometry(QtCore.QRect(115, 0, 60, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.students.setFont(sfont)
        self.students.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.students.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.students.setText('Students')
        self.students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.studentPage))
        # Teachers Button
        self.teachers = QtWidgets.QPushButton(tframe)
        self.teachers.setGeometry(QtCore.QRect(190, 0, 65, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.teachers.setFont(sfont)
        self.teachers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teachers.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.teachers.setText('Teachers')
        self.teachers.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.teacherPage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.counsellorPage)
        frame.setStyleSheet('padding:20px;')
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        # Fill up the table
        df = pd.read_sql("SELECT Name, Uname, Type FROM USERS WHERE Type='Counsellor' AND Inst="+str(gdata[3])+" ORDER BY Name;", mycon)
        j = 0
        df.rename(columns = {'Uname':'Username'}, inplace = True)
        print(df)
        for row in df.iteritems():
            i = 1
            label = QtWidgets.QLabel(frame)
            label.setMinimumSize(QtCore.QSize(0, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;padding:15px;")
            label.setText(row[0])
            glayout.addWidget(label, 0, j, 1, 1)
            
            for element in row[1]:
                self.makeTableLabel(frame, glayout, str(element), i, j)
                i += 1
            j += 1

        glayout.addItem(spacer, 10, 0, 1, 1)
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.counsellorPage)

    # Students Page   
    def studentPeoplePage(self):
        self.studentPage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.studentPage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.studentPage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Counsellors Button
        self.counsellors = QtWidgets.QPushButton(tframe)
        self.counsellors.setGeometry(QtCore.QRect(20, 0, 80, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.counsellors.setFont(sfont)
        self.counsellors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.counsellors.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.counsellors.setText('Counsellors')
        self.counsellors.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.counsellorPage))
        # Students Button
        self.students = QtWidgets.QPushButton(tframe)
        self.students.setGeometry(QtCore.QRect(115, 0, 60, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.students.setFont(sfont)
        self.students.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.students.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.students.setText('Students')
        self.students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.studentPage))
        # Teachers Button
        self.teachers = QtWidgets.QPushButton(tframe)
        self.teachers.setGeometry(QtCore.QRect(190, 0, 65, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.teachers.setFont(sfont)
        self.teachers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teachers.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.teachers.setText('Teachers')
        self.teachers.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.teacherPage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.studentPage)
        frame.setStyleSheet('padding:20px;')
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        # Fill up the table
        df = pd.read_sql("SELECT Name, Uname, Type FROM USERS WHERE Type='Student' AND Inst="+str(gdata[3])+" ORDER BY Name;", mycon)
        j = 0
        df.rename(columns = {'Uname':'Username'}, inplace = True)
        print(df)
        for row in df.iteritems():
            i = 1
            label = QtWidgets.QLabel(frame)
            label.setMinimumSize(QtCore.QSize(0, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;padding:15px;")
            label.setText(row[0])
            glayout.addWidget(label, 0, j, 1, 1)
            
            for element in row[1]:
                self.makeTableLabel(frame, glayout, str(element), i, j)
                i += 1
            j += 1

        glayout.addItem(spacer, 10, 0, 1, 1)
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.studentPage)

    # Teachers Page   
    def teacherPeoplePage(self):
        self.teacherPage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.teacherPage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.teacherPage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Counsellors Button
        self.counsellors = QtWidgets.QPushButton(tframe)
        self.counsellors.setGeometry(QtCore.QRect(20, 0, 80, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.counsellors.setFont(sfont)
        self.counsellors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.counsellors.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.counsellors.setText('Counsellors')
        self.counsellors.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.counsellorPage))
        # Students Button
        self.students = QtWidgets.QPushButton(tframe)
        self.students.setGeometry(QtCore.QRect(115, 0, 60, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.students.setFont(sfont)
        self.students.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.students.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.students.setText('Students')
        self.students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.studentPage))
        # Teachers Button
        self.teachers = QtWidgets.QPushButton(tframe)
        self.teachers.setGeometry(QtCore.QRect(190, 0, 65, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.teachers.setFont(sfont)
        self.teachers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teachers.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.teachers.setText('Teachers')
        self.teachers.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.teacherPage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.teacherPage)
        frame.setStyleSheet('padding:20px;')
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        # Fill up the table
        df = pd.read_sql("SELECT Name, Uname, Type FROM USERS WHERE Type='Teacher' AND Inst="+str(gdata[3])+" ORDER BY Name;", mycon)
        j = 0
        df.rename(columns = {'Uname':'Username'}, inplace = True)
        print(df)
        for row in df.iteritems():
            i = 1
            label = QtWidgets.QLabel(frame)
            label.setMinimumSize(QtCore.QSize(0, 30))
            label.setFont(mfont)
            label.setStyleSheet("border: none;padding:15px;")
            label.setText(row[0])
            glayout.addWidget(label, 0, j, 1, 1)
            
            for element in row[1]:
                self.makeTableLabel(frame, glayout, str(element), i, j)
                i += 1
            j += 1

        glayout.addItem(spacer, 10, 0, 1, 1)
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.teacherPage)

    # Line Page
    def lineStatsPage(self):
        # Line Page
        self.linePage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.linePage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.linePage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Line Button
        self.line = QtWidgets.QPushButton(tframe)
        self.line.setGeometry(QtCore.QRect(20, 0, 40, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.line.setFont(sfont)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.line.setText('Line')
        self.line.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.linePage))
        # Bar Button
        self.bar = QtWidgets.QPushButton(tframe)
        self.bar.setGeometry(QtCore.QRect(75, 0, 30, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.bar.setFont(sfont)
        self.bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bar.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.bar.setText('Bar')
        self.bar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        # Pie Button
        self.pie = QtWidgets.QPushButton(tframe)
        self.pie.setGeometry(QtCore.QRect(120, 0, 30, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.pie.setFont(sfont)
        self.pie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pie.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.pie.setText('Pie')
        self.pie.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.piePage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.linePage)
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        df = pd.read_sql("select count(*) as frequency, date from meetups where meetupby is not null group by date;", mycon)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(df.date, df.frequency)
        sc.axes.set_xlabel("Dates")
        sc.axes.set_ylabel("Number of Meetups")
        glayout.addWidget(sc, 0, 0, 1, 1)
        
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.linePage)


    # Pie Page
    def pieStatsPage(self):
        # Pie Page
        self.piePage = QtWidgets.QWidget()
        vlayout = QtWidgets.QVBoxLayout(self.piePage)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)

        # Top Frame
        tframe = QtWidgets.QFrame(self.piePage)
        tframe.setStyleSheet('border:none;border-bottom:1px solid black;background-color:white;')
        tframe.setMinimumSize(QtCore.QSize(0, 40))
        tframe.setMaximumSize(QtCore.QSize(10000, 40))
        # Line Button
        self.line = QtWidgets.QPushButton(tframe)
        self.line.setGeometry(QtCore.QRect(20, 0, 40, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.line.setFont(sfont)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.line.setText('Line')
        self.line.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.linePage))
        # Bar Button
        self.bar = QtWidgets.QPushButton(tframe)
        self.bar.setGeometry(QtCore.QRect(75, 0, 30, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.bar.setFont(sfont)
        self.bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bar.setStyleSheet('QPushButton{color:black;border:none;margin-bottom:3px} QPushButton::hover{color:#0278ae;}')
        self.bar.setText('Bar')
        self.bar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.requestedPage))
        # Pie Button
        self.pie = QtWidgets.QPushButton(tframe)
        self.pie.setGeometry(QtCore.QRect(120, 0, 30, 40))
        sfont = QtGui.QFont()
        sfont.setFamily("Tahoma")
        sfont.setPointSize(12)
        self.pie.setFont(sfont)
        self.pie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pie.setStyleSheet('color:#0278ae;border:none;border-bottom: 3px solid #0278ae;')
        self.pie.setText('Pie')
        self.pie.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.piePage))
        
        vlayout.addWidget(tframe)

        # Frames
        frame = QtWidgets.QFrame(self.piePage)
        glayout = QtWidgets.QGridLayout(frame)
        glayout.setContentsMargins(0, 0, 0, 0)
        glayout.setSpacing(0)

        self.pieData=[]
        self.pieName=[]
        sql = "SELECT Id FROM users WHERE Type='Counsellor';"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            for element in row:
                sql = "SELECT COUNT(Id) FROM meetups WHERE meetupBy="+str(element)
                cursor.execute(sql)
                sdat = cursor.fetchone()
                self.pieData.append(sdat[0])

                sql = "SELECT Name FROM Users WHERE Id="+str(element)
                cursor.execute(sql)
                tdat = cursor.fetchone()
                self.pieName.append(tdat[0])
        print(self.pieData)
        print(self.pieName)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.pie(self.pieData, labels=self.pieName, autopct="%1.1f%%")
        glayout.addWidget(sc, 0, 0, 1, 1)
        
        vlayout.addWidget(frame)
        self.stackedWidget.addWidget(self.piePage)
                
    def changePassword(self):
        if self.opas.text() == gdata[5]:
            np = self.npas.text()
            sql = "UPDATE USERS SET Passw = '" + np + "' WHERE Id =" + str(gdata[0])
            cursor.execute(sql)
            mycon.commit()
            print("Password Changed Successfully")
        else:
            print("Old Password Incorrect")

    def requestMeetupForMyself(self):
        regarding = self.regarding1.toPlainText() 
        sql = "INSERT INTO MEETUPS (MeetupFor, Regarding, Status) VALUES ("+str(gdata[0])+", '"+regarding+"', 'Open')"
        cursor.execute(sql)
        mycon.commit()
        print("Meetup Requested Successfully")

    def scheduleMeetup(self):
        muname = self.uname_s.text()
        mdate = self.date_s.text()
        mtime = self.time_s.text()
        mregarding = self.regarding_s.toPlainText()
        
        sql = "SELECT Id FROM USERS WHERE Uname='"+muname+"'"
        cursor.execute(sql)
        mdata=cursor.fetchone()
        print(mdata[0])
        sql = "INSERT INTO MEETUPS (MeetupBy, MeetupFor, Date, Time, Regarding, Status) VALUES ("+str(gdata[0])+", "+str(mdata[0])+", '"+mdate+"', '"+mtime+"', '"+mregarding+"', 'Assigned');"
        cursor.execute(sql)
        mycon.commit()
        print("Meetup Scheduled Successfully")

    def editMeetup(self):
        mid = self.mid.text()
        mdate = self.date_e.text()
        mtime = self.time_e.text()
        
        sql = "UPDATE MEETUPS SET MeetupBy="+str(gdata[0])+", Date='"+mdate+"', Time='"+mtime+"', Status='Assigned' WHERE Id="+mid+";"
        cursor.execute(sql)
        mycon.commit()
        print("Meetup Edited Successfully")
        
    # Admin Functions
    def createAccount(self):
        nam_a = self.name_a.text()
        una_a = self.uname_a.text()
        pas_a = self.passw_a.text()
        typ_a = self.type_a.currentText()
        print(nam_a, una_a, pas_a, typ_a)
        if nam_a!="" and una_a!="" and pas_a!="" and typ_a!="":
            sql = "INSERT INTO USERS (Name, Uname, Passw, Type, Inst) VALUES ('"+nam_a+"', '"+una_a+"', '"+pas_a+"', '"+typ_a+"', "+str(gdata[3])+");"
            cursor.execute(sql)
            mycon.commit()
            self.indicator_a.setText("Account created successfully!")
        else:
            self.indicator_a.setText("One or more textfields are empty.")
    
    def createAccountsViaCSV(self):
        df = pd.read_csv("CSV Files\\accounts.csv")

        for row in df.iterrows():
            sql = "INSERT INTO USERS (Name, Uname, Passw, Type, Inst) VALUES ('"+row[1]['Name']+"', '"+row[1]['Uname']+"', '"+row[1]['Passw']+"', '"+row[1]['Type']+"', "+str(gdata[3])+",);"
            cursor.execute(sql)
        mycon.commit()

        self.indicator_a.setText("Accounts via CSV created successfully!")
        
    # Register Account
    def registerAccount(self):
        name_r = self.nam.text()
        inst_r = self.ins.text()
        user_r = self.use_r.text()
        pass_r = self.pas_r.text()
        sql = "INSERT INTO INSTITUTIONS (Name) VALUE ('"+inst_r+"')"
        cursor.execute(sql)
        mycon.commit()
        sql = "SELECT Id FROM INSTITUTIONS WHERE Name='"+inst_r+"'"
        cursor.execute(sql)
        data = cursor.fetchone()
        instno = str(data[0])
        sql = "INSERT INTO USERS (Name, Uname, Passw, Type, Inst) VALUES ('"+name_r+"', '"+user_r+"', '"+pass_r+"', 'Admin', "+instno+")"
        cursor.execute(sql)
        mycon.commit()
        self.stackedWidget.setCurrentIndex(4)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
