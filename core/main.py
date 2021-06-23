from core.utils import make_prediction, text_preprocessor
from fastapi import FastAPI, status
from pydantic import BaseModel

#load
import joblib
LR_MODEL = './core/models/lr.joblib'
TFIDF_MODEL = './core/models/tf.joblib'

objs = []
with (open(LR_MODEL, 'rb')) as lr:
  while True:
    try:
      objs.append(joblib.load(lr))
    except EOFError:
      break
with (open(TFIDF_MODEL, 'rb')) as vector:
  while True:
    try:
      objs.append(joblib.load(vector))
    except EOFError:
      break

model, tfidf = objs[0], objs[1]

app = FastAPI()

class Input(BaseModel):
  text: str

@app.get('/', status_code=status.HTTP_200_OK)
def get_root():
  return {'status':200, 'data':'FastAPI bhimsur@2021', 'message':'success'}

@app.post('/api/v1/predict/', status_code=status.HTTP_201_CREATED)
def post_predict(input: Input):
  text = text_preprocessor(input.text)
  classes = make_prediction(model, tfidf, text)
  if classes == 1:
    return {'status':201, 'data':'clickbait', 'message':'success'}
  elif classes == 0:
    return {'status':201, 'data':'not clickbait', 'message':'success'}
  else:
    return {'status':400, 'data':'bad request', 'message':'success'}

@app.post('/api/v1/preprocess', status_code=status.HTTP_201_CREATED)
def post_preprocess(input: Input):
  text = text_preprocessor(input.text)
  return {'status':201, 'data':text,'message':'success'}