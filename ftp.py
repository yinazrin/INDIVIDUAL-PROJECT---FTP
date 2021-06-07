from ftplib import FTP
import os
import getpass

ftp = FTP('192.168.56.112')

authUser = input ("Username: ")
password = getpass.getpass()
authPass = password
ftp.login(user = authUser, passwd = authPass)

os.getcwd()

def ftpGet():
    filename = input ("File to download: ")
    try:
        localfile = open(filename, 'wb')                            
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)   
        print (filename + " is retrieved successfully.")
        localfile.close()
    except:
        print ("File does not exist on the server. Retrieval unsuccessful.")
        os.remove(filename)
    

def ftpPut():
    filename = input ("File to upload: ")
    try:
        localfile = open(filename, 'rb')                           
        ftp.storbinary('STOR ' + filename, localfile)              
        print (filename + " is uploaded successfully.")
        localfile.close()
    except:
        print ("File does not exist on the current directory. Upload unsuccessful.")
    
def ftpDel():
    filename = input ("File to delete: ")                          
    try:
        ftp.size(filename)                                         
    except:
        print ("File does not exist on the server.")
    else:
        delConfirm = input ("Are you sure [Y/N]: ")                
        if delConfirm == 'Y' or delConfirm == 'y':
            ftp.delete(filename)
            print (filename + " is deleted successfully.")
        else:
            print (filename + " is not deleted.")
        

def ftpList():
    print ("\nDIRECTORY: home/" + authUser + ftp.pwd() + "\n------------------------------------------------------------")
    print ('Permission                            Size Date   Time  Name')
    ftp.dir()

def ftpDirMove():
    pathname = input ("Move to directory: ")                        
    try:
        ftp.cwd(pathname)                                           
    except:
        print ("Directory does not exist.")
    else:
        ftpList()

def ftpDirReturn():
    ftp.cwd("../")                                                  
    ftpList()
    
def ftpDirHome():
    ftp.cwd("/")                                                    
    ftpList()
    
def ftpDirDel():
    dirname = input ("Delete a folder: ")
    try:
        ftp.cwd(dirname)                                            
    except:
        print ("Directory does not exist on the server.")
    else:
        delConfirm = input ("Are you sure [Y/N]: ")                 
        if delConfirm == 'Y' or delConfirm == 'y':
            try:
                ftp.cwd('../') 
                ftp.rmd(dirname)
                print (dirname + " is deleted successfully.")
            except:
                print("Directory is not empty.")
        else:
            print (dirname + " is not deleted.")



print ("\nHello, " + authUser)                                    
ftpList()                                                           
menu = ''
while menu != 'X' or menu != 'x':
    print ("""
 MENU 
 [1] List all files        [Q] Move to a different directory
 [2] Download a file       [E] Return to home directory
 [3] Upload a file         [X] Exit
 [4] Delete a file         
    """)
    menu = input ("-> ")
    if menu == '1':
        ftpList()
    elif menu == '2':
        ftpGet()
    elif menu == '3':
        ftpPut()
    elif menu == '4':
        ftpDel()
 
    elif menu == 'Q' or menu == 'q':
        ftpDirMove()
 
    elif menu == 'E' or menu == 'e':
        ftpDirHome()
    
   
    elif menu == 'X' or menu == 'x':
        print ("Goodbye!\n")
        break
    else:
        print ("***PLEASE INPUT A VALID KEY***")
    
ftp.quit()
