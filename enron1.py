import numpy as np
import pandas as pd
import statsmodels.api as sm
import pdb
import math

df = open("Enron1.txt", "r")

def one(n):
	if n == "viagra":
		return 1
	else:
		return 0
df['Constant'] = df['email'].apply(one)

logit = sm.Logit(df['Constant'], df[Ind_Vars])
result = logit.fit()
coeff = result.params

print result.summary()
