import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'DRAG AND DROP'
        self.setWindowTitle(self.title)
        self.resize(400,400)
        
        #Accept Drops
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
    	if event.mimeData().hasUrls():
    		event.accept()
    	else:
    		event.ignore()

    def dropEvent(self, event):
    	files = [u.toLocalFile() for u in event.mimeData().urls()]

    	for file in files:
    		image = cv2.imread(file)
    		cv2.imshow('image', image)
    		cv2.waitKey(0)

        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
