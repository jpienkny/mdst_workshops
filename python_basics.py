"""
MDST Workshop 1 - Python Basics Starter Code
"""
import random
import base64
# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    # When testing, replace x with num
    
    #x = input("Enter a number.")
    #x = int(x)
    x = num
    if x%2 == 1:
        print("Odd!")
    else:
        print("Even!")
        
        


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    test = 0
    rand_no = random.randint(1,9)
    while(test == 0):
        user = input("Pick an integer from 1 to 9: ")
        if user == "exit":
            test = 1
            break
        user = int(user)
        if user == rand_no:
            print("Goteem")
        elif user > rand_no:
            print("You are too high")
        elif user < rand_no:
            print("You are too low")



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    check = 0
    length = len(string)
    mod = length % 2
    if mod == 1:
        cnt = int((length-1)/2)
        for i in range(0,cnt):
            if string[i] != string[-(i+1)]:
                check = 1
    if mod == 0:
        cnt = int(length/2)
        for i in range(0,cnt-1):
            if string[i] != string[-(i+1)]:
                check = 1
    if check == 1:
        print("Not a palindrome")
    elif check == 0:
        print("We have a palindrome")
        
            
                
            
        
    
    


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    f = open(filename, "w")
    use_encrypt = str(base64.b64encode(username.encode("utf-8")))
    #print(use_encrypt)
    pass_encrypt = str(base64.b64encode(password.encode("utf-8")))
    #print(pass_encrypt)
    f.write(use_encrypt+"\n")
    f.write(pass_encrypt)
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    use_ec = f.readline()
    pass_ec = f.readline()
    use_ec1 = use_ec[1:]
    pass_ec1 = pass_ec[1:]
    passByte = base64.b64decode(pass_ec1)
    passStr = str(passByte, "utf-8")
    useByte = base64.b64decode(use_ec1)
    useStr = str(useByte, "utf-8")
    print("Username: " + useStr + "\n" + "Password: " + passStr)
    if password != None:
        #print(password)
        part4a(filename, useStr, password)
    
        
    
        
        
            

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
