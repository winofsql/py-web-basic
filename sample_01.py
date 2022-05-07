#!/usr/local/bin/python3.7

import cgi
import cgitb
cgitb.enable()

import sys
import io
import os
import urllib.parse
from xml.sax.saxutils import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8")
print( "Expires: Thu, 19 Nov 1981 08:52:00 GMT" )
print( "Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0" )
print( "Pragma: no-cache" )
print()

data1 = "こんにちは"
data2 = [1,2,3,4]
data3 = (1,2,3,4,"")
data4 = {"A":1, "B":2, "C":3, "D":4 }

type1 = str(type(data1))
type2 = str(type(data2))
type3 = str(type(data3))
type4 = str(type(data4))

"""
print( data1 + "<br>" )
print( escape(type1) + "<br>" )

print( str(data2) + "<br>" )
print( escape(type2) + "<br>" )

print( str(data3) + "<br>" )
print( escape(type3) + "<br>" )

print( str(data4) + "<br>" )
print( escape(type4) + "<br>" )
"""

view = f"""<!DOCTYPE html>
<html>
<head>
	<meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport">
	<meta charset="UTF-8">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/css/bootstrap.min.css">
</head>
<body>
<div id="main">
	<form method="get">
		<div>
			<div>氏名</div>
			<div><input type="text" name="field1" value=""></div>
		</div>

		<div>
			<div>フリガナ</div>
			<div><input type="text" name="field2" value=""></div>
			<div><input type="submit" name="send" value="送信"></div>
		</div>
	</form>
</div>
</body>
</html>"""

print( view )
