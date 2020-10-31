#taking input from the user
s1 =input("Enter your first sentence: ")
words1 = s1.split()
s2 =input("Enter your second sentence: ")
words2 = s2.split()
count = 0
#checking common words
for i in words1:
    for j in words2:
        if(i==j):
            count = count+1
print("a. "+str(count))
b = [] #store
#Words in S1 but not in S2
for i in words1:
    flag  = 0
    for j in words2:
        if(i==j):
            flag = 1
    if(flag == 0):
         b.append(i)
print("b. ",b)

b = []
#Words in S2 but not in S1
for i in words2:
    flag  = 0
    for j in words1:
        if(i==j):
            flag = 1
    if(flag == 0):
        b.append(i)
print("c. ",b)
