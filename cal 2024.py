class Calender_2024:
    def __init__(self,d):
        self.d=d
    def jan(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==1):
                day[i]="MONDAY"
            elif(k==2):
                day[i]="TUESDAY"
            elif(k==3):
                day[i]="WEDNESDAY"
            elif(k==4):
                day[i]="THURSDAY"
            elif(k==5):
                day[i]="FRIDAY"
            elif(k==6):
                day[i]="SATURDAY"
            elif(k==7):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def feb(self):
        day=[None]*31
        k=1
        for i in range(1,29):
            if(k>7):
                k=1
            if(k==1):
                day[i]="THURSDAY"
            elif(k==2):
                day[i]="FRIDAY"
            elif(k==3):
                day[i]="SATURDAY"
            elif(k==4):
                day[i]="SUNDAY"
            elif(k==5):
                day[i]="MONDAY"
            elif(k==6):
                day[i]="TUESDAY"
            elif(k==7):
                day[i]="WEDNESDAY"
            k=k+1
        print(day[self.d])
    def march(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==1):
                day[i]="FRIDAY"
            elif(k==2):
                day[i]="SATURDAY"
            elif(k==3):
                day[i]="SUNDAY"
            elif(k==4):
                day[i]="MONDAY"
            elif(k==5):
                day[i]="TUESDAY"
            elif(k==6):
                day[i]="WEDNESDAY"
            elif(k==7):
                day[i]="THURSDAY"
            k=k+1
        print(day[self.d])
    def april(self):
        day=[None]*31
        k=1
        for i in range(1,30):
            if(k>7):
                k=1
            if(k==1):
                day[i]="MONDAY"
            elif(k==2):
                day[i]="TUESDAY"
            elif(k==3):
                day[i]="WEDNESDAY"
            elif(k==4):
                day[i]="THURSDAY"
            elif(k==5):
                day[i]="FRIDAY"
            elif(k==6):
                day[i]="SATURDAY"
            elif(k==7):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def may(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==6):
                day[i]="MONDAY"
            elif(k==7):
                day[i]="TUESDAY"
            elif(k==1):
                day[i]="WEDNESDAY"
            elif(k==2):
                day[i]="THURSDAY"
            elif(k==3):
                day[i]="FRIDAY"
            elif(k==4):
                day[i]="SATURDAY"
            elif(k==5):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def june(self):
        day=[None]*31
        k=1
        for i in range(1,30):
            if(k>7):
                k=1
            if(k==3):
                day[i]="MONDAY"
            elif(k==4):
                day[i]="TUESDAY"
            elif(k==5):
                day[i]="WEDNESDAY"
            elif(k==6):
                day[i]="THURSDAY"
            elif(k==7):
                day[i]="FRIDAY"
            elif(k==1):
                day[i]="SATURDAY"
            elif(k==2):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def july(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==1):
                day[i]="MONDAY"
            elif(k==2):
                day[i]="TUESDAY"
            elif(k==3):
                day[i]="WEDNESDAY"
            elif(k==4):
                day[i]="THURSDAY"
            elif(k==5):
                day[i]="FRIDAY"
            elif(k==6):
                day[i]="SATURDAY"
            elif(k==7):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def august(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==5):
                day[i]="MONDAY"
            elif(k==6):
                day[i]="TUESDAY"
            elif(k==7):
                day[i]="WEDNESDAY"
            elif(k==1):
                day[i]="THURSDAY"
            elif(k==2):
                day[i]="FRIDAY"
            elif(k==3):
                day[i]="SATURDAY"
            elif(k==4):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
        
    def september(self):
        day=[None]*31
        k=1
        for i in range(1,30):
            if(k>7):
                k=1
            if(k==2):
                day[i]="MOMDAY"
            elif(k==3):
                day[i]="TUESDAY"
            elif(k==4):
                day[i]="WEDNESDAY"
            elif(k==5):
                day[i]="THURSDAY"
            elif(k==6):
                day[i]="FRIDAY"
            elif(k==7):
                day[i]="SATURDAY"
            elif(k==1):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def october(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==7):
                day[i]="MONDAY"
            elif(k==1):
                day[i]="TUESDAY"
            elif(k==2):
                day[i]="WEDNESDAY"
            elif(k==3):
                day[i]="THURSDAY"
            elif(k==4):
                day[i]="FRIDAY"
            elif(k==5):
                day[i]="SATURDAY"
            elif(k==6):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def november(self):
        day=[None]*31
        k=1
        for i in range(1,30):
            if(k>7):
                k=1
            if(k==4):
                day[i]="MONDAY"
            elif(k==5):
                day[i]="TUESDAY"
            elif(k==6):
                day[i]="WEDNESDAY"
            elif(k==7):
                day[i]="THURSDAY"
            elif(k==1):
                day[i]="FRIDAY"
            elif(k==2):
                day[i]="SATURDAY"
            elif(k==3):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
    def december(self):
        day=[None]*31
        k=1
        for i in range(1,31):
            if(k>7):
                k=1
            if(k==2):
                day[i]="MONDAY"
            elif(k==3):
                day[i]="TUESDAY"
            elif(k==4):
                day[i]="WEDNESDAY"
            elif(k==5):
                day[i]="THURSDAY"
            elif(k==6):
                day[i]="FRIDAY"
            elif(k==7):
                day[i]="SATURDAY"
            elif(k==1):
                day[i]="SUNDAY"
            k=k+1
        print(day[self.d])
print("enter the month")
m=input()
d=int(input("enter the date"))
if d>31:
    print("invalid date")
elif d<=0:
    print("invalid date")
elif m=="feburary"and d>29:
        print("invalid date")
elif (m=="april"or m=="june"or m=="september"or m== "november")and d>30:
        print("invalid date")
else:
    c=Calender_2024(d)
    if m=="january":
        c.jan()
    elif m=="february":
        c.feb()
    elif m=="march":
        c.march()
    elif m=="april":
        c.april()
    elif m=="may":
        c.may()
    elif m=="june":
        c.june()
    elif m=="july":
        c.july()
    elif m=="august":
        c.august()
    elif m=="september":
        c.september()
    elif m=="october":
        c.october()
    elif m=="november":
        c.november()
    else:
        c.december()
    
