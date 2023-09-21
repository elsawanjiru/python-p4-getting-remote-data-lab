from GetRequester import GetRequester
class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = '[{"name":"Daniel","occupation":"LG Fridge Salesman"},{"name":"Joe","occupation":"WiFi Fixer"},{"name":"Avi","occupation":"DJ"},{"name":"Howard","occupation":"Mountain Legend"}]'
CONVERTED_DATA = [{ 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' }, { 'name': 'Joe', 'occupation': 'WiFi Fixer' }, { 'name': 'Avi', 'occupation': 'DJ' }, { 'name': 'Howard', 'occupation': 'Mountain Legend' }]

def test_get_response():
        '''get_response_body function returns response.'''
        requester = GetRequester(URL)
        assert(requester.get_response_body() == JSON_STRING)

def test_load_json():
        '''load_json function returns response.'''
        requester = GetRequester(URL)
        assert(requester.load_json() == CONVERTED_DATA)
