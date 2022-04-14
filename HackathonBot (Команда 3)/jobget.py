import requests

api = 'v3.r.136525014.b04c1263d31b4ff0f92ad70fde0c4a0d8377bc8a.182abcaec3e32d7806b9a489cf4f10bf1fd9b538'

def request(age, gender, experience):
    response = requests.get('https://api.superjob.ru/2.0/'+api+'/vacancies/',
    params={'town': 'Москва', 'age': age, 'gender': gender, 'experience': experience})
    return response.text
    
    
    


