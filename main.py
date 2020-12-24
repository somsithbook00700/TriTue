from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Function_ui import *
from ui_nhanhdangand import Ui_MainWindow
import sys 
import cv2


class Mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.text = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## Function more for GUI
        self.ui.pushButton_browse.clicked.connect(lambda: self.singleBrowse())
        self.ui.pushButton_nhandang.clicked.connect(lambda: self.convert())
        self.ui.pushButton_clear.clicked.connect(lambda: self.btnClear())
        self.ui.pushButton_save.clicked.connect(lambda: self.btnSave())
        self.show()

    ############# FUNCTION #######################
    def convert(self):
        
        self.btnClear()

        ## process
        filename_get = self.ui.label_input_name.text()
        
        # UI_function.readPicture(self.filename)
        
        # Đọc file ảnh và chuyển về ảnh xám
        image = cv2.imread(r"{}".format(filename_get))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # tách đen trắng
        gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Ghi tạm ảnh xuống ổ cứng để sau đó
        filename = "{}.png".format(os.getpid()) ############## change get id
        cv2.imwrite("./images/draft/{}".format(filename), gray)

        # Load ảnh và apply nhận dạng bằng Tesseract OCR
        text = pytesseract.image_to_string(Image.open("./images/draft/{}".format(filename)),lang='vie') ######################################

        self.ui.label_2.setPixmap(QPixmap(u"{}".format("./images/draft/{}".format(filename))))
       
        # Xóa ảnh tạm sau khi nhận dạng
        # os.remove("./images/draft/{}".format(filename))


        # Hiển thị các ảnh chúng ta đã xử lý.
        cv2.imshow("Image", image)
        cv2.imshow("Output", gray)

        # In dòng chữ nhận dạng được ### change to save 
        self.ui.textEdit.insertPlainText(text)
        self.ui.textEdit.moveCursor(QTextCursor.End)
        ## finished
        print("CONVERT COMPLETED")

    def btnClear(self):
        self.ui.textEdit.clear()

    def btnSave(self):
        text = self.ui.textEdit.toPlainText().strip()
        if text  == "":
            return 0
        else: 
            print(os.getcwd())
            name = QFileDialog.getSaveFileName(self, "Save File", r"~\Desktop\Tri Tue Nhan Tao Project\results\\" , '*.txt')
            print("Saved :",name[0])

            with open(name[0], 'w', encoding="utf-8") as file:
                text = self.ui.textEdit.toPlainText()
                file.write(text)

    def singleBrowse(self):
        filePath = QFileDialog.getOpenFileName(self,'Single File',"~\Desktop\Tri Tue Nhan Tao Project","*.png and *.jpg")
        # filename = filePath[0].strip().split("/")
        self.ui.label_input_name.setText(filePath[0])
        print("Browsed :",filePath[0])
        self.ui.label.setPixmap(QPixmap(u"{}".format(filePath[0])))
                                                                                                                      
        

if __name__ == "__main__":
    app = QApplication()
    main = Mainwindow()
    sys.exit(app.exec_())
    
