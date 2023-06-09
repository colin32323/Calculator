import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 720)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(480, 720))
        MainWindow.setMaximumSize(QtCore.QSize(480, 720))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setMaximumSize(QtCore.QSize(16777215, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.display.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setText("")
        self.display.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout_2.addWidget(self.display, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_e = QtWidgets.QPushButton(self.centralwidget)
        self.button_e.setMinimumSize(QtCore.QSize(110, 40))
        self.button_e.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_e.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_e.setFont(font)
        self.button_e.setObjectName("button_e")
        self.gridLayout.addWidget(self.button_e, 0, 0, 1, 1)
        self.button_bracket = QtWidgets.QPushButton(self.centralwidget)
        self.button_bracket.setMinimumSize(QtCore.QSize(110, 40))
        self.button_bracket.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_bracket.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_bracket.setFont(font)
        self.button_bracket.setObjectName("button_bracket")
        self.gridLayout.addWidget(self.button_bracket, 0, 1, 1, 1)
        self.button_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.button_backspace.setMinimumSize(QtCore.QSize(110, 40))
        self.button_backspace.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_backspace.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_backspace.setFont(font)
        self.button_backspace.setObjectName("button_backspace")
        self.gridLayout.addWidget(self.button_backspace, 0, 2, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setMinimumSize(QtCore.QSize(110, 40))
        self.button_clear.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_clear.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 0, 3, 1, 1)
        self.button_log = QtWidgets.QPushButton(self.centralwidget)
        self.button_log.setMinimumSize(QtCore.QSize(110, 40))
        self.button_log.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_log.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_log.setFont(font)
        self.button_log.setObjectName("button_log")
        self.gridLayout.addWidget(self.button_log, 1, 0, 1, 1)
        self.button_ln = QtWidgets.QPushButton(self.centralwidget)
        self.button_ln.setMinimumSize(QtCore.QSize(110, 40))
        self.button_ln.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_ln.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_ln.setFont(font)
        self.button_ln.setObjectName("button_ln")
        self.gridLayout.addWidget(self.button_ln, 1, 1, 1, 1)
        self.button_mod = QtWidgets.QPushButton(self.centralwidget)
        self.button_mod.setMinimumSize(QtCore.QSize(110, 40))
        self.button_mod.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_mod.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_mod.setFont(font)
        self.button_mod.setObjectName("button_mod")
        self.gridLayout.addWidget(self.button_mod, 1, 2, 1, 1)
        self.button_mul = QtWidgets.QPushButton(self.centralwidget)
        self.button_mul.setMinimumSize(QtCore.QSize(110, 40))
        self.button_mul.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_mul.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_mul.setFont(font)
        self.button_mul.setObjectName("button_mul")
        self.gridLayout.addWidget(self.button_mul, 1, 3, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setMinimumSize(QtCore.QSize(110, 40))
        self.button_7.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setMinimumSize(QtCore.QSize(110, 40))
        self.button_8.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setMinimumSize(QtCore.QSize(110, 40))
        self.button_9.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setMinimumSize(QtCore.QSize(110, 40))
        self.button_4.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 3, 0, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setMinimumSize(QtCore.QSize(110, 40))
        self.button_5.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 3, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setMinimumSize(QtCore.QSize(110, 40))
        self.button_6.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 3, 2, 1, 1)
        self.button_sub = QtWidgets.QPushButton(self.centralwidget)
        self.button_sub.setMinimumSize(QtCore.QSize(110, 40))
        self.button_sub.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_sub.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_sub.setFont(font)
        self.button_sub.setObjectName("button_sub")
        self.gridLayout.addWidget(self.button_sub, 3, 3, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setMinimumSize(QtCore.QSize(110, 40))
        self.button_1.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 4, 0, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setMinimumSize(QtCore.QSize(110, 40))
        self.button_2.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 4, 1, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setMinimumSize(QtCore.QSize(110, 40))
        self.button_3.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 4, 2, 1, 1)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setMinimumSize(QtCore.QSize(110, 40))
        self.button_add.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_add.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.gridLayout.addWidget(self.button_add, 4, 3, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setMinimumSize(QtCore.QSize(110, 40))
        self.button_0.setMaximumSize(QtCore.QSize(110, 110))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 5, 0, 1, 1)
        self.button_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.button_decimal.setMinimumSize(QtCore.QSize(110, 40))
        self.button_decimal.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_decimal.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_decimal.setFont(font)
        self.button_decimal.setObjectName("button_decimal")
        self.gridLayout.addWidget(self.button_decimal, 5, 1, 1, 1)
        self.button_sign = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign.setMinimumSize(QtCore.QSize(110, 40))
        self.button_sign.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_sign.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_sign.setFont(font)
        self.button_sign.setObjectName("button_sign")
        self.gridLayout.addWidget(self.button_sign, 5, 2, 1, 1)
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setMinimumSize(QtCore.QSize(110, 40))
        self.button_equals.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_equals.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_equals.setFont(font)
        self.button_equals.setObjectName("button_equals")
        self.gridLayout.addWidget(self.button_equals, 5, 3, 1, 1)
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setMinimumSize(QtCore.QSize(110, 40))
        self.button_div.setMaximumSize(QtCore.QSize(110, 110))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 202, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_div.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_div.setFont(font)
        self.button_div.setObjectName("button_div")
        self.gridLayout.addWidget(self.button_div, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.button_e.setText(_translate("MainWindow", "e^"))
        self.button_bracket.setText(_translate("MainWindow", "( )"))
        self.button_backspace.setText(_translate("MainWindow", "C"))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_log.setText(_translate("MainWindow", "log"))
        self.button_ln.setText(_translate("MainWindow", "ln"))
        self.button_mod.setText(_translate("MainWindow", "%"))
        self.button_mul.setText(_translate("MainWindow", "x"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_sub.setText(_translate("MainWindow", "-"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_decimal.setText(_translate("MainWindow", "."))
        self.button_sign.setText(_translate("MainWindow", "+/-"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_div.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Calculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
