
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from pprint import pprint as pp
from binance.client import Client
from PyQt5.QtWidgets import QMenu, QWidget, QAction, QDesktopWidget, QMainWindow, QApplication, QToolTip, QPushButton, QMessageBox, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication



class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        api_key = 'gUuYNVvJVIwMjcXXSF9yNpg7xd1bzoQPibRIoN5DkycJZL8IbxH7i5g4IeyXPyB0'
        api_secret = 'sen1iAzGVE1JyRutNVC8rfRLfH8RwiZqJAGqXUcP5GsMY87CXsDaMxnx25pzDZhF'
        self.client = Client(api_key, api_secret)

        self.initUI()
        self.main()

    def main(self):
        prices = self.client.get_all_tickers()
        pp(prices)

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 300, 220)
        self.setFixedSize(300, 300)
        self.center()
        self.setWindowTitle('Crypto')
        self.setWindowIcon(QIcon('web.png'))

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(qApp.quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 80)

        exitAct = QAction(QIcon('/home/hazik/Pictures/material-design-icons/action/1x_web/ic_exit_to_app_white_48dp.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Z')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
