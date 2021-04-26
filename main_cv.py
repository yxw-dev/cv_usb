import cv2
import sys
from cv_show import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyMainWindow(QMainWindow , Ui_MainWindow):
    def __init__(self ):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.cam_time = QtCore.QTimer()
        self.cam_time.timeout.connect(self.show_pic)
        self.open_cam.clicked.connect(self.start_grap)
        self.close_cam.clicked.connect(self.stop_cam)

    def start_grap(self):
        self.cap = cv2.VideoCapture(0)
        self.cam_time.start(100)

    def stop_cam(self):
        self.cap.release()
        self.cam_time.stop()

    def show_pic(self):
        ret, img = self.cap.read()
        if not ret:
            print('read error!\n')
            return
        cv2.flip(img, 1, img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())