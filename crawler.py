import requests
from bs4 import BeautifulSoup

# Hardcode URL for testing purposes, will integrate input later
url = ""                      # needs to be verified as valid URL
try:
    # downloading HTML page
    target = requests.get(url)
    # initializing bs4 object
    soup = BeautifulSoup(target.content, 'html.parser')
    status = target.status_code

    # contains names or ids of text fields only; final output of the program
    field = []

    for form in soup.find_all('input', type='text'):
        '''
            Build input field list here
                Remember to only record text inputs
        '''
        field.append([{'id': form.get('id'), 'name': form.get('name')}])
        ''' 
            field is stored as a list of dictionaries 
            each containing the 'id' and 'name' attributes of the respective input text fields.
            If the attribute isn't present it's value is stored as None
        '''
except Exception as exception:
    print(exception)
    print('URL DOES NOT EXIST!')
