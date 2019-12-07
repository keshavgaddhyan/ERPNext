
import numpy as np
import pymysql
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
 conn = pymysql.connect(host='54.186.139.64' , user='root', passwd='erpdeploy', db='_1bd3e0294da19198')
 query = 'SELECT * FROM _1bd3e0294da19198.`tabSales Order`'
 results = pd.read_sql_query(query, conn)
 results.to_csv("output.csv", index=False)
 df=pd.read_csv("output.csv")
 df=df.dropna()
 print(df.columns)
#  print(results)
#  print(results.groupby(["customer_name"]).sum().sort_values("total", ascending=True))
 #result10 = results.groupby(["customer_name"])
 #print(result10.get_group())
 #plt.scatter(results["customer_name"], result10["total"], color="red")
 #plt.show()


