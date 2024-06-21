from sqlmodel import create_engine, SQLModel, Session, select
from model.postModel import Post

#db 연결정보
DATABASE_URI: str = "mysql+pymysql://byeori:sh100422@localhost:3306/diary"
#db엔진(이라고 하네) 생성
engine = create_engine(DATABASE_URI, echo=True)


#테이블 생성할 때
def create_db_and_tables():
	return SQLModel.metadata.create_all(engine)

#with...as 구문 : 스트림 open, close를 자동으로 해줌
#yield가 뭐야...?
def session():
	with Session(engine) as session:
		return session
