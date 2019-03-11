import base64

# Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings.
# More on the topic: https://docs.python.org/release/3.0.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit
passwd = 'abracadabra'
print(f'type(passwd): {type(passwd)}')

# you need to pass to b64encode a byte string, not a "text" string
passwd_bytes = passwd.encode("utf-8")

# Encode the bytes-like objects using Base64 and return the encoded bytes.
encoded_pass_bytes = base64.b64encode(passwd_bytes)

# in python 3 encoded_pass_bytes will be a 'byte' string
print(f'type(encoded_pass_bytes): {type(encoded_pass_bytes)}')
print(f'encoded_pass_bytes: {encoded_pass_bytes}')

# if you need it to be a "normal" (i.e. text str), you have to decoded it back with:
encoded_pass_str = encoded_pass_bytes.decode("utf-8")
print(f'encoded_pass_str: {encoded_pass_str}')

print(base64.b64decode(encoded_pass_str).decode())


