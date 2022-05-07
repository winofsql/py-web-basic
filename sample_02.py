#!C:\app2\Python\python.exe

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

print( "<div style='padding:30px;font-size:20px;word-break:break-all;'>" )

# QueryString の文字列を取得します
try:
    qs = os.environ["QUERY_STRING"]
except Exception as e:
    qs = ""

# QueryString の文字列です
print(qs + "<br>")

# 値が無い場合は、エントリは作成されません
form_get =  urllib.parse.parse_qs(qs)

# qs が空文字列の場合は form_get は {} となります
print(str(form_get) + "<br>")

# このリストのデータを キーに持つディクショナリ(form_get)を確実に作成します
# form_get は、値が全て配列で、通常 [0] の値を使用します
fields = [ "field1", "field2", "field3" ]
for field_name in fields:
    if form_get.get(field_name) is None:
        form_get[field_name] = [""]

# 以降で使用可能なディクショナリの内容です
print(str(form_get) + "<br>")

print( "</div>" )

view = f"""<!DOCTYPE html>
<html>
<head>
<meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport">
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/css/bootstrap.min.css">

<style>
#main {{
    padding: 30px;
    font-size: 24px;
}}

form {{
    margin-bottom: 20px;
}}

.inline {{
    display: inline-block;
}}
.ttl {{
    width: 100px;
}}
</style>
</head>
<body>
<div class="alert alert-primary" role="alert">
    Bootstrap Alerts()
</div>
<div id="main">
    <form method="get">
        <div>
            <div class="inline ttl">氏名</div>
            <div class="inline"><input type="text" name="field1" value="{form_get["field1"][0]}"></div>
        </div>

        <div>
            <div class="inline ttl">フリガナ</div>
            <div class="inline"><input type="text" name="field2" value="{form_get["field2"][0]}"></div>
            <div class="inline ms-2"><input type="submit" name="send" value="送信"></div>
        </div>
    </form>
</div>
</body>
</html>"""

print(view)

