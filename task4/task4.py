#!/usr/bin/env python
# coding: utf-8

import argparse

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    nums = [int(line.strip()) for line in lines]
    return nums

def calculate_min_moves(nums):
    median = sorted(nums)[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main(file_path):
    nums = read_numbers_from_file(file_path)
    moves = calculate_min_moves(nums)
    print(moves)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the median and the minimum number of moves.")
    parser.add_argument("file", help="Path to the input file containing the array of numbers")
    args = parser.parse_args()

    main(args.file)





