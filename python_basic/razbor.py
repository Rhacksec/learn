import os, csv
way='/mnt/data/WORK/'
#way= '/mnt/data/'
with open('contents2.csv', 'w') as ff:
    dwayf = {}
    for dirpath, dirnames, filenames in os.walk(way):
        
        for filename in filenames:
            
            full_path_to_file = os.path.join(dirpath, filename)
            csv.writer(ff).writerow([full_path_to_file, os.path.getsize(full_path_to_file)])
            if filename in dwayf.keys(): dwayf[filename].append(full_path_to_file)
            else : dwayf[filename]=[os.path.getsize(full_path_to_file), full_path_to_file]

#print (dwayf)
for key in dwayf:
    if len(dwayf[key]) > 2 : print (dwayf[key])
