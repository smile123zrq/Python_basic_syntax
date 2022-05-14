class Parent:
    def myMethod(self):
        print('调用父类方法')

    def test(self):
        print('父类第二个方法')


class Child(Parent):
    def myMethod(self):
        print('调用子类方法')
        super(Child, self).myMethod()  # 调用父类的方法，是写在子类里面的
        super(Child, self).test()      # 可以调用父类中的任何方法


c = Child()     # 子类实例化
c.myMethod()    # 子类调用重写的方法
'''
调用子类方法
调用父类方法
父类第二个方法
'''