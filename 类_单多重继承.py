class People:
    #  定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('{}说：我{}岁，{}斤。'.format(self.name, self.age, self.__weight))


# 单继承演示
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print('{}说，我{}岁了，我在读{}年级！'.format(self.name, self.age, self.grade))


# 单继承实例化
s = Student('晓晓', 16, 90, '6')
s.speak()
# 晓晓说，我16岁了，我在读6年级！


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, t, n):
        self.topic = t
        self.name = n

    def speak(self):
        print('我叫{}，我是一个演说家，我演说的主题是{}！'.format(self.name, self.topic))


# 多重继承演示
class Sample(Speaker, People):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, t, n)


# 多继承实例化
s2 = Sample('晓晓', 16, 90, '高二', '明天你好')
s2.speak()  # #方法名同，默认调用的是在括号中排前地父类的方法
# 我叫晓晓，我是一个演说家，我演说的主题是明天你好！
