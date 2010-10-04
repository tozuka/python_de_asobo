import httplib,urllib,urllib2
# import oauth.oauth as oauth
import oauth
 
url = "http://gdd-2010-quiz-japan.appspot.com/oauth/d773c16097cec09c95643b94"
# params = urllib.urlencode({ 'hello': 'world' })
params = { 'hello': 'world' }

consumer_key = 'd773c16097cec09c95643b94'
secret_key   = '9b3d2aa7352a6e65d96388d5'
 
consumer = oauth.OAuthConsumer(consumer_key, secret_key)
#request  = oauth.OAuthRequest.from_consumer_and_token(consumer, http_method='POST', http_url=url, parameters=params)
request  = oauth.OAuthRequest.from_consumer_and_token(consumer, http_method='POST', http_url=url, parameters=params)
request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, None)
#self.connection.request(oauth_request.http_method, self.request_token_url, headers=oauth_request.to_header()) 
#        response = self.connection.getresponse()
#stream = urllib.urlopen(request.to_url())
#print stream.read()
print request.to_url()
print request.to_header()

conn = httplib.HTTPConnection("gdd-2010-quiz-japan.appspot.com")
conn.request("POST", "/oauth/d773c16097cec09c95643b94", urllib.urlencode(params), request.to_header('devquiz'))
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
print data

 
# req = urllib2.Request(request.to_url(),data=data,headers=request.to_header('devquiz'))
#try:
#  print urllib2.urlopen(req).read()
#except urllib2.HTTPError, e:
#  print e
