def check_password_strength(password):
    password_strength = True if password.__len__()>=8 else False
    
    isUpper = False
    isLower = False
    isDigit = False
    isSpecial = False

    for i in password:
        if(65<=ord(i)<=90):
            isUpper = True
        if(97<=ord(i)<=127):
            isLower = True
        if(49<=ord(i)<=57):
            isDigit = True
        if(32<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126):
            isSpecial = True
        
    password_strength =  isUpper and isLower and isDigit and isSpecial

    if(password_strength):
        print("Password is STRONG")
    if(not isUpper):
        print("Your password is missing upper case")
    if(not isLower):
        print("Your password is missing lower case")
    if(not isDigit):
        print("Your password is missing number")
    if(not isSpecial):
        print("Your password is missing special character")

    return 1


def main():
    password = ""
    while(password!="n"):
        print("Enter n to terminate")
        password = input("Enter the password: ")
        check_password_strength(password)
        print("\n")

main()
