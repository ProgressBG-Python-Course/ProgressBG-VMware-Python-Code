import base64

passwd = 'abracadabra'

# base64 needs a byte string
# encoded = base64.b64encode(b'data to be encoded')

passwd_bytes = passwd.encode()
passwd_b64 = base64.b64encode(passwd_bytes)

print(f'passwd_b64: {passwd_b64}')
