import numpy as np

pa = 0.1053 # proportion of the first population
na = 133 # first population size
pb = 0.3233 # poportion of the second population
nb = 133 # second population size

def compute_confidence_interval(pa, pb, na, nb, alpha=0.05):
    """
    This function allow to compute the CI for difference of proportion
    when the sample size is big.

    Parameters
    ----------
    pa : proportion of the first population
    pb : proportion of the second population
    na : size of the first population
    nb : size of the second population
    alpha : the risk level default 5%

    Returns
    -------
    CI : list which represent the Confidence interval.
    """
  alphas = {0.05: 1.96, 
            0.1: 1.645,
            0.2: 1.282,
            0.01: 2.576}
  var_a = pa * (1-pa)
  var_b = pb * (1-pb)
  ecart = alphas[alpha] * np.sqrt(var_a/na + var_b/nb)
  diff_prop = pb - pa
  CI = [diff_prop - ecart, diff_prop + ecart]
  CI[0] = np.round(CI[0]*100, 2)
  CI[1] = np.round(CI[1]*100, 2)
  return CI


compute_stats(pa, pb, na, nb)
  
