#!/usr/bin/python

#########Pre-requisite#########
#sudo pip install yahoo-finance
###############################

from yahoo_finance import Share


class PrintInColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, s, **kwargs):
        print(cls.RED + s + cls.END)

    @classmethod
    def green(cls, s, **kwargs):
        print(cls.GREEN + s + cls.END)

    @classmethod
    def yellow(cls, s, **kwargs):
        print(cls.YELLOW + s + cls.END)

    @classmethod
    def lightPurple(cls, s, **kwargs):
        print(cls.LIGHT_PURPLE + s + cls.END)

    @classmethod
    def purple(cls, s, **kwargs):
        print(cls.PURPLE + s + cls.END)

stock_list = ['AAPL', 'TSLA', 'SNAP']

for indexID in range(len(stock_list)):
	stock_name = Share(stock_list[indexID])
	print stock_name.get_price()

"""
PrintInColor.red('hello world')
PrintInColor.green('hello world')
PrintInColor.yellow('hello world')
PrintInColor.lightPurple('hello world')
PrintInColor.purple('hello world')
"""