#import urllib and requests libraries
import urllib
import requests

#Insert your API key generated from cuttly API page
api_key = 'insert api key here'

#Enter the link you want to shorten
url = urllib.parse.quote('insert url you want to shorten')
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=insert your custom name here(optional)"

#Get data from your API provider. Data shall be sent in json format
data = requests.get(api_url).json()["url"]

#If data status returned is equal to 7, then new link will be returned. Check API documentation for other status codes.
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("Error Shortening URL:", data)