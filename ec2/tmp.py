# coding: utf-8
get_ipython().magic('save -f tmp.py 1-19')
import requests
get_ipython().magic('save -f tmp.py 1-19')
requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document/')
response = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document/')
response.text
get_ipython().magic('save -f tmp.py 1-19')
