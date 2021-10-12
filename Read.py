# -*- coding:utf-8 -*-
"""
 @Time: 2021/10/12 下午3:04
 @Author: LiuHe
 @File: Read.py
 @Describe: the read module for test
"""
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    text = input("Input data: ")
    print("place your tag to write")
    reader.write(text)
    print("completed")
finally:
    GPIO.cleanup()