"""####################
Author: Nathan Mador-House
Title: StockTicker
####################"""

#######################
"""####################
Index:
    1. Imports and Readme
    2. Initialization Functions
    3. Setup with supplied files/input
    4. General Functions
    5. Main
    6. Testing
    7. GUI / Visual
####################"""
#######################

###################################################################
# 1. Imports and Readme
###################################################################
"""####################
This program is designed to provide easily digestible and useful
information on a select few stocks, either ones of your choosing
or the default ones. Default stocks include Apple, Microsoft,
Google, Intel, Samsung, Tesla, Sony, FaceBook, Qualcomm and
Amazon.
####################"""

import ystockquote as ys

###################################################################
# 2. Initialization Functions
###################################################################


###################################################################
# 3. Setup with supplied files/input
###################################################################

defaultStocks = ["AAPL", "MSFT", "INTC", "GOOG", "SSNLF", "TSLA", "SNE", "FB", "QCOM", "AMZN", "NFLX"]

###################################################################
# 4. General Functions
###################################################################

def getCompanyNames(stockList):
    names = []
    for i in stockList:
        name = ys.get_company_name(i)
        names.append(name)
    return names

def getCurrentPrices(stockList):
    prices = []
    for i in stockList:
        price = ys.get_last_trade_price(i)
        prices.append(price)
    return prices

def getYearLow(stockList):
    yearLow = []
    for i in stockList:
        low = ys.get_52_week_low(i)
        yearLow.append(low)
    return yearLow

def getYearHigh(stockList):
    yearHigh = []
    for i in stockList:
        high = ys.get_52_week_high(i)
        yearHigh.append(high)
    return yearHigh

###################################################################
# 5. Main
###################################################################

names = getCompanyNames(defaultStocks)
prices = getCurrentPrices(defaultStocks)
yLow = getYearLow(defaultStocks)
yHigh = getYearHigh(defaultStocks)

for i in range(0, len(defaultStocks)):
    print(names[i])
    print("Current Price: " + prices[i])
    print("Year Low: " + yLow[i])
    print("Year High: " + yHigh[i])
    print("-------------------")

###################################################################
# 6. Testing
###################################################################

###################################################################
# 7. GUI / Visual
###################################################################

