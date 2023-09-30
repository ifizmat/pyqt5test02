from PyQt5 import uic, QtWidgets

Form, _ = uic.loadUiType("mainwindow.ui")

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        
        self.label_test.setText("UI started... OK!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_win = Ui()
    main_win.show()
    sys.exit(app.exec_())
























