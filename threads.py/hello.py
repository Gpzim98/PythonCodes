import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for _ in range(20):
            time.sleep(1)
            print(threading.currentThread().getName())

x = MyThread(name='Sending\n')
y = MyThread(name='Receiving\n')

x.start()
y.start()

# Args and KwArgs
locals()['sun'](10,20)