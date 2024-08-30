import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

a = len(first)
aa = len(second)

aaa = len(first) if len(first) < len(second) else len(second)

print(list(map(lambda f, s: True if f == s else False, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        if isinstance(file_name, str):
            with open(file_name, 'w') as f_obj:
                for s in data_set:
                    f_obj.write(str(s))
        else:
            print('Не верное имя файла!')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *args):
        self.words = args

    def __call__(self, *args, **kwargs):
        return random.choice(self.words)


from random import choice

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


z = 10
