# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\ui\settings.ui'
#
# Created: Thu Dec 06 17:06:57 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsMenu(object):
    def setupUi(self, SettingsMenu):
        SettingsMenu.setObjectName(_fromUtf8("SettingsMenu"))
        SettingsMenu.resize(505, 362)
        SettingsMenu.setWindowTitle(QtGui.QApplication.translate("SettingsMenu", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/monokuma-green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsMenu.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsMenu)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(SettingsMenu)
        self.label_3.setText(QtGui.QApplication.translate("SettingsMenu", "umdimage Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(SettingsMenu)
        self.label_4.setText(QtGui.QApplication.translate("SettingsMenu", "umdimage2 Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(SettingsMenu)
        self.label.setText(QtGui.QApplication.translate("SettingsMenu", "ISO Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SettingsMenu)
        self.label_2.setText(QtGui.QApplication.translate("SettingsMenu", "ISO File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(SettingsMenu)
        self.label_6.setText(QtGui.QApplication.translate("SettingsMenu", "EBOOT.BIN (Original)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(SettingsMenu)
        self.label_7.setText(QtGui.QApplication.translate("SettingsMenu", "Voice directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(SettingsMenu)
        self.label_8.setText(QtGui.QApplication.translate("SettingsMenu", "Copy changes to...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_9 = QtGui.QLabel(SettingsMenu)
        self.label_9.setText(QtGui.QApplication.translate("SettingsMenu", "Make backup to...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.txtIsoDir = QtGui.QLineEdit(SettingsMenu)
        self.txtIsoDir.setObjectName(_fromUtf8("txtIsoDir"))
        self.gridLayout.addWidget(self.txtIsoDir, 0, 1, 1, 1)
        self.txtIsoFile = QtGui.QLineEdit(SettingsMenu)
        self.txtIsoFile.setObjectName(_fromUtf8("txtIsoFile"))
        self.gridLayout.addWidget(self.txtIsoFile, 1, 1, 1, 1)
        self.txtUmdDir = QtGui.QLineEdit(SettingsMenu)
        self.txtUmdDir.setObjectName(_fromUtf8("txtUmdDir"))
        self.gridLayout.addWidget(self.txtUmdDir, 2, 1, 1, 1)
        self.txtUmd2Dir = QtGui.QLineEdit(SettingsMenu)
        self.txtUmd2Dir.setObjectName(_fromUtf8("txtUmd2Dir"))
        self.gridLayout.addWidget(self.txtUmd2Dir, 3, 1, 1, 1)
        self.txtEbootOrig = QtGui.QLineEdit(SettingsMenu)
        self.txtEbootOrig.setObjectName(_fromUtf8("txtEbootOrig"))
        self.gridLayout.addWidget(self.txtEbootOrig, 4, 1, 1, 1)
        self.txtVoice = QtGui.QLineEdit(SettingsMenu)
        self.txtVoice.setObjectName(_fromUtf8("txtVoice"))
        self.gridLayout.addWidget(self.txtVoice, 8, 1, 1, 1)
        self.txtCopy = QtGui.QLineEdit(SettingsMenu)
        self.txtCopy.setObjectName(_fromUtf8("txtCopy"))
        self.gridLayout.addWidget(self.txtCopy, 9, 1, 1, 1)
        self.txtBackup = QtGui.QLineEdit(SettingsMenu)
        self.txtBackup.setObjectName(_fromUtf8("txtBackup"))
        self.gridLayout.addWidget(self.txtBackup, 10, 1, 1, 1)
        self.btnIsoDir = QtGui.QPushButton(SettingsMenu)
        self.btnIsoDir.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIsoDir.setObjectName(_fromUtf8("btnIsoDir"))
        self.gridLayout.addWidget(self.btnIsoDir, 0, 2, 1, 1)
        self.btnIsoFile = QtGui.QPushButton(SettingsMenu)
        self.btnIsoFile.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIsoFile.setObjectName(_fromUtf8("btnIsoFile"))
        self.gridLayout.addWidget(self.btnIsoFile, 1, 2, 1, 1)
        self.btnUmdDir = QtGui.QPushButton(SettingsMenu)
        self.btnUmdDir.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUmdDir.setObjectName(_fromUtf8("btnUmdDir"))
        self.gridLayout.addWidget(self.btnUmdDir, 2, 2, 1, 1)
        self.btnUmd2Dir = QtGui.QPushButton(SettingsMenu)
        self.btnUmd2Dir.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUmd2Dir.setObjectName(_fromUtf8("btnUmd2Dir"))
        self.gridLayout.addWidget(self.btnUmd2Dir, 3, 2, 1, 1)
        self.btnEbootOrig = QtGui.QPushButton(SettingsMenu)
        self.btnEbootOrig.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEbootOrig.setObjectName(_fromUtf8("btnEbootOrig"))
        self.gridLayout.addWidget(self.btnEbootOrig, 4, 2, 1, 1)
        self.btnVoice = QtGui.QPushButton(SettingsMenu)
        self.btnVoice.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnVoice.setObjectName(_fromUtf8("btnVoice"))
        self.gridLayout.addWidget(self.btnVoice, 8, 2, 1, 1)
        self.btnCopy = QtGui.QPushButton(SettingsMenu)
        self.btnCopy.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCopy.setObjectName(_fromUtf8("btnCopy"))
        self.gridLayout.addWidget(self.btnCopy, 9, 2, 1, 1)
        self.btnBackup = QtGui.QPushButton(SettingsMenu)
        self.btnBackup.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBackup.setObjectName(_fromUtf8("btnBackup"))
        self.gridLayout.addWidget(self.btnBackup, 10, 2, 1, 1)
        self.label_10 = QtGui.QLabel(SettingsMenu)
        self.label_10.setText(QtGui.QApplication.translate("SettingsMenu", "!toc.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_11 = QtGui.QLabel(SettingsMenu)
        self.label_11.setText(QtGui.QApplication.translate("SettingsMenu", "!toc2.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.txtToc = QtGui.QLineEdit(SettingsMenu)
        self.txtToc.setObjectName(_fromUtf8("txtToc"))
        self.gridLayout.addWidget(self.txtToc, 5, 1, 1, 1)
        self.txtToc2 = QtGui.QLineEdit(SettingsMenu)
        self.txtToc2.setObjectName(_fromUtf8("txtToc2"))
        self.gridLayout.addWidget(self.txtToc2, 6, 1, 1, 1)
        self.btnToc = QtGui.QPushButton(SettingsMenu)
        self.btnToc.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnToc.setObjectName(_fromUtf8("btnToc"))
        self.gridLayout.addWidget(self.btnToc, 5, 2, 1, 1)
        self.btnToc2 = QtGui.QPushButton(SettingsMenu)
        self.btnToc2.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnToc2.setObjectName(_fromUtf8("btnToc2"))
        self.gridLayout.addWidget(self.btnToc2, 6, 2, 1, 1)
        self.label_5 = QtGui.QLabel(SettingsMenu)
        self.label_5.setText(QtGui.QApplication.translate("SettingsMenu", "Terminology", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.txtTerminology = QtGui.QLineEdit(SettingsMenu)
        self.txtTerminology.setObjectName(_fromUtf8("txtTerminology"))
        self.gridLayout.addWidget(self.txtTerminology, 7, 1, 1, 1)
        self.btnTerminology = QtGui.QPushButton(SettingsMenu)
        self.btnTerminology.setText(QtGui.QApplication.translate("SettingsMenu", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTerminology.setObjectName(_fromUtf8("btnTerminology"))
        self.gridLayout.addWidget(self.btnTerminology, 7, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsMenu)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsMenu)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsMenu.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsMenu.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsMenu)
        SettingsMenu.setTabOrder(self.txtIsoDir, self.btnIsoDir)
        SettingsMenu.setTabOrder(self.btnIsoDir, self.txtIsoFile)
        SettingsMenu.setTabOrder(self.txtIsoFile, self.btnIsoFile)
        SettingsMenu.setTabOrder(self.btnIsoFile, self.txtUmdDir)
        SettingsMenu.setTabOrder(self.txtUmdDir, self.btnUmdDir)
        SettingsMenu.setTabOrder(self.btnUmdDir, self.txtUmd2Dir)
        SettingsMenu.setTabOrder(self.txtUmd2Dir, self.btnUmd2Dir)
        SettingsMenu.setTabOrder(self.btnUmd2Dir, self.txtEbootOrig)
        SettingsMenu.setTabOrder(self.txtEbootOrig, self.btnEbootOrig)
        SettingsMenu.setTabOrder(self.btnEbootOrig, self.txtToc)
        SettingsMenu.setTabOrder(self.txtToc, self.btnToc)
        SettingsMenu.setTabOrder(self.btnToc, self.txtToc2)
        SettingsMenu.setTabOrder(self.txtToc2, self.btnToc2)
        SettingsMenu.setTabOrder(self.btnToc2, self.txtVoice)
        SettingsMenu.setTabOrder(self.txtVoice, self.btnVoice)
        SettingsMenu.setTabOrder(self.btnVoice, self.txtCopy)
        SettingsMenu.setTabOrder(self.txtCopy, self.btnCopy)
        SettingsMenu.setTabOrder(self.btnCopy, self.txtBackup)
        SettingsMenu.setTabOrder(self.txtBackup, self.btnBackup)

    def retranslateUi(self, SettingsMenu):
        pass

import icons_rc
