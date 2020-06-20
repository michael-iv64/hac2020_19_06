import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
# nltk.download()
print(nltk.__version__)

# стемминг и лемматизация
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# чтение текстового русского файла без обработки 
with open("nlp/testRu.txt", "r") as file:
    text = file.read()
print(text)

# вывод только слова и цифр 
import re
sentence = text
pattern = r"[^\w]"
textClear = re.sub(pattern, " ", sentence)
print(textClear)

#  токенизация по словам 
wordsAll = nltk.word_tokenize(textClear)
print(wordsAll)

#  приведение к нормальной форме
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

words = wordsAll
normalize_words = []
for word in words:
    p = morph.parse(word)[0]
    normalize_words.append(p.normal_form)
    # print(p.normal_form)
print(normalize_words)  



# стоп слова загрузка 
from nltk.corpus import stopwords
print()
# print('стоп - слова')
# print(stopwords.words("russian"))

# 1 способ (медленный??)
stop_words = set(stopwords.words("russian"))
sentence = normalize_words

words = sentence
without_stop_words = [word for word in words if not word in stop_words]
print()
print('предложение без стоп-слов  1 способ ')
print(without_stop_words)

# 2 способ (быстрее??)

words = sentence
without_stop_words = []
for word in words:
    if word not in stop_words:
        without_stop_words.append(word)

print('2 способ ')
print(without_stop_words)

