from fastapi import FastAPI, APIRouter

base_router = APIRouter()

@base_router.get('/')
def welcome():
  app_name = os.getenv()
  return{
    'message': 'hello world'
  }