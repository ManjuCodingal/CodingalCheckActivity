# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

def wordMatch(words):
    count=0
    lst=[]

    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            count+=1
            lst.append(i)
    print("Words with matching 1st and last character are", lst)
    return count
main_list=['abs', 'def','etcre','aba','etc']
counter=wordMatch(main_list)

print("Total words with lenght more than 2 with matching fisrt and last letters are : ",counter)
