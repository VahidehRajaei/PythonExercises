import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#---------------------------------- Read From csv -----------------------------

def read_csv_file(fileName):
    return pd.read_csv(fileName)
#---------------------------------- Fill NaN -------------------------------------
def fill_NaN(df):
    df[['View','Like','Order']]=df[['View','Like','Order']].fillna(0)
    return df
#-------------------------------Calling the function to read from a file----------------------------

df_Product_A=read_csv_file('product_A.csv')
df_Product_B=read_csv_file('product_B.csv')
df_Product_C=read_csv_file('product_C.csv')
print(df_Product_A)
print(50*'=')
print(df_Product_B)
print(50*'=')
print(df_Product_C)
print(50*'=')
#-------------------------------- Nan Calling the zeroing function---------------------------

fill_NaN_Product_A=fill_NaN(df_Product_A)
print(fill_NaN_Product_A)
print(50*'=')
#------------------------------------Dataframe aggregationم--------------------------------------

combined_df=pd.concat([fill_NaN_Product_A,df_Product_B,df_Product_C],ignore_index=True)
print(combined_df.to_string())
print(50*'=')
#-----------------------------------Finding the maximum values---------------------------------

max_Result=combined_df.groupby(['Code']).max(['View','Like','Order'])
print(max_Result)
print(50*'=')
#-----------------------------------Drawing the first diagram-----------------------------------

x1=np.array(max_Result['View'].index)
y1=np.array(max_Result['View'])
plt.subplot(1,3,1)
plt.bar(x1,y1,color='blue')
plt.title('View') #  1C پربازدیدترین کالا

x2=np.array(max_Result['Like'].index)
y2=np.array(max_Result['Like'])
plt.subplot(1,3,2)
plt.bar(x2,y2,color='green')
plt.title('Like') # 1C محبوبترین کالا

x3=np.array(max_Result['Order'].index)
y3=np.array(max_Result['Order'])
plt.subplot(1,3,3)
plt.bar(x3,y3,color='orange')
plt.title('Order') # 1B پرفروش ترین کالا 

plt.show() 
# --------------------------------------Drawing the secound diagram-----------------------------------

font1={'family':'Tahoma','color':'green','size':8}
font2={'family':'Arial','color':'black','size':10}


x1=np.array(fill_NaN_Product_A['Day'])
y1=np.array(fill_NaN_Product_A['Order'])
plt.subplot(3,1,1)
plt.plot(x1,y1)
plt.title('Product_A',fontdict=font1)
plt.grid() 

x2=np.array(df_Product_B['Day'])
y2=np.array(df_Product_B['Order'])
plt.subplot(3,1,2)
plt.plot(x2,y2)
plt.text(8,235,'Product_B',fontdict=font1) 
plt.grid() 

x3=np.array(df_Product_C['Day'])
y3=np.array(df_Product_C['Order'])
plt.subplot(3,1,3)
plt.plot(x3,y3)
plt.text(8,220,'Product_C',fontdict=font1) 
plt.xlabel('Day of month',fontdict=font2)
plt.ylabel('Order quantity',fontdict=font2)
plt.grid() 

plt.show()
# In general, all three products had the highest number of orders in the middle of the month (approximately the 17th).
# In addition to that, the first product also had more orders at the end of the month.