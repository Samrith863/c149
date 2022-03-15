from tkinter import *
import random 
root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")
root.configure(background="blue")
label1=Label(root)

list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(list1[0:26])

def secretCode():
    random_num1=random.randint(0,25)
    random_num2=random.randint(0,25)
    random_num3=random.randint(0,25)
    random_num4=random.randint(0,25)
    random_num5=random.randint(0,25)
    random_num6=random.randint(0,25)
    
    random_letter1=list1[random_num1]
    random_letter2=list1[random_num2]
    random_letter3=list1[random_num3]
    random_letter4=list1[random_num4]
    random_letter5=list1[random_num5]
    random_letter6=list1[random_num6]
    label1['text']=random_letter1+random_letter2+random_letter3+random_letter4+random_letter5+random_letter6
btn=Button(root,text="What is your secret code?",bg="black",fg="white",command=secretCode)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

