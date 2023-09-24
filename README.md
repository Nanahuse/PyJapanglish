# PyJapanglish
English words to japanese kana  
英単語をカナでの発音へ開きます。

# How to use

```python
from pyjapanglish import Japanglish

japanglish = Japanglish()

# 辞書からの変換
print(japanglish.convert("test")) # テスト

# ユーザー辞書による読み変換
japanglish.user_dict["test"] = "ホゲホゲ"
print(japanglish.convert("test")) # ホゲホゲ

# 辞書にない言葉の読み推定変換
print(japanglish.convert("japanglish")) # ジャパングリシュ

# 読み推定を行わない。変換できない場合はNoneを返す
print(japanglish.convert("japanglish", False)) # None

# アルファベットではない文字が含まれるとNoneを返す。
print(japanglish.convert("ホゲホゲ")) # None
```

# License
[MIT License](LICENSE)

一部にCMUdictの成果を含んでいます。  
ライセンスは[LICENSE_cmudict](LICENSE_cmudict)を確認してください。  
CMUdict ( GitHub : https://github.com/cmusphinx/cmudict )  
Copyright (C) 1993-2015 Carnegie Mellon University.  

