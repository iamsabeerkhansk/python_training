class OverloadDemo:
    def multiply(self,a,b):
        print(a*b)
    def multiply(self,a,b,c):
        print(a*b*c)
m=OverloadDemo()
m.multiply(5,10)

'''
Output:
Traceback (most recent call last):
  File [35m"/home/main.py"[0m, line [35m7[0m, in [35m<module>[0m
    [31mm.multiply[0m[1;31m(5,10)[0m
    [31m~~~~~~~~~~[0m[1;31m^^^^^^[0m
[1;35mTypeError[0m: [35mOverloadDemo.multiply() missing 1 required positional argument: 'c'[0m
[?2004h
'''
