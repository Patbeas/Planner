import json
import datetime
import os 
from os import walk
import playsound
os.chdir('C:/Users/Patrick Beasley/Desktop/Python_Projects/Planner/Planner MK2')

daysofweekDict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
hourdict= {'1am':1, '2am':2, '3am':3, '4am':4, '5am':5, '6am':6, '7am':7, '8am':8, '9am':9, '10am':10, '11am':11, '12noon':12, '1pm':13, '2pm':14, '3pm':15, '4pm':16, '5pm':17, '6pm':18, '7pm':19, '8pm':20, '9pm':21, '10pm':22, '11pm':23, '12midnight':24}
convertdict = {1:'1 am ', 2:'2 am ', 3:'3 am ', 4:'4 am ', 5:'5 am ', 6:'6 am ', 7:'7 am ', 8:'8 am ' , 9:'9 am ', 10:'10 am ', 11:'11 am ', 12:'12 noon ', 13:'1 pm ', 14:'2 pm ', 15:'3 pm ', 16:'4 pm ', 17:'5 pm ', 18:'6 pm ', 19:'7 pm ', 20:'8 pm ', 21:'9 pm ', 22:'10 pm ', 23:'11 pm ', 24:'12 pm '}
blankTodoList = {"monday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "tuesday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "wednesday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "thursday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "friday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "saturday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""},
                "sunday": {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": ""}}
spmedict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'elevem', '12':'twelve'}

def listToString(s):  
    # initialize an empty string
    str1 = " " 
    # return string  
    return (str1.join(s))

def speak(text):
    #Get file names from phrases folder 
    f = []
    for (dirpath, dirnames, filenames) in walk('C:/Users/Patrick Beasley/Desktop/Python_Projects/Text To Speech/voice/phrases'):
        f.extend(filenames)
        break

    #Get list of phrases
    phrases = []
    for phrase in f:
        phrase = str(phrase).replace('.mp3', '')
        phrases.append(phrase)
        
    textli = str(text).split(' ')
    z = []
    p = []
    for n in textli:
        p.append(n)
        c = listToString(p)
        z.append(c)
    #Identify pre-recorded phrases in text
    phraseInTesxt = [x for x in phrases if x in text]
    print(phraseInTesxt)
    h = []
    #reorder phrases in list correctly
    
    for x in textli: 
        
        for g in phraseInTesxt:
            if x in g:
                if g not in h:
                    h.append(g)
        
    t = text
    for q in phraseInTesxt:
        t = str(t).replace(q , 'i')
        print(text)
    t = t.split(' ')
    m = 0
    w = 0
    for j in t:
        
        if j == 'i':
            t[w] = h[m]
            m += 1
        elif j in spmedict:
            t[w] = spmedict[j]
        w += 1
    for d in t:

        playsound.playsound('./voice/' + d +'.mp3')

def getdate():
    getdatetime = datetime.datetime.today()
    date = getdatetime.strftime("%m/%d/%Y")
    dow = daysofweekDict[getdatetime.weekday()]
    return date, dow

def getTodoList():
    date, dow = getdate()
    filename = date.replace('/', '-')
    
    
    print(date)
    print(dow)
    with open('saved date.txt', 'r') as f:
        savedDate = f.read()
        print(savedDate)
    if dow =='Monday':
        if date != savedDate:
            with open('saved date.txt', 'w')as f:
                f.write(date)
                f.close()
            with open(filename+'.txt', 'w') as f:
                f.write(json.dumps(blankTodoList))
                f.close()
            print('todo list cleared')

    with open( filename +'.txt', 'w') as k:
        try:
            data = k.read()
            my_todo_list = json.loads(data)
        except: 
            my_todo_list = blankTodoList
        k.close()
    
    return my_todo_list

def getPlannerInfo():#class? 
    mon = []
    tues = []
    wed = []
    thurs = []
    fri = []
    sat = []
    sun = []
    x = 1
    while x<25:
        mon.append(my_todo_list['monday'][x])
        tues.append(my_todo_list['tuesday'][x])
        wed.append(my_todo_list['wednesday'][x])
        thurs.append(my_todo_list['thursday'][x])
        fri.append(my_todo_list['friday'][x])
        sat.append(my_todo_list['saturday'][x])
        sun.append(my_todo_list['sunday'][x])

        x +=1
    mon = [x for x in mon if x!='']
    print(mon)
    print(tues)
    print(wed)
    print(thurs)
    print(fri)
    print(sat)
    print(sun)

def editPlanner():
    print('Add Event:')
    event = input()
    print('What day would you like to add an event too?')
    day = input()
    day = day.lower()
    print('What time would you like?')
    t = input().lower()
    t = t.replace(' ','')
    print(t)
    my_todo_list[day][hourdict[t]] = event
    print(convertdict[hourdict[t]] + my_todo_list[day][hourdict[t]])
    date, dow = getdate()
    filename = date.replace('/', '-')
    with open(filename +'.txt', 'w') as f:
        f.write(json.dumps(my_todo_list))
        f.close()

def WeekAtGlance():
    for i in my_todo_list:
        j = 1
        print(i + ':')

        while j <25:
            if my_todo_list[i][str(j)] != '':
                
                print(convertdict[j] + my_todo_list[i][str(j)])
            j += 1
        print('\n')

def viewDay():
    print('what day:')
    day = input()
    day = day.lower()
    print(day)
    k = 1
    j = 1
    while j < 25:
        while j > 6 and j < 17:
            print(convertdict[j] + my_todo_list[day][str(j)])
            j += 1
        else:
            if my_todo_list[day][str(j)] != '':
                print(convertdict[j] + my_todo_list[day][str(j)])
        j += 1

def speakDay():
    print('what day:')
    day = 'tuesday'
    day = day.lower()
    print(day)
    j = 1
    j = 1
    while j < 25:
        if my_todo_list[day][str(j)] != '':
                speak(convertdict[j] + my_todo_list[day][str(j)])
        j+=1
    
my_todo_list = getTodoList()
print('\nHello Welcome to your Planner!')
print('\nWhat would you like to do?')
print('1. See full week')
print('2. See specific day')
print('3. Add Event')
print('4. speak days events')

req = input()
if req == '1':
    WeekAtGlance()
elif req == '2':
    viewDay()
elif req == '3':
    editPlanner()
elif req == '4':
    speakDay()
