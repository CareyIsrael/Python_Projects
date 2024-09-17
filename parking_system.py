import tkinter as tk
import time
from tkinter import Button, Checkbutton, Entry, Label, Toplevel, StringVar, messagebox

# Slot status tracking
slot_status = {}


# Quit application function
def quitApp():
    exit()


# Display Rates Function.
def DisplayRates():
    new_window = Toplevel(root)
    new_window.geometry("150x100")
    new_window.title("Toll Rates")
    new_window.resizable(False, False)
    lbl = Label(new_window, text="Car=5$/-\nTwo-wheeler=3$/-\nTruck=10$/-")
    lbl.pack()
    btn = Button(new_window, text="Close", bg='red', command=new_window.destroy)
    btn.pack()


# Exit Parking Function
def Exit_Parking():
    new_window4 = Toplevel(root)
    new_window4.geometry("200x200")
    new_window4.title("Exit a Vehicle")
    new_window4.resizable(False, False)
    lbl = Label(new_window4, text="Select the slot to exit")
    lbl.pack()

    # Create buttons to free up slots
    for slot, status in slot_status.items():
        if status == "occupied":
            Button(new_window4, text=slot, command=lambda s=slot: exit_vehicle(s)).pack(pady=5)

    close_button = Button(new_window4, text="Close", bg='red', command=new_window4.destroy)
    close_button.pack()


# Function to mark a slot as available after exit
def exit_vehicle(slot):
    slot_status[slot] = "available"
    slots[slot].config(bg="Green")
    messagebox.showinfo("Exit Successful", f"Slot {slot} is now available again.")


# Parking function
def Park():
    new_window2 = Toplevel(root)
    new_window2.geometry("500x600")
    new_window2.title("Park A Vehicle")
    new_window2.resizable(False, False)

    # Frame and labels for parking slots
    frame2 = tk.Frame(new_window2, bg='white')
    frame2.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    lowerframe = tk.Frame(new_window2, bg='#80c1ff', bd=10)
    lowerframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label2 = tk.Label(frame2, text="Available slots are: ")
    label2.place(relwidth=1, relheight=1)
    label = tk.Label(frame2, text="Book Slot")
    label.pack()

    # Function to open booking window for each slot
    def book_slot(slot):
        if slot_status[slot] == "occupied":
            messagebox.showerror("Error", "Slot already booked!")
            return

        def display_details():
            emptylabel.config(text="Vehicle number is: " + data.get())

        def my_upd():
            l1_v1.set(c1_v1.get())

        new_window3 = Toplevel(root)
        new_window3.geometry("600x600")
        new_window3.title(f"Booking Slot {slot}")
        new_window3.resizable(False, False)

        label1 = Label(new_window3, text="Enter Vehicle Number:", font=14)
        label1.grid(row=0, column=0, padx=5, pady=10)

        data = StringVar()
        textbox1 = Entry(new_window3, textvariable=data, fg='black', font=14)
        textbox1.grid(row=0, column=1)

        # Checkbuttons for vehicle types
        label_select = Label(new_window3, text='Vehicle Type:', font=14, fg='black')
        label_select.place(relx=0.1, rely=0.5)

        c1_v1 = StringVar(new_window3)
        c1_v1.set('Select Vehicle Type')

        car_btn = Checkbutton(new_window3, text="Car", variable=c1_v1, onvalue='Car', offvalue='', command=my_upd)
        car_btn.place(relx=0.2, rely=0.2)
        bike_btn = Checkbutton(new_window3, text="Two-Wheeler", variable=c1_v1, onvalue='Two-Wheeler', offvalue='',
                               command=my_upd)
        bike_btn.place(relx=0.2, rely=0.3)
        truck_btn = Checkbutton(new_window3, text="Truck", variable=c1_v1, onvalue='Truck', offvalue='', command=my_upd)
        truck_btn.place(relx=0.2, rely=0.4)

        l1_v1 = StringVar(new_window3)
        l1 = Label(new_window3, textvariable=c1_v1, font=10)
        l1.place(relx=0.3, rely=0.5)

        emptylabel = Label(new_window3, fg="blue", font=14)
        emptylabel.place(relx=0.1, rely=0.6)

        numberplate = Button(new_window3, text='Enter Vehicle Number:', command=display_details)
        numberplate.place(relx=0.6, relheight=0.06, relwidth=0.3)

        # Book the slot and change button color to red
        def confirm_booking():
            vehicle_number = data.get()
            vehicle_type = c1_v1.get()
            if vehicle_number and vehicle_type != "Select Vehicle Type":
                slot_status[slot] = "occupied"
                slots[slot].config(bg="Red")
                messagebox.showinfo("Booking Confirmed",
                                    f"Vehicle {vehicle_number} ({vehicle_type}) has booked slot {slot}")
                new_window3.destroy()
            else:
                messagebox.showerror("Error", "Please enter valid vehicle details.")

        book_button = Button(new_window3, bg='blue', fg='yellow', text='Confirm Booking', command=confirm_booking)
        book_button.place(relx=0.5, rely=0.9, relwidth=0.2)

        current_time = time.strftime('%H:%M:%p')
        clock_info = Label(new_window3, text='Time: ', font=14)
        clock_info.place(rely=0.7, relx=0.1)
        clock_label = Label(new_window3, font=10, bg='white', text=current_time)
        clock_label.place(relx=0.3, rely=0.7)

        close_button = Button(new_window3, bg='red', text="Close", command=new_window3.destroy)
        close_button.place(rely=0.9, relx=0.9)

    # Create buttons for each parking slot
    global slots
    slots = {}
    available_slots = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5',
                       'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5',
                       'E1', 'E2', 'E3', 'E4', 'E5']
    for i, slot in enumerate(available_slots):
        row = i // 5
        col = i % 5
        slot_status[slot] = "available"
        slots[slot] = tk.Button(lowerframe, text=slot, bg="Green", fg='white', padx=10, pady=10,
                                command=lambda s=slot: book_slot(s))
        slots[slot].grid(row=row, column=col)

    close_button = Button(new_window2, bg='red', text="Close", command=new_window2.destroy)
    close_button.pack(side='top')


# Main window configuration
root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
title = tk.Label(root, text="Parking Lot System", bg='yellow', font=25)
title.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)
frame = tk.Frame(root, bg='white')
frame.place(relx=0.30, rely=0.30, relwidth=0.45, relheight=0.30)

Park_Button = tk.Button(frame, text="Park a Vehicle", bg='gray', command=Park).pack(padx=4, pady=4)
Exit_Button = tk.Button(frame, text="Exit Parking", bg='gray', command=Exit_Parking).pack(padx=4, pady=4)
Rates_Button = tk.Button(frame, text="Display Rates", bg="gray", command=DisplayRates).pack(pady=4, padx=4)
Quit_Button = tk.Button(frame, text="Quit Application", bg="red", command=quitApp).pack(pady=4, padx=4)

root.mainloop()
