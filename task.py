#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":

    scores = tuple(map(int, input("Введите баллы 20 команд в поорядке убывания: ").split()))
    if len(scores) < 20:
        print("Количество команд меньше 20", file=sys.stderr)
        exit(1)
    for i, num in enumerate(scores):
        if i == 0: continue
        if num > scores[i-1]: 
            print("Баллы расположены не в порядке убывания", file=sys.stderr)
            exit(1)
    
    n = int(input("Введите количество баллов, для которого нужно подсчитать место: "))
    if n not in scores:
        print("Такого балла нет", file=sys.stderr)
        exit(1)
    
    print("Команда с данным баллом заняла", scores.index(n)+1, "место")
