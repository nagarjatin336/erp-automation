from bs4 import BeautifulSoup
from format import formatName

def getFullName(soup):
    try:
        return formatName(soup.find(id='name').get('value'))
    except Exception:
        return None

def getFatherName(soup):
    try:
        return formatName(soup.find(id='prnt_father_name').get('value'))
    except Exception:
        return None

def getMotherName(soup):
    try:
        return formatName(soup.find(id='prnt_mother_name').get('value'))
    except Exception:
        return None

def getGender(soup):
    try:
        return soup.find(id='sex').find('option',attrs={'selected':'selected'}).get('value')[0].capitalize()
    except Exception:
        return None

def getAadharNumber(soup):
    try:
        return soup.find(id='aadhar_card_no').get('value')[-12:]
    except Exception:
        return None

def getMobileNumber(soup):
    try:
        return soup.find(id='phone').get('value')[-10:]
    except Exception:
        return None

def getEmailAddress(soup):
    try:
        return soup.find(id='email').get('value').lower()
    except Exception:
        return None

def getBloodGroup(soup):
    try:
        return soup.find(id='blood_group').find('option',attrs={'selected':'selected'}).get('value')
    except Exception:
        return None

def extract(response, roll, batch):
    soup = BeautifulSoup(response,'html.parser')
    try:
        data = (
            str(roll),
            getFullName(soup),
            getEmailAddress(soup),
            getFatherName(soup),
            getMotherName(soup),
            getMobileNumber(soup),
            getAadharNumber(soup),
            getGender(soup),
            getBloodGroup(soup),
            str(batch),
        )
        return data
    except Exception as error:
        print(error)
        return None
