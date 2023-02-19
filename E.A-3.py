########## Problem-1
def SNL(x): #SLN=Sum of Number in List
  t = 0
  for i in x:
    t = t + i
  return t
inputlist = [8,2,3,0,7]
print ("The sum of my_list is", SNL(inputlist))

########## Problem-2
def b(s):  
    t = ''
    for i in s:  
        t = i + t  
    return t      
s = input()   
print("The reverse string is -->", b(s))

########## Problem-3
def sentence(s):
    d={"UpperCase":0, "LowerCase":0}
    for c in s:
        if c.isupper():
           d["UpperCase"]+=1
        elif c.islower():
           d["LowerCase"]+=1
        else:
           pass
    print ("No. of Upper case characters : ", d["UpperCase"])
    print ("No. of Lower case Characters : ", d["LowerCase"])

sentence('The quick Brown Fox')