import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def getMonthDetails(array,date):
    print(array)
    header=['Spend_ID','Category','Amount','Spent_On','Comments']
    df=pd.DataFrame(array,columns=header)
    
    df1=df.copy()
    months=df1['Spent_On'].tolist()

    months=[(temp[0:len(date)]) for temp in months]
    df1['months']=months
    
    reqDf=df1[df1['months']==date]
    reqDf=reqDf[["Spend_ID","Category","Amount","Spent_On","Comments"]]
    total=reqDf['Amount'].sum()
    countOf=reqDf['Amount'].count()

    #categorising
    grouped=df.groupby('Category')
    categorised={}
    eachsum={}
    for name,group in grouped:
        categorised[name]=group.values.tolist()
        eachsum[name]=group['Amount'].sum()
    print(eachsum)


    #drawing the pie chart
    length=len(eachsum)
    colors = ['#ff9999','#66b3ff','#99ff99','#BEB1F1','#B7658A','#F7C86C']
    colors=colors[0:length]
    temp=[0]*length
    
    temp[0]=0.1
    explode = (temp)
    
    labels=[names for names,values in eachsum.items()]
    sums=[values for names,values in eachsum.items()]
    print(sums)
    fig1, ax1 = plt.subplots()
    ax1.pie(sums, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.savefig("tracker/static/images/pie.png")


    return[reqDf.values.tolist(),total,countOf,categorised,eachsum]
    

