#condig=utf-8
import requests
import os

FilePath = r'C:\Users\58294\Desktop\银行股票数据'

BankDict = {'中国银行':601988, '交通银行':601328, '兴业银行':601166, '农业银行':601288, '工商银行':601398, '平安银行':'000001', '建设银行':601939, '招商银行':600036, '民生银行':600016, '浦发银行':600000}

if __name__ == '__main__':
    dir=os.listdir(FilePath)
    for k,v in BankDict.items():
        if k == '平安银行':
            url = "https://eniu.com/chart/marketvaluea/sz"+v
            resp = requests.get(url).text
            with open(FilePath+'\\'+k+'\\'+'sz'+v+'.txt','w')as w:
                w.write(resp)
                w.close()
            print(resp)
        else:
            url = "https://eniu.com/chart/marketvaluea/sh"+str(v)
            resp = requests.get(url).text
            with open(FilePath+'\\'+k+'\\'+'sh'+str(v)+'.txt','w')as w:
                w.write(resp)
                w.close()
            print(resp)