newfile = open('sample.txt', 'w')
newfile.write('Writing some stuff in my text file\n')
newfile.write('I like bacon\n and cheese')
newfile.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)

fr.close()

