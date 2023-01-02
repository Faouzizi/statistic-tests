import pandas as pd

# Chi 2 test of independence

# H0: Variables are independent
# H1: Variables are not independent

matrice = pd.crosstab(df.sexe, 
                      df.activity)

khi2, pval , ddl , contingent_theorique = chi2_contingency(matrice)
