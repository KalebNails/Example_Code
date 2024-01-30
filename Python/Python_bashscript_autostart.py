# set_variables.py
#Kaleb Nails

import subprocess

# List of sensor devices
sensor_devices = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2']  # Add more devices if needed

# Create a Bash script content
bash_script_content = '#!/bin/bash\n\n'

# Loop through each sensor device
for i, device in enumerate(sensor_devices, start=1):
    # Set the variable for each sensor
    variable_name = f'alpha{i}_device'
    bash_script_content += f'{variable_name}="{device}"\n'

    # Start the logger for each sensor
    bash_script_content += f'echo "Starting alpha{i} logger"\n'
    bash_script_content += f'screen -dm -S alpha{i} python3 OPC_Simple_v2.py ${variable_name}\n\n'

# Write the Bash script to a file
with open('test_start_loggers.sh', 'w') as bash_script_file:
    bash_script_file.write(bash_script_content)

# Make the Bash script executable
#subprocess.run(['chmod', '+x', 'test_start_loggers.sh.sh'])
