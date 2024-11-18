# recursion
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
i = 0
def demo():
    global i
    i=i+1
    print("hello", i)
    demo()

demo()