from oauth2client.client import SignedJwtAssertionCredentials
from googleapiclient.discovery import build

import httplib2

# YOU NEED TO CREATE A SERVICE ACCOUNT ON CONSOLE DEVELOPERS
service_account_name='XXXXXXXXXXXX-nh32ofjd3lotfbjj206bfp2eqvstco7p@developer.gserviceaccount.com'
scope='https://www.googleapis.com/auth/urlshortener'
f = file('/tmp/shortener.p12','rb')
key = f.read()
f.close()

credentials = SignedJwtAssertionCredentials(service_account_name, key, scope)
http = credentials.authorize(httplib2.Http())

service = build("urlshortener", "v1", http=http)
url = service.url()

# INSERT
#body = {'longUrl': 'http://code.google.com/apis/urlshortener/' }
#resp = url.insert(body=body).execute()

# GET
item = url.get(shortUrl='http://goo.gl/1KZjUU')
result = item.execute()
print result

# LIST (dont working)
items = url.list()
print 'Token: %s' % items.http.request.credentials.token_response
result = items.execute(http=http)
print result

