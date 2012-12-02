﻿################################################################################
### Copyright © 2012 BlackDragonHunt
### 
### This file is part of the Super Duper Script Editor.
### 
### The Super Duper Script Editor is free software: you can redistribute it
### and/or modify it under the terms of the GNU General Public License as
### published by the Free Software Foundation, either version 3 of the License,
### or (at your option) any later version.
### 
### The Super Duper Script Editor is distributed in the hope that it will be
### useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
### 
### You should have received a copy of the GNU General Public License
### along with the Super Duper Script Editor.
### If not, see <http://www.gnu.org/licenses/>.
################################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFileDialog
from ui_settings import Ui_SettingsMenu

import common
import os.path

class SettingsMenu(QtGui.QDialog):
  def __init__(self, parent=None):
    super(SettingsMenu, self).__init__(parent)
    
    self.ui = Ui_SettingsMenu()
    self.ui.setupUi(self)
    self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    
    # I so don't feel like doing this in Qt Designer. :D
    self.connect(self.ui.btnIsoDir,       QtCore.SIGNAL("clicked()"), self.get_iso_dir)
    self.connect(self.ui.btnIsoFile,      QtCore.SIGNAL("clicked()"), self.get_iso_file)
    self.connect(self.ui.btnUmdDir,       QtCore.SIGNAL("clicked()"), self.get_umd_dir)
    self.connect(self.ui.btnUmd2Dir,      QtCore.SIGNAL("clicked()"), self.get_umd2_dir)
    self.connect(self.ui.btnEbootOrig,    QtCore.SIGNAL("clicked()"), self.get_eboot_orig)
    self.connect(self.ui.btnToc,          QtCore.SIGNAL("clicked()"), self.get_toc)
    self.connect(self.ui.btnToc2,         QtCore.SIGNAL("clicked()"), self.get_toc2)
    self.connect(self.ui.btnTerminology,  QtCore.SIGNAL("clicked()"), self.get_terminology)
    self.connect(self.ui.btnVoice,        QtCore.SIGNAL("clicked()"), self.get_voice)
    self.connect(self.ui.btnCopy,         QtCore.SIGNAL("clicked()"), self.get_copy)
    self.connect(self.ui.btnBackup,       QtCore.SIGNAL("clicked()"), self.get_backup)
    
    # Load in all our info from the config file.
    self.ui.txtIsoDir.setText       (common.editor_config.iso_dir)
    self.ui.txtIsoFile.setText      (common.editor_config.iso_file)
    self.ui.txtUmdDir.setText       (common.editor_config.umdimage_dir)
    self.ui.txtUmd2Dir.setText      (common.editor_config.umdimage2_dir)
    self.ui.txtEbootOrig.setText    (common.editor_config.eboot_orig)
    self.ui.txtToc.setText          (common.editor_config.toc)
    self.ui.txtToc2.setText         (common.editor_config.toc2)
    self.ui.txtTerminology.setText  (common.editor_config.terminology)
    self.ui.txtVoice.setText        (common.editor_config.voice_dir)
    self.ui.txtCopy.setText         (common.editor_config.changes_dir)
    self.ui.txtBackup.setText       (common.editor_config.backup_dir)
  
  ##############################################################################
  ### DIALOG FUNCTIONS
  ##############################################################################
  def get_save_file(self, default, filter):
    file = QFileDialog.getSaveFileName(self, directory = default, filter = filter + ";;All files (*.*)")
    if not file == "":
      return os.path.abspath(file)
    else:
      return file
  
  def get_open_file(self, default, filter):
    file = QFileDialog.getOpenFileName(self, directory = default, filter = filter + ";;All files (*.*)")
    if not file == "":
      return os.path.abspath(file)
    else:
      return file
  
  def get_dir(self, default):
    dir = QFileDialog.getExistingDirectory(self, directory = default)
    if not dir == "":
      return os.path.abspath(dir)
    else:
      return dir
  
  ##############################################################################
  ### DIALOG STUFF
  ##############################################################################
  def get_iso_dir(self):
    dir = self.get_dir(self.ui.txtIsoDir.text())
    if not dir == "":
      self.ui.txtIsoDir.setText(dir)

  def get_iso_file(self):
    file = self.get_save_file(self.ui.txtIsoFile.text(), filter = "PSP ISO Files (*.iso)")
    if not file == "":
      self.ui.txtIsoFile.setText(file)

  def get_umd_dir(self):
    dir = self.get_dir(self.ui.txtUmdDir.text())
    if not dir == "":
      self.ui.txtUmdDir.setText(dir)

  def get_umd2_dir(self):
    dir = self.get_dir(self.ui.txtUmd2Dir.text())
    if not dir == "":
      self.ui.txtUmd2Dir.setText(dir)

  def get_eboot_orig(self):
    file = self.get_open_file(self.ui.txtEbootOrig.text(), filter = "EBOOT-ORIG.BIN (*.bin)")
    if not file == "":
      self.ui.txtEbootOrig.setText(file)

  def get_toc(self):
    file = self.get_open_file(self.ui.txtToc.text(), filter = "!toc.txt (*.txt)")
    if not file == "":
      self.ui.txtToc.setText(file)
    return

  def get_toc2(self):
    file = self.get_open_file(self.ui.txtToc2.text(), filter = "!toc2.txt (*.txt)")
    if not file == "":
      self.ui.txtToc2.setText(file)

  def get_terminology(self):
    file = self.get_open_file(self.ui.txtTerminology.text(), filter = "terminology.csv (*.csv)")
    if not file == "":
      self.ui.txtTerminology.setText(file)

  def get_voice(self):
    dir = self.get_dir(self.ui.txtVoice.text())
    if not dir == "":
      self.ui.txtVoice.setText(dir)

  def get_copy(self):
    dir = self.get_dir(self.ui.txtCopy.text())
    if not dir == "":
      self.ui.txtCopy.setText(dir)

  def get_backup(self):
    dir = self.get_dir(self.ui.txtBackup.text())
    if not dir == "":
      self.ui.txtBackup.setText(dir)
  
  ##############################################################################
  ### SLOTS
  ##############################################################################
  
  ##############################################################################
  ### @fn   accept()
  ### @desc Overrides the Save button.
  ##############################################################################
  def accept(self):
    if self.ui.txtIsoDir.text().length() == 0 or \
       self.ui.txtIsoFile.text().length() == 0 or \
       self.ui.txtUmdDir.text().length() == 0 or \
       self.ui.txtUmd2Dir.text().length() == 0 or \
       self.ui.txtEbootOrig.text().length() == 0 or \
       self.ui.txtToc.text().length() == 0 or \
       self.ui.txtToc2.text().length() == 0 or \
       self.ui.txtTerminology.text().length() == 0 or \
       self.ui.txtVoice.text().length() == 0 or \
       self.ui.txtCopy.text().length() == 0 or \
       self.ui.txtBackup.text().length() == 0:
      QtGui.QMessageBox.critical(self, "Error", "Please fill in all the boxes.")
      return
    
    common.editor_config.iso_dir = unicode(self.ui.txtIsoDir.text().toUtf8(), "UTF-8")
    common.editor_config.iso_file = unicode(self.ui.txtIsoFile.text().toUtf8(), "UTF-8")
    common.editor_config.umdimage_dir = unicode(self.ui.txtUmdDir.text().toUtf8(), "UTF-8")
    common.editor_config.umdimage2_dir = unicode(self.ui.txtUmd2Dir.text().toUtf8(), "UTF-8")
    common.editor_config.eboot_orig = unicode(self.ui.txtEbootOrig.text().toUtf8(), "UTF-8")
    common.editor_config.toc = unicode(self.ui.txtToc.text().toUtf8(), "UTF-8")
    common.editor_config.toc2 = unicode(self.ui.txtToc2.text().toUtf8(), "UTF-8")
    common.editor_config.terminology = unicode(self.ui.txtTerminology.text().toUtf8(), "UTF-8")
    common.editor_config.voice_dir = unicode(self.ui.txtVoice.text().toUtf8(), "UTF-8")
    common.editor_config.changes_dir = unicode(self.ui.txtCopy.text().toUtf8(), "UTF-8")
    common.editor_config.backup_dir = unicode(self.ui.txtBackup.text().toUtf8(), "UTF-8")
    
    common.editor_config.save_config()
    
    super(SettingsMenu, self).accept()
  
  ##############################################################################
  ### @fn   reject()
  ### @desc Overrides the Cancel button.
  ##############################################################################
  def reject(self):
    super(SettingsMenu, self).reject()

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)
  app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
              app,
              QtCore.SLOT("quit()")
             )
  
  form = SettingsMenu()
  form.show()
  sys.exit(app.exec_())

### EOF ###