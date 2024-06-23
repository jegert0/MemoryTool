#   program returns text file with folders using the most memory

import os
import os.path as op
from maxHeapNode import maxHeap
import dir
import loading as ld

#   dictionary will store all folder paths and their size
dic = {}

#   default start is c drive
start_path = "C:\\"

#   depth variables if you dont want to scan entire computer
# maxDepth = 10000
# cDepth = 0

for dirpath, dirnames, filenames in os.walk(start_path):
    # if cDepth >= maxDepth:
    #     break
    try:
        size = dir.get_dir_size(dirpath)
        dic[dirpath] = (size // (2^20))
    except:
        continue
    ld.loading("scanning", dirpath)
    
    #cDepth += 1

#   arbitrary max heap size
heap = maxHeap(99999999)

#   loading dictonary into heap
for n in dic:
    ld.loading("heaping", n)
    heap.insert(dic[n], n)

#   write heap into text file
f = open('final.txt', 'a')
while heap.size > 0:
    node = heap.removeMax()
    ld.loading("writing", node.path)
    try: #sometimes unwritble characters
        f.write(str(node.data) + ', ' + node.path +  '\n')
    except:
        continue
    
f.close
