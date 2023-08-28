import argparse
import logging


class Factorial:
    _instance = None
    logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
                        format='%(levelname)s, %(asctime)s, %(message)s')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._arg_archive = []
            cls._instance._number_archive = []
            cls._instance._factorial = 1
        return cls._instance

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        logging.info(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive


f = Factorial()
# print(f(3))
# print(f(4))
# print(f(5))
# print(f.number_archive())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='логер факториала')
    parser.add_argument('a', type=int, help='Введите число для расчета факториала', default=5)

    print(f(int(input('>>> '))))
