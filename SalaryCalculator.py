import tkinter as tk
HEIGHT= 600
WIDTH= 600
root= tk.Tk()

canvas =tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame=tk.Frame(root,bg='#99ccff')
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

#button=tk.Button(frame,text="Calculate",bg='gray')
#button.pack(side='left')
label= tk.Label(frame,text="TOTAL WORKING DAYS IN A MONTH",bg='gray')
label.grid(row=0,column=0)
entry= tk.Entry(frame, bg='white')
entry.grid(row=0, column=1)

label2= tk.Label(frame,text="NUMBER OF DAYS WORKED BY EMPLOYEE",bg='yellow')
label2.grid(row=1,column=0)
entry2=tk.Entry(frame,bg='white')
entry2.grid(row=1,column=1)

label3=tk.Label(frame,text='SALARY PER DAY IS 330Rs/-')
label3.grid(row=2,column=1)

label4=tk.Label(frame,text='PROVIDENT FUND CUTS=')
label4.grid(row=3,column=0)
entry4=tk.Entry(frame,bg='white')
entry4.grid(row=3,column=1)


root.mainloop()
