# -*- coding: utf-8 -*-
"""9_Find the Runner-Up Score!

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qwnEFjgRrVzKj-yofY8-hbb9zHPwfO2z
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums = sorted(list(set(arr)))
    print(nums[-2])