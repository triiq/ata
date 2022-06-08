import subprocess
import csv
import random
import datetime
import os

c = 0  #creates and sets the variable "c" to 0 
DefaultSize = "mode con: cols=152 lines=30"
os.system(DefaultSize)

def Header():
    print("""   d888888o.   8 8888888888   b.             8 8 888888888o. 8888888 8888888888 ,o888888o.     8 8888     ,88' 8 8888888888   b.             8
 .`8888:' `88. 8 8888         888o.          8 8 8888    `^888.    8 8888    . 8888     `88.   8 8888    ,88'  8 8888         888o.          8
 8.`8888.   Y8 8 8888         Y88888o.       8 8 8888        `88.  8 8888   ,8 8888       `8b  8 8888   ,88'   8 8888         Y88888o.       8
 `8.`8888.     8 8888         .`Y888888o.    8 8 8888         `88  8 8888   88 8888        `8b 8 8888  ,88'    8 8888         .`Y888888o.    8
  `8.`8888.    8 888888888888 8o. `Y888888o. 8 8 8888          88  8 8888   88 8888         88 8 8888 ,88'     8 888888888888 8o. `Y888888o. 8
   `8.`8888.   8 8888         8`Y8o. `Y88888o8 8 8888          88  8 8888   88 8888         88 8 8888 88'      8 8888         8`Y8o. `Y88888o8
    `8.`8888.  8 8888         8   `Y8o. `Y8888 8 8888         ,88  8 8888   88 8888        ,8P 8 888888<       8 8888         8   `Y8o. `Y8888
8b   `8.`8888. 8 8888         8      `Y8o. `Y8 8 8888        ,88'  8 8888   `8 8888       ,8P  8 8888 `Y8.     8 8888         8      `Y8o. `Y8
`8b.  ;8.`8888 8 8888         8         `Y8o.` 8 8888    ,o88P'    8 8888    ` 8888     ,88'   8 8888   `Y8.   8 8888         8         `Y8o.`
 `Y8888P ,88P' 8 888888888888 8            `Yo 8 888888888P'       8 8888       `8888888P'     8 8888     `Y8. 8 888888888888 8            `Yo
                                                                                                                                                      
""")

def Clrscrn():
     # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def Choice():
    Clrscrn()
    Header()
    print("What are we going to do? \nTo send any amount of one token to one address: 1 \nFor any amount of one token to many addresses press: 2\nTo send one each of many tokens to one address:  3\nFor one each of many tokens randomly distributed to many addresses: 4")
    branch = input("Please enter 1, 2, 3 or 4:  ")
    if branch == "1":
        One()
    elif branch == "2":
        Many()
    elif branch == "3":
        MtoOne()
    elif branch == "4":
        MtoMany()
    else:
        Choice()

def One():
    Clrscrn()
    Header()
    token = input("what is the address of the token you want to send?  ")
    amount = input("how many tokens you want to send to the recipient?  ")
    recipient = input("What is the address you want to send " + amount + " tokens to?  ")
    Send(token, amount, recipient)
    output(token, recipient)
    Clrscrn()
    Header()
    print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")  #a final message for the user
    input("Press Enter(Return) to close")  #holds the program open so the user may see the results and final message
                                
def Send(token, amount, recipient):
    subprocess.Popen(['spl-token','transfer','--fund-recipient','--allow-unfunded-recipient',token,amount,recipient])

def Many():
    Clrscrn()
    Header()
    token = input("what is the address of the token you want to send?  ")
    amount = input("how many tokens you want to send to each recipient?  ")
    spot = input("Please enter the exact filepath to the TXT file containing the addresses you wish to send to \n")
    with open(spot, "r+") as file_r:
        file_reader = file_r.readlines()
    for row in file_reader:
        recipient = row[0]
        Send(token, amount, recipient)
        output(token, recipient)
    Clrscrn()
    Header()
    print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")  #a final message for the user
    input("Press Enter(Return) to close")  #holds the program open so the user may see the results and final message

def MtoOne():
    Clrscrn()
    Header()
    amount = str("1")
    tokenFile = input("Please enter the exact filepath to the TXT file containing the tokens you wish to send\n")
    with open(tokenFile, "r+") as t:  #open the file containing token addresses as read/write and store it as variable "t" 
        lines = t.readlines()  #read the lines from the token file and store the addresses as <a list?> in variable "lines" 
        token = []  #create an empty list called "token" 
        for i in lines:  #for each item "i" in <list?> "lines" do the following 
            i = i.strip()  #strip whitespace and escape characters from item "i" 
            token.append(i)  #append item "i" to list "token" 
            tokenCount = len(token)  #save the number of items in list "token" to variable "tokenCount"
    recipient = input("What is the address you want to send  tokens to?  ")
    c = 0  #creates and sets the variable "c" to 0 
    while c <= count: #the conditions for the loop are: as long as "c" is less than or equal to the shortest list of "token" or "address" as counted in lines 12 &2 0 it will do the following 
        Send(token[c], amount, recipient)  #Calling the function defined at line 30 
        print(str(c) + " of " + str(count))  #displaying which iteration of the loop we are on 
        output(recipient, token[c])
        c += 1
    Clrscrn()
    Header()
    print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")  #a final message for the user
    input("Press Enter(Return) to close")  #holds the program open so the user may see the results and final message

def MtoMany():
    Clrscrn()
    Header()
    amount = str("1")
    tokenFile = input("Please enter the exact filepath to the TXT file containing the tokens you wish to send\n")
    with open(tokenFile, "r+") as t:  #open the file containing token addresses as read/write and store it as variable "t" 
        lines = t.readlines()  #read the lines from the token file and store the addresses as <a list?> in variable "lines" 
        token = []  #create an empty list called "token" 
        for i in lines:  #for each item "i" in <list?> "lines" do the following 
            i = i.strip()  #strip whitespace and escape characters from item "i" 
            token.append(i)  #append item "i" to list "token" 
            tokenCount = len(token)  #save the number of items in list "token" to variable "tokenCount" 

    addressFile = input("Please enter the exact filepath to the TXT file containing the addresses you wish to send to \n")
    with open(addressFile, 'r+') as f: #open the file containing receiving addresses as read/write and store it as variable "f" 
        lines = f.readlines()  #read the lines from the addresses file and store the addresses as <a list?> in variable "lines" 
        recipient = []  #create an empty list called "address" 
        for i in lines:  #for each item "i" in <list?> "lines" do the following 
            i = i.strip()  #strip whitespace and escape characters from item "i" 
            recipient.append(i)  #append item "i" to list "address" 
            addressCount = len(recipient)  #save the number of items in list "address" to variable "addressCount" 

    random.shuffle(token)  #rearrange the items of list "token"
    random.shuffle(recipient)  #rearrange the items of list "address"

    if addressCount > tokenCount:  #check if the vairable "addressCount" is larger than "tokenCount" and makes sure every token gets matched to an address with addresses left over 
        count = tokenCount - 1  #counting for loops starts at 0 not 1, this fixes an error 
    else:  #if "addressCount" is smaller than "tokenCount" each address will get a token with tokens left over 
        count = addressCount - 1  #counting for loops starts at 0 not 1, this fixes an error                                                                                                                                                     
    c = 0  #creates and sets the variable "c" to 0 
    while c <= count: #the conditions for the loop are: as long as "c" is less than or equal to the shortest list of "token" or "address" as counted in lines 12 &2 0 it will do the following 
        Send(token[c], amount, recipient[c])  #Calling the function defined at line 30 
        print(str(c) + " of " + str(count))  #displaying which iteration of the loop we are on 
        output(recipient[c], token[c])
        c += 1
    Clrscrn()
    Header()
    print("Airdrop finished.  \nPlease see the results of which token went to which address in:  \n dropResult.csv")  #a final message for the user
    input("Press Enter(Return) to close")  #holds the program open so the user may see the results and final message

def output(recipient, token):
    with open('dropResult.csv', 'w') as w:  #creates/opens the file "dropResult.csv" in write mode and stores it in variable "w" 
        w.truncate()  #empties the "dropResult" file 
        w.close()  #closes the "dropResult" file
    now = datetime.datetime.now()  #getting the date and time 
    now = now.strftime("%Y-%m-%d %H:%M:%S")  #formatting the date and time 
    line = recipient + "," + token + ',' + now  #storing which address received which token at the time it was sent

    with open('dropResult.csv', 'a', newline='\n') as w:  #opens the file "dropResult.csv" in append mode and stores it in variable "w" 
        w.write(line + '\n')  #writes the information defined in variable "line" (44) to the file 

Choice()