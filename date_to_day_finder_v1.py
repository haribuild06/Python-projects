#potta verison
#DAY FINDER USING ZELLER CONGRUENCE VERSION 1
def date_to_day(date, month, year):
    print('welcome to python date to day finder')
    print(f'date : {date}/{month}/{year}')
    while True:
        #date
        if (date<=0) or (date>31):
            print('invalid input')
            break
        else:
            q = date
        #month
        if (month<=0) or (month>12):
            print('invalid input')
            break
        else:
            if month == 1:
                m = 13
                year -=1
            elif month == 2:
                m = 14
                year -=1
            else:
                m = month
        #year 
        if (year<=0) or (year>2026):
            print('invalid input')
            break
        else:
            k = year%100
            j = (year-k)//100

        
      
            def formula(q,m,k,j):
                h = (q + ((13*(m+1))//5) +(k) + (k//4) + (j//4) + (5*j)) % 7#zeller's formula
                return h
            def day_correspounding(h):
                while True:  
                    if h == 0:
                        day = "saturday"      
                    elif h == 1:
                        day = "sunday"
                    elif h == 2:
                        day = "monday"
                    elif h == 3:
                        day = "tuesday"
                    elif h == 4:
                        day = "wedensday"
                    elif h == 5:
                        day = "thursday"
                    elif h == 6:
                        day = "friday"            
                    else:
                        print('error occure')
                        break
                    return f"the day is {day}"

#test
            funct1 = formula(q,m,k,j)
            return day_correspounding(funct1) 
funct3 = date_to_day(date=24, month=5, year=2006) #error
print(funct3)   