import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

def get_tfidf(tfidf, text):
  return tfidf.transform([text])

def make_prediction(model, tfidf, text):
  vector = get_tfidf(tfidf, text)
  yp = model.predict(vector)
  return yp

def text_preprocessor(text):
  def lowercase(text):
    return text.lower()

  def remove_punctuation(text):
    text = re.sub('\n',' ',text) # Remove every '\n'
    text = re.sub('rt',' ',text) # Remove every retweet symbol
    text = re.sub('user',' ',text) # Remove every username
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text) # Remove every URL
    text = re.sub('  +', ' ', text) # Remove extra spaces
    text = re.sub('[^0-9a-zA-Z]+', ' ', text) # Remove nonalphanumeric
    text = re.sub(r"\d+", "", text) # Remove number
    return text

  def remove_whitespace_LT(text):
    return text.strip() # Remove leading and trailing space

  def remove_whitespace_multiple(text):
    text = text.strip()
    return re.sub('\s+',' ',text)

  def remove_single_char(text):
    return re.sub(r'\b(?:\w{,1})\b', '', text)

  def remove_stopword(text):
    return stopword.remove(text)

  def stemming(text):
    return stemmer.stem(text)

  text = lowercase(text)
  text = remove_punctuation(text)
  text = remove_whitespace_LT(text)
  text = remove_whitespace_multiple(text)
  text = remove_single_char(text)
  text = stemming(text)
  text = remove_stopword(text)
  return text
