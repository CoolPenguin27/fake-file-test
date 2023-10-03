import os
import sys

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print("Missing file paramater!")
        exit(1)

    if not os.path.isfile(filename):
        print(f"Provided file does not exist!")
        exit(1)

    fakeName = f"fake.{filename}"

    print("Grabbing File Length, might take a while.")
    with open(filename, "r", encoding="iso-8859-15") as file:
        # encoding is specified to avoid encoding errors https://stackoverflow.com/questions/16528468
        realSize = 0
        for line in file:
            realSize += len(line)
        file.close()

    print("Creating filler string...")
    fakeString = "".ljust(realSize, "0")
    
    print(f"Saving file '{fakeName}'... (might lag your device.)")
    
    with open(f"fake.{filename}", "w") as file:
        file.write(fakeString)
        file.close()

    print("DONE!")


