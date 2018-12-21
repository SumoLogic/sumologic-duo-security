import duo_client
import time
from botocore.vendored import requests
import os
import json

i_key = os.environ.get('I_KEY')
s_key = os.environ.get('S_KEY')
host = os.environ.get('HOST')
collector_url = os.environ.get('COLL_ENDPOINT')
scan_interval_in_sec = int(os.environ['SCAN_INTERVAL_IN_SEC'])

admin_api = duo_client.Admin(
        ikey=i_key,
        skey=s_key,
        host=host
    )



def fetch_logs(min_time=None, max_time=None):
    auth_logs = admin_api.get_authentication_log(api_version=2, mintime=min_time, maxtime=max_time) # kwarg mintime
    return auth_logs['authlogs'] #this isn't considering iteration in event too many messages returned.



def fetch_admin_logs(min_time=None):
    admin_logs = admin_api.get_administrator_log(mintime=min_time) 
    print('Retrieved admin Logs.')    
    return admin_logs


def fetch_telephony_logs(min_time=None):
    telephony_logs = admin_api.get_telephony_log(mintime=min_time) 
    print('Retrieved Telephony Logs::')    
    return telephony_logs

def format_auth_logs(data):
     out = []
     for i in data:
         i['auth_device']['name'] = '*****'
         out.append(i)
     data = '\n'.join([json.dumps(i) for i in out])
     return data

def format_telephony_logs(data):
     out = []
     for i in data:
         i['phone']= '*****'
         out.append(i)
     data = '\n'.join([json.dumps(i) for i in out])
     return data




def format_admin_logs(data):
    out= []
    for i in data:
        if(i.get('description')):
            i['description'] = json.loads(i['description'])
            if('device' in i['description']):
                i['description']['device'] = "*****"
            elif ('phones' in i['description'] ):
                for ph in (i['description']['phones']):
                    i['description']['phones'][ph]['number'] = "*****"
            elif ('phone' in i['description'] ):
                i['description']['phone'] ="*****"
            out.append(i)
        else:
            print("admin logs without description")
            
    data = '\n'.join([json.dumps(i) for i in out])
    return data
        
        
            
 
        


def dump_logs(data):
    print('dumping logs')
    r = requests.post(url=collector_url, data=data)
    tries = 10
    while r.status_code != 200:
        if tries <= 0:
            raise Exception('Excessive retries. Issue in posting log data.')
        tries-=1
        time.sleep(2)
        r = requests.post(collector_url, data=data)
    print('dumped successfully.')

def lambda_handler(req, context):
    logs = fetch_logs(min_time=(time.time()-scan_interval_in_sec)*1000, max_time=time.time()*1000)
    logs = format_auth_logs(logs)
    #print(logs)
    dump_logs(logs)

#fetch admin logs
    logs_admin = fetch_admin_logs(min_time=(time.time()-scan_interval_in_sec))
    logs_admin = format_admin_logs(logs_admin)
    #print(logs_admin)
    dump_logs(logs_admin)

#fetch telephony logs
    logs_telephony = fetch_telephony_logs(min_time=(time.time()-scan_interval_in_sec))
    logs_telephony = format_telephony_logs(logs_telephony)
    #print(logs_telephony)
    dump_logs(logs_telephony)


