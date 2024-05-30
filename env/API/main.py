from fastapi import FastAPI
from model import Diary
from db import database
from sqlmodel import select

#api 객체
app = FastAPI()

#regDate?yyyymmdd
@app.get('/')
def getDiary(regDate: str):
	session = database.session()
	#statement = select(Diary).where(Diary.regDate == regDate)
	return {'message': '여기가 루트'}