import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1117973953 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.1
    _, p_value = stats.ttest_ind(x, y, alternative='two-sided')
    return (p_value < alpha)
