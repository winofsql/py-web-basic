# WEB 出力の最小バージョン
WEB 出力の最小バージョン
```python
import sys
import io

# 標準出力へ utf-8 で出力
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# HTTP ヘッダ
print("Content-Type: text/html; charset=utf-8")
print("")
```

## XAMPP で Python を実行できるようにするには、httpd.conf の 『AddHandler cgi-script .cgi .pl .asp』 に .py を追加します
![image](https://user-images.githubusercontent.com/1501327/167241625-0a2699d6-9298-4459-8586-f9cefe59e6c4.png)
