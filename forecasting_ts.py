'''

Get this information here: https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/

'''

# Load modules

import pandas as pd
import os
import matplotlib.pylab as plt
from statsmodels.tsa.stattools import adfuller
import numpy as np



# Get initial data
data = pd.read_csv("AirPassengers.csv")
print data[1:10]
print data.head()

# Create a TS index
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m') # error
data = pd.read_csv('AirPassengers.csv',parse_dates=['Month'], index_col='Month', date_parser=dateparse)
print data.head()


data.index

ts = data['#Passengers'] # generate good data.....
ts.head(10)
plt.plot(ts)



# Check Stationarity(constant mean, constant variance or autocovariate not depending on time)
# We can check formally check stationarity using rolling statistics or Dickey-Fuller test

# Determing rolling statistics
rolmean = pd.rolling_mean(ts, window=12)
rolstd = pd.rolling_std(ts, window=12)

# Plot rolling statistics:
orig = plt.plot(ts, color='blue', label='Original')
mean = plt.plot(rolmean, color='red', label='Rolling Mean')
std = plt.plot(rolstd, color='black', label='Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show(block=False)


#Perform Dickey-Fuller test:
print 'Results of Dickey-Fuller Test:'
dftest = adfuller(ts, autolag='AIC')
dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
for key,value in dftest[4].items():
    dfoutput['Critical Value (%s)'%key] = value
print dfoutput


# The same as above but as a function to be reused later...

def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    # Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print 'Results of Dickey-Fuller Test:'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print dfoutput


test_stationarity(ts)



# Read more about ADF test: https://www.thoughtco.com/the-augmented-dickey-fuller-test-1145985

# Estimating and Eliminating trend
ts_log = np.log(ts)
plt.plot(ts_log)


moving_avg = pd.rolling_mean(ts_log,12)
plt.plot(ts_log)
plt.plot(moving_avg, color='red')


ts_log_moving_avg_diff = ts_log - moving_avg
ts_log_moving_avg_diff.head(22)


ts_log_moving_avg_diff.dropna(inplace=True)
test_stationarity(ts_log_moving_avg_diff)


# Decompose
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(ts_log)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(ts_log, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()


# Forecasting Time Series

from statsmodels.tsa.arima_model import ARIMA

# AR model
model = ARIMA(ts_log, order=(2, 1, 0))
results_AR = model.fit(disp=-1)

ts_log_diff = ts_log - ts_log.shift()

plt.plot(ts_log_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-ts_log_diff)**2))

