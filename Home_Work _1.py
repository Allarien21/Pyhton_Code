import random

tries = 0 

number = random.randint(1 , 10)

print ('Угадай число о котором я дума от 1 до 10 ')


while tries < 6:
	guess = int(input('Предложи число:'))

	tries+=1

	if guess < number:
		print('Слишком меаленькое число')
	
	if guess > number:
		print('Слишком большое число')

	if guess == number:
		print(f'Поздравляю, ты угадал мое число в {tries} попыток')
		break

	if guess != number and tries == 6:
		print(f'Извини, ты не справился. Мое число было: {number}')
		break