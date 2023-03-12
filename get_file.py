import os
import time
DIRECTORY_PATH = r"G:"
DIRECTORY_PATH = "G:\\"

def get_files_data():
    files = []
    for i in os.listdir(DIRECTORY_PATH):
        if i[0]=='.':
            continue
        for i in os.listdir(DIRECTORY_PATH):
            if os.path.isdir(DIRECTORY_PATH+i):
                t_i=time.localtime(os.path.getctime(DIRECTORY_PATH+f'/{i}'))
                files.append({
                    'name':i,
                    'type':'dir',
                    'time':f"{t_i.tm_year}/{t_i.tm_mon}/{t_i.tm_mday} \
{t_i.tm_hour}:{t_i.tm_min if t_i.tm_min>10 else f'0{t_i.tm_min}'}:{t_i.tm_sec}"})
            else:
                files.append({'name':i,'type':'file',
                              'size':os.path.getsize(DIRECTORY_PATH+f'/{i}'),
                              'time':f"{t_i.tm_year}/{t_i.tm_mon}/{t_i.tm_mday} \
{t_i.tm_hour}:{t_i.tm_min if t_i.tm_min>10 else f'0{t_i.tm_min}'}:{t_i.tm_sec}"
                })
        files.sort(key=lambda x:x['type'])

        return files

    return files