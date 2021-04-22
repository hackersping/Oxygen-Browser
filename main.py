import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # home button
        home_btn = QAction(QIcon("home.png"), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        navbar.addSeparator()

        # adding back action to the tool bar
        back_btn = QAction(QIcon("back.png"), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # adding forward action to the tool bar
        forward_btn = QAction(QIcon("forward.png"), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        navbar.addSeparator()

        # adding reload action to the tool bar
        reload_btn = QAction(QIcon("undo.png"), 'Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        navbar.addSeparator()
        navbar.addSeparator()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        # adding stop action to the tool bar
        navbar.addSeparator()
        stop_btn = QAction(QIcon("cross.png"), 'Remove', self)
        stop_btn.setStatusTip("Stop loading current page")

        # adding action to the stop button
        # making browser to stop
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl("https://" + url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Oxygen Browser')

window = MainWindow()
app.exec_()
