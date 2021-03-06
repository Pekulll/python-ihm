from PyQt5.QtWidgets import *

def box(icon, name, description, details=None, callback=None):
    box = QMessageBox()
    
    box.setIcon(icon)
    box.setWindowTitle("Gandalf (2022.02.10 • par Pékul)")
    box.setText(name)
    box.setInformativeText(description)
    box.setStandardButtons(QMessageBox.Ok)
    
    if details is not None: box.setDetailedText(details)
    if callback is not None: box.buttonClicked.connect(callback)
    
    box.exec_()

def info_box(name, description, callback=None):
    box(QMessageBox.Information, name, description, callback=callback)

def warn_box(name, description, details=None, callback=None):
    box(QMessageBox.Warning, name, description, details=details, callback=callback)

def error_box(name, description, details=None, callback=None):
    box(QMessageBox.Critical, name, description, details=details, callback=callback)
