
# import requests,json
# data=requests.get('http://saral.navgurukul.org/api/courses').json()
# with open("coures.json","w")as f:
#     json.dump(data,f,indent=4)

# with open("coures.json","r")as f: 
#     r=json.load(f)
#     # print(r)

#     for i in r['availableCourses']:
#         print(i['id'],' ',i['name'])

#     num=int(input("enter number: "))
#     data1=requests.get('http://saral.navgurukul.org/api/courses/'+str(num)+'/exercises').json()
#     print(data1)
#     with open("soures1.json","w")as f1:
#         json.dump(data1,f1,indent=4)
#     x=0
#     lst=[]
#     for i in data1['data']:
#         print(x,i['slug'])
#         lst.append(i['slug'])
#         x+=1 
#     slug1=int(input("enter your choice slug number: "))
#     data2=requests.get('http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug='+str(lst[slug1])).json()
#     with open("soures2.json","w")as f2:
#         json.dump(data2,f2,indent=4)
# print("code complate: " )


str1=input("enter your farst values: ")
str2=input("enter your secound values: ")
str1=str1.lower()
str2=str2.lower()
if len(str1)==len(str2):
    print("str1 and str2 len are right: ")
    s_str1 = sorted(str1)
    s_str2 = sorted(str2)
    if(s_str1 == s_str2):
        print("this is anagram  ")
    else:
        print(str1+" and "+ str2+ " are not anagram.")
else:
    print(str1 + " and " + str2 + " len of not right")

ran=int(input("enter your range: : "))
lst=[]
for i in range(ran):
    val=input("enter your values: ")
    lst.append(val)
print(lst)

# str1=input("enter your farst values: ")
# str2=input("enter your secound values: ")
# c=0
# if len(str1)!=len(str2):
#     print("not anagram: ")
# else:
#     for i in str1:
#         if i in str2:
#             c+=1
# if c==len(str1):
#     print("this are anagram: ")
# else:
#     print("not anagram: ")





