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
    counter = 1

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
    counter = 1

    for symbol in symbols:
        try:
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
            trailingPE.append(info['trailingPE'])

            
            print(f"{counter} of 504: {symbol}")

        except KeyError:
            print(f"{ticker}-------------- TRAILING PE NOT FOUND")
            trailingPE.append(0)
                
        counter = counter + 1

    print("-------------")
    print(len(trailingPE))
    print(len(constituents))
    print("-------------")

    constituents["Open"] = opens
    constituents["Low"] = lows
    constituents["Close"] = close
    constituents["High"] = highs
    constituents["beta"] = beta
    constituents["forwardPE"] = forwardPE
    constituents["averageVolume"] = avgVolume
    constituents["marketCap"] = marketCap
    constituents["Trailing PE"] = trailingPE
    constituents["dividendYield"] = divYield

    constituents["Open"] = constituents["Open"].astype("float")
    constituents["Low"] = constituents["Low"].astype("float")
    constituents["Close"] = constituents["Close"].astype("float")
    constituents["High"] = constituents["High"].astype("float")
    constituents["beta"] = constituents["beta"].astype("float")
    constituents["forwardPE"] = constituents["forwardPE"].astype("float")
    constituents["averageVolume"] = constituents["averageVolume"].astype("float")
    constituents["marketCap"] = constituents["marketCap"].astype("float")
    constituents["Trailing PE"] = constituents["Trailing PE"].astype("float")
    constituents["dividendYield"] = constituents["dividendYield"].astype("float")

    record = constituents.to_dict('records')

    print("------------------")
    print("Successful!")
    print("------------------")

    return record
    
