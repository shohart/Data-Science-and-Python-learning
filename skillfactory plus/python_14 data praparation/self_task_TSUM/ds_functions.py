import numpy as np

def outliers_iqr(data, feature, left=1.5, right=1.5, log_scale=False):
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned

def outliers_z_score(data, feature, log_scale=False, left=3, right=3):
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

def uninform_finder(dataframe, thresh=0.95):
    #список неинформативных признаков
    low_information_cols = [] 

    #цикл по всем столбцам
    for col in dataframe.columns:
        #наибольшая относительная частота в признаке
        top_freq = dataframe[col].value_counts(normalize=True).max()
        #доля уникальных значений от размера признака
        nunique_ratio = dataframe[col].nunique() / dataframe[col].count()
        # сравниваем наибольшую частоту с порогом
        if top_freq > thresh:
            low_information_cols.append(col)
            print(f'{col}: {round(top_freq*100, 2)}% одинаковых значений')
        # сравниваем долю уникальных значений с порогом
        if nunique_ratio > thresh:
            low_information_cols.append(col)
            print(f'{col}: {round(nunique_ratio*100, 2)}% уникальных значений')
    print('Возвращаю список неинформативных столбцов...')
    return low_information_cols