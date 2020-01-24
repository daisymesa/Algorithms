#!/usr/bin/python

import argparse

# Write a function find_max_profit that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.


def find_max_profit(prices):
    # price list must have at least two prices in it
    if (len(prices) <= 1):
        return None

    else:
        # find best price to sell stocks
        selling_price = max(prices)
        # list of prices at which stocks can be bought (prices before the best price to sell)
        buy_choices = prices[0:prices.index(selling_price)]
        # find the lowest price in from the buy_choices prices
        buying_price = min(buy_choices)

        # diff btw selling_price and buying_price
        max_profit = selling_price - buying_price

        # print("highest price: ", selling_price)
        # print("buy choices: ", buy_choices)
        # print("buying price: ", buying_price)

    return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
