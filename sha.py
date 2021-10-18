import hashlib

while(True):
 n=int(input("----SHA Algorithm----\n1) String input\n2) File encoding\n3) Exit\nEnter your choice:"))
 if(n==1):
    str1 = input("Enter String:")
    str1=str1.encode()
    while(True):
        m=int(input("1)SHA1\n2)SHA224\n3)SHA256\n4)SHA384\n5)SHA512\n6)Exit\nPick a method:"))
        if(m==1):
            hv1=hashlib.sha1(str1)
            print("Hash value: ",hv1.hexdigest())
            print("Byte size: ",hv1.digest_size)
            print("Block size: ",hv1.block_size)
        elif(m==2):
            hv2=hashlib.sha224(str1)
            print("Hash value: ",hv2.hexdigest())
            print("Byte size: ",hv2.digest_size)
            print("Block size: ",hv2.block_size)
        elif(m==3):
            hv3=hashlib.sha256(str1)
            print("Hash value: ",hv3.hexdigest())
            print("Byte size: ",hv3.digest_size)
            print("Block size: ",hv3.block_size)
        elif(m==4):
            hv4=hashlib.sha3_384(str1)
            print("Hash value: ",hv4.hexdigest())
            print("Byte size: ",hv4.digest_size)
            print("Block size: ",hv4.block_size)
        elif(m==5):
            hv5=hashlib.sha512(str1)
            print("Hash value: ",hv5.hexdigest())
            print("Byte size: ",hv5.digest_size)
            print("Block size: ",hv5.block_size)
        elif(m==6):
            break
        else:
            print("Wrong choice")
 elif(n==2):
    with open("sample.txt","rb") as f:
        bytes = f.read()
        print("String: ",bytes.decode())
        while(True):
            m=int(input("1)SHA1\n2)SHA224\n3)SHA256\n4)SHA384\n5)SHA512\n6)Exit\nPick a method:"))
            if(m==1):
                hv1=hashlib.sha1(bytes)
                print("Hash value: ",hv1.hexdigest())
                print("Byte size: ",hv1.digest_size)
                print("Block size: ",hv1.block_size)
            elif(m==2):
                hv2=hashlib.sha224(bytes)
                print("Hash value: ",hv2.hexdigest())
                print("Byte size: ",hv2.digest_size)
                print("Block size: ",hv2.block_size)
            elif(m==3):
                hv3=hashlib.sha256(bytes)
                print("Hash value: ",hv3.hexdigest())
                print("Byte size: ",hv3.digest_size)
                print("Block size: ",hv3.block_size)
            elif(m==4):
                hv4=hashlib.sha3_384(bytes)
                print("Hash value: ",hv4.hexdigest())
                print("Byte size: ",hv4.digest_size)
                print("Block size: ",hv4.block_size)
            elif(m==5):
                hv5=hashlib.sha512(bytes)
                print("Hash value: ",hv5.hexdigest())
                print("Byte size: ",hv5.digest_size)
                print("Block size: ",hv5.block_size)
            elif(m==6):
                break
            else:
                print("Wrong choice")        
 elif(n==3):
     break
 else:
    print("Wrong choice")