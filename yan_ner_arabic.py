##########yan_ner_arabic.py###########
import stanza

nlp = stanza.Pipeline('ar')

def arabic_ner(text):
	try:
		doc = nlp(text)
		return [e.to_dict() for e in doc.ents]
	except:
		return None
##########yan_ner_arabic.py###########
