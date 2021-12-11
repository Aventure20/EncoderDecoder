import base64
import time

while True:
    which = input("Do you want to Encode or Decode?\n")
    which = which.lower()

    if which == "encode":
        while True:
            what = input("What do you want to Encode? Text or File?\n")
            what = what.lower()

            if what == "text":
                data = input("Please Paste or Enter the text you want to encode\n")
                data = data.encode("ascii")
                data = base64.b64encode(data)
                data = data.decode("ascii")
                print("Encoding...")
                time.sleep(2)
                print(data)
                break
            
            elif what == "file":
                print("Encoding file...")
                break

            else:
                print("Please answer by Text or File")
                what = input("What do you want to Encode? Text or File?\n")
                continue
        break
    
    elif which == "decode":
        print("Decoding...")
        break

    else:
        print("Please answer by Encode or Decode")
        which = input("Do you want to Encode or Decode?\n")
        continue