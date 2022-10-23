import requests
import json
from lxml import html
import bs4

url = 'https://weblogin.uu.se/idp/profile/cas/login?execution=e1s1'

import requests
from bs4 import BeautifulSoup

login_data = {
             'name' : 'USERNAME',
             'pass' : 'PASSWORD',
             'form_id':'new_login_form',
             'op':'login'
  }

with requests.Session() as s:
    r = s.get(url,headers='',verify=False) 
    print(r.content) # to find name of csrftoken and form_build_id
    soup = BeautifulSoup(r.text, 'lxml')

    csrfToken = soup.find('input',attrs = {'name':'csrfToken'})['value']
    form_build_id = soup.find('input',attrs = {'name':'form_build_id'}) 
    ['value']

    login_data['csrfToken'] = csrfToken
    login_data['form_build_id'] = form_build_id

    r = s.post(url,data=login_data,headers = headers)
    print(r.content)