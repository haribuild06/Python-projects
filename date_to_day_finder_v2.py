#DAY FINDER USING ZELLER CONGRUENCE VERSION 1
# 1. Raw processing of input data
def inputs_processing(date,month,year): # this function take the raw input,
                               # check whether the inputs are numerically and 
                               # logically correct
        if (
                (type(date) is str or float) or (date<=0) or (date>31)) or (
                        (type(month) is str or float) or (month<=0) or (month > 12)) or (
                                (type(year) is str or float) or (year<=0) or (year > 2026)): #this check whether the input is non-zero, non-negative, less than 31 and  is not a string
                return 'ERROR'
        else:
            return (date, month, year)
        
# 2. Checking for leap year        
def year_check(year):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): #checking for leap year 
          leap_year = True
        else:
          leap_year = False
        return leap_year  

# 3. Checking the logic of months and date
def month_date_check(date, month, leap_year):
        month_max_days = {
               1: 31, 2: 28, 3: 31, 4: 30, 
               5: 31, 6: 30, 7: 31, 8: 31, 
               9: 30, 10: 31, 11: 30, 12: 31
        }                
        if month == 2:
           max_days = 29 if leap_year else 28
        else:
           max_days = month_max_days[month] 
            
        if date <= max_days:
           m = month
           q = date
           return q, m
        else:
           return 'ERROR'    

          
# 4. Final input poilish
def input_finals(q, m, year): 
   if (m == 1) or (m == 2):
        zeller_year = year - 1
        m = m + 12 # jan is 13th and feb is 14th month for zeller formula
        k = zeller_year % 100
        j = (zeller_year - k) // 100
   else:    
        k = year % 100
        j = (year - k) // 100
   return q, m, k, j


# 5. Passing the polished inputs to ZELLER's formula      
def formula(q, m, k, j):
        h = (q + ((13*(m+1))//5) +(k) + (k//4) + (j//4) + (5*j)) % 7
        return h 


# 6. Displaying the output neatly              
def display(h,date,month,year):
       days = ['SATURDAY','SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
       day_corr = days[h]
       return f'THIS IS PYTHON DATE TO DAY FINDER\nDATE ENTERED : {date}/{month}/{year}\nTHE DAY CORRESPOUNDING : {day_corr}'


#function calling and error handling
call1 = inputs_processing(24.0,5,2006)
if call1 != "ERROR":
   call2 = year_check(call1[2]) #2
   call3 = month_date_check(call1[0], call1[1], call2) #3
   if call3 != "ERROR":
     call4 = input_finals(call3[0], call3[1], call1[2]) #4
     call5 = formula(call4[0], call4[1], call4[2], call4[3]) #5
     call6 = display(call5, call1[0], call1[1], call1[2]) #6
     print(call6)
   else:
     print('ERROR IN DATE OR MONTH')     
else:
     print('ERROR IN INPUT DATES')