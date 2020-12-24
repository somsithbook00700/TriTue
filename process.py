from PIL import Image
import pytesseract
import argparse
import cv2
import random
import sys
import os

# function
def writefile():
	with open("./output/{}".format(args["output"]), 'w', encoding='utf-8') as file:
		file.write(text)
		os.system('open ./output/{}'.format(args["output"]))

# sarng tham so dau vao
# -i file ảnh cần nhận dạng
# -p [blur : Làm mờ ảnh để giảm noise, thresh: Phân tách đen trắng]
# -o đưa ra đoạn văn đã nhận dạng -> .txt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="ảnh nhận dạng")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="Bước tiền xử lý ảnh")
ap.add_argument("-o", "--output", required=True,
	help="đưa ra đoạn văn đã nhận dạng -> .txt ")
args = vars(ap.parse_args())

# Đọc file ảnh và chuyển về ảnh xám
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Check xem có sử dụng tiền xử lý ảnh không
# Nếu phân tách đen trắng
if args["preprocess"] == "thresh":
    	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif args["preprocess"] == "blur":
    	gray = cv2.medianBlur(gray, 3)
# Ghi tạm ảnh xuống ổ cứng để sau đó 
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Load ảnh và apply nhận dạng bằng Tesseract OCR
text = pytesseract.image_to_string(Image.open(filename),lang='vie')
# Xóa ảnh tạm sau khi nhận dạng
os.remove(filename)

# In dòng chữ nhận dạng được
print(text)
writefile()
# Hiển thị các ảnh chúng ta đã xử lý.
cv2.imshow("Image", image)
cv2.imshow("Output", gray)

# waiting for typing some key to stop
cv2.waitKey(0)
