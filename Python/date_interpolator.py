#Kaleb Nails 
#interpolate in between dates from a string.
#This will give all the dates in between these two dates, I could make this a function
#but this is fine for now.

from datetime import datetime, timedelta

date_cell = '2024_12_15'
date_start = '2024_12_12'
                        
#Convert date format
start_date = datetime.strptime(date_start, '%Y_%m_%d')
end_date = datetime.strptime(date_end, '%Y_%m_%d')
                        
# Generate a list of strings of all the dates in between start and end dates
date_list = []

current_date = start_date
while current_date <= end_date:
  date_list.append(current_date.strftime('%Y_%m_%d'))
  current_date += timedelta(days=1)
  
print(date_list)
