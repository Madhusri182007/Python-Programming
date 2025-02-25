a=input("Enter a string:")
c=0
for i in range (0,len(a)):
    if(a[i]=='a' or  a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        c+=1
        print("vowel is found at the positions:",i,"and the vowel is:",a[i])
    elif(a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
        c+=1
        print("vowel is found at the positions:",i,"and the vowel is:",a[i])
print("Total number of vowels founded in the given string are:",c)                
