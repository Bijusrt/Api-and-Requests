
import requests,json
def Calling_an_api():
    m={}
    with open('courses.json','r') as b:
        s=json.load(b)
        s=json.loads(s)
        c=1
        for i in s:
            for j in s[i]:
                for k in j:
                    if k=='name':
                        print(c," ",j[k])
                        m[c]=j['id']
                        c+=1
    e=int(input('enter the no: '))
    data={}
    lo="Loading...."
    print("\t\t",lo,end="\r")
    for l in m:
        request=requests.get("http://saral.navgurukul.org/api/courses/"+str(m[l])+"/exercises")
        p=request.text
        p=json.loads(p)
        for i in p:
            if p[i]==[]:
                data[l]=["Nothing is available in this page"]
            a=[]
            for j in p[i]:
                for k in j:
                    if k=="name":
                        a.append(j["name"])
                data[l]=a
    return data,e
data,e=Calling_an_api()
while 1:
    for x,i in enumerate(data[e]):
        print("\t\t",x+1,".",i)
    ask=input("\n------FOR NEXT PAGE PRESS N----FOR PREVIOUS PAGE PRESS P-----FOR ALL PRESS A------ :").lower()
    print("\n")
    if ask=="n":
        e+=1
        if e==57:
            e=1
    elif ask=="p":
        e-=1
        if e==0:
            e=56
    elif ask=="a":
        data,e=Calling_an_api()
    else:
        print('INVALID REQUEST')
        break

