import pandas as pd
import os
import quandl
import time

quandl.ApiConfig.api_key = "nrEHd32tMgesWjRx25KQ"
data = quandl.get_table('ZACKS/FC', ticker='AAPL')

print(data)
