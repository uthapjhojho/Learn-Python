class A():
    def parent_func(self, arg):
        print(arg)

class B(A):
    def child_func(self, arg):
        print(arg)

myobject = B()
myobject.parent_func('from parent function')
myobject.child_func('from child function')
