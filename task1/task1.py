#!/usr/bin/env python
# coding: utf-8

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('n', type=int, help='An integer for the n value')
parser.add_argument('m', type=int, help='An integer for the m value')

args = parser.parse_args()

n = args.n
m = args.m

array = list(range(1, n + 1))

path = []

while True:
    path.append(array[0])

    end_segment = array[-(n - m + 1):]
    start_segment = array[:m - 1]
    promArr = end_segment + start_segment

    if promArr[m-1] == 1:
        path.append(promArr[0])
        break

    array = promArr

print(path)




