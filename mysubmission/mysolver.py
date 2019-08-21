import requests
import sys

def solver():
    print("Here is the answer! Hope you had fun!")
    #put solver here

#create solver after this works
r = requests.post('https://api.noopschallenge.com/pathbot/start').json()
#print(r)
print(r['status'])
print(r['message'])
print(r['exits'])
print(r['description'])
print(r['mazeExitDirection'])
print(r['mazeExitDistance'])
print(r['locationPath'])

# make a way for a user to post and keep going foward, maybe add a solver
# if they give up

while r['status'] != 'finished':
    answer = input("Where would you like to go? Type quit to see the answer and leave the program.")
    if "q" in answer.lower():
        solver()
        sys.exit()
    #get post here to work
    r = requests.post('https://api.noopschallenge.com/pathbot/'+r['locationPath']+answer).json()
    print(r)
    print(r['status'])
    print(r['message'])
    print(r['exits'])
    print(r['description'])
    print(r['mazeExitDirection'])
    print(r['mazeExitDistance'])
    print(r['locationPath'])
    quit = input("")
