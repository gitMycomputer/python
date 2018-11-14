#常用module
import calendar,time
print("HelloWorld")
now1=time.clock()
t=calendar.isleap(2018)

now=time.ctime()#取当前时间，以字符串形式
time.sleep(1)#睡眠一秒
#time.clock()#显示CPU运行时间，Java中用于计算程序运行时间
now2=time.clock()
print(t)
print(now2-now1)

#自动义时间格式

a=time.localtime()#以时间元祖表示当前时间
ad=time.strftime("%Y%m%d %H%M",a)
print(ad)
help(time)

#import datetime
#import timeit时间测量工具

#生成列表
sum=[]
for i in range(1000):
    sum.append(i)
