import random


def safeLock():
    shuffleKey=raw_input('Enter the shuffleKey :')
    #sets the shuffleKey value as the randomizing parameter
    #Checks if the entered key is a safeLock key or not
    if (shuffleKey != '1996'):
        print "shuffleKey accepted! Running..."
        callMenu(shuffleKey)
    else :
        #Yet to add: A set of safe messages will be printed as the result of decryption
        print "Initiating safeLock! Print random safe messages here! ;)"

def encrypt(shuffleKey):
    keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
    keyBaseArray = list(keyBase)
    codeKeyArray = keyBaseArray
    sentence = raw_input("What do you want to encrypt? : ")
    charArray = list(sentence)
    print shuffleKey
    for count1,elem in enumerate(charArray):
        shuffleKey=int(shuffleKey)
        shuffleKey+=count1
        random.seed(shuffleKey)
        random.shuffle(codeKeyArray)
        for count2,elem2 in enumerate(keyBase):
            if elem == elem2:
                charArray[count1]=codeKeyArray[count2]
    string1=''.join(charArray)
    return string1

def decrypt(shuffleKey):
    keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
    keyBaseArray = list(keyBase)
    codeKeyArray = keyBaseArray
    sentence = raw_input("What do you want to decrypt? : ")
    charArray = list(sentence)
    for count1,elem in enumerate(charArray):
        shuffleKey=int(shuffleKey)
        shuffleKey+=count1
        random.seed(shuffleKey)
        random.shuffle(codeKeyArray)
        for count2,elem2 in enumerate(codeKeyArray):
            if elem == elem2:
                keyBaseArray = list(keyBase)
                charArray[count1]=keyBaseArray[count2]
    string1=''.join(charArray)
    return string1

def callMenu(shuffleKey):
    choice = 0
    while (choice!='3'):
        choice = raw_input("\n1.Encrypt \n2.Decrpyt \n3.Exit \nEnter your choice : ")
        if choice=="1":
            answer=encrypt(shuffleKey)
            print 'Encrypted sentence is : ' + '\033[1m\033[31m' + answer + '\033[0m'

        elif choice=="2":
            answer=decrypt(shuffleKey)
            print 'Decrypted sentence is : ' + '\033[1m\033[32m' + answer + '\033[0m'
        elif choice=="3":
            exit()
        else:
            print("Invalid choice, please choose again\n")

if __name__ == '__main__':
    try:
        safeLock()
    except KeyboardInterrupt:
        print('\nExiting...')
