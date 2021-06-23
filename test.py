from starlette import responses
from core.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_root():
  response = client.get('/')
  assert response.status_code == 200

def test_post_predict():
  response = client.post('/api/v1/predict/', json={'text':'bukan berita biasa'})
  assert response.status_code == 201

def test_post_preprocess():
  response = client.post('/api/v1/preprocess', json={'text':'mari berlari di pagi hari'})
  assert response.status_code == 201