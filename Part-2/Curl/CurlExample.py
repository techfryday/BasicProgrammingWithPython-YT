import pycurl
from io import BytesIO
import certifi

c = pycurl.Curl()
bobj = BytesIO()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(pycurl.URL, "https://api.github.com/users")
c.setopt(pycurl.WRITEDATA, bobj)
c.perform()
c.close()
body = bobj.getvalue()
print(body.decode('utf8'))