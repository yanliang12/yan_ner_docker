##########yan_ner_arabic.py###########

'''
https://universaldependencies.org/treebanks/ar_padt/index.html
'''

import stanza

nlp = stanza.Pipeline('ar')

def arabic_ner(text):
	try:
		doc = nlp(text)
		return [e.to_dict() for e in doc.ents]
	except:
		return None


def text_to_lemma_text(
	text,
	):
	try:
		doc = nlp(text)
		lemma_text = ' '.join([w.lemma for w in doc.iter_words()])
		return lemma_text
	except:
		return None


##########yan_ner_arabic.py###########