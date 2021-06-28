#please read the README.md file before running this code
import png
import sys

def convertRow(pixelSize, colorSize, inRow):
    outRow = []
    brightness = 0

    for b in range(0, len(inRow)):
        color = float(inRow[b])

        if(len(sys.argv) > 4):
            color = 255 - float(inRow[b])

        if(b % pixelSize == colorSize - 1):
            brightness += color

            if(int(brightness) < int(sys.argv[1]) * colorSize):
                outRow = outRow + [0]
            else:
                outRow = outRow + [255]
            
            brightness = 0
        elif(b % pixelSize < colorSize - 1):
            brightness += color
    
    return([outRow])

inTuple = png.Reader(sys.argv[2]).read()
inImage = (list(inTuple[2])).copy()
outImage = []

for a in inImage:
    if('palette' in inTuple[3].keys()):
        inRow = ()

        for b in a:
            inRow = inRow + inTuple[3]['palette'][int(b)]
        
        outImage = outImage + convertRow(3, 3, inRow)
    elif(inTuple[3]['planes'] == 3):
        outImage = outImage + convertRow(3, 3, a)
    elif(inTuple[3]['planes'] == 4):
        outImage = outImage + convertRow(4, 3, a)
    else:
        print("""I was not programmed to convert this picture. 
        Please send this picture to my programmer so he/she/they/it can update me.""")

outFile = open(sys.argv[3], 'wb')
png.Writer(inTuple[0], inTuple[1], greyscale = True, alpha = False).write(outFile, outImage)
outFile.close()