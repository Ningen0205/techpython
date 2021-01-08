import threading
import time

class MyThread(threading.Thread):
  def run(self):
    # some heavy processing
    time.sleep(3)
    
if __name__ == '__main__':
  t = MyThread()
  t.start()
  print('thread started')
  t.join()
  print('thread finished')