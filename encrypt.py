def encrypt(strIn):
  strOut = ''
  for char in strIn:
    strOut += chr((ord(char) + 2))
  return strOut

def decrypt(strIn):
  strOut = ''
  for char in strIn:
    strOut += chr((ord(char) - 2))
  return strOut

def main():
  strIn = 'Hello, my name is Andrew!'
  print("String to encrypt: ", strIn)
  
  encryptedString = encrypt(strIn)
  print("Encrypted version: ", encryptedString)

  decryptedString = decrypt(encryptedString)
  print("Decrypted version: ", decryptedString)

if __name__ == '__main__':
  main()

