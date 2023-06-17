#!/home/hahnpv/anaconda3/bin/python3

import math
import numpy as np
from random import randrange
from sstudentt import SST

class t_dist:
  # https://dailyspeculations.com/Egan_Dis.pdf
  #DAILY he fitted values and 95% confidence intervals computed using maximum likelihood estimation are: 
  # mu = 0.042% (0.029%-0.054%) 
  # sigma = 0.609% (0.596%-0.623%) 
  # nu = 3.60 (3.33-3.81) 
  # no value of tau provided

  def __init__(self, model):
    if model == "daily":
      # daily
      self.dist = SST(mu = 0.00042, sigma = 0.00609, nu = 3.6, tau = 3) # note tau unknown, lower tau bigger jumps
      self.period = 252
    elif model == "monthly":
      #monthly
      # Monthly returns - raise mu to the power of trading days per month. Returns 10.6% which is sensical
      # however there are no very large drawdowns etc... maybe monthly stat set != integration of daily?
      self.dist = SST(mu = pow(1+0.00042,21)-1, sigma = 0.00609*math.sqrt(21), nu = 3.6, tau = 20) # note tau unknown, lower tau bigger jumps
      self.period = 12
    elif model == "yearly":
      # yearly returns - untested
      self.dist = SST(mu = pow(1+0.00042,252)-1, sigma = 0.00609*math.sqrt(252), nu = 3.6, tau = 20) # note tau unknown, lower tau bigger jumps
      self.period = 1
    else:
      raise ValueError("Invalid model specified")
    
  def __str__(self):
    return f"SST Financial Model"

  def series(self,num):
    return {'return': np.array(self.dist.r(num))};


# test
if __name__=="__main__":
  import matplotlib.pyplot as plt
  m = t_dist("yearly");
  years = 40
  for x in range(2000):
    np.random.seed(x)
    r = m.series(years)
    plt.plot(r)

  plt.show()