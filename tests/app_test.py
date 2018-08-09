import sys 
import pytest 
import requests 
import json 


 



 

 def test_get_emp_details(url): 
     url_formatted = '{0}{1}'.format(url, 'check1/') 
     r = requests.get(url_formatted) 
     assert 200 == r.status_code, r.text 
 

 

// def test_ial_alert_insert(url): 
//     url_formatted = '{0}{1}'.format(url, 'ial_alert') 
//     payload = get_alert_payload() 
//     headers = {'content-type': 'application/json'} 
 

//     r = requests.post(url=url_formatted, 
//                       data=json.dumps(payload), 
//                       headers=headers) 
//     assert 201 == r.status_code, r.text 
