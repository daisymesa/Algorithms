#!/usr/bin/python

import argparse

# Write a function find_max_profit that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.


def find_max_profit(prices):
    pass

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
