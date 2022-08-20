import requests,json
r=requests.get("http://saral.navgurukul.org/api/courses")
a=r.json() 
with open("COURSES.json","w") as f1:
    new=json.dump(a,f1,indent=4)
store=(a["availableCourses"])
name=[]
id=[]
for i in range (len(store)):
    name.append(store[i]["name"])
    id.append(store[i]["id"])
    print(i,store[i]["name"],end="-")
    print(store[i],["id"])
print("  ")
for i in a:
    j=1
    for k in a[i]:
        print(j,"=",k["name"],k["id"])
        j+=1
user=int(input("enter the chapter you want to read:-"))-1
user1=name[user]
user2=id[user]
print(user2,":",user1)

req=requests.get("http://saral.navgurukul.org/api/courses/74/exercises" )
x=req.json()
with open("Content.json","w") as f2:
    new1=json.dump(x,f2,indent=4)
req1=requests.get("http://saral.navgurukul.org/api/courses/"+user2+"/exercises")
content=req1.json()
with open("Content1.json","w") as f3:
    new2=json.dump(content,f3,indent=4) 
slug=[]
i=0
while i<len(content['data']):
    print(i+1,content["data"][i]["name"])  
    print()
    if content["data"][i]["childExercises"]==[]:
        print("")
        store=content["data"][i]["slug"]
        slug.append(store)
    else:
        j=0
        while j<len(content["data"][i]["childExercises"]):
            print("",j+1,content["data"][i]["childExercises"][j]["name"])
            j+=1
    i+=1
k=0
while k<len(slug):
    print(k,slug[k])
    k=k+1
var1=int(input("show the content of slug:"))-1
var2=requests.get("https://saral.navgurukul.org/api/courses/"+user2+"/exercise/getBySlug?slug="+(slug[var1]))
z=var2.json()
with open("Content2.json","w") as f4:
    new3=json.dump(z,f4,indent=4)
    x=var1
    x+=1
    d=requests.get("https://saral.navgurukul.org/api/courses/"+user2+"/exercise/getBySlug?slug="+(slug[x]))
    r=d.json()
    print(r["content"],"\n")