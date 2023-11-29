#Written by group 9(Chakong Lor and Preston)
#Date: 11/22/2023

import pysftp
import sys

try:
    if(len(sys.argv) > 4 or len(sys.argv) < 3):
        raise Exception("There must be 3 or 4 arguments! Your arguments: " + str(len(sys.argv)))

except Exception as e:
    print(e)

def main():

    if (len(sys.argv) == 4 and sys.argv[1]=="-d"):
        hostname = input("Enter hostname of VPS: ")
        username = input("Enter username to VPS: ")
        private_key = input("Enter local path to private key: ")
        passphrase = input("Enter passphrase: ")
        cnopt = pysftp.CnOpts()
        cnopt.hostkeys = None
        print("Connecting...")
        sftp = pysftp.Connection(hostname,username=username,private_key=private_key,private_key_pass=passphrase,cnopts=cnopt)
        sftp.put_r(sys.argv[2],sys.argv[3])
        sftp.close()
        print("Done!")
    elif (len(sys.argv) == 3):
        hostname = input("Enter hostname of VPS: ")
        username = input("Enter username to VPS: ")
        private_key = input("Enter local path to private key: ")
        passphrase = input("Enter passphrase: ")
        cnopt = pysftp.CnOpts()
        cnopt.hostkeys = None
        print("Connecting...")
        sftp = pysftp.Connection(hostname,username=username,private_key=private_key,private_key_pass=passphrase,cnopts=cnopt)
        sftp.cd(sys.argv[2])
        sftp.put(sys.argv[1])
        sftp.close()
        print("Done!")
    
    try:
        if (sys.argv[1]!="-d" and len(sys.argv) == 4):
            raise Exception("Wrong arguments! Try -d")
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()