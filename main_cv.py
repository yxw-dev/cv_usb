import cv2
import sys
import time
from cv_show import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyMainWindow(QMainWindow , Ui_MainWindow):
    def __init__(self ):
        super(MyMainWindow, self).__init__()
        self.mear_step = 20
        self.setupUi(self)
        self.start_time1 = time.time()
        self.start_time2 = time.time()
        self.frame1=0
        self.frame2=0
        self.width_step_max = 50
        self.height_step_max = 50
        self.width_step = 50        #横向两红线间隔默认值
        self.height_step = 50       #纵向两红线间隔默认值
        self.doubleSpinBox.setValue(self.height_step)
        self.doubleSpinBox_2.setValue(self.width_step)
        self.cam_time = QtCore.QTimer()
        self.cam_time2 = QtCore.QTimer()
        self.cam_time.timeout.connect(self.show_pic)
        self.cam_time2.timeout.connect(self.show_pic2)
        self.actionExit.triggered.connect(self.close)
        self.action_1.triggered.connect(self.start_grap)
        self.action_2.triggered.connect(self.start_grap2)
        self.setFocus()

    #键盘监控事件
    def keyPressEvent(self,event):
        if(event.key() == Qt.Key_Q):
            self.close()
        if(event.key() == Qt.Key_F):
            self.start_grap()
        if (event.key() == Qt.Key_B):
            self.start_grap2()
        if(event.key() == Qt.Key_A):
            self.horizontalSlider.setValue(self.horizontalSlider.value() - 1)
            self.drawline()
        if (event.key() == Qt.Key_D):
            self.horizontalSlider.setValue(self.horizontalSlider.value() + 1)
            self.drawline()
        if(event.key() == Qt.Key_W):
            if(self.width_step < self.width_step_max):
                self.width_step = self.width_step + 1
            else:
                self.width_step = 0
            self.drawline()
            self.doubleSpinBox_2.setValue(self.width_step)
        if (event.key() == Qt.Key_S):
            if (self.width_step > 0):
                self.width_step = self.width_step - 1
            else:
                self.width_step = self.width_step_max
            self.drawline()
            self.doubleSpinBox_2.setValue(self.width_step)

        if (event.key() == Qt.Key_Left):
            self.verticalSlider.setValue(self.verticalSlider.value() + 1)
            self.drawline()
        if (event.key() == Qt.Key_Right):
            self.verticalSlider.setValue(self.verticalSlider.value() - 1)
            self.drawline()
        if (event.key() == Qt.Key_Up):
            if (self.height_step < self.height_step_max):
                self.height_step = self.height_step + 1
            else:
                self.height_step = 0
            self.drawline()
            self.doubleSpinBox.setValue(self.height_step)
        if (event.key() == Qt.Key_Down):
            if (self.height_step > 0):
                self.height_step = self.height_step - 1
            else:
                self.height_step = self.height_step_max
            self.drawline()
            self.doubleSpinBox.setValue(self.height_step)



    def drawline(self):
        print(1)
    #移动滑块调节指示线位置
    def moveline(self):
        sta_x = self.horizontalSlider.x()
        sta_y = self.line_2.y()
        length = float(self.horizontalSlider.width()) / 100.0
        sta = sta_x + length/3
        val = self.horizontalSlider.value()
        self.line.move(sta + val*length + val/15 - self.mear_step/2 , sta_y)
        self.line_2.move(sta + val*length + val/15 + self.mear_step/2 , sta_y)

    def start_grap(self):
        self.start_time1 = time.time()
        self.frame1=0
        self.cap1 = cv2.VideoCapture(1+ cv2.CAP_DSHOW)
        self.cam_time.start(60)
        self.label_5.setText("正面相机：运行")

    def start_grap2(self):
        self.start_time2 = time.time()
        self.frame2=0
        self.cap2 = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        self.cam_time2.start(60)
        self.label_7.setText("侧面相机：运行")

    def stop_cam(self):
        self.cap1.release()
        self.cam_time.stop()

    def show_pic(self):
        ret, img = self.cap1.read()
        if not ret:
            print('read error!\n')
            self.label_5.setText("正面相机：打开失败")
            self.cam_time.stop()
            return
        #cv2.flip(img, 1, img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label.setPixmap(pixmap)
        end_time1 = time.time()
        diff_time1 = (end_time1 - self.start_time1)
        self.frame1 = self.frame1 + 1
        if diff_time1>1:
            self.start_time1 = end_time1
            self.label_6.setText('帧率(1):' + str(self.frame1))
            self.frame1 = 0

    def show_pic2(self):
        ret_2, img_2 = self.cap2.read()
        if not ret_2:
            print('read error!\n')
            self.label_7.setText("侧面相机：打开失败")
            self.cam_time2.stop()
            return
        cv2.flip(img_2, 1, img_2)
        cur_frame = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.label_2.setPixmap(pixmap)
        end_time2 = time.time()
        diff_time2 = (end_time2 - self.start_time2)
        self.frame2 = self.frame2 + 1
        if diff_time2 > 1:
            self.start_time2 = end_time2
            self.label_8.setText('帧率(2):' + str(self.frame2))
            self.frame2 = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.showFullScreen()
    sys.exit(app.exec_())



