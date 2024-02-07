#Kaleb Nails
import sys
import os
from datetime import datetime, timedelta
#Don't really need this class, but its fine to include for this example
class Message:
    def __init__(self, content):
        self.content = content

# Create an instance of the Message class
message = Message('meto')



# This checks for the date arguement
def contains_date(discord_message):
    # Split the message into words
    words = discord_message.split()

    # Iterate through each word to check for the date format
    date_cell = []
    for word in words:
        if len(word) == 10 and word.count('_') == 2:
            # Check if the word has the format "YYYY_MM_DD"
            try:
                year, month, day = map(int, word.split('_'))
                # You can add additional checks for valid date ranges if needed
                if 2022 <= year <= 2200 and 1 <= month <= 12 and 1 <= day <= 31:

                    date_cell.append({'year':year,'month':month,'day':day })

            except ValueError:
                # Ignore if there is a ValueError (e.g., non-integer parts)
                pass

    return  date_cell



directory_location = "/var/tmp/wx/"
print(message.content.lower())

if 'meto' in message.content.lower():#'ip?':
    try:
        print('its true')
        python_script_path = 'discord_meteogram.py'

        #argnum dictates how many arguements have as an input and sort the dates in order
        date_cell = contains_date(message.content.lower())
        print(f"the unsorted date_cell: \n {date_cell}")
        date_cell = sorted(date_cell, key=lambda x: (x['year'], x['month'], x['day']))
        print(f"the sorted date_cell: \n {date_cell}")

        #checks for the propper amounts of dates
        if  0<= len(date_cell) <= 2:
            for i in date_cell:
                python_script_path += f" {i['year']}_{str(i['month']).zfill(2)}_{str(i['day']).zfill(2)}"
                print(python_script_path)


            if len(date_cell) == 0:
                python_script_path = 'discord_meteogram.py'
                print(python_script_path)
                #await message.channel.send("Generating") ###########################
                #subprocess.run(['python',python_script_path]) #######################

            #double check file exists
            elif len(date_cell)==1:
                print('using one provided date')
                file_path = f"{directory_location}{date_cell[0]['year']}_{str(date_cell[0]['month']).zfill(2)}_{str(date_cell[0]['day']).zfill(2)}_weather_station_data.csv"

                if os.path.exists(file_path):
                        print("File exists.")

                        python_script_path = f"discord_meteogram.py {date_cell[0]['year']}_{str(date_cell[0]['month']).zfill(2)}_{str(date_cell[0]['day']).zfill(2)}"
                        print(python_script_path)
                        #await message.channel.send(f"Date exists. Generating {file_path}") ###########################
                        #subprocess.run(['python',python_script_path]) #######################
                else:
                    print(f"File {file_path} does not exist. defaulting to current date")


            #This is for a range of 2 dates
            elif len(date_cell)==2:
                print('using two provided date')
                date_start = f"{date_cell[0]['year']}_{str(date_cell[0]['month']).zfill(2)}_{str(date_cell[0]['day']).zfill(2)}"
                date_end =  f"{date_cell[1]['year']}_{str(date_cell[1]['month']).zfill(2)}_{str(date_cell[1]['day']).zfill(2)}"
                print(date_start)
                print(date_end)

                start_date = datetime.strptime(date_start, '%Y_%m_%d')
                end_date = datetime.strptime(date_end, '%Y_%m_%d')

                # Generate a list of strings of all the dates in between start and end dates
                date_list = []
                current_date = start_date
                while current_date <= end_date:
                    date_list.append(current_date.strftime('%Y_%m_%d'))
                    current_date += timedelta(days=1)

                # Print the list of dates
                print(date_list)
                #Check if all the files exist
                file_path_list = [f"{directory_location}{date_temp}_weather_station_data.csv" for date_temp in date_list]
                print(file_path_list)
                all_exist = all(os.path.exists(file_path_tmp) for file_path_tmp in file_path_list)

                if all_exist:
                    # Run the subprocess
                    print(f"Date exist between {date_start} {date_end}.")
                    python_script_path = f"discord_meteogram.py {date_start} {date_end}"
                    print(python_script_path)
                    #await message.channel.send(f"Date exist between {date_start} {date_end}.") ###########################
                    #subprocess.run(['python',python_script_path]) #######################
                else:
                    print("Not all files exist.")
                    #await message.channel.send(f"not all dates exist between {date_start} and {date_end}.") ###########################

        else:
            error_message = '''invalid amount of dates sent please enter following the example inputs below:
                current date: meto
                specific date: meto 2024_08_01
                date range: meto 2023_06_05 2024_08_01'''

            print(error_message)
            #await message.channel.send(error_message) ##########################
    except ValueError:
        # Ignore if there is a ValueError (e.g., non-integer parts)
        pass
