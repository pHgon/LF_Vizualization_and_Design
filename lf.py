# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 695)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 131, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 109, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 58, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 20, 901, 631))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setMouseTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_nitidez = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_nitidez.setFont(font)
        self.spinBox_nitidez.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_nitidez.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_nitidez.setSuffix("")
        self.spinBox_nitidez.setMinimum(-100)
        self.spinBox_nitidez.setMaximum(100)
        self.spinBox_nitidez.setSingleStep(1)
        self.spinBox_nitidez.setProperty("value", 0)
        self.spinBox_nitidez.setDisplayIntegerBase(10)
        self.spinBox_nitidez.setObjectName("spinBox_nitidez")
        self.gridLayout.addWidget(self.spinBox_nitidez, 3, 2, 1, 1)
        self.label_brilho = QtWidgets.QLabel(self.groupBox_2)
        self.label_brilho.setObjectName("label_brilho")
        self.gridLayout.addWidget(self.label_brilho, 1, 0, 1, 1)
        self.label_nitidez = QtWidgets.QLabel(self.groupBox_2)
        self.label_nitidez.setObjectName("label_nitidez")
        self.gridLayout.addWidget(self.label_nitidez, 3, 0, 1, 1)
        self.label_contraste = QtWidgets.QLabel(self.groupBox_2)
        self.label_contraste.setObjectName("label_contraste")
        self.gridLayout.addWidget(self.label_contraste, 2, 0, 1, 1)
        self.label_saturacao = QtWidgets.QLabel(self.groupBox_2)
        self.label_saturacao.setObjectName("label_saturacao")
        self.gridLayout.addWidget(self.label_saturacao, 4, 0, 1, 1)
        self.slider_contraste = QtWidgets.QSlider(self.groupBox_2)
        self.slider_contraste.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_contraste.setMinimum(-100)
        self.slider_contraste.setMaximum(100)
        self.slider_contraste.setProperty("value", 0)
        self.slider_contraste.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contraste.setObjectName("slider_contraste")
        self.gridLayout.addWidget(self.slider_contraste, 2, 1, 1, 1)
        self.slider_saturacao = QtWidgets.QSlider(self.groupBox_2)
        self.slider_saturacao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_saturacao.setMinimum(-100)
        self.slider_saturacao.setMaximum(100)
        self.slider_saturacao.setProperty("value", 0)
        self.slider_saturacao.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturacao.setObjectName("slider_saturacao")
        self.gridLayout.addWidget(self.slider_saturacao, 4, 1, 1, 1)
        self.slider_brilho = QtWidgets.QSlider(self.groupBox_2)
        self.slider_brilho.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.slider_brilho.setMouseTracking(False)
        self.slider_brilho.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_brilho.setMinimum(-100)
        self.slider_brilho.setMaximum(100)
        self.slider_brilho.setProperty("value", 0)
        self.slider_brilho.setTracking(True)
        self.slider_brilho.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brilho.setObjectName("slider_brilho")
        self.gridLayout.addWidget(self.slider_brilho, 1, 1, 1, 1)
        self.spinBox_saturacao = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_saturacao.setFont(font)
        self.spinBox_saturacao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_saturacao.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_saturacao.setSuffix("")
        self.spinBox_saturacao.setMinimum(-100)
        self.spinBox_saturacao.setMaximum(100)
        self.spinBox_saturacao.setSingleStep(1)
        self.spinBox_saturacao.setProperty("value", 0)
        self.spinBox_saturacao.setDisplayIntegerBase(10)
        self.spinBox_saturacao.setObjectName("spinBox_saturacao")
        self.gridLayout.addWidget(self.spinBox_saturacao, 4, 2, 1, 1)
        self.spinBox_contraste = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_contraste.setFont(font)
        self.spinBox_contraste.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_contraste.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_contraste.setSuffix("")
        self.spinBox_contraste.setMinimum(-100)
        self.spinBox_contraste.setMaximum(100)
        self.spinBox_contraste.setProperty("value", 0)
        self.spinBox_contraste.setObjectName("spinBox_contraste")
        self.gridLayout.addWidget(self.spinBox_contraste, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.slider_nitidez = QtWidgets.QSlider(self.groupBox_2)
        self.slider_nitidez.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_nitidez.setMinimum(-100)
        self.slider_nitidez.setMaximum(100)
        self.slider_nitidez.setProperty("value", 0)
        self.slider_nitidez.setOrientation(QtCore.Qt.Horizontal)
        self.slider_nitidez.setObjectName("slider_nitidez")
        self.gridLayout.addWidget(self.slider_nitidez, 3, 1, 1, 1)
        self.spinBox_brilho = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_brilho.setFont(font)
        self.spinBox_brilho.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_brilho.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_brilho.setSuffix("")
        self.spinBox_brilho.setMinimum(-100)
        self.spinBox_brilho.setMaximum(100)
        self.spinBox_brilho.setProperty("value", 0)
        self.spinBox_brilho.setDisplayIntegerBase(10)
        self.spinBox_brilho.setObjectName("spinBox_brilho")
        self.gridLayout.addWidget(self.spinBox_brilho, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 430, 141, 61))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 430, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 510, 141, 61))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 510, 141, 61))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 590, 141, 61))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 590, 141, 61))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setObjectName("pushButton_6")
        self.l_ang_hoz = QtWidgets.QLabel(self.centralwidget)
        self.l_ang_hoz.setGeometry(QtCore.QRect(300, 190, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_ang_hoz.setFont(font)
        self.l_ang_hoz.setObjectName("l_ang_hoz")
        self.l_ang_ver = QtWidgets.QLabel(self.centralwidget)
        self.l_ang_ver.setGeometry(QtCore.QRect(340, 190, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_ang_ver.setFont(font)
        self.l_ang_ver.setObjectName("l_ang_ver")
        self.label_hist = QtWidgets.QLabel(self.centralwidget)
        self.label_hist.setGeometry(QtCore.QRect(30, 100, 201, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_hist.setPalette(palette)
        self.label_hist.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_hist.setMouseTracking(True)
        self.label_hist.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_hist.setAutoFillBackground(True)
        self.label_hist.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_hist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_hist.setLineWidth(5)
        self.label_hist.setText("")
        self.label_hist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hist.setIndent(0)
        self.label_hist.setObjectName("label_hist")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 161, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(278, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.radioButton_red = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_red.setGeometry(QtCore.QRect(40, 190, 51, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_red.setPalette(palette)
        self.radioButton_red.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_red.setChecked(True)
        self.radioButton_red.setAutoExclusive(False)
        self.radioButton_red.setObjectName("radioButton_red")
        self.radioButton_green = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_green.setGeometry(QtCore.QRect(100, 190, 61, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_green.setPalette(palette)
        self.radioButton_green.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_green.setChecked(True)
        self.radioButton_green.setAutoExclusive(False)
        self.radioButton_green.setObjectName("radioButton_green")
        self.radioButton_blue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_blue.setGeometry(QtCore.QRect(170, 190, 61, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 43, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.radioButton_blue.setPalette(palette)
        self.radioButton_blue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_blue.setChecked(True)
        self.radioButton_blue.setAutoExclusive(False)
        self.radioButton_blue.setObjectName("radioButton_blue")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 0, 121, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.radioButton_original = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_original.setGeometry(QtCore.QRect(150, 40, 83, 16))
        self.radioButton_original.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_original.setObjectName("radioButton_original")
        self.radioButton_maximizar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_maximizar.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.radioButton_maximizar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_maximizar.setChecked(True)
        self.radioButton_maximizar.setObjectName("radioButton_maximizar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.slider_brilho.valueChanged['int'].connect(self.spinBox_brilho.setValue)
        self.spinBox_brilho.valueChanged['int'].connect(self.slider_brilho.setValue)
        self.slider_saturacao.valueChanged['int'].connect(self.spinBox_saturacao.setValue)
        self.spinBox_saturacao.valueChanged['int'].connect(self.slider_saturacao.setValue)
        self.slider_contraste.valueChanged['int'].connect(self.spinBox_contraste.setValue)
        self.spinBox_contraste.valueChanged['int'].connect(self.slider_contraste.setValue)
        self.slider_nitidez.valueChanged['int'].connect(self.spinBox_nitidez.setValue)
        self.spinBox_nitidez.valueChanged['int'].connect(self.slider_nitidez.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LytroFake"))
        self.label_brilho.setText(_translate("MainWindow", "Brilho"))
        self.label_nitidez.setText(_translate("MainWindow", "Nitidez"))
        self.label_contraste.setText(_translate("MainWindow", "Contraste"))
        self.label_saturacao.setText(_translate("MainWindow", "Saturação"))
        self.label_11.setText(_translate("MainWindow", "Cores"))
        self.pushButton.setText(_translate("MainWindow", "Gerar Depth Map"))
        self.pushButton_2.setText(_translate("MainWindow", "Gerar todos\n"
"Depth Maps"))
        self.pushButton_3.setText(_translate("MainWindow", "Upscaling 2x"))
        self.pushButton_4.setText(_translate("MainWindow", "Upscaling 4x"))
        self.pushButton_5.setText(_translate("MainWindow", "Visão de Mosca"))
        self.pushButton_6.setText(_translate("MainWindow", "ROI ZigZag"))
        self.l_ang_hoz.setText(_translate("MainWindow", "x:"))
        self.l_ang_ver.setText(_translate("MainWindow", "y:"))
        self.label_9.setText(_translate("MainWindow", "Histograma"))
        self.label_10.setText(_translate("MainWindow", "Minimapa"))
        self.radioButton_red.setText(_translate("MainWindow", "Red"))
        self.radioButton_green.setText(_translate("MainWindow", "Green"))
        self.radioButton_blue.setText(_translate("MainWindow", "Blue"))
        self.label_12.setText(_translate("MainWindow", "Exibição"))
        self.radioButton_original.setText(_translate("MainWindow", "Original"))
        self.radioButton_maximizar.setText(_translate("MainWindow", "Maximizar"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))

