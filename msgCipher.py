def caesarCipher(key, msg):
    newMsg = ""
    for i in range(0, len(msg)):
        numValue = ord(msg[i]) - ord('a') + key
        numValue %= 26
        numValue += ord('a')
        newMsg += chr(numValue)
    return newMsg

def symmCipher(msg):
    newMsg = ""
    for i in range(0, len(msg)):
        symmIndex = ord('z') - ord(msg[i]) + ord('a')
        newMsg += chr(symmIndex)
    return newMsg
        
    
def main():
    msg = input("Please enter your message: ")
    key = int(input("Please pick a key: "))
    caesarMsg = caesarCipher(key, msg)
    symmMsg = symmCipher(msg)
    print(f"Original msg: {msg}")
    print(f"Caesar msg: {caesarMsg}")
    print(f"Symmetrical msg: {symmMsg}")
