import tkinter as tk

HEIGHT = 600
WIDTH = 600
SALARY_PER_DAY = 330

def calculate_salary():
    try:
        # Get the input values
        total_days = int(entry.get())
        worked_days = int(entry2.get())
        provident_fund = float(entry4.get())

        # Calculate the gross and net salary
        gross_salary = worked_days * SALARY_PER_DAY
        net_salary = gross_salary - provident_fund

        # Update the result label
        result_label.config(text=f"Net Salary: {net_salary} Rs")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#99ccff')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Label and entry for total working days
label = tk.Label(frame, text="TOTAL WORKING DAYS IN A MONTH", bg='gray')
label.grid(row=0, column=0)
entry = tk.Entry(frame, bg='white')
entry.grid(row=0, column=1)

# Label and entry for number of days worked
label2 = tk.Label(frame, text="NUMBER OF DAYS WORKED BY EMPLOYEE", bg='yellow')
label2.grid(row=1, column=0)
entry2 = tk.Entry(frame, bg='white')
entry2.grid(row=1, column=1)

# Salary per day label
label3 = tk.Label(frame, text='SALARY PER DAY IS 330 Rs/-')
label3.grid(row=2, column=1)

# Label and entry for provident fund cuts
label4 = tk.Label(frame, text='PROVIDENT FUND CUTS=')
label4.grid(row=3, column=0)
entry4 = tk.Entry(frame, bg='white')
entry4.grid(row=3, column=1)

# Button to calculate salary
button = tk.Button(frame, text="Calculate", bg='gray', command=calculate_salary)
button.grid(row=4, column=1)

# Label to display the result (Net Salary)
result_label = tk.Label(frame, text="")
result_label.grid(row=5, column=1)

root.mainloop()
