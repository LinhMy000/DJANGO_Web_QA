import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = set(stopwords.words('english1'))
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wn = WordNetLemmatizer()

def clean(text):
    result = re.sub(r'[^a-zA-Z0-9]', ' ', text).lower()
    result = [word for word in word_tokenize(result) if word not in stop]
    result = [wn.lemmatize(word) for word in result]
    result = [wn.lemmatize(word, "v") for word in result]
    return ' '.join(result)  # match token to sentence

def cleanData(data):
    data['Clean'] = [clean(text) for text in data['Question']]
    return data


