from sqlmodel import Field, SQLModel

'''
class Diary(상속받을 클래스, 생성자? Diary 객체 생성할때 table을 true로 생성하기?)
table=True로 하면 db모델이고 이게 없으면 dataModel임
'''
class Diary(SQLModel, table=True):
	#타입에 int | None > 이거 자체로 optional
	#int | str | None 이런식으로 여러개 지정 가능
	#뒤에 = Field 이렇게 가는거는 초기화 한거;
	seq: int | None = Field(primary_key=True)	#primary_key 말그대로 키값 지정해준거
	title: str
	content: str
	regDate: str
	regUser: str
	delYn: str = Field(default='N')
	udtDate: str | None
	udtUser: str | None
	viewCnt: int | None = Field(default=0)
	likeCnt: int | None = Field(default=0)
	fileYn: str | None = Field(default='N')
