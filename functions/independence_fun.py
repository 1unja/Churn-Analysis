import pandas as pd
import numpy as np
from scipy.stats import chi2



def independece_chi2_test(df, column1_name, column2_name = 'total', a = 0.01, deg = 1):

    expected = (df[column2_name] * (sum(df[column1_name])/sum(df[column2_name])))

    statistics = (
        (df[column1_name] - expected) ** 2
        / expected
    ).sum()

    chi_sqr = chi2.ppf(1 - a, deg)


    return(
        statistics,
        chi_sqr
    )
