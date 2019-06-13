import os, sys
import time
file_path = os.path.dirname(sys.path[0])
sys.path.insert(0, file_path)

from adbui import Device

#------------------research----------------------


#------------------eg--------------------

'''
d = Device('127.0.0.1:62001')  # 手机的sn号，如果只有一个手机可以不写
d.init_ocr('10126986', 'AKIDT1Ws34B98MgtvmqRIC4oQr7CBzhEPvCL', 'AAyb3KQL5d1DE4jIMF2f6PYWJvLaeXEk')

btn = d.check_ui(get_ui_fun=d.get_ui_by_ocr, get_ui_lambda=lambda f:f(text='微信'), try_num=2, per_try_time=3)
btn.click()
'''

'''
btn = d.get_ui_by_ocr_delay(text='微信')  # 找到爱拍文字的位置
btn.click()  # 点击爱拍

btn = d.get_ui_by_ocr_delay(text='登录')  # 找到爱拍文字的位置
btn.click()  # 点击爱拍
'''