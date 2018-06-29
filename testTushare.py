import tushare as ts # TuShare is a utility for crawling historical data of China stocks
import pandas as pd
import numpy as np
df = pd.read_csv('stockIndices.csv')
print(df.head())
print(len(df))

start_date = '2015-01-01'
end_date = '2018-06-24'
cnt=1
errorList=[]
for index in df['StockIndex']:
    stock=index[0:index.find('.')]# 获取纯数字的股票编号
    csv_name = './stockData/{}.csv'.format(stock)# 定义要存储csv文件名
    try:
        df2 = ts.get_k_data(code=stock, start=start_date,end=end_date, autype=None)# 获取股票的日线数据
    except Exception as e:
        errorList.append(int(stock))
        print('%s error! Sleeping...' % (index))
        time.sleep(120)
    else:
        df2 = df2.reset_index(drop=True)
        col_list=['open','high','low','volume','close']
        df2 = df2[col_list]
        df2['volume'] = df2['volume'] / 1000000 #数据预处理
        df2.to_csv(csv_name, index=False) #保存数据
        print('%s done! %d/%d, %.2f%%' % (index,cnt,len(df),float(cnt)/len(df)*100))
        cnt+=1
np.savetxt("./errorResult.txt",errorList,fmt='%d')