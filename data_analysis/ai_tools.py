# -*- coding: utf-8 -*-
import pandas as pd

def collect_data(datafile_path, col=None):
    """
        数据获取
        type(data.df)
        data_df.info()
        根据类型查看是否有噪声数据，后面进行数据清洗
    """
    if col:
        data_df = pd.read_csv(datafile_path, usecols=col)
    else:
        data_df = pd.read_csv(datafile_path)
    return data_df

def inspect_data(data_df):
    """
        查看数据
    """
    print('数据一共有{}行，{}列'.format(data_df.shape[0], data_df.shape[1]))

    print('数据预览：')
    print(data_df.head())

    print('数据统计信息：')
    print(data_df.describe())