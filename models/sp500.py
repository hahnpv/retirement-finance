#!/home/hahnpv/anaconda3/bin/python3

import numpy as np
from random import randrange

# Historical annual returns from 1929-2022 and interest rates
# Return source: https://www.macrotrends.net/2324/sp-500-historical-chart-data
# Interest source: https://www.thebalancemoney.com/u-s-inflation-rate-history-by-year-and-forecast-3306093
# FIXME: are the returns already adjusted for interest? you may be double-dipping

# eventually add initializers "annual", "daily", "monthly"
class sp500:
  def __init__(self):
    pass
    self.period = 1
  def __str__(self):
    return f"SP500 Financial Model"

  def series(self,num):
    start = randrange(len(self.sp500_ann_year))
    series = [(i + start) % len(self.sp500_ann_year) for i in range(num)];
    return {'return': np.array([self.sp500_ann_returns[i] for i in series]), 'interest': [self.sp500_ann_interest[i] for i in series], 'year': [self.sp500_ann_year[i] for i in series]}

  sp500_ann_returns  = [-0.119, -0.285, -0.471, -0.152, 0.466, -0.059, 0.414, 0.279, -0.386, 0.252, -0.055, -0.153, -0.179, 0.124, 0.195, 0.138, 0.307, -0.119, 0.000, -0.007, 0.103, 0.218, 0.165, 0.118, -0.066, 0.450, 0.264, 0.026, -0.143, 0.381, 0.085, -0.030, 0.231, -0.118, 0.189, 0.130, 0.091, -0.131, 0.201, 0.077, -0.114, 0.001, 0.108, 0.156, -0.174, -0.297, 0.316, 0.192, -0.115, 0.011, 0.123, 0.258, -0.097, 0.148, 0.173, 0.014, 0.263, 0.146, 0.020, 0.124, 0.273, -0.066, 0.263, 0.045, 0.071, -0.015, 0.341, 0.203, 0.310, 0.267, 0.195, -0.101, -0.130, -0.234, 0.264, 0.090, 0.030, 0.136, 0.035, -0.385, 0.235, 0.128, 0.000, 0.134, 0.296, 0.114, -0.007, 0.095, 0.194, -0.062, 0.289, 0.163, 0.269, -0.194]
  sp500_ann_interest = [0.006, -0.064, -0.093, -0.103, 0.008, 0.015, 0.030, 0.014, 0.029, -0.028, 0.000, 0.007, 0.099, 0.090, 0.030, 0.023, 0.022, 0.181, 0.088, 0.030, -0.021, 0.059, 0.060, 0.008, 0.007, -0.007, 0.004, 0.030, 0.029, 0.018, 0.017, 0.014, 0.007, 0.013, 0.016, 0.010, 0.019, 0.035, 0.030, 0.047, 0.062, 0.056, 0.033, 0.034, 0.087, 0.123, 0.069, 0.049, 0.067, 0.090, 0.133, 0.125, 0.089, 0.038, 0.038, 0.039, 0.038, 0.011, 0.044, 0.044, 0.046, 0.061, 0.031, 0.029, 0.027, 0.027, 0.025, 0.033, 0.017, 0.016, 0.027, 0.034, 0.016, 0.024, 0.019, 0.033, 0.034, 0.025, 0.041, 0.001, 0.027, 0.015, 0.030, 0.017, 0.015, 0.008, 0.007, 0.021, 0.021, 0.019, 0.023, 0.014, 0.070, 0.065] 
  sp500_ann_year     = [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

'''
def sp500annual(num):
  start = randrange(len(sp500_ann_year))
  series = [(i + start) % len(sp500_ann_year) for i in range(num)];
  return np.array([sp500_ann_returns[i] for i in series]), [sp500_ann_interest[i] for i in series], [sp500_ann_year[i] for i in series]
'''

# test
if __name__=="__main__":
  import matplotlib.pyplot as plt
  m = sp500();
  years = 40
  for x in range(2000):
    np.random.seed(x)
    r, i, y = m.series(years)
    plt.plot(r)

  plt.show()
