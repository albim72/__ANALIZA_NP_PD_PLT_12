from googletrans import Translator
from textblob import TextBlob

text = "I love programming in Python!"
translator = Translator()
translated = translator.translate(text, src='en', dest='pl')

print(translated.text)

print("_"*50)
print("sprawdzenie poprawności gramatycznej")
blob = TextBlob(text)
corrected = blob.correct()
print(corrected)

print("_"*50)
print("analiza gramatyczna")
# sentences = blob.sentences
# print(sentences)
tags = blob.tags
print(tags)
