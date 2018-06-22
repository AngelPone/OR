#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pone
线性规划求解TSP问题
"""
import numpy as np
def lp_tsp(s,V,d_matrix):
    l = []
    lists = []
    lists.append(V)
    lists.append([])
    if len(V) != 0:
        for i in V:
            d_si = d_matrix[s][i]
            a = list(V)
            a.remove(i)
            tsp,b = lp_tsp(i,a,d_matrix)
            l.append(d_si + tsp)
            lists[1].append(b)
        lists.append(V[l.index(min(l))])
    else:
        l.append(d_matrix[s][0])
        lists[1].append([])
        lists.append(0)
    return min(l),lists

def sign(lists):
    global order
    try:
        a = list(lists[0])
        print('未到达位置：%s'%a)
        b = lists[2]
        order.append(b)
        print('目标位置：%s'%b)
        a.remove(b)
        for j in lists[1]:
            if j[0] == a:
                sign(j)
        return lists[2]
    except ValueError:
        return 0


if __name__ == '__main__':
    V = range(1,11) #0为起点，n+1为终点
    d_matrix = [[0,19,24,19,20,28,30,25,28,36,28],
                [7,0,8,6,11,12,14,9,12,20,15],
                [7,8,0,14,19,8,16,17,20,21,23],
                [7,6,14,0,5,9,11,6,9,17,12],
                [7,11,19,5,0,16,18,13,16,16,11],
                [7,12,8,9,16,0,8,9,12,20,15],
                [7,14,16,11,18,8,0,5,11,17,17],
                [7,9,17,6,13,9,5,0,6,14,12],
                [7,12,20,9,16,12,11,6,0,8,15],
                [7,20,28,17,16,20,17,14,8,0,11],
                [7,15,23,12,11,15,17,12,15,11,0]]
    order = [0]
    minre,sign_list = lp_tsp(0,V,d_matrix)
    sign(sign_list)
    print('总路程：%s'%minre)
    print('顺序为%s'%order)

