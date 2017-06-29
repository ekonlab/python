__author__ = 'albertogonzalez'


# 1.- Import publications sheet:

# 2.- Create a function to generate the screenshot

# Import modules
import sys
import os
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

# Set the working directory
os.chdir("/home/albertogonzalez/Desktop/bestiario/Quadrigram/2016/marketing/get_screenshots/")
print(os.getcwd() + "\n")


# Class to generate one screenshot

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        self.load(QUrl(url))
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        image.save(output_file)

    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True



# Execute the class that generates the screenshot
s = Screenshot()
s.capture('http://www.quadrigram.com/hosting/aileen_chew/provision_percentage/#p/Page1', 'website.png')



























