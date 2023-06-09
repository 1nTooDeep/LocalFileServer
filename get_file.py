import os
import time
DIRECTORY_PATH = "G:\\"
# DIRECTORY_PATH = "/home/weii/Workfile/python/LocalFileServer"

def get_files_data():
    files = []
    for i in os.listdir(DIRECTORY_PATH):
        if i[0]=='.':
            continue
        if os.path.isdir(DIRECTORY_PATH+i):
            t_i=time.localtime(os.path.getctime(DIRECTORY_PATH+f'/{i}'))
            files.append({
                'name':i,
                'type':'dir',
                'ctime':f"{t_i.tm_year}/{t_i.tm_mon}/{t_i.tm_mday} \
{t_i.tm_hour}:{t_i.tm_min if t_i.tm_min>10 else f'0{t_i.tm_min}'}:{t_i.tm_sec}"})
            continue
        else:
            t_i=time.localtime(os.path.getctime(DIRECTORY_PATH+f'/{i}'))
            files.append({'name':i,'type':'file',
                            'size':os.path.getsize(DIRECTORY_PATH+f'/{i}'),
                            'ctime':f"{t_i.tm_year}/{t_i.tm_mon}/{t_i.tm_mday} \
{t_i.tm_hour}:{t_i.tm_min if t_i.tm_min>10 else f'0{t_i.tm_min}'}:{t_i.tm_sec}"
            })
    files.sort(key=lambda x:x['type'])

    return files