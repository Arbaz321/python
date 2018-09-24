numbers = [2, 4, 3, 5, 1, 6, 7, 10, 9, 8]
answer = 10

def linSearch(num):
    i = 0
    count = 0
    for i in range(len(numbers)):
        count += 1
        if numbers[i] == num:
            print("LinSearch found %i in index %i after %i steps" % (num, i, count))

def biSearch(num):
    i = 0
    low = 0
    high = len(numbers)
    center = (high + low)//2
    count = 0
    for i in range(len(numbers)):
        count += 1
        #print "i: %i, high: %i, low: %i, center: %i, numbers[center]: %i, num: %i" % (i, high, low, center, numbers[center], num)
        if numbers[center] == num:
            print ("BiSearch found %i in index %i after %i steps" % (num, center, count))
            return ""
        elif numbers[center] > num:
            high = center
            center = (high + low)//2 
        elif numbers[center] < num:
            low = center
            center = (high + low)//2
        else:
            print("No number was found")
    
def bubbleSort(num):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(num)-1):
            if(num[i] > num[i+1]):
                num[i], num[i+1] = num[i+1], num[i]
                sorted = False
    print(str(num))

def selectionSort(num):
    for i in range(len(num)-1):
        temp = num[i]
        tempIndex = i
        for j in range(i+1, len(num)):
            if num[j] < temp:
                temp = num[j]
                tempIndex = j
        num[i], num[tempIndex] = temp, num[i]
    print(str(num))

def readFromFile():
    #reads from a file and stores it in a variable, including line breaks
    lines = ""
    with open("testText.txt") as txt:
        lines = txt.read()
    print(lines)

def insertionSort(num):
    print(num)
    #start at i = 1 and loop through array
    for i in range(1, len(num)):
        j = i
        #at each increment, loop back from current i to 0 (j)
        while(j > 0):
            #if number at j-1 > j, swap the two
            if(num[j-1] > num[j]):
                num[j-1], num[j] = num[j], num[j-1]
            j -= 1
    #print array
    print(num)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(num):
    if len(num) < 2:
        return num
    else:
        half = len(num)//2
        left = mergeSort(num[:half])
        right = mergeSort(num[half:])
        return merge(left, right)

import re
def tokenize(doc):
    return re.sub(r'([^\s\w]|_)+', '', doc).lower().split(' ')
    
def documentDistance(doc1, doc2):
    doc1 = tokenize(doc1)
    doc2 = tokenize(doc2)

def main():         
    #sort array before using binary search!!!
        # print(biSearch(answer))
    # linSearch(answer)
    # bubbleSort(numbers)
    # selectionSort(numbers)
    # readFromFile()
    # insertionSort(numbers)
    # print(mergeSort(numbers))
    # documentDistance('Hello, my name is Arbaz Aziz', 'Hello, my name is Arbaz Aziz')

if __name__ == '__main__':
    main()