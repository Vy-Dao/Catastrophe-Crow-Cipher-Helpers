arr1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr2 = ['w','v','n','x','o','b','z','r','h','m','y','e','q','t','l','u','f','i','a','c','g','j','s','p','k','d']
arr3 = [
    ['o','j','t','a','u','i','o','s','e','r','o','e','a','i','n','p','t','g','e','t','i','i','n','e','z','u'],
    ['o','e','g','d','e','s','a','e','q','i','d','w','t','a','n','u','i','c','b','u','e','r','o','l','t','h'],
    ['s','d','f','e','n','h','f','f','m','o','y','m','l','n','f','r','i','h','a','i','o','i','s','a','n','u'],
    ['r','h','d','e','e','i','h','o','v','t','r','m','d','o','o','d','a','i','l','a','p','j','r','i','r','i'],
    ['l','i','n','u','o','m','d','a','e','h','s','a','d','p','e','l','w','t','o','t','a','d','e','g','k','t'],
    ['a','a','e','w','i','n','n','z','l','j','d','e','n','l','s','a','e','p','h','s','n','a','y','i','e','h'],
    ['e','d','o','h','n','t','n','t','a','s','h','l','d','m','r','r','o','u','m','r','f','t','s','e','n','e'],
    ['o','g','k','a','d','i','y','h','l','k','a','h','q','i','t','w','a','e','s','y','s','e','o','n','b','l'],
    ['n','e','r','e','n','s','c','h','r','c','i','x','d','e','l','t','d','y','y','y','a','s','t','u','m','v'],
    ['r','s','a','k','f','b','r','s','i','m','e','r','b','s','e','n','n','o','e','i','t','t','u','s','l','m'],
]
done = False
def Newline():
    print("#################")
    print()

def AlphabetCipher():
    cont = "Y"
    while cont == "Y":
        result = ""
        code = input("Please enter the code here: ")
        for char in code:
            if (char == " "):
                result += " "
            else:
                indexCode = arr2.index(char.lower())
                result += arr1[indexCode].upper()
        print("Code: " + code)
        print("Result: " + result)
        cont = input("Do you want to continue (Y/N): ").upper()
        print()


def CrossAlphabetCipher():
    cont = "Y"
    while cont =="Y":
        result = ""
        keyCode = input("Please enter the key code (Alphabet): ")
        keyCodeSize = len(keyCode)
        keyCodeIndex = 0
        numberCode = input("Please enter the number code: ")
        for num in numberCode:
            index1 = 0
            if keyCodeIndex == keyCodeSize:
                keyCodeIndex = 0
            if (num != "0"):
                index1 = int(num) - 1
            else:
                index1 = len(arr3) -1
            if(keyCode[keyCodeIndex] == " "):
                result += " "
            else:
                index2 = int(arr1.index(keyCode[keyCodeIndex].lower()))
                result += arr3[index1][index2]
            keyCodeIndex += 1
        print("Result: " + result)
        cont = input("Do you want to continue (Y/N): ").upper()
        print()    



while not done:
    print("Welcome to Catastrophe Crow Helper")
    print("1. Alphabet Cipher")
    print("2. Cross Alphabet Cipher")
    print("3. Quit")
    userInput = input("What do yo want to do: ")
    if (userInput == "1"):
        AlphabetCipher()
        Newline()
    elif(userInput == "2"):
        CrossAlphabetCipher()
        Newline()
    else:
        done = True

