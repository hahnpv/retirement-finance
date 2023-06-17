#!/home/hahnpv/anaconda3/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf
import statistics
import math
from sstudentt import SST
from models.sp500 import sp500
from models.t_dist import t_dist

# could be handy: a[start:stop:step] # start through not past stop, by step for plotting etc

# TODO
# 1. separate generation of finance series from their analysis
# 1.1 add difference ways to generate finance series (maybe a separate script that pulls S&P historical and queries samples?)
# 1.2 add drawdown tail moves, one time and persistent, 1.1 can inform
# 1.3 the t distribution averages ~10% which is right but doesn't seem to have enough tail moves
# 2. come up with a 'strategy' class or function
# 2.1 will need to feed some key indicators back to strategy and then return drawdown
# 3. beef up analysis
# 3.1 instead of .cumprod() integrate month-by-month querying strategy
# 3.2 add a 'cash holdings' pot
# 4. beef up plotting
# 4.1 not just FV but PV
# 4.2 look at statistical distribution of outcomes
#  ...
# end goal: simulate stock markets and strategies for robustness

### INPUTS ###
# Pick a distribution function
#dist  = sp500()
dist = t_dist("yearly")

# Set simulation parameters
years = 40              # Years to simulate
start_price = 1         # Starting portfolio value
interest = 0.03         # Fixed interest rate (FIXME: make interest model [note: you have one correlated with s&p])
indices = 100           # Number of Monte Carlo indices

### INTERNAL SETUP ###
pv = []                 # Present Value
fv = []                 # Future Value
roi = []                # Annualized Return on Investment
returns = []            # Returns [% change in portfolio]
period = dist.period    # Periods per year
np.random.seed(1)       # Fixed seed for repeatable results

### GENERATE FINANCIAL SERIES ### 
for x in range(indices):
  returns.append(dist.series(period*years)['return'])

### MODIFY FINANCIAL SERIES ###
for x in range(indices):
  returns[x][int(np.random.rand(1)*period*years)] = -0.5  # single year 50% drawdown ... 

### ANALYZE FINANCIAL SERIES USING STRATEGY ###
drag = 0.04/period      # Withdrawls (FIXME: replace with investment strategy model)

for r in returns:
  price = start_price*(1+r-drag).cumprod()  # When we develop an investment strategy model we'll need to call it period by period
  fv.append(price[-1])
  roi.append(pow(1+((price[-1]-price[1])/price[1]), 1/years))
  plt.plot(price)

plt.show()

print("ROI: " + str(statistics.mean(roi)) + " (" + str(min(roi)) + " ... " + str(max(roi)) + ") ")
print("FV:  " + str(statistics.mean(fv)) + " (" + str(min(fv)) + " ... " + str(max(fv)) + ") ")
pv = -npf.pv(interest/period,period*years,0,fv)
print("PV:  " + str(statistics.mean(pv)) + " (" + str(min(pv)) + " ... " + str(max(pv)) + ") ")
