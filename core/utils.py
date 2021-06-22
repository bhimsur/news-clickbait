def get_tfidf(tfidf, text):
  return tfidf.transform([text])

def make_prediction(model, tfidf, text):
  vector = get_tfidf(tfidf, text)
  yp = model.predict(vector)
  return yp