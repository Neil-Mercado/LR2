
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

def median(num):
    num.sort()
    n=len(num)
    med=int(n/2);
    if(n%2==1):
        return num[med]
    else:
        return (0)

def mean(num):
    n=len(num)
    if (n%2==1):
        mn=0
        for i in num:
            mn=mn+i;
        return mn/n
    else:
        return(0)

def mode(num):
    n=len(num)
    if(n>=1):
        mod = max(set(num), key = num.count)
        return (mod)
    else:
        return (0)

num = []
for line in f:
    numbers = line.split()
    for list in numbers:
        num.append(float(list))
print("List:")
print(num)
print()
print("Median: ", median(num))
print("Mean: ", mean(num))
print("Mode: ", mode(num))

