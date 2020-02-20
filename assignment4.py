import requests
import json
repoDict={}
def getInfoApi(name):
    r=requests.get('https://api.github.com/users/'+name+'/repos')
    print(r.status_code)
    print("The user has "+str(len(r.json())) + " repos, names and commits as the following: ")
    for i in r.json(): # i refers to items
        s=requests.get('https://api.github.com/repos/'+name+'/'+i['name']+'/commits')
        commitsList=s.json()
        commitsDict=commitsList[0]
        print("Name: " +i['name']+"; Commits: "+str(len(commitsDict)))
    return "Right"