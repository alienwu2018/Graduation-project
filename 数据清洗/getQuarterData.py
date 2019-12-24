#coding=utf-8
import json
import pandas as pd

def Quarter():
    with open("C:\\Users\\58294\\Desktop\\银行股票数据\\工商银行\\sh601398.txt","r")as f:
        data = f.read()
        f.close()
    #str 2 dict
    ddata=json.loads(data)
    #将原字典转换成 {日期:总市值}的形式
    date = ddata["date"]
    MarketValue = ddata["market_value"]
    nddata = dict()
    for d,m in zip(date,MarketValue):
        nddata[d] = m
    return nddata

def DataCleaning():
    IO = "C:\\Users\\58294\\Desktop\\银行股票数据\\工商银行\\SH601398LRB.xls"
    sheet = pd.read_excel(io=IO)
    # print(sheet)
    # print(sheet.shape)
    # print(sheetT)
    #只需获取的列数
    targetColumns = [0,7,39,49,52,59,62,65]
    for c,r in sheet.iterrows():  #以列的形式遍历dataframe
        if c not in targetColumns:
            sheet=sheet.drop(c,axis=0)      #删除不必要的行
    # print(sheet.columns.values)  #获取列名
    return  sheet



if __name__ == '__main__':
    # Quarter()
    DataCleaning()