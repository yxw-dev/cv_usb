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
        self.cam_time2 = QtCore.QTimer()
        self.cam_time.timeout.connect(self.show_pic)
        self.cam_time2.timeout.connect(self.show_pic2)
        self.open_cam.clicked.connect(self.start_grap)
        self.open_cam_2.clicked.connect(self.start_grap2)
        self.close_cam.clicked.connect(self.stop_cam)


    def start_grap(self):
        self.cap1 = cv2.VideoCapture(2+ cv2.CAP_DSHOW)
        self.cam_time.start(100)

    def start_grap2(self):
        self.cap2 = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
        self.cam_time2.start(100)

    def stop_cam(self):
        self.cap1.release()
        self.cam_time.stop()

    def show_pic(self):
        ret, img = self.cap1.read()
        if not ret:
            print('read error!\n')
            return
        cv2.flip(img, 1, img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label.setPixmap(pixmap)

    def show_pic2(self):
        ret_2, img_2 = self.cap2.read()
        if not ret_2:
            print('read error!\n')
            return
        cv2.flip(img_2, 1, img_2)
        cur_frame = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label_2.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())