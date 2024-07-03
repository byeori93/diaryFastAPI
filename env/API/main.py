from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from model.postModel import Post
from db import database
from sqlmodel import select, Session
from PIL import Image
import io
from pytesseract import image_to_string
from core.StringUtil import string_to_dict

#api 객체
app = FastAPI()
#모듈명이랑 클래스명이랑 같아서 생긴 착각...파이썬에서는 다를 수 있어서 모듈.클래스 명확히 해줘야함(모듈=파일)
diary = Post

#regDate?yyyymmdd
@app.get('/')
def getDiary(regDate: str, db: Session = Depends(database.session)):
	statement = select(diary).where(diary.reg_date == regDate)
	#.all()을 하던지 iterator를 해야함,,, 안하면 null로 보인다!!! ㅜㅜ
	result = db.exec(statement).all()
	return {'message': result}

@app.post('/ocrImg')
async def ocrValue(file: UploadFile = File(...)):
	try:
		print('fileName :: ', file.filename)
		#파일 읽기
		content = await file.read()
		ocrImg = Image.open(io.BytesIO(content))

		#ocr 처리
		custom_config = r'--psm 6'
		text = image_to_string(ocrImg, lang="kor+eng", config=custom_config)
		value = string_to_dict(text)
		print('text :: ', text)
		print('value :: ', value)

		#정상값 return 다시커밋
		return JSONResponse(status_code=200, content=value)
	
	#에러
	except Exception as e:
		return JSONResponse(status_code=400, content={"detaile": str(e)})