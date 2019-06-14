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

try_num=5
try_per_sec=12
d = Device('127.0.0.1:62001')

# btn = d.get_ui_by_ocr_range_try('登录', True, (45,1149,197,1199), try_num, try_per_sec)
btn = d.get_ui_by_ocr_range_try('快报', True, None, try_num, try_per_sec)
btn.click()

btn = d.get_ui_by_ocr_range_try('张大', True, None, try_num, try_per_sec)
btn.click()
