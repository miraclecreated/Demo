#!/bin/usr/ python3
# --*-- coding:utf-8 --*--

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解

def quadratic(a,b,c):
    for i in [a,b,c]:
        if not isinstance(i,(int,float)):
            raise TypeError('bad operand type!')
        if a == 0 :
            if b != 0 :
                return -b/c
            else:
                if c != 0:
                    return "此方程式无实根"
                else:
                    return 0
        condition = b*b - 4*a*c
        if condition < 0:
            return "此方程式无实根"
        elif contion == 0:
            return -b/(2*a)
        else:
            return ((-b + condition**0.5)/(2*a), (-b - condition**0.5)/(2*a))
        
