# 練習bmi資訊
height = input('請輸入您的身高(公尺)：')
height = float(height)
weight = input('請輸入您的體重(公斤)：')
weight = float(weight)
bmi = weight / (height * height)
if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重正常')
elif bmi >=24 and bmi < 27:
	print('過重')
elif bmi >=27 and bmi < 30:
	print('輕度肥胖')
elif bmi >=30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')