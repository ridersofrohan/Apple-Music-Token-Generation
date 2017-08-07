# MAKE SURE TO RUN USING PYTHON 2

import jwt
import cryptography
import datetime
import requests

def create_token():
  keyfile = open("YOUR_FILENAME.p8", 'r')
  secret = keyfile.read()

  kid = "6666666666"
  iss = "9999999999"
  iat = datetime.datetime.now()
  exp = datetime.datetime.now() + datetime.timedelta(weeks=6)

  payload = {
    "iss": iss,
    "exp": exp,
    "iat": iat
  }

  headers = {
    "alg": "ES256",
    "kid": kid
  }

  token = jwt.encode(payload, secret, algorithm='ES256', headers=headers)
  return token

def make_request(token):
  url = "https://api.music.apple.com/v1/catalog/us/charts?types=songs,albums&genre=20&limit=1"
  headers = {"Authorization": "Bearer {}".format(token)}
  print(headers)
  response = requests.get(url, headers=headers, allow_redirects=False)
  print(response.content)
  print(response.status_code)

if __name__ == "__main__":
  token = create_token()
  print(token.decode('utf-8'))

  make_request(token.decode('utf-8'))
