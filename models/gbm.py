#!/home/hahnpv/anaconda3/bin/python3

# Asset Path
import numpy as np


def GBMsimulator(seed, So, mu, sigma, Cov, T, N):
    """
    Parameters

    seed:   seed of simulation
    So:     initial stocks' price
    mu:     expected return
    sigma:  volatility
    Cov:    covariance matrix
    T:      time period
    N:      number of increments
    """

    np.random.seed(seed)
    dim = np.size(So)
    t = np.linspace(0., T, int(N))
    A = np.linalg.cholesky(Cov)
    S = np.zeros([dim, int(N)])
    S[:, 0] = So
    for i in range(1, int(N)):    
        drift = (mu - 0.5 * sigma**2) * (t[i] - t[i-1])
        Z = np.random.normal(0., 1., dim)
        diffusion = np.matmul(A, Z) * (np.sqrt(t[i] - t[i-1]))
        S[:, i] = S[:, i-1]*np.exp(drift + diffusion)
    return S, t


class gbm:
  # Generalized Brownian Motion
  # https://towardsdatascience.com/how-to-simulate-financial-portfolios-with-python-d0dc4b52a278 
  # https://github.com/richard303d/MediumNotebooks/blob/main/How_to_simulate_financial_portfolios_with_Python.ipynb
  # check out his covariance analysis etc. for building portfolios

  def __init__(self, So, mu, sigma, Cov, T, N):
  #  self.seed = seed
    self.So = So
    self.mu = mu
    self.sigma = sigma
    self.Cov = Cov
    self.T = T
    self.N = N

  def __str__(self):
    return f"GBM Financial Model"

  def series(self):
#    np.random.seed(seed)
    dim = np.size(So)
    t = np.linspace(0., T, int(N))
    A = np.linalg.cholesky(Cov)
    S = np.zeros([dim, int(N)])
    S[:, 0] = So
    for i in range(1, int(N)):    
        drift = (mu - 0.5 * sigma**2) * (t[i] - t[i-1])
        Z = np.random.normal(0., 1., dim)
        diffusion = np.matmul(A, Z) * (np.sqrt(t[i] - t[i-1]))
        S[:, i] = S[:, i-1]*np.exp(drift + diffusion)
    return S, t
    return {'return': np.array(self.dist.r(num))};


# test
if __name__=="__main__":
  import matplotlib.pyplot as plt
  m = gbm();
  years = 40
  for x in range(1000):
    np.random.seed(x)
    r = m.series(years)
    plt.plot(r)

  plt.show()