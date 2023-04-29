"""
Question 2 - 

Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

                                  

Input : string1 = "India"

Output : uniqueLetters = i,n,d,a


Input : string1 = "Dedication"

Output : uniqueLetters = d,e,i,c,a,t,o,n

"""

string1=input("string1 : ")
string1=string1.lower()
l=[]

for word in string1:
    if word not in l:
        l.append(word)
print("uniqueLetters = ",end='')
print(*l,sep=",")


'''
        OUTPUT - 1
string1 : Dedication
uniqueLetters = d,e,i,c,a,t,o,n

        OUTPUT - 2
string1 : India
uniqueLetters = i,n,d,a

        OUTPUT - 3
string1 : few people cried few people smiled most of the people were silent
uniqueLetters = f,e,w, ,p,o,l,c,r,i,d,s,m,t,h,n

'''