from nltk.corpus import stopwords

stopwords_list = list(stopwords.words('english'))

processed = []

for word in word_tok:
  if word not in stopwords_list:
    processed.append(word)

print(processed)
