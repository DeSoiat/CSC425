from PIL import Image
import numpy as np
import sys
import os
import csv

def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    labels = []
    names = []
    keywords = {"angry" : "0","disgus": "1","fear" : "2","happy" : "3","sad" : "4","surprise" : "5"}
    for root, dirs, files in os.walk(myDir, topdown=True):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
            for keyword in keywords:
                if keyword in name:
                    labels.append(keywords[keyword])
                else:
                    continue
            names.append(name)
    return fileList, labels, names

# load the original image
myFileList, labels, names  = createFileList(r'C:\Users\DeSoiat\Desktop\face\All')

i = 0
for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()
# get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
# Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()
# Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((width, height))
    value = value.flatten()
    value = np.append(value,labels[i])
    i +=1
    print(i)
    print(value)
    with open("dataset.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)