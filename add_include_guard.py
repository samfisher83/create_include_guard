import os
import glob



def add_include_guard(filename):
    file = open(filename,"r")
    content = [i.strip() for i in file.readlines()]
    file.close()

    cap_file_name = filename.upper().replace(".","_")


    if(not does_contain_ifndef(content)):
        content.insert(0,"#define {0}".format(cap_file_name))
        content.insert(0,"#ifndef {0}".format(cap_file_name))
        content.append("#endif")
    else:
        return
        
    
    file = open(filename,"w")
    content = map(lambda x:x + '\n',content) 
    file.writelines(content)
    file.close()



def does_contain_ifndef(data):
    has_indef = False
    
    for i in data:
        if "ifndef" in i:
            has_indef = True

    return has_indef
    

def handle_all_csv():
    files = glob.glob("*.h")
    for file in files:
        add_include_guard(file)

handle_all_csv()

