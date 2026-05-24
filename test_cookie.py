import requests
s = requests.Session()
r2 = s.post('http://localhost:5000/aau/threatmapper/aaulab/xss_low', data={'username': 'Hermela', 'password': 'passwd4'}, allow_redirects=False)
for cookie in s.cookies:
    print(cookie.name, cookie.value, "HttpOnly:", cookie.has_nonstandard_attr('HttpOnly'))
