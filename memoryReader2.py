import os
import os.path as op


lst = {}

start_path = r'C:\\'

maxDepth = 10000
cDepth = 0

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            #get size of subfolders
            # elif entry.is_dir():
            #     total += get_dir_size(entry.path)
    return total


dots = 0
for dirpath, dirnames, filenames in os.walk(start_path):
    if cDepth >= maxDepth:
        break
    try:
        size = get_dir_size(dirpath)
        lst[dirpath] = (size // (2^20))
    except:
        continue
    print("scanning: " + dirpath)
    
    #cDepth += 1

os.system("cls")
def sort_dict_max(original_dict):
    sorted_dict = {}
    while original_dict:
        max_key = max(original_dict, key=original_dict.get)
        sorted_dict[max_key] = original_dict.pop(max_key)
        print("sorting: " + max_key)
    return sorted_dict

final = sort_dict_max(lst)
os.system("cls")
f = open('result_Tree.txt', 'a')
for it in final:
    f.write(str(final[it]) + ', ' + it +  '\n')
    print("writing: " + it)

f.close
