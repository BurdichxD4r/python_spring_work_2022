#todo: Написать функцию logger() которая принимает в качестве аргумента текст который дописывается
# в файл error.log Новое сообщение должно располагаться на новой строчки.

logger = open('error.log', 'at')
logger.write('Hello!\n')
logger.close()