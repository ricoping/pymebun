# pymebun
You can get a result of mecab as python object without python-mecab library.

## How to use
<p>
You just need to install mecab v0.996 on your linux environment.
 </p>
<p>
You can get a list of dictionary that contains noun, adverb and so on by using <i>mecab2obj function</i>. And it also contains data about how many times a word appears in sentence you input.
 </p>
<p>
Both mecabing.bash and mecabing.py are required to be on the same directory.
 </p>

## Examples
~~~
import mecabing

sentence = "幸運は用意された心のみに宿る。宿るといったら宿る。"
print(mecabing.mecab2obj(sentence))
~~~

## Result
~~~
[{'attr1': '動詞', 'attr2': '自立', 'count': 3, 'word': '宿る'},
 {'attr1': '名詞', 'attr2': '一般', 'count': 1, 'word': '幸運'},
 {'attr1': '助詞', 'attr2': '係助詞', 'count': 1, 'word': 'は'},
 {'attr1': '名詞', 'attr2': 'サ変接続', 'count': 1, 'word': '用意'},
 {'attr1': '動詞', 'attr2': '自立', 'count': 1, 'word': 'さ'},
 {'attr1': '動詞', 'attr2': '接尾', 'count': 1, 'word': 'れ'},
 {'attr1': '助動詞', 'attr2': '*', 'count': 1, 'word': 'た'},
 {'attr1': '名詞', 'attr2': '一般', 'count': 1, 'word': '心'},
 {'attr1': '助詞', 'attr2': '副助詞', 'count': 1, 'word': 'のみ'},
 {'attr1': '助詞', 'attr2': '格助詞', 'count': 1, 'word': 'に'},
 {'attr1': '助詞', 'attr2': '格助詞', 'count': 1, 'word': 'と'},
 {'attr1': '動詞', 'attr2': '自立', 'count': 1, 'word': 'いっ'},
 {'attr1': '助動詞', 'attr2': '*', 'count': 1, 'word': 'たら'}]
~~~
