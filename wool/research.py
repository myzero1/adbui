import os, sys
import time
file_path = os.path.dirname(sys.path[0])
sys.path.insert(0, file_path)

from adbui import Device

#------------------research----------------------
import tesserocr
import pytesseract
from PIL import Image
from PIL import ImageOps
import os,sys

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print("-----------------\n")
print(tesserocr.get_languages())  # prints tessdata path and list of available languages
print("-----------------\n")

pwd = os.getcwd()+'\\wool'
img_path = pwd+'\\temp_12700162001.png'

print(img_path)

# image = Image.open(img_path).crop((40, 1150,200, 1210))
# image = Image.open(img_path).crop((40, 1150,720, 1210))
image = Image.open(img_path)
image.save(pwd+'\\temp_test1.png')
image = image.convert('1', dither=Image.NONE)
image.save(pwd+'\\temp_test2.png')
# text = tesserocr.image_to_text(image, 'chi_sim')
result_data = pytesseract.image_to_data(image, 'chi_sim', '', 0, 'dict')
# image = image.convert('RGB')
# image = ImageOps.invert(image)
# image.save(pwd+'\\temp_test3.png')
# text = text + "\n" + tesserocr.image_to_text(image, 'chi_sim')
print(result_data)  # print ocr text from image



#------------------eg--------------------


d = Device('127.0.0.1:62001')  # 手机的sn号，如果只有一个手机可以不写
d.init_ocr('10126986', 'AKIDT1Ws34B98MgtvmqRIC4oQr7CBzhEPvCL', 'AAyb3KQL5d1DE4jIMF2f6PYWJvLaeXEk')

btn = d.check_ui(get_ui_fun=d.get_ui_by_ocr, get_ui_lambda=lambda f:f(text='微信'), try_num=2, per_try_time=3)
btn = d.get_uis_by_ocr_range_try('登录')
# btn.click()



'''
btn = d.get_ui_by_ocr_delay(text='微信')  # 找到爱拍文字的位置
btn.click()  # 点击爱拍

btn = d.get_ui_by_ocr_delay(text='登录')  # 找到爱拍文字的位置
btn.click()  # 点击爱拍
'''