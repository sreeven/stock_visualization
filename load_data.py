# Imports

import yfinance as yf
import pandas as pd


def data():
    # Read file
    constituents = pd.read_csv('sp500.csv')
    constituents = constituents[["Symbol","Security","Sector","GICS Sub-Industry"]]
    # constituents = constituents.head()
    # Find Data
    symbols = constituents["Symbol"]

    opens = []
    lows = []
    highs = []
    close = []
    divYield = []
    marketCap = []
    beta = []
    forwardPE = []
    avgVolume = []
    trailingPE = []

    counter = 0

    for symbol in symbols:
        # if counter == 5:
            # break
        ticker = yf.Ticker(symbol)
        history = ticker.history(period='1d').reset_index().iloc[:1]
        opens.append(history["Open"])
        lows.append(history["Low"])
        highs.append(history["High"])
        close.append(history["Close"])
        info = ticker.info
        divYield.append(info['dividendYield'])
    #     10 day
        marketCap.append(info['marketCap'])
        beta.append(info['beta'])
        forwardPE.append(info['forwardPE'])
        avgVolume.append(info["averageVolume"])
    #     trailingPE.append(info['trailingPE'])
        
        try:
            print(f"{ticker}{info['trailingPE']}")
            trailingPE.append(info['trailingPE'])

        except KeyError:
            print(f"{ticker}-------------- NOT FOUND")
            trailingPE.append(0)
        # counter = counter + 1

    # Add to dataframe

    constituents["Open"] = opens
    constituents["Low"] = lows
    constituents["Close"] = close
    constituents["High"] = highs
    # constituents["dividendYield"] = divYield
    constituents["beta"] = beta
    constituents["forwardPE"] = forwardPE
    constituents["averageVolume"] = avgVolume
    constituents["marketCap"] = marketCap
    constituents["Trailing PE"] = trailingPE

    # Get necessary info 
# 505
    for x in range(505):
        try:
            constituents["Open"][x] = opens[x][0]
            constituents["Close"][x] = close[x][0]
            constituents["High"][x] = highs[x][0]
            constituents["Low"][x] = lows[x][0]  
        except IndexError:
            print("Out of range")
            constituents = constituents.drop(x)
 

    constituents["dividendYield"] = divYield
    constituents["beta"] = beta
    constituents["forwardPE"] = forwardPE
    constituents["averageVolume"] = avgVolume
    constituents["marketCap"] = marketCap

    # Delete duplicate divYield
    # del constituents["divYield"]

    test = constituents.to_dict('records')

    return test





    
