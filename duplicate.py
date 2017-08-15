# remove duplicates numbers in a file
import os.path

def removeDuplicate(filename1, filename2):
    fileRead = open(filename1, "r")
    fileWrite = open(filename2, "w")
    originalList = []
    count = 0

    for line in fileRead:
        if line.rstrip('\n') in originalList:
            count = count + 1
            continue
        else:
            originalList.append(line.rstrip('\n'))

    print("Removed {} duplicates.".format(count))

    for line in originalList:
        fileWrite.write(line)
        fileWrite.write('\n')

    fileRead.close()
    fileWrite.close()

filename1 = input("Select phone number file to open:")
filename2 = input("Create a new file to write:")

if os.path.isfile(filename2):
    input1 = input("File {} already exists, do you want to override?".format(filename2)).lower()

    if input1 in 'yes y':
        removeDuplicate(filename1, filename2)
    else:
        print("Exiting...")
else:
    removeDuplicate(filename1, filename2)

print("End of program.")
