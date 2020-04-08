'''
Created on 17/02/2013

@author: Xiang
'''
import re











mo = re.match("http://.+\net", "http://mundogeek.net")
mo = re.match("http://(.+)\(.{3})", "http://mundogeek.net")
print mo.groups()