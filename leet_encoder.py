import sys
import string

f = open('dictionary.txt')
l = f.readlines()
f.close()

if len(sys.argv) == 1:
    print('Error:No input text')
    sys.exit()
text = sys.argv[1]

for i in text:
    chr = i.upper()
    leet = l[ord(chr) - 65]
    leet = leet.replace('\n','')
    print(leet, end='')

print()
