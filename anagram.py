h1={}
h2={}
def anagrams(str1,str2):
        if len(str1)!=len(str2):
                return False
        else:
                num=0
                for x in str1:
                        h1[num]=x
                        num+=1
                num=0
                for x in str2:
                        h2[num]=x
                        num+=1
                a=sorted(h1.values())
                b=sorted(h2.values())
                if a==b:
                        return True
                else:
                        return False
string1=input("Enter the string")
string2=input("Enter the string to find wheather it is anagram")
print(anagrams(string1,string2))
                
