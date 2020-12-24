from numpy.core.fromnumeric import argsort
from main import Mainwindow
from PIL import Image
import pytesseract
import cv2
import os
class UI_function(Mainwindow):

    def readPicture(imageInput):
        
        # Đọc file ảnh và chuyển về ảnh xám
        image = cv2.imread(imageInput)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Nếu phân tách đen trắng
        gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Ghi tạm ảnh xuống ổ cứng để sau đó
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # Load ảnh và apply nhận dạng bằng Tesseract OCR
        text = pytesseract.image_to_string(Image.open(filename),lang='vie')
        os.remove(filename)

        # In dòng chữ nhận dạng được
        print(text)