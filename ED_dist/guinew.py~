import sys
from PyQt4 import QtCore, QtGui
import main as m

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EmotionRecognizer(object):
    def setupUi(self, EmotionRecognizer):
        EmotionRecognizer.setObjectName(_fromUtf8("EmotionRecognizer"))
        EmotionRecognizer.resize(865, 660)
        self.InputImageLabel = QtGui.QLabel(EmotionRecognizer)
        self.InputImageLabel.setGeometry(QtCore.QRect(10, 60, 91, 17))
        self.InputImageLabel.setObjectName(_fromUtf8("InputImageLabel"))
        self.InputImagePath = QtGui.QTextEdit(EmotionRecognizer)
        self.InputImagePath.setGeometry(QtCore.QRect(100, 56, 610, 31))
        self.InputImagePath.setObjectName(_fromUtf8("InputImagePath"))
        self.BrowseButton = QtGui.QPushButton(EmotionRecognizer)
	self.BrowseButton.clicked.connect(self.Browse_action)
        self.BrowseButton.setGeometry(QtCore.QRect(770, 56, 85, 31))
	self.BrowseButton.setObjectName(_fromUtf8("BrowseButton"))
        
	self.OkButton = QtGui.QPushButton(EmotionRecognizer)
	self.OkButton.setText("OK")
	self.OkButton.clicked.connect(self.Ok_action)
        self.OkButton.setGeometry(QtCore.QRect(715, 56, 50, 31))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))



        self.FindEmotionButton = QtGui.QPushButton(EmotionRecognizer)
        self.FindEmotionButton.setGeometry(QtCore.QRect(400, 100, 98, 27))
        self.FindEmotionButton.setObjectName(_fromUtf8("FindEmotionButton"))
	self.FindEmotionButton.clicked.connect(self.FindEmotion_action)
        self.ImageViewArea = QtGui.QGraphicsView(EmotionRecognizer)
	self.ImageViewArea.setGeometry(QtCore.QRect(10, 150, 640, 500))
        self.ImageViewArea.setObjectName(_fromUtf8("ImageViewArea"))

	self.ImotionViewArea = QtGui.QGraphicsView(EmotionRecognizer)
	self.ImotionViewArea.setGeometry(QtCore.QRect(655, 150, 200, 500))
        self.ImotionViewArea.setObjectName(_fromUtf8("ImotionViewArea"))

        self.retranslateUi(EmotionRecognizer)
        QtCore.QMetaObject.connectSlotsByName(EmotionRecognizer)
	
	scene = QtGui.QGraphicsScene()
	pixmap = QtGui.QPixmap('/home/qburst/Desktop/Emotion_detection/ED_dist/Necessaries/0090095001466406148_emotion_window_0.jpg')
   	pixmap5 = pixmap.scaled(190, 450)
	scene.addItem(QtGui.QGraphicsPixmapItem(pixmap5))
	view = self.ImotionViewArea
	view.setScene(scene)
	view.setRenderHint(QtGui.QPainter.Antialiasing)
	view.show()


    def show_image_gview(self,path):	
	scene = QtGui.QGraphicsScene()
	pixmap = QtGui.QPixmap(path)
   	pixmap5 = pixmap.scaled(630, 450)
	scene.addItem(QtGui.QGraphicsPixmapItem(pixmap5))
	view = self.ImageViewArea
	view.setScene(scene)
	view.setRenderHint(QtGui.QPainter.Antialiasing)
	view.show()


    def Ok_action(self):
	path = self.InputImagePath.toPlainText()
	
	if path.count(' ') == path.length() :        
		QtGui.QMessageBox.about(None, "Error !", "please input an image.")
        elif QtCore.QFileInfo(path).exists() == False :  
		
		QtGui.QMessageBox.about(None, "Error !", "Image path doesn't exists.")
	else :
		self.show_image_gview(path)


    def Browse_action(self):
	path = QtGui.QFileDialog.getOpenFileName(None, 'Open File',"." , "Image Files (*.jpg *.png *.jpeg *.JPG)")
        self.InputImagePath.setText(_translate("EmotionRecognizer",path, None))
	self.show_image_gview(path)
    
    
    
    def FindEmotion_action(self):
	image_path = '' 
	image_path = self.InputImagePath.toPlainText()	
	
	if image_path.count(' ') == image_path.length() :        
		QtGui.QMessageBox.about(None, "Error !", "please input an image.")
        elif QtCore.QFileInfo(image_path).exists() == False :  
		
		QtGui.QMessageBox.about(None, "Error !", "Image path doesn't exists.")
	else :
		face_count, path = m.detect(str(image_path))
		
   		if face_count == 0 :
			QtGui.QMessageBox.about(None, "Error !", "No face(s) detected.")
		else :
			self.show_image_gview(path)
    
    


    def retranslateUi(self, EmotionRecognizer):
        EmotionRecognizer.setWindowTitle(_translate("EmotionRecognizer", "EmotionRecognizer", None))
        self.InputImageLabel.setText(_translate("EmotionRecognizer","<html><head/><body><p><span style=\" font-weight:600;\">Input image</span></p></body></html>", None))
        self.BrowseButton.setText(_translate("EmotionRecognizer", "Browse", None))
        self.FindEmotionButton.setText(_translate("EmotionRecognizer", "Find Emotion", None))





def main():
    import sys
    #app = QtGui.QApplication(sys.argv)
    EmotionRecognizer = QtGui.QWidget()
    ui = Ui_EmotionRecognizer()
    ui.setupUi(EmotionRecognizer)
    EmotionRecognizer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    sys.exit(main())

    
