# -*- coding:utf-8 -*-
"""
 @Time: 2021/10/12 下午3:10
 @Author: LiuHe
 @File: Write.py
 @Describe: the write module for test
"""
import RPi.GPIP as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    uid, text = reader.read()
    print("uid: ", uid)
    print("text: ", text)
finally:
    GPIO.cleanup()