########yan_sentence_segmentation.py########
import stanza
nlp = stanza.Pipeline(**{'processors': 'tokenize,mwt,pos', 'lang': 'en', }) 

def text_to_sentences(input):
	try:
		doc = nlp(input)
		return [s.text for s in doc.sentences]
	except:
		return [input]

'''
print(text_to_sentences("Barack Obama was born in Hawaii.  He was elected president in 2008."))
'''
########yan_sentence_segmentation.py########
