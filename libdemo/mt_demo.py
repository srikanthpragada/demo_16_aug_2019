import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        self.name = "Child Thread"
        print(threading.current_thread().name)
        print(threading.active_count())
        for i in range(1, 11):
            print(i)


print(threading.current_thread().name)
t1 = PrintThread()
t1.start()
print("The End")
