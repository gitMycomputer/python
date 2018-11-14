import mo01 as m
#可以去别名

stu=m.student("小明同学",24)
stu.study()
m.Greeting()


#module路径
import sys
print(sys.path)
#print(type(sys.path))
for p in sys.path:
    print(p)

#添加路径
sys.path.append()

#包，管理模块的文件夹

