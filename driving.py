country = input('請輸入您的國家: ')
age = input('請輸入您的年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以考取駕照')
	else:
		print('您還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('您可以考取駕照')
	else:
		print('您還不能考駕照')
else:
	print('此程式只支援台灣及美國地區')