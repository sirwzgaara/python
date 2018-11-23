
onethy.py       单个进程
mtsleepA.py     使用thread，简单的两个线程，主进程通过sleep的方式等待两个线程
mtsleepB.py     使用thread，通过判断锁，等待多个线程
mtsleepC.py     使用threading，通过join()等待多个线程
mtsleepD.py     使用threading，传递对象而不是函数
mtsleepE.py     使用继承threading.Thread的子类，使用这些子类
MyThread.py     将继承threading.Thread的子类封装成包，其他模块可以import
facfic.py       多线程和单线程执行若干函数对比区别
atexit.py       退出机制

