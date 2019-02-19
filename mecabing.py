import subprocess, os, pprint, re, copy, math, sqlite3

def mecab(sentence):
	sentence = sentence.strip().replace("\n", "").replace("\t", "")
	sentence = sentence.replace(" ", "").replace("　", "")
	sentence = sentence.replace("(", "").replace(")", "")
	path = os.path.dirname(os.path.abspath(__file__))
	command = path + "/mecabing.bash" + " " + sentence
	proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	mecabed = proc.stdout.read().decode()
	return mecabed

def mecab2obj(sentence):
	"""MECAB RESULT"""
	data = []
	mecabed = mecab(sentence)
	for mcb in mecabed.split("\n"):
		"""ONE DATA"""
		mcb = mcb.replace("\t", ",")
		mcb_split = mcb.split(",")
		if len(mcb_split) > 1:
			datum = {}
			word = mcb_split[0]
			attr1 = mcb_split[1]
			attr2 = mcb_split[2]
			datum["word"] = word
			datum["attr1"] = attr1
			datum["attr2"] = attr2

			is_counted = False

			if not data:
				datum["count"] = 1

			for d in data:
				if d["word"] == word and d["attr1"] == attr1 and d["attr2"] == attr2:
					d["count"] = d["count"] + 1
					is_counted = True
					continue
				else:
					datum["count"] = 1
			if not is_counted:
				data.append(datum)
	for datum in data:
		pattern = re.compile("^(、|。|　|「|」|（|）|・)$")
		if pattern.match(datum["word"]):
			data.remove(datum)

	sorted_data = sorted(data, key=lambda x: x["count"], reverse=True)
	return sorted_data

print(mecab2obj("私は太朗です"))

def has_word(word, doc):
	data = mecab2obj(doc)
	for d in data:
		if d["word"] in word:
			return True
	return False