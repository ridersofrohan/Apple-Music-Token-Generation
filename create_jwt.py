# MAKE SURE TO RUN USING PYTHON 2

import jwt
import cryptography
import datetime
import requests

def create_token():
  # Replace YOUR_FILENAME with the filename of your secret key
  filename = "YOUR_FILENAME.p8"
  keyId = "1121212121"
  teamId = "2222222222"

  keyfile = open(filename, 'r')
  secret = keyfile.read()

  iat = datetime.datetime.now()
  exp = datetime.datetime.now() + datetime.timedelta(weeks=6)

  payload = {
    "iss": teamId,
    "exp": exp,
    "iat": iat
  }

  headers = {
    "alg": "ES256",
    "kid": keyId
  }

  token = jwt.encode(payload, secret, algorithm='ES256', headers=headers)
  return token

def make_request(token):
  url = "https://api.music.apple.com/v1/catalog/us/charts?types=songs,albums&genre=20&limit=1"
  headers = {"Authorization": "Bearer {}".format(token)}
  response = requests.get(url, headers=headers, allow_redirects=False)

  print("\n\n-----RESPONSE------")
  print(response.status_code)
  print(response.content)

if __name__ == "__main__":
  token = create_token().decode('utf-8')

  print("\n\n-----TOKEN------")
  print(token)
  print("\n\n-----CURL-------")
  print("curl -v -H 'Authorization: Bearer {}' \"https://api.music.apple.com/v1/catalog/us/charts?types=songs,albums&genre=20&limit=1\" ".format(token))

  make_request(token)
