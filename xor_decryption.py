

def decode(words, key):
    list1 = words[:]
    for i in range(len(list1)):
        list1[i] = list1[i]^key[i%3]

    #print sum(list1)
    # check if 'the' or 'of' in the text
    for i in range(len(list1)):
        list1[i] = chr(list1[i])

    list1 = ''.join(list1)
    if 'the' in list1 and 'of' in list1:
        print list1
        print key
        raw_input('pause')

fobj = open('p059_cipher.txt')
words = fobj.read().split(',')
for i in range(len(words)):
    words[i] = int(words[i])

#key = [103, 111, 100]
#decode(words, key)
#quit()

start = ord('a')
for i in range(26):
    for j in range(26):
        for k in range(26):
            key = [start+i, start+j, + start+k]
            decode(words, key)
