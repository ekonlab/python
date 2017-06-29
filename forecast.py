__author__ = 'albertogonzalez'


'''
2.- FORECAST FOR THE NEXT CYCLE

https://sites.google.com/site/aslugsguidetopython/data-analysis/pandas/calling-r-from-python
http://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/

LIBRARIES: import rpy2, pymongo

'''
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import os
os.chdir("/home/albertogonzalez/Desktop/python_materials/data_analysis/stocks_bot/")
print(os.getcwd() + "\n")
import matplotlib.pylab as plt


###########################################################################################################

# SET DATES
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')

# GET DATA
data = pd.read_csv('historic_data.csv', parse_dates='Date', index_col='Date',date_parser=dateparse)
print data.dtypes
data.index


# DATE AND VALUE
data_ref = data['Close']
data_ref.head()
print data_ref.dtypes
data_ref.index


plt.plot(data_ref)


###########################################################################################################

# FORECAST

###########################################################################################################

# STATIONARITY

from statsmodels.tsa.stattools import adfuller

def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    #Perform Dickey-Fuller test:
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput


test_stationarity(data_ref)

dfuller_test = adfuller(data_ref)
print type(dfuller_test)
print len(dfuller_test)


te = dfuller_test[0]
ci = dfuller_test[4]
ci_value = ci.values()[0]
print te
print ci_value

if te < ci_value:
    print "stationary"
else:
    print "not stationary"


# HOW TO MAKE A TS STATIONARY

# REDUCE TREND WITH TRANSFORMATION
data_ref_log = np.log(data_ref)
print type(data_ref_log)
data_ref_log.head()

# MOVING AVERAGE
moving_avg = pd.rolling_mean(data_ref_log,12)
log_moving_avg_diff = data_ref_log - moving_avg
print log_moving_avg_diff

log_moving_avg_diff.dropna(inplace=True)
test_stationarity(log_moving_avg_diff)

# EXPONENTIAL MOVING AVERAGE
expwighted_avg = pd.ewma(data_ref_log, halflife=12)

ts_log_ewma_diff = data_ref_log - expwighted_avg
test_stationarity(ts_log_ewma_diff)

###########################################################################################################


# ARIMA MODELS
from statsmodels.tsa.arima_model import ARIMA

model_1 = ARIMA(data_ref_log, order=(2, 1, 0))
results_AR = model_1.fit(disp=-1)

model_2 = ARIMA(data_ref_log, order=(0, 1, 2))
results_MA = model_2.fit(disp=-1)

model_3 = ARIMA(data_ref_log, order=(2, 1, 2))
results_ARIMA = model_3.fit(disp=-1)

# Store predicted results as separate series
predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print predictions_ARIMA_diff.head()

# Cumulative sum at index and add it to the base number
predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print predictions_ARIMA_diff_cumsum.head()

# Create a series with all values as base number and add differences to it.
predictions_ARIMA_log = pd.Series(data_ref_log.ix[0], index=data_ref_log.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
predictions_ARIMA_log.head()

# Take the exponent and compare with the original series
predictions_ARIMA = np.exp(predictions_ARIMA_log)
print predictions_ARIMA[1:10]
print predictions_ARIMA.tail(20)

# Reverse the ARIMA output
arima_pred_rev = predictions_ARIMA.iloc[::-1]
print arima_pred_rev.head()
print len(arima_pred_rev)


arima_pred_rev.to_csv("/home/albertogonzalez/Desktop/python_materials/data_analysis/stocks_bot/predictions_ARIMA.csv")



###########################################################################################################



































