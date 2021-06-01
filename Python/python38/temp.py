class Student:
    def __init__(self, xh, name, age):
        self.xh = xh
        self.name = name
        self.age = age

    def hello(self):
        print("你好，我是:", self.name)

    # 3. 创建方法
    def set(self, xh, name, age):
        self.xh = xh
        self.name = name
        self.age = age


# 2. 创建实例
zs = Student("001", "张三", 18)
ls = Student("002", "李四", 18)
print("学号", "姓名", "年龄")
print(zs.xh, zs.name, zs.age)
print(ls.xh, ls.name, ls.age)
zs.hello()
ls.hello()

# 3. 调用方法
zs.set("003", "王五", "19")
print(zs.xh, zs.name, zs.age)
zs.hello()
