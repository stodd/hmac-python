from urllib2 import Request
from urllib import quote
from hashlib import sha1
import hmac
import binascii

def sign_request(request, secret_key):
	req = Request(request)
	raw = "%s\n%s\n%s\n%s" % (req.get_method(),req.get_host(),req.get_selector().split('?')[0],req.get_selector().split('?')[1])
	key = bytes(secret_key)
	print(raw)
	hashed = hmac.new(key, raw, sha1)
	signature = binascii.b2a_base64(hashed.digest())
	return request + '&signature=%s' % quote(signature, '\n')

