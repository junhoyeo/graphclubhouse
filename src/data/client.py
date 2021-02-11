import json
from constants import API_URL, USER_ID, AUTH_TOKEN, HEADERS

def authenticated_request(request_function, endpoint, *args):
    res = request_function(API_URL + endpoint, headers=dict({
        'CH-UserID': str(USER_ID),
        'Authorization': f'Token {AUTH_TOKEN}'
    }, **HEADERS), *args)
    try:
        data = json.loads(res.text)
    except:
        data = res.text
    return [res.status_code, data]
