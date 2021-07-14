# WEB 出力の最小バージョン
WEB 出力の最小バージョン
```
import sys
import io

# 標準出力へ utf-8 で出力
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```
