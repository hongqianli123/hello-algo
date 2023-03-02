"""
File: array_stack.py
Created Time: 2022-11-29
Author: Peng Chen (pengchzn@gmail.com)
"""

import sys, os.path as osp
sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from modules import *

class ArrayStack:
    """ 基于数组实现的栈 """
    def __init__(self):
        """ 构造方法 """
        self.__stack = []

    def size(self):
        """ 获取栈的长度 """
        return len(self.__stack)

    def is_empty(self):
        """ 判断栈是否为空 """
        return self.__stack == []

    def push(self, item):
        """ 入栈 """
        self.__stack.append(item)

    def pop(self):
        """ 出栈 """
        assert not self.is_empty(), "栈为空"
        return self.__stack.pop()

    def peek(self):
        """ 访问栈顶元素 """
        assert not self.is_empty(), "栈为空"
        return self.__stack[-1]
    
    def to_list(self):
        """ 返回列表用于打印 """
        return self.__stack


""" Driver Code """
if __name__ == "__main__":
    """ 初始化栈 """
    stack = ArrayStack()

    """ 元素入栈 """
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print("栈 stack =", stack.to_list())

    """ 访问栈顶元素 """
    peek = stack.peek()
    print("栈顶元素 peek =", peek)

    """ 元素出栈 """
    pop = stack.pop()
    print("出栈元素 pop =", pop)
    print("出栈后 stack =", stack.to_list())

    """ 获取栈的长度 """
    size = stack.size()
    print("栈的长度 size =", size)

    """ 判断是否为空 """
    is_empty = stack.is_empty()
    print("栈是否为空 =", is_empty)
