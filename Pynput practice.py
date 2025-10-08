from pynput import keyboard 
#we want to use the non-blocking version to not interupt the code

def on_release(key):# defines the funciton that happens upon release or when the user lifts up from any key they pressed
 if(key==keyboard.KeyCode.from_char('l')):
    print(key)
'''def on_press(key):# defines the funciton that happens upon pressing any key , happens right away 
    print("Pressed")'''
l = keyboard.Listener(on_release=on_release)
l.start()
while(True):#we need to tell the program to continue running while waiting for input otherwise the code will terminate 
    1+1
# we may want to create multiple of those functions for different parts of the code if need be