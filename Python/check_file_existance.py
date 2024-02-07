import os

def check_file_existance(filenames):
        if all(os.path.exists(file_path_tmp) for file_path_tmp in file_path_list):
            print("all files exist")
            return True
            
        else:
            print("not all files exist")
            return False
