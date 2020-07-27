import requests

def get_api_status():
	url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
	headers = {'Accept': 'application/vnd.github.v3+json'}		
	r = requests.get(url, headers=headers)		
	status_code = r.status_code
	return status_code

	