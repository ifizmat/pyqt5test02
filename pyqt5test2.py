from PyQt5 import uic, QtWidgets

Form, _ = uic.loadUiType("mainwindow.ui")

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.test_label.setText("UI started... OK!")
        self.start_button.clicked.connect(self.start_button_onclick)
        self.stop_button.clicked.connect(self.stop_button_onclick)
        
    def start_button_onclick(self):
        self.test_label.setText("Start")        

    def stop_button_onclick(self):
        self.test_label.setText("Stop")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_win = Ui()
    main_win.show()
    sys.exit(app.exec_())
























