#Kaleb Nails
#Created: 10/3/2022
#Modified: 10/25/2022
#Purpose: shows how to take bytes that are fromatted like a JSON that
#have bits inside of the message itself.

import json
import struct

#my_bytes_value = b'[{\'Date\': \'2016-05-21T21:35:40Z\', \'CreationDate\': \'2012-05-05\', \'LogoType\': \'png\', \'Ref\': 164611595, \'Classe\': [\'Email addresses\', \'Passwords\'],\'Link\':\'http://some_link.com\'}]'

#The number in binary should be 1.2
my_bytes_value = b'{"DeviceID":"MAMA0001","MessageID":"Y9U7","Payload":"\x9a\x99\x99?","path":"","hops":1,"duckType":2,"topic":16}\r\n'

# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
my_json = my_bytes_value.decode('raw_unicode_escape').replace("'", '"')
print( my_json)
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
print(data)

#This selects the correct value based on the index
#print(data[0]["CreationDate"])
byte_Data = (data["Payload"].encode('raw_unicode_escape'))
readable = struct.unpack('f',byte_Data)
print('-'*20)
print(readable)