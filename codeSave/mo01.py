#模块 代码块

class student():
    def __init__(self,name="Noname",age=18):
        self.name=name
        self.age=age

    def study(self):
        print("{0}在学习，别烦我i".format(self.name))

def Greeting():
    print("HelloWorld")

if __name__=='__main__': #如果此类是当作主函数运行，即不是作为模块时
   print("wo")