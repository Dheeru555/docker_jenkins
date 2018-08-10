import sys
import pytest
import requests
import json

def test_get_emp_details():
    url_formatted = '{0}'.format('http://opsitcdkr01:5067/')
    r = requests.get(url_formatted)
    assert 200 == r.status_code, r.text
     


def test_emp_age_details():
    url_formatted = '{0}'.format('http://opsitcdkr01:5067/')
    r = requests.get(url_formatted)
    data = r.json()
    assert 2005 == data['EMP_Details'][0]['age']
    
     



def test_emp_post_details():
    url_formatted = '{0}{1}'.format('http://opsitcdkr01:5067/', 'emp/check')
    payload = get_alert_payload()
    headers = {'content-type': 'application/json'}


    r = requests.post(url=url_formatted,
                       data=json.dumps(payload),
                       headers=headers)
    assert 200 == r.status_code, r.text
     

def get_alert_payload():
    return {
        "name":"Sai Dheeraj Devineni","company":"TCS","age":23
    }
