import pysftp
import sys

try:
    if(len(sys.argv) > 3 or len(sys.argv) < 3):
        raise Exception("There must be 3 arguments! Your arguments: " + str(len(sys.argv)))

except Exception as e:
    print(e)

def main():
    hostname = input("Enter hostname of VPS: ")
    username = input("Enter username to VPS: ")
    private_key = input("Enter local path to private key: ")
    passphrase = input("Enter passphrase: ")
    #pw = input("password: ")
    cnopt = pysftp.CnOpts()
    cnopt.hostkeys = None
    print("Connecting...")
    sftp = pysftp.Connection(hostname,username=username,private_key=private_key,private_key_pass=passphrase,cnopts=cnopt)
    sftp.put_r(sys.argv[1],sys.argv[2])
    print("Done!")


if __name__ == "__main__":
    main()