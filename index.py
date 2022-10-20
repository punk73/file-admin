
# get sub dir 

# loop through sub dir

# if contain date, make new folder based on that specific date

# move to that folder
from datetime import datetime
import os
import re 
from distutils.dir_util import copy_tree

def get_immediate_subdirectories(a_dir):
    
    res = [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

    return sorted(res)

def getdate(folder, reg = '\d+-\d+-\d+'):
    # is contain date

    # check if that day folder exists if not create

    # move this folder to that folder / or atleast copy
    res = re.search(reg, folder)
    if res:
        res = res.group(0)
        return res.strip()
    else:
        return ''

def move():
    monthFolder= input("input directory untuk dirapikan : ") # "./agustus"
    subdir = get_immediate_subdirectories(monthFolder)
    # print(subdir)
    res = []
    for folder in subdir:
        # print(folder)
        dt = getdate(folder)
        if dt != '':
            dtobj =  datetime.strptime(dt, '%Y-%m-%d')
        else:
            continue

        new_format = dtobj.strftime('%d %B')
        new_folder = monthFolder +'/results/'+ new_format
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # print(new_format, folder)
        copy_tree(  monthFolder + "/"+ folder, new_folder + '/' + folder )
        # new_folder = 

move()
print('finish! data rapi! yeayyy!!!')
