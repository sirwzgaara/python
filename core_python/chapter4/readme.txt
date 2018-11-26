
onethy.py       单个进程
mtsleepA.py     使用thread，简单的两个线程，主进程通过sleep的方式等待两个线程
mtsleepB.py     使用thread，通过判断锁，等待多个线程
mtsleepC.py     使用threading，通过join()等待多个线程
mtsleepD.py     使用threading，传递对象而不是函数
mtsleepE.py     使用继承threading.Thread的子类，使用这些子类
mtsleepF.py     多线程并发锁的使用
MyThread.py     将继承threading.Thread的子类封装成包，其他模块可以import
facfic.py       多线程和单线程执行若干函数对比区别
atexit_local.py       退出机制
candy.py        信号量，消费者和生产者系统
proccons.py     使用Queue作为线程间通信机制

