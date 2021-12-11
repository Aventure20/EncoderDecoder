import base64

while True:
    which = input("Do you want to Encode or Decode?\n")
    which = which.lower()

    if which == "encode":
        while True:
            what = input("What do you want to Encode? Text or File?\n")
            what = what.lower()

            if what == "text":
                print("Encoding text...")
                break
            
            elif what == "file":
                print("Encoding file...")
                break

            else:
                print("Please answer by Text or File")
                what = input("What do you want to Encode? Text or File?\n")
                continue
        
        print("Encoding...")
        break
    
    elif which == "decode":
        print("Decoding...")
        break

    else:
        print("Please answer by Encode or Decode")
        which = input("Do you want to Encode or Decode?\n")
        continue