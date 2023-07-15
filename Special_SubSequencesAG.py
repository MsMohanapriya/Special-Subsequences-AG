def SpecialSubSequencesAG(string):
    result=0
    a_count=0
    
    for i in range(len(string)):
        if string[i]=='A' or string[i]=='a':
            a_count+=1
        elif string[i]=='G' or string[i]=='g':
            result+=a_count
    return result

string=input("Enter the string: ")
print(SpecialSubSequencesAG(string))