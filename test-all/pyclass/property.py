
## 装饰器 @property可以将一个函数映射为一个属性使用
## 比如 一般使用 a.name = '一个值' 来设置一个对象的值, 但是这样是很不安全的, 我们不能针对外部值的有效性进行校验
## 类似java一样, 我们都会将属性私有化, 然后提供一个setter方法 专门用来设置对象属性的值, 然后在setter方法中,我们可以按照自己的需要进行操作.
## 但是在python中, 没有真正的属性私有化机制, 所以 避免不了 a.xx = 'xx'的情况, @property 看起来解决了这个问题,
## 使用property 注解的函数在使用上很方便 看起来和a.xx = 'xx' 没有区别

class Student(object):

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self,gender):
        # raise ValueError('就是不想你设置值')
        self._gender = gender

    @property
    def age(self):
        return 25

    def __str__(self):
        return self._gender + ', ' + str(self.age)


stu = Student()


stu.gender = 'test'
# Traceback (most recent call last):
#   File "property.py", line 20, in <module>
#     stu.gender = 'test'
#   File "property.py", line 16, in gender
#     raise ValueError('就是不想你设置值')
# ValueError: 就是不想你设置值

print(stu.gender)   ## test
print(stu.__str__())

# stu.age = 35    只读属性不能改变
# Traceback (most recent call last):
#   File "property.py", line 41, in <module>
#     stu.age = 35
# AttributeError: can't set attribute


## 真是一个神奇的 @property

## 使用 @property注解的属性就是一个只读属性 如上面的 age

## 我猜测 在python中, property已经成为class属性的一个抽象类了 可以对class的全部属性进行控制 真的好神奇!!!!




class Screen(object):

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = width

    @property
    def resolution(self):
        return 'hello'

    def toString(self):
        ## 这两种方式都可以 不多我想 第二种应该更好一点
        # return str(self._height) + ', ' + str(self._width) + ', ' + str(self.resolution)
        return str(self.height) + ', ' + str(self.width) + ', ' + str(self.resolution)


sc = Screen()
sc.height = 23
sc.width = 25
sc._height = 124  ## 不过这种方式依然可以使用
# sc.resolution = 'test'

print(sc.toString())
