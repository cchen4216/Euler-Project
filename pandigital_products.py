# two different implementing method: iterative and recurssive methods 

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1 = 0
len_num1 = 0
num2 = 0
prodset = set([])

testcount = 0

def check_prod(list0):
    global num1, num2, testcount, prodset
    prod = num1 * num2
    temp = prod
    list1 = []
    while temp != 0:
        list1.append(temp%10)
        temp = temp/10

    if sorted(list1)==sorted(list0):
        prodset.add(prod)
        print num1, num2


def get_num2(list0):
    global num2

    for i in list0:
        num2 = i
        list1 = list0[:]; list1.remove(i)
        check_prod(list1)
        for i in list1:
            num2 = num2*10 + i
            list2 = list1[:]; list2.remove(i)
            check_prod(list2)
            for i in list2:
                num2 = num2*10 + i
                list3 = list2[:]; list3.remove(i)
                check_prod(list3)
                for i in list3:
                    num2 = num2*10 + i
                    list4 = list3[:]; list4.remove(i)
                    check_prod(list4)
                    num2 /= 10
                num2 /= 10
            num2 /= 10
        num2 /= 10


def get_num1(list0):
    #num1 could own 1 to 4 digits
    global num1

    for i in list0:
        num1 = i
        list1 = list0[:]; list1.remove(i)
        get_num2(list1)
        for i in list1:
            num1 = num1*10 + i
            list2 = list1[:]; list2.remove(i)
            get_num2(list2)
            for i in list2:
                num1 = num1*10 + i
                list3 = list2[:]; list3.remove(i)
                get_num2(list3)
                for i in list3:
                    num1 = num1*10 + i
                    list4 = list3[:]; list4.remove(i)
                    get_num2(list4)
                    num1 /= 10
                num1 /= 10
            num1 /= 10
        num1 /= 10

def get_num11(list0):
    global num1, digits, len_num1
    if len(list0) < 5:
        return
    for i in list0:
        num1 = i if len(list0)==len(digits) else num1*10 + i
        list1 = list0[:]; list1.remove(i)
        len_num1 = len(digits) - len(list1)
        get_num22(list1)    # take num2 and check product
        get_num11(list1)   # take one more digit
        num1 /= 10         # reset current digit for next cycle

def get_num22(list0):
    global num2, len_num1, digits
    if len(list0) < 2:
        return
    for i in list0:
        num2 = i if len(list0)==len(digits)-len_num1 else num2*10 + i
        list1 = list0[:]; list1.remove(i)
        check_prod(list1)      # check the product with current digits
        get_num22(list1)       # get one more digit
        num2 /= 10             # reset current digit for next cycle


get_num11(digits)
print prodset
print sum(prodset)
