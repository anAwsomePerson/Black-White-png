import png
import sys
inTuple = png.Reader(sys.argv[2]).read()
outImage = []

for a in inTuple[2]:
    outRow = []
    brightness = 0
    #print(type(b))
    for b in range(0, len(a)):
        if(b % 4 == 2):
            brightness += float(a[b])

            if(int(brightness) < int(sys.argv[1]) * 3):
                outRow = outRow + [0]
            else:
                outRow = outRow + [255]
            
            brightness = 0
        elif(b % 4 == 3):
            outRow += [a[b]]
        else:
            brightness += float(a[b])
        
    outImage = outImage + [outRow]

outFile = open(sys.argv[3], 'wb')
png.Writer(inTuple[0], inTuple[1], greyscale = True, alpha = True).write(outFile, outImage)
outFile.close()