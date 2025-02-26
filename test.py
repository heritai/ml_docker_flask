'''
This module only erves for trying requests to the API
'''

import requests


#localhost_url='http://127.0.0.1:5000' #flask debugging
localhost_url='http://127.0.0.1'    # docker

routes={'index_url' : localhost_url ,
    'functions_url' : localhost_url + '/functions',
    'classification_url' : localhost_url+'/classification/process', 
    'regression_url' : localhost_url + '/regression/process',
    'process_url' : localhost_url + '/process'}

input_params = {
    "n_samples": 10,
    "n_features": 5
}


for i in routes:
    print("\n \n ======= Testing route {} ========= \n \n".format(routes[i]) )
    try:
        response = requests.post(routes[i], data=input_params)
        res=response.json()
    except :
        response=requests.get(routes[i])
        res=response.json()
    print(res)
