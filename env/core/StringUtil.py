def string_to_dict(txt):
	lines = txt.split('\n')
	result = {}

	keys = ["거래금액", "카드종류", "카드번호/", "거래일시", "거래종류/", "금액", "부가세", "봉사료", "거래금액 합계", "가맹점명", "업종", "가맹점번호", "가맹점주소", "사업자등록번호"]

	for key in keys:
		for line in lines:
			if key in line:
				value = line.replace(key, "").strip()
				result[key] = value
				break
	return result