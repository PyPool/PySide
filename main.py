import sys
from PySide import QtGui, QtCore
from main_window import Ui_MainWindow


class PyPoolMainWindow(QtGui.QMainWindow):
    log = QtCore.Signal(str)

    def __init__(self, parent=None):
        # Initialise the window and populate it with the GUI elements we've created in QtDesigner.
        super(PyPoolMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up the graphics widget.
        self.svg = None
        self.graphics_item = None
        self.scene = QtGui.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = PyPoolMainWindow()
    mySW.show()
    sys.exit(app.exec_())