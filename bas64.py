import base64

def encode_base64(plain_text):
    return base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
    

to_encode = "Hello, World!"
encoded = encode_base64(to_encode)

print(f"Oryginalny tekst: {to_encode}")
print(f"Zaszyfrowany tekst: {encoded}")

def deszyfruj_base64(encoded_text):
    return base64.b64decode(encoded_text).decode('utf-8')

decoded = deszyfruj_base64(encoded)

print(f"Odszyfrowany tekst: {decoded}")
