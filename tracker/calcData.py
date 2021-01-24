import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def getMonthDetails(array,date):
    print(array)

    if len(array)>=1:
        havedetails=True

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
        grouped=reqDf.groupby('Category')
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

        showbar=False
        if len(date)==4:
            getMonthAnalysis(df,date)
            showbar=True

        return[reqDf.values.tolist(),total,countOf,categorised,eachsum,showbar,havedetails]
    
    else:
        havedetails=False
        return[[[]],0,0,None,None,None,havedetails]

def allSpendings(array):
    print("here It is", len(array))
    if len(array)>=1:
        havedetails=True

        header=['Spend_ID','Category','Amount','Spent_On','Comments']
        df=pd.DataFrame(array,columns=header)
        
        
        total=df['Amount'].sum()
        countOf=df['Amount'].count()

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
        plt.savefig("tracker/static/images/allPie.png")


        return[df.values.tolist(),total,countOf,categorised,eachsum,havedetails]

    else:
        havedetails=False
        print(havedetails)
        return[[[]],0,0,None,None,None,havedetails]

def getMonthAnalysis(df,year):
    monthDf=df.copy()
    reqYear=str(year)
    months=monthDf['Spent_On'].tolist()
    months=[temp[0:7] for temp in months ]
    monthDf["months"]=months
    groupedMonth=monthDf.groupby('months')

    sumMonths={}
    for month,table in groupedMonth:
        if reqYear in month:
            sumMonths[month]=table['Amount'].sum()

    print(sumMonths)
    sumDf=pd.Series(sumMonths)
    fig1, ax1 = plt.subplots()

    sumDf.plot.bar(colormap="Accent")
    plt.savefig("tracker/static/images/bar.png")

def getDayDetails(array,date):
    print("DAY DETAILS")
    print(date)
    haveday=True
    daysum=0
    filteredarray=[]
    if len(array)>=1:
        print("IN")
        header=['Spend_ID','Category','Amount','Spent_On','Comments']
        
        filteredarray=[temp for temp in array if temp[3]==date]
        if len(filteredarray)>=1:
            print("IN")
            df1=pd.DataFrame(filteredarray,columns=header)
            daysum=df1['Amount'].sum()
            print(daysum)
            print(filteredarray)
        else:
            haveday=False

    else:
        haveday=False
        

    return [haveday,daysum]


