import logging
#from TraceParser import Trace
import sys
import matplotlib
from PyQt5 import QtGui, QtCore, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

# matplotlib.use('Qt5Agg')


# class MyMplCanvas(FigureCanvas):
#
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         #self.trace = Trace('E:\\PySpace\Collector\\AES trace simulation.trs')
#         self.trace = Trace('D:\\trace\\aes\\aes_template.trs')
#         self.trace.parseTraceHeader()
#         self.axes.hold(False)
#         self.compute_initial_figure()
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#         FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
#
#     def compute_initial_figure(self):
#         # t = arange(0.0, 3.0, 0.01)
#         # s = sin(2*pi*t)
#         traceList = self.trace.getTrace(0)
#         self.axes.plot(traceList[2])
#
#
# class ApplicationWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         QtWidgets.QMainWindow.__init__(self)
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
#         self.setWindowTitle("application main window")
#         self.file_menu = QtWidgets.QMenu('&File', self)
#         self.file_menu.addAction('&Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
#         self.menuBar().addMenu(self.file_menu)
#         self.help_menu = QtWidgets.QMenu('&Help', self)
#         self.menuBar().addSeparator()
#         self.menuBar().addMenu(self.help_menu)
#
#         self.help_menu.addAction('&About', self.about)
#         self.main_widget = QtWidgets.QWidget(self)
#
#         l = QtWidgets.QVBoxLayout(self.main_widget)
#         sc = MyMplCanvas(self.main_widget, width=5, height=5, dpi=100)
#         l.addWidget(sc)
#
#         self.main_widget.setFocus()
#         self.setCentralWidget(self.main_widget)
#
#         self.statusBar().showMessage("All hail matplotlib!", 2000)
#
#     def fileQuit(self):
#         self.close()
#
#     def closeEvent(self):
#         self.fileQuit()
#
#     def about(self):
#         QtGui.QMessageBox.about(self, "about", "about")

if __name__ == '__main__':
    # logging.basicConfig(filename='logger.log', level=logging.DEBUG)
    # traceSample = Trace('E:\\PySpace\Collector\\test.trs')
    # traceSample.parseTraceHeader()
    # x = b'\x41\x42'.hex()
    # qApp = QtWidgets.QApplication(sys.argv)
    # aw = ApplicationWindow()
    # aw.setWindowTitle("Test Program")
    # aw.show()
    # sys.exit(qApp.exec_())
    #value = arange(1, 100, 0.00001)
    #trace = Trace('E:\\PySpace\Collector\\test.trs')
    #trace.setPointCount(10000000)
    #trace.setTraceNumber(1)
    #trace.setSampleCoding(1, 4)
    #trace.generateTraceHeader()
    #trace.generateTrace(value)
    #trace.generateTrace([0.0, 1.2, 2.4, 3.2, 4.4, 5.12, 6.89, 7.22, 8.888, 9.123])
    #trace.generateTrace([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    qApp = QtWidgets.QApplication(sys.argv)
    button = QtWidgets.QPushButton("Quit")
    button.clicked.connect(QtWidgets.QApplication.quit)

    button.show()
    sys.exit(qApp.exec_())



