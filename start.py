import uvicorn
from core.main import app

if __name__=='__main__':
  uvicorn.run('start:app', reload=True, port=5000)