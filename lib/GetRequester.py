import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            response_body = response.content.decode('utf-8')
            print("Response content:")
            print(response_body)
            return response_body
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON: {str(e)}")
