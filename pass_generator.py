import random

def password_generator(count_char=8):

	arr = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m',
	'Q','W','E','R','T','Y','U','I','O','P','L','K','J','H','G','F','D','S','A','Z','X','C','V','B','N','M','1','2',
	'3','4','5','6','7','8','9']

	passw = []

	for i in range (count_char):
		passw.append(random.choice(arr))
	return "".join(passw)


print(password_generator())