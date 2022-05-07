#!C:\app2\Python\python.exe

import sys
import io
# python -m pip install mysql-connector-python
import mysql.connector

# 標準出力へ utf-8 で出力
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8")
print("")

# **************************************
# ログ出力
# **************************************
def log( message ):
    with open('debug.log', 'a') as f:
        print(message,end='\n',file=f)

cnn = mysql.connector.connect(
    host='localhost',
    port=3306,
    db='lightbox',
    user='root',
    passwd='',
    charset='utf8',
    autocommit=True)

cursor = cnn.cursor()
cursor.execute("select * from 社員マスタ where 社員コード <= '0010'")

result = ""
for row in cursor:
    log( row )
    (社員コード,氏名,フリガナ,所属,性別,作成日,更新日,給与,手当,管理者,生年月日) = row

    if 手当 is None:
        手当 = ""
    if 管理者 is None:
        管理者 = ""

    作成日 = "{0:%Y/%m/%d}".format(作成日)
    更新日 = "{0:%Y/%m/%d}".format(更新日)
    生年月日 = "{0:%Y/%m/%d}".format(生年月日)

    result += f"""
<div>
{社員コード} : {氏名} : {フリガナ} : {所属} : {性別} : {作成日} : {更新日} : {給与} : {手当} : {管理者} : {生年月日}
</div>
"""

cnn.close()

html = f"""
<html>
<head>
<meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport">
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/css/bootstrap.min.css">
</head>
</body>
<div class="alert alert-primary" role="alert">
    Bootstrap Alerts()
</div>
<div class="m-4">
{result}
</div>
</body>
</html>
"""

print( html )
