#this tracks how many times it has rebooted:
def load_reboot_count():
    try:
        with open('reboot_count.json', 'r+') as f:
            print("file found")
            data = json.load(f)
            print(data)
            data["reboots"] = data["reboots"] + 1
            data["reboot_dates"].append(str(datetime.now()))
            f.seek(0) #makes sure it overwrites itself
            json.dump(data,f)
            return data["reboots"]
    #this will create the file if it doesnt exist
    except FileNotFoundError:
        with open('reboot_count.json', 'w') as f:
            print("file not found, creating new file")
            data = {"reboots":1,"reboot_dates":[]}
            json.dump(data,f,indent=4)
            print("new file made")
        return 1
