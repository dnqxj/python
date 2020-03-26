# -*- coding:utf-8 -*-

import pandas as pd
import os
import matplotlib.pyplot as plt
import ai_tools

# filedata_path = './2018-01-01~2020-03-03.csv'
filedata_path = './鞠婧祎2018-01-01~2020-03-03.csv'

# 结果保存路径
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)



def process_data(data_df):
    data_df['time'] = pd.to_datetime(data_df['time'])
    data_df.set_index(keys='time', inplace=True)
    resampled_weibo_df = data_df.resample('M').mean()
    resampled_weibo_df.dropna()
    return resampled_weibo_df

def analyze_data(data_df):
    """
        数据分析
    """
    data_df['MA 10'] = data_df['start'].rolling(window=10).mean()
    return data_df

def save_plot_results(resampled_weibo_df):
    resampled_weibo_df.to_csv(os.path.join(output_path, 'resampled_weibo_df.csv'))
    resampled_weibo_df[['start', 'MA 10']].plot(rot=45)
    plt.title('start')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, './webo.png'))
    plt.show()


def main():
    # 数据获取
    data_df = ai_tools.collect_data(filedata_path)
    # 查看数据
    ai_tools.inspect_data(data_df)
    # 处理数据
    cln_data_df = process_data(data_df)
    # 分析数据
    resampled_weibo_df = analyze_data(cln_data_df)

    # 展示数据
    save_plot_results(resampled_weibo_df)

if __name__ == '__main__':
    main()
