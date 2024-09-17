import tkinter as tk
import os
import time
from tkinter import Button, Checkbutton, Entry, Frame, Label, LabelFrame, StringVar, Text, Toplevel, font
from tkinter.constants import CENTER, E, NE, S, SEL, W
from typing import Collection
#quit application funtion        
def quitApp():
    exit()

#Rates Display Function.
def DisplayRates():
    new_window=Toplevel(root)
    new_window.geometry("150x100")
    new_window.title("Toll Rates")
    new_window.resizable(False,False)
    lbl=Label(new_window,text="Car=5$/-\nTwo-wheeler=3$/-\nTruck=10$/-")
    lbl.pack()
    btn=Button(new_window,text="close",bg='red',command=new_window.destroy)
    btn.pack()

def Exit_Parking():
    new_window4=Toplevel(root)
    new_window4.geometry("200x200")
    new_window4.title("Exit a Vehicle")
    new_window4.resizable(False,False)
    lbl=Label(new_window4,text="Print Exit ticket")
    btn_car=btn=Button(new_window4,text="Car")
    btn_car.pack()
    btn_truck=Button(new_window4,text="Truck")
    btn_truck.pack()
    btn_bike=Button(new_window4,text="Two-wheeler")
    btn_bike.pack()






#Parking vehicle function starts here
def Park():
    new_window2=Toplevel(root)
    new_window2.geometry("500x600")
    new_window2.title("Park A Vehicle")
    new_window2.resizable(False,False)
    frame2=tk.Frame(new_window2,bg='white')
    frame2.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
    lowerframe=tk.Frame(new_window2,bg='#80c1ff',bd=10)
    lowerframe.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
    label2=tk.Label(frame2,text="Available slots are: ")
    label2.place(relwidth=1,relheight=1)
    label=tk.Label(frame2,text="Book Slot")
    label.pack()

    def col():
        button1.configure(bg='red')


    #positions parking places as green buttons. 
    button1=tk.Button(lowerframe,text='A1',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button1.grid(row=1,column=0)
    button2=tk.Button(lowerframe,text='A2',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button2.grid(row=1,column=1)
    button3=tk.Button(lowerframe,text='A3',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button3.grid(row=1,column=2)
    button4=tk.Button(lowerframe,text='A4',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button4.grid(row=1,column=3)
    button5=tk.Button(lowerframe,text='A5',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button5.grid(row=1,column=4)
    button6=tk.Button(lowerframe,text='B1',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button6.grid(row=2,column=0)
    button7=tk.Button(lowerframe,text='B2',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button7.grid(row=2,column=1)
    button8=tk.Button(lowerframe,text='B3',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button8.grid(row=2,column=2)
    button9=tk.Button(lowerframe,text='B4',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button9.grid(row=2,column=3)
    button10=tk.Button(lowerframe,text='B5',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button10.grid(row=2,column=4)
    button11=tk.Button(lowerframe,text='C1',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button11.grid(row=3,column=0)
    button12=tk.Button(lowerframe,text='C2',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button12.grid(row=3,column=1)
    button13=tk.Button(lowerframe,text='C3',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button13.grid(row=3,column=2)
    button14=tk.Button(lowerframe,text='C4',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button14.grid(row=3,column=3)
    button15=tk.Button(lowerframe,text='C5',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button15.grid(row=3,column=4)
    button16=tk.Button(lowerframe,text='D1',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button16.grid(row=4,column=0)
    button17=tk.Button(lowerframe,text='D2',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button17.grid(row=4,column=1)
    button18=tk.Button(lowerframe,text='D3',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button18.grid(row=4,column=2)
    button19=tk.Button(lowerframe,text='D4',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button19.grid(row=4,column=3)
    button20=tk.Button(lowerframe,text='D5',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button20.grid(row=4,column=4)
    button21=tk.Button(lowerframe,text='E1',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button21.grid(row=5,column=0)
    button22=tk.Button(lowerframe,text='E2',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button22.grid(row=5,column=1)
    button23=tk.Button(lowerframe,text='E3',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button23.grid(row=5,column=2)
    button24=tk.Button(lowerframe,text='E4',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button24.grid(row=5,column=3)
    button25=tk.Button(lowerframe,text='E5',bg="Green",fg='white',padx=10,pady=10,command=button_1)
    button25.grid(row=5,column=4)
    close_button=Button(new_window2,bg='red',text="close",command=new_window2.destroy)
    close_button.pack(side='top')



#Parking buttons functionality
def button_1():
    def display_details():
        emptylabel.config(text="Vehicle number is:-  "+data.get())
    
    def my_upd():
        l1_v1.set(c1_v1.get())
                

    new_window3=Toplevel(root)
    new_window3.geometry("600x600")
    new_window3.title("Parking slot Booking")
    new_window3.resizable(False,False)
    
    label1=Label(new_window3,text="Enter Vehicle Number:",font=14)
    label1.grid(row=0,column=0,padx=5,pady=10)

    data=StringVar()
    textbox1=Entry(new_window3,textvariable=data,fg='black',font=14)
    textbox1.grid(row=0,column=1)

    #checkbuttons positioning
    label_select=Label(new_window3,text='Vehicle Type:-  ',font=14,fg='black')
    label_select.place(relx=0.1,rely=0.5)
    # Car Checkbutton.
    c1_v1=StringVar(new_window3)
    c1_v1.set('Select Vehicle Type')
    c= Checkbutton(new_window3,text="Car",variable=c1_v1,onvalue='Car',offvalue='',command=my_upd)
    c.place(relx=0.2,rely=0.2)
    l1_v1=StringVar(new_window3)
    l1=Label(new_window3,textvariable=c1_v1,font=10)
    l1.place(relx=0.3,rely=0.5)
    #Two-Wheeler Check button
    t=Checkbutton(new_window3,text="Two-Wheeler",variable=c1_v1,onvalue='Two Wheeler',offvalue='',command=my_upd)
    t.place(relx=0.2,rely=0.3)
    #Truck Check Button
    T=Checkbutton(new_window3,text="Truck",variable=c1_v1,onvalue='Truck',offvalue='',command=my_upd)
    T.place(relx=0.2,rely=0.4)

    emptylabel=Label(new_window3,fg="blue",font=14)
    emptylabel.place(relx=0.1,rely=0.6)
    #vehicle number button
    numberplate=Button(new_window3,text='Enter Vehicle Number:',command=display_details)
    numberplate.place(relx=0.6,relheight=0.06,relwidth=0.3)
    #close button positioning
    close_button=Button(new_window3,bg='red',text="close",command=new_window3.destroy)
    close_button.place(rely=0.9,relx=0.9)
    #book slot button
    book_button=Button(new_window3,bg='blue',fg='yellow',text='Print Ticket')
    book_button.place(relx=0.5,rely=0.9,relwidth=0.2)
    #add time in window
    current_time=time.strftime('%H:%M:%p')
    clock_info=Label(new_window3,text='Time: ',font=14)
    clock_info.place(rely=0.7,relx=0.1)
    clock_label=Label(new_window3,font=10,bg='white',text=current_time)
    clock_label.place(relx=0.3,rely=0.7)




    







root=tk.Tk()




canvas=tk.Canvas(root,width=500,height=500)
canvas.pack()
title=tk.Label(root,text="Parking Lot System",bg='yellow',font=25)
title.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)
frame=tk.Frame(root,bg='white')
frame.place(relx=0.30,rely=0.30,relwidth=0.45,relheight=0.30)

Park_Button=tk.Button(frame,text="Park a Vehicle",bg='gray',command=Park).pack(padx=4,pady=4)
Exit=tk.Button(frame,text="Exit Parking",bg='gray',command=Exit_Parking).pack(padx=4,pady=4)
Rates=tk.Button(frame,text="Display Rates",bg="gray",command=DisplayRates).pack(pady=4,padx=4)
Quit=tk.Button(frame,text="Quit Application",bg="red",command=quitApp).pack(pady=4,padx=4)

root.mainloop()
