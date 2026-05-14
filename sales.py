import tkinter as tk
from matplotlib import pyplot as plt


class SalesGUI():
    def __init__(sales):
        #Create Window
        sales.salesWin = tk.Tk()
        sales.salesWin.title("Sales")
        sales.salesWin.minsize(width=600,height=400)
        sales.salesWin.resizable(False,False)
        
        x_Left = int((sales.salesWin.winfo_screenwidth() - 600)/2)
        y_Top = int((sales.salesWin.winfo_screenheight() - 400)/2)
        sales.salesWin.geometry("%dx%d+%d+%d" %(600,400,x_Left,y_Top))

        #Open the Files
        temp1 = open("MatPricing.txt",'r')
        matData=temp1.readlines()
        temp1.close()
        temp2=open("EveningPricing.txt",'r')
        eveData=temp2.readlines()
        temp2.close()
        temp3 =open("seatsBought1.txt",'r')
        matSales=temp3.readlines()
        temp3.close()
        temp4 =open("seatsBought2.txt",'r')
        eveSales=temp4.readlines()
        temp4.close()

        #Create Lists
        prices1=[0]
        prices2=[0]
        tempTotal1=[0]
        tempTotal2=[0]
        totalBought=[0]
        seats = [0]
        matRemaining=[0]
        eveRemaining=[0]

    
        count = 0
        for line in matSales:
            matSales[count] = int(line)
            count+=1
        count=0
        for line in eveSales:
            eveSales[count] = int(line)
            count+=1
        count=0
        for line in matSales:
            this = matSales[count]+eveSales[count]
            totalBought.append(this)
            count+=1
        totalBought.remove(0)

        #Get prices from matinee file
        count=0
        for line in matData:
            matData[count] = line.rstrip()
            count+=1
        count = 0
        for line in matData:
            matData[count] = line.split(";")
            count+=1
            
        count=0
        #Put in own list
        for line in matData:
            geode = matData[count][1]
            rock = matData[count][0]
            hamster=int(matData[count][2])-matSales[count]
            
            count+=1
            matRemaining.append(hamster)
            seats.append(rock)
            prices1.append(geode)
        prices1.remove(0)
        seats.remove(0)
        matRemaining.remove(0)
        
        count=0
        #Make it a list of integers
        for line in prices1:
            prices1[count]=prices1[count].strip()
            prices1[count]=prices1[count].strip("$")
            prices1[count]=float(prices1[count])
            count+=1
            
        count=0
        #Get the total sales for matinee
        for line in matSales:
            matSales[count]=float(matSales[count])
            filler = prices1[count]*matSales[count]
            tempTotal1.append(filler)
            count+=1
        tempTotal1.remove(0)
        total1=0
        for line in tempTotal1:
            total1 += line
              
        #Data from evening file    
        count=0
        for line in eveData:
            eveData[count] = line.rstrip()
            count+=1
        count=0
        for line in eveData:
            eveData[count]=line.split(";")
            count+=1
            
        count=0
        #Put prices in list
        for line in eveData:
            geode = eveData[count][1]
            hamster = int(eveData[count][2])-eveSales[count]
            count+=1
            eveRemaining.append(hamster)
            prices2.append(geode)
        eveRemaining.remove(0)
        prices2.remove(0)
        
        count=0
        #Convert to list of integers
        for line in prices2:
            prices2[count]=prices2[count].strip()
            prices2[count]=prices2[count].strip("$")
            prices2[count]=float(prices2[count])
            count+=1

        #Get the total sales for evening
        count=0
        for line in eveSales:
            eveSales[count]=float(eveSales[count])
            filler = prices2[count]*eveSales[count]
            tempTotal2.append(filler)
            count+=1
        tempTotal2.remove(0)
        total2=0
        for line in tempTotal2:
            total2 += line

        #Total sales of the day
        total = total1+total2
        total = "%.2f" % total
        total = str(total)

        
        #Total Sales labels
        sold = list(range(len(totalBought)))
        index =0
        yAxis = 170
        for area in totalBought:    
            sold[index] = tk.Label(sales.salesWin,text=totalBought[index], font =("Century Schoolbook",13),\
                                   width=8)
            sold[index].place(x=310,y=yAxis)
            
            index = index+1
            yAxis += 25
            
        #Mat Sales labels
        sold1 = list(range(len(matSales)))
        index =0
        yAxis = 170
        for area in matSales:    
            sold1[index] = tk.Label(sales.salesWin,text=str(int(matSales[index])), font =("Century Schoolbook",13),\
                                   width=8)
            sold1[index].place(x=130,y=yAxis)
            
            index = index+1
            yAxis += 25
            
        #Evening Sales Labels
        sold2 = list(range(len(eveSales)))
        index =0
        yAxis = 170
        for area in eveSales:    
            sold2[index] = tk.Label(sales.salesWin,text=str(int(eveSales[index])), font =("Century Schoolbook",13),\
                                   width=8)
            sold2[index].place(x=220,y=yAxis)
            
            index = index+1
            yAxis += 25
            
        #Heading (sold) labels
        sales.salesWin.matSoldLabel = tk.Label(sales.salesWin,text="Matinee\nSold",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.matSoldLabel.place(x=130,y=120)
        
        sales.salesWin.eveSoldLabel = tk.Label(sales.salesWin,text="Evening\nSold",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.eveSoldLabel.place(x=220,y=120)
        
        sales.salesWin.totalSoldLabel = tk.Label(sales.salesWin,text="Total\nSold",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.totalSoldLabel.place(x=310,y=120)

        #Heading (section) label
        sales.salesWin.sectLabel = tk.Label(sales.salesWin,text="Sections",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.sectLabel.place(x=25,y=120)
        
        #Heading (remaining) labels
        sales.salesWin.matRemLabel = tk.Label(sales.salesWin,text="Matinee\nRemaining",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.matRemLabel.place(x=400,y=120)
        
        sales.salesWin.eveRemLabel = tk.Label(sales.salesWin,text="Evening\nRemaining",\
                                            font=("Century Schoolbook",13), width=8)
        sales.salesWin.eveRemLabel.place(x=500,y=120)
        
        #Grand heading labels
        sales.salesWin.heading = tk.Label(sales.salesWin,text="Mosaic Theater",\
                                            font=("Viner Hand ITC",20),\
                                          fg="sandybrown",width=15)
        sales.salesWin.heading.place(x=180,y=10)
        
        sales.salesWin.todaysSales = tk.Label(sales.salesWin,text="Today's Sales",\
                                            font=("Century Schoolbook",16),\
                                              fg="sandybrown",width=15)
        sales.salesWin.todaysSales.place(x=210,y=50)

        #Section number labels
        seating = list(range(len(totalBought)))
        index =0
        yAxis = 170
        for area in seats:    
            seating[index] = tk.Label(sales.salesWin,text=seats[index], font =("Century Schoolbook",13),\
                                   width=12)
            seating[index].place(x=5,y=yAxis)
            
            index = index+1
            yAxis += 25
        
        sales.salesWin.profit = tk.Label(sales.salesWin,text="Total Sales: $"+total,\
                                            font=("Century Schoolbook",14),\
                                         width=20)
        sales.salesWin.profit.place(x=25,y=350)
        
        #Mat remaining labels
        rem1 = list(range(len(matRemaining)))
        index =0
        yAxis = 170
        for area in eveSales:    
            rem1[index] = tk.Label(sales.salesWin,text=str(matRemaining[index]), font =("Century Schoolbook",13),\
                                   width=8)
            rem1[index].place(x=400,y=yAxis)
            
            index = index+1
            yAxis += 25
            
        #Eve remaining labels
        rem2 = list(range(len(eveRemaining)))
        index =0
        yAxis = 170
        for area in eveSales:    
            rem2[index] = tk.Label(sales.salesWin,text=str(eveRemaining[index]), font =("Century Schoolbook",13),\
                                   width=8)
            rem2[index].place(x=500,y=yAxis)
            
            index = index+1
            yAxis += 25

        #Bar chart
        plt.barh(seats,totalBought)
        plt.ylabel("Section")
        plt.xlabel("Number Bought")
        plt.title("Sales")
        plt.show()
        plt.close()

        

        
        
