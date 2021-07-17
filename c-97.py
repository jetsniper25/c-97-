name="shubham"
print(name)
a = 22
print(a)
friend=[1,2,3,4]
print(friend[0])

for f in friend:
    print(f)

count=3
while (count>0):
    count-=1
    pm=int(input("Enter the pocket money you get every month"))
    if (pm>500):
        print("wow!")

    elif(pm>100):
        print("Good")

    else:
        print("It's Ok")    

intro=input("Introduce yourself")
charCount=0
wordCount=1
for i in intro:
    charCount=charCount+1
    
    if(i==" "):
        wordCount=wordCount+1

print(charCount, wordCount)