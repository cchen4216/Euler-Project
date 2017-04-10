

def calc_num(word):
    a = ord('a') - 1
    summ = 0
    for i in word:
        summ += ord(i) - a
    return summ
#print calc_num('sky')
#quit()

def get_tri_nums(n):
    list1 = []
    summ = 0
    for i in range(1,n):
        summ += i
        list1.append(summ)
    return list1
#print get_tri_nums(10)
#quit()
tri_nums = get_tri_nums(100)
fobj = open('p042_words.txt')
words = fobj.read().split(',')

count = 0
for word in words:
    word = word[1:-1].lower()
    num = calc_num(word)
    if num in tri_nums:
        count += 1

print count
