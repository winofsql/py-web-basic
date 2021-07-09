#!C:\Users\lightbox\AppData\Local\Programs\Python\Python39\python.exe

import sys
import io
#import mysql.connector

# 標準出力へ utf-8 で出力
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8")

print("")

print("こんにちは")
