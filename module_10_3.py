from threading import Thread, Lock
import threading
import random
import time

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            x = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += x
            print(f'Пополнение: {random.randint(50, 500)}. Баланс:{self.balance}')
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            y = random.randint(50, 500)
            print(f'Запрос на {y}')
            if y <= self.balance:
                self.balance -= y
                print(f'Снятие: {y}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')