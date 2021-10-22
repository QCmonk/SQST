import numpy as np 
import matplotlib.pyplot as plt 
from multiprocessing import Pool

from utility import * 


#######################################################
############## Problem specification ##################
#######################################################
# setup desired problem dimension (assume qubits)
N = 2
dim = 2**N
# desired error in estimator
epsilon = 1e-2
# desired failure probability of estimator 
delta = 1e-2
# total number of unique states to perform SQST on (larger number means a more complete error distribution) 
state_num = 1000
# set random seed for repeatability
np.random.seed(1234)
#######################################################


# compute number of state copies required for each estimator
sample_num = 4*np.log(2/delta)/epsilon**2
# generate MUB 
MUB = MUB_gen(nq=N)

# setup multiprocessing pool 

# simulate data collection task

# return estimate of random element and exact value 

# plot histogram of errors

