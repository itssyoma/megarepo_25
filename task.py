#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":

    scores = tuple(map(int, input("Введите баллы 20 команд в поорядке убывания: ").split()))
    if len(scores) < 20:
        print("Количество команд меньше 20", file=sys.stderr)
        exit(1)        
    for num1, num2 in zip(scores, scores[1:]):
        if num2 > num1:
            print("Баллы расположены не в порядке убывания", file=sys.stderr)
            exit(1)
    
    n = int(input("Введите количество баллов, для которого нужно подсчитать место: "))
    if n not in scores:
        print("Такого балла нет", file=sys.stderr)
        exit(1)
    
    result = {score: position for position, score in enumerate(scores, start=1)}

    print("Команда с данным баллом заняла", result[n], "место")
