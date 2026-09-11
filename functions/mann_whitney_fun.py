import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import numpy as np


def mann_whitney_test(u1, u2, group1_name, group2_name) : 

    result = mannwhitneyu(u1, u2)


    new_df = pd.DataFrame(

        {
            'median' : 
                [u1.median(), 
                 u2.median()],

            'std' : 
                [u1.std(), 
                 u2.std()],

            'mean' : 
                [u1.mean(), 
                 u2.mean()]
        },

        index = [group1_name, group2_name]
    )

    #EFFECT SIZE

    n1 = len(u1)
    n2 = len(u2)

    mean_u = n1 * n2 / 2

    std_u = np.sqrt(
        n1 * n2 * (n1 + n2 + 1) / 12
    )

    z = (result.statistic - mean_u) / std_u

    effect_size = z / np.sqrt(n1 + n2)

    return(
        result, new_df, effect_size
    )

