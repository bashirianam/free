import requests
import time

def login():
	url = 'https://api.tapswap.ai/api/account/login'
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://app.tapswap.club',
	    'Referer': 'https://app.tapswap.club/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'x-app': 'tapswap_server',
	    'x-cv': '608'
	}
	data = {"init_data":"query_id=AAG0MuMHAwAAALQy4wfVrgq3&user=%7B%22id%22%3A6574781108%2C%22first_name%22%3A%22Amir%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22fa%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1717083440&hash=f108015b041346a130018e94bbad5ed3215856c366f803f3094bdc08533a4e14","referrer":"","bot_key":"app_bot_0"}
	
	response = requests.post(url, headers=headers, json=data)
	return response.json()["access_token"]
print(login())
url = 'https://api.tapswap.ai/api/player/submit_taps'

headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Authorization': f'Bearer {login()}',
	    'Connection': 'keep-alive',
	    'Content-Id': '6574231932',
	    'Content-Type': 'application/json',
	    'Origin': 'https://app.tapswap.club',
	    'Referer': 'https://app.tapswap.club/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'x-app': 'tapswap_server',
	    'x-cv': '608'
	}
while True:
	try:
		data ={"taps":13,"time":1717083543277}
		time.sleep(10)
		
		response = requests.post(url, headers=headers, json=data)
		
		print(response.json())
	except Exception as e:
		print(e)
