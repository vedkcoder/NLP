import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
nltk.download('punkt')
nltk.download('stopwords')

str = "WASHINGTON: India is committed to rules-based international .Read more at: http://timesofindia.indiatimes.com/articleshow/89630443.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst"

lower_str = str.lower()

sentence = sent_tokenize(lower_str)
word =word_tokenize(lower_str)

print(sentence)
print(word)
