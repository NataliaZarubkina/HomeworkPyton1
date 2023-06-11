# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он
#  их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они
#  разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:                                           Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам          Парам пам-пам

def same_by (values):
    list_1 = values.upper().split()
    f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    if all([f(i) == f(list_1[0]) for i in list_1]):
        return 'Парам пам-пам'
    return 'Пам парам'
 
values = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(same_by(values))			
