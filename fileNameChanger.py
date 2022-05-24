# Copy absolute path of the required directory
# Choose the media type of the file
# Choose the new file name ( it will be concatenated with 'fileType' and 'number' )

import os

# Program variables
path = input("Give me the absolute path of the directory: ")
fileType = input("What type of file is this? (image / video): ").lower()
newFileName = input("What is the new name that you want to rename to (name + fileType + number): ").title()
number = 1

imageExtension = [
    ".jpg",
    ".jpeg",
    ".png",
]

videoExtension = [
    ".mov",
    ".mp4",
]

# Loops through the directory given by the user, checks the extension of the current file and matches with the user input 'fileType'
for file in os.listdir(os.path.abspath(path)):
    if fileType == "image":    
        if file.endswith(imageExtension[0]) or file.endswith(imageExtension[0].upper()):
            file_name = os.path.splitext(file)[0]
            os.rename(os.path.join(path, file), os.path.join(path, newFileName + fileType.title() + str(number) + imageExtension[0]))
            number += 1
        
        elif file.endswith(imageExtension[1]) or file.endswith(imageExtension[1].upper()):
            file_name = os.path.splitext(file)[0]
            os.rename(os.path.join(path, file), os.path.join(path, newFileName + fileType.title() + str(number) + imageExtension[1]))
            number += 1
        
        elif file.endswith(imageExtension[2] or file.endswith(imageExtension[1].upper())):
            file_name = os.path.splitext(file)[0]
            os.rename(os.path.join(path, file), os.path.join(path, newFileName + fileType.title() + str(number) + imageExtension[2]))
            number += 1

    elif fileType == "video":    
        if file.endswith(videoExtension[0]) or file.endswith(videoExtension[0].upper()):
            file_name = os.path.splitext(file)[0]
            os.rename(os.path.join(path, file), os.path.join(path, newFileName + fileType.title() + str(number) + videoExtension[0]))
            number += 1
        
        elif file.endswith(videoExtension[1]) or file.endswith(videoExtension[1].upper()):
            file_name = os.path.splitext(file)[0]
            os.rename(os.path.join(path, file), os.path.join(path, newFileName + fileType.title() + str(number) + videoExtension[1]))
            number += 1

