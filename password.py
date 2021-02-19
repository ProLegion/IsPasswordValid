'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
def hasLower(word):
    #Split the string into a list(array)
    wordArray = list(word)
    #Get Length of the List, not needed as for loops can just know the length of lists
    #wordLen = len(wordArray)    
    for x in wordArray:
        if(x.islower() == True):
            return True

    return False

def hasUpper(word):
    wordArray = list(word)
    for x in wordArray:
        if(x.isupper() == True):
            return True

    return False

def hasNumber(word):
    wordArray = list(word)
    for x in wordArray:
        if(x.isnumeric() == True):
            return True

    return False

def hasSymbol(word):
    wordArray = list(word)
    for x in wordArray:
        if(x.isalpha() == False):
            if(x.isnumeric() == False):
                return True

    return False

def isVaid(password):
    if(len(password)  > 6):
        if(len(password) < 12):
            if(hasLower(password) == True):
                if(hasUpper(password) == True):
                    if(hasNumber(password) == True):
                        if(hasSymbol(password) == True):
                            return True
    return False

#isValid function test code
'''
pwList = ['1234' , 'password', 'PassWord', 'PassW0rd', 'P@ssW0rd']

for x in pwList:
    print(x, isVaid(x), '\n')
'''

userInput = input("Enter Passwords (Seperate multiples with ,): \n")
passwordList = userInput.split(",")

print('Valid Passwords Are: \n')

for x in passwordList:
    if(isVaid(x) == True):
        print(x, "\n")