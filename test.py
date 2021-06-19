from core.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
def test_get_root():
  response = client.get('/')
  assert response.status_code == 200
  assert response.json() == {'status':200, 'message':'FastAPI bhimsur@2021'}

def test_post_predict():
  response = client.post('/api/v1/predict/', json={'text':'bukan berita biasa'})
  assert response.status_code == 200
  assert response.json() == {'status':200,'message':'not clickbait'}