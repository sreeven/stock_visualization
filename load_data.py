# Imports

import yfinance as yf
import pandas as pd


def load_data():
    # Read file
    constituents = pd.read_csv('sp500.csv')
    constituents = constituents[["Symbol","Security","Sector","GICS Sub-Industry"]]

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


    for symbol in symbols:
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

    for x in range(505):
    constituents["Open"][x] = opens[x][0]
    constituents["Close"][x] = close[x][0]
    constituents["High"][x] = highs[x][0]
    constituents["Low"][x] = lows[x][0]    

    constituents["dividendYield"] = divYield
    constituents["beta"] = beta
    constituents["forwardPE"] = forwardPE
    constituents["averageVolume"] = avgVolume
    constituents["marketCap"] = marketCap

    # Delete duplicate divYield
    del constituents["divYield"]

    return constituents





    
