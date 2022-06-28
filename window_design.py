

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 506)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Anek_Latin;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #505050;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: 	#787878;\n"
"}\n"
"	")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_ans = QLabel(self.centralwidget)
        self.label_ans.setObjectName(u"label_ans")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_ans.sizePolicy().hasHeightForWidth())
        self.label_ans.setSizePolicy(sizePolicy1)
        self.label_ans.setStyleSheet(u"font-size: 20pt;\n"
"color: #909090;")
        self.label_ans.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_ans)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setLayoutDirection(Qt.RightToLeft)
        self.le_entry.setStyleSheet(u"font-size: 45pt;\n"
"border: none;")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setDragEnabled(False)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_plus = QPushButton(self.centralwidget)
        self.button_plus.setObjectName(u"button_plus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_plus, 5, 5, 1, 1)

        self.button_dot = QPushButton(self.centralwidget)
        self.button_dot.setObjectName(u"button_dot")
        sizePolicy2.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_dot, 6, 4, 1, 1)

        self.button_multiply = QPushButton(self.centralwidget)
        self.button_multiply.setObjectName(u"button_multiply")
        sizePolicy2.setHeightForWidth(self.button_multiply.sizePolicy().hasHeightForWidth())
        self.button_multiply.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_multiply, 3, 5, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_1, 5, 1, 1, 1)

        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy2.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_7, 3, 1, 1, 1)

        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy2.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_8, 3, 3, 1, 1)

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy2.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_5, 4, 3, 1, 1)

        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy2.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_6, 4, 4, 1, 1)

        self.button_negative = QPushButton(self.centralwidget)
        self.button_negative.setObjectName(u"button_negative")
        sizePolicy2.setHeightForWidth(self.button_negative.sizePolicy().hasHeightForWidth())
        self.button_negative.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_negative, 6, 1, 1, 1)

        self.button_divide = QPushButton(self.centralwidget)
        self.button_divide.setObjectName(u"button_divide")
        sizePolicy2.setHeightForWidth(self.button_divide.sizePolicy().hasHeightForWidth())
        self.button_divide.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_divide, 2, 5, 1, 1)

        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_9, 3, 4, 1, 1)

        self.button_equals = QPushButton(self.centralwidget)
        self.button_equals.setObjectName(u"button_equals")
        sizePolicy2.setHeightForWidth(self.button_equals.sizePolicy().hasHeightForWidth())
        self.button_equals.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_equals, 6, 5, 1, 1)

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy2.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_4, 4, 1, 1, 1)

        self.button_0 = QPushButton(self.centralwidget)
        self.button_0.setObjectName(u"button_0")
        sizePolicy2.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_0, 6, 3, 1, 1)

        self.button_minus = QPushButton(self.centralwidget)
        self.button_minus.setObjectName(u"button_minus")
        sizePolicy2.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_minus, 4, 5, 1, 1)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy2.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_3, 5, 4, 1, 1)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_2, 5, 3, 1, 1)

        self.button_backspace = QPushButton(self.centralwidget)
        self.button_backspace.setObjectName(u"button_backspace")
        sizePolicy2.setHeightForWidth(self.button_backspace.sizePolicy().hasHeightForWidth())
        self.button_backspace.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/Icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_backspace.setIcon(icon)
        self.button_backspace.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.button_backspace, 2, 4, 1, 1)

        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy2.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_clear, 2, 3, 1, 1)

        self.button_ce = QPushButton(self.centralwidget)
        self.button_ce.setObjectName(u"button_ce")
        sizePolicy2.setHeightForWidth(self.button_ce.sizePolicy().hasHeightForWidth())
        self.button_ce.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.button_ce, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_ans.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.button_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.button_dot.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.button_dot.setShortcut(QCoreApplication.translate("MainWindow", u"., ,", None))
#endif // QT_CONFIG(shortcut)
        self.button_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.button_multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.button_negative.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.button_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.button_divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.button_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.button_equals.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.button_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.button_backspace.setText("")
        self.button_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"backspace", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.button_ce.setShortcut(QCoreApplication.translate("MainWindow", u"ESC", None))
    # retranslateUi

