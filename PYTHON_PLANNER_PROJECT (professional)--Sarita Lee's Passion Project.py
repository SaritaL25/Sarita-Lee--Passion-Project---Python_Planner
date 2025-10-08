from datetime import datetime, timedelta
import time
from pynput import keyboard
import pygame 
import os 


    
def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/saritasamuelalee/Documents/Sarita Lee--Passion Project - Python_Planner/Songs/iphone_alarm.mp3")
    pygame.mixer.music.play()
   
def speak(dialogue):
    os.system('say "{}"'.format(dialogue))
print("Welcome to your daily planner 🎉! " \
    "Hope you're having a great day lets get started!")
speak("Welcome to your daily planner ! Hope you're having a great day lets get started!")
print("Loading...")
time.sleep(5)
#defining task class 
class Task :
    def __init__(self,name="", duration=0):
        self.name=name
        self.duration=duration
        self.complete=False
    def Begin_Task(self):
        print("Whenever you are done PRESS the \033[1m'cmd/ctrl'+'d'\033[0m key")
        print("Your next task is :{} " \
    "You have {} minute(s) to complete this task " \
    "TURN OFF ALL DISTRACTIONS you have 10 seconds to do so".format(self.name,self.duration))
        speak("Whenever you are done PRESS the 'cmd/ctrl'+'d' key Your next task is :{} You have {} minute(s) to complete this task TURN OFF ALL DISTRACTIONS you have 10 seconds to do so".format(self.name,self.duration))
        time.sleep(10)
        self.startTime= datetime.now()#gets current time
        self.endTime=self.startTime+timedelta(minutes=self.duration)#calcualtes the end time ,i checked this works pretty well
        self.has_extended=False#initializes extension to false, you don't want to give them 5 minutes right away, when time is up they must indicate so 
        self.Task_Timer()#begins the next function 
    def mark_as_done(self):
            if(not self.complete):
                self.complete=True
                print("Congrats you're done with {} !🎉".format(self.name))
    
    '''def for_canonical(f):
        return lambda kou: f(keyboard.Listener.canonical(k))'''
#this function begins the internal timer for each individual task
    '''def start_done_listener(self):
        done_indicator = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+d'), self.mark_as_done)
        listener = keyboard.Listener(
            on_press=Task.for_canonical(done_indicator.press),
            on_release=Task.for_canonical(done_indicator.release))
        listener.start()'''
    def on_release(key):# defines the funciton that happens upon release or when the user lifts up from any key they pressed
        if(key==keyboard.KeyCode.from_char('d')):
            current_user.todo_list[task_tracker].mark_as_done()
#hi
    l = keyboard.Listener(on_release=on_release)
    l.start()
    def Task_Timer(self):
        
        print("The timer ⏲️ has begun you have {} minute(s) on the clock!".format(self.duration))
        speak("The timer has begun you have {} minute(s) on the clock!".format(self.duration))
        print("NOW:{}".format(datetime.now()))
        print("END:{}+".format(self.endTime))
        while(not self.complete):
            if(datetime.now()>=self.endTime and not self.has_extended):
                print("Would you like to add 5 more minutes to wrap up?(y/n)")
                user_input= input().strip().lower()
                if(user_input=="y"):
                    self.endTime= datetime.now()+timedelta(minutes=5)#adds 5 minutes
                    self.has_extended=True
                    continue  
                else:
                    self.complete=False
                    break
            elif(datetime.now()>=self.endTime and self.has_extended):
                break
        self.overdue= 5
        self.endTime=datetime.now()+timedelta(minutes=self.overdue)
        last_min_left=None 
        while(datetime.now()<self.endTime and not self.complete):
            now=datetime.now()
            TimeLeft=(self.endTime-datetime.now()).total_seconds()/60
            minutes_left = int(TimeLeft)
            seconds_left = int((TimeLeft - minutes_left) * 60)
            if(last_min_left!=minutes_left and datetime.now()<self.endTime):
                play_alarm_sound()
                if(minutes_left>0):
                 print("WARNING : You have {:.1f} minute(s) ⏳ left, please MARK AS DONE by pressing the 'd' key. " \
                "If you're not done i'll move forward without you ...".format(minutes_left))
                 speak("WARNING : You have {:.1f} second(s) left, please MARK AS DONE by pressing the 'ctrl'+'d' key. If you're not done i'll move forward without you ...".format(minutes_left))

                else:
                    print("WARNING : You have {:.1f} second(s) ⏳ left, please MARK AS DONE by pressing the 'ctrl'+'d' key. " \
                "If you're not done i'll move forward without you ...".format(seconds_left))
                    speak("WARNING : You have {:.1f} second(s) left, please MARK AS DONE by pressing the 'ctrl'+'d' key. If you're not done i'll move forward without you ...".format(seconds_left))
                last_min_left=minutes_left
            time.sleep(1)
        play_alarm_sound()
        print("⏰ TIMES UP ! if you're not done too bad so sad, if you are please indicate so later...")
        speak('TIMES UP!')
        pygame.mixer.music.stop()
        #heres where i really need help, if the person inputs nothing i want the code 
        # to continue UNTIL they enter soemthing if they do not enter anything let the 
        # code continue until time is up once time is up they will still need to mark when they are done, 
        # if they are still not done after witing another 10 minutes the program will atuomatically
        # advance to the next task on the list and prompt them to continue throughout the 10 minute grace period 
        # for example : it will print "You are "+str(datetime.now()-self.endtime)+" minute(s) overdue PLEASE MARK AS DONE IF DONE IF NOT JUST MOVE ON and mark done"
        return self.complete
    #define user class
class User:
    def __init__(self,name):#each user has a name, todo list, and a boolean that tells us if the list was already set up
        self.name=name
        self.todo_list=[]
        self.list_set=False
    def ToDo_setUp(self):
        count =1
        while(not self.list_set):
            print("Enter task #"+str(count))#allows person to enter tasks to their list
            self.todo_list.append(Task())
            self.todo_list[count-1].name= input()
            print("Enter task #"+str(count)+"'s duration")
            self.todo_list[count-1].duration=int(input())#enter times in minutes not hours
            print("Would you like to add more tasks? (y/n)")
            user_input=input().strip().lower()
            if(user_input=="n"):
             self.list_set=True
             break
            else :
                count+=1
    def Edit_List(self):#function that allows person to edit the list they already have
        print("Enter an index")
        index=int(input())-1#input is automatically a string so i need to convert to int 
        print("Enter N: Rename Task \n Enter D: Edit Duration of Task \n Enter R: Remove a task ")
        user_input=input().strip().upper()
        if(user_input=="R"):
            removed = self.todo_list.pop(index)
            print("Removing {}... ".format(removed.name))
            time.sleep(5)
            print("{} Removed".format(removed.name))
            
        else:
            print("Enter new duration for Task: ")
            self.todo_list[index].duration=int(input())
    def summary(self):
        avg_time=0
        num_complete=0
        for task in self.todo_list:
            avg_time+=task.duration
        avg_time/=len(self.todo_list)
        if(task.complete):
                num_complete+=1
        return avg_time, num_complete,len(self.todo_list)
        

#____________MAIN METHOD_____________
#how do i indicate that this is the main method without a comment ? to make it clear to other programmers

def break_timer():
    print("How long would you like your break to be?(enter the letter)" \
    "a) 5 Minutes" \
    "b) 10 Minutes" \
    "c) 15 Minutes")
    user_input= input()
    if(user_input=='a'):
        sleepTimer=5
    if(user_input=='b'):
        sleepTimer=10
    if(user_input=='c'):
        sleepTimer=15
    print("Enjoy your {} minute break...".format(sleepTimer))
    print(" ☀️ Break in Progress 🏖️")
    speak("Enjoy your {} minute break...Break in Progress".format(sleepTimer))
    time.sleep(sleepTimer*60)
    print("Welcome back ! Ready to hit the ground running? " \
    "Let's get back to your to-do list!")
    time.sleep(3)

currentTime=datetime.now()
print("What is your name? ")
current_user= User(input())
speak("Hello,"+current_user.name+" lets set up your to-do list!")
print("Hello,"+current_user.name+" lets set up your to-do list!")
current_user.ToDo_setUp()
Running_Main=True
task_tracker=0


menu={1:current_user.todo_list[task_tracker].Begin_Task,2:current_user.Edit_List,3:break_timer}
menu_label={1:'Start Task',2:'Edit To-Do List',3:'Take a Break'}



while(Running_Main):#I want person to be able to remove tasks and edit the list while they go how do i fix this ?
    print("Here's your to-do list: ")
    for x in range(0,len(current_user.todo_list)):
        if(current_user.todo_list[x].complete):
            print("✅ "+current_user.todo_list[x].name)
        else:
             print(current_user.todo_list[x].name)
    print("Loading menu options...")
    time.sleep(10)
    print("\033[1m Option menu:\033[0m")
    for key in menu.keys():
        print("Press {} for {}".format(str(key),str(menu_label[key])))#how do i change the way this is printing the values ?
    time.sleep(2)
    user_input=int(input())
    if user_input in menu :
            menu[user_input]()
    else:
        while(user_input not in menu or (user_input==4 and task_tracker==0)):
            print("Option not availible please try again")
            time.sleep(3)
            print("Waiting for user input...")
            user_input=int(input())
            if(user_input in menu ):
                menu[user_input]()
                break
    time.sleep(5)
    if(current_user.todo_list[task_tracker].complete):
        task_tracker+=1#increments the task so we move on 
    if(task_tracker==len(current_user.todo_list)):
        break

time.sleep(5)
pygame.mixer.music.stop()
my_summary= current_user.summary()
speak("Congrats you've made it through the whole list...Here's a breif summary of what we've done today: Average time spent on each task: {} Number of Tasks Completed: {}  Number of Total Tasks: {} Great work ! See ya real soon ! ".format(*my_summary))#the symbol * unpacks the tuple returned
Time_spent,num_complete,num_tasks=current_user.summary()
print("Congrats you've made it through the whole list..." \
"Here's a breif summary of what we've done today:" \
"Average time spent on each task: {}" \
"Number of Tasks Completed: {}" \
"Number of Total Tasks: {}" \
"Great work ! See ya real soon ! ".format(Time_spent,num_complete,num_tasks))#the symbol * unpacks the tuple returned
#play the hotdog mickey mouse song






