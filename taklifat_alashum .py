from tkinter import *
from tkinter import messagebox

# Create The Main App Window
arrow_app = Tk()

# Change App Text
arrow_app.title("حساب تكلفة تعديل السهم")

# Set Dimensions
arrow_app.geometry("500x300")
arrow_app.configure(background="lightblue")
# Write Age Label
the_text = Label(arrow_app, text="ادخل قيمة الشراء الأولى", height=1, bg="lightblue",
                 font=("Arial", 20)).place(x=280, y=5)
the_text2 = Label(arrow_app, text="ادخل الكمية الأولى", height=1, bg="lightblue", font=("Arial", 20)).place(x=330, y=55)
the_text3 = Label(arrow_app, text="ادخل قيمة الشراء الثانية", height=1, bg="lightblue", font=("Arial", 20)).place(x=285,
                                                                                                                  y=105)
the_text4 = Label(arrow_app, text="ادخل الكمية الثانية", height=1, bg="lightblue", font=("Arial", 20)).place(x=330,
                                                                                                             y=150)
the_text5 = Label(arrow_app, text="abohoal@gmail.com", height=2, bg="lightblue", font=("Arial", 10)).place(x=350, y=260)

# Place The Text Into The Main Window

# Age Variables
arrow = StringVar()
arrow2 = StringVar()
arrow3 = StringVar()
arrow4 = StringVar()
arrow5 = StringVar()


# Set Default Value For Age


def clear():
    arrow.set(" ")
    arrow2.set(" ")
    arrow3.set(" ")
    arrow4.set(" ")
    arrow5.set(" ")


# Create The Input For Age
arrow_input = Entry(arrow_app, width=7, font=("Arial", 30), textvariable=arrow).place(x=5, y=10)
arrow2_input = Entry(arrow_app, width=7, font=("Arial", 30), textvariable=arrow2).place(x=5, y=55)
arrow3_input = Entry(arrow_app, width=7, font=("Arial", 30), textvariable=arrow3).place(x=5, y=105)
arrow4_input = Entry(arrow_app, width=7, font=("Arial", 30), textvariable=arrow4).place(x=5, y=150)
arrow5_input = None


# Place The Input Into The Main Window


def calc():
    # Get Average_price

    the_arrow_value = arrow.get()
    the_arrow2_value = arrow2.get()
    the_arrow3_value = arrow3.get()
    the_arrow4_value = arrow4.get()

    first_value = float(the_arrow_value) * float(the_arrow2_value)  # 2*5=10
    second_value = float(the_arrow3_value) * float(the_arrow4_value)  # 3*5=15
    Total_previous_cost = int(first_value) + float(second_value)  # 10+15=25
    total_quantity = float(the_arrow2_value) + float(the_arrow4_value)  # 5+5=10عدد الأسهم
    Average_price = float(Total_previous_cost) / float(total_quantity)  # 25/10=2.5
    Total_current_cost = float(Average_price) * float(total_quantity)  # 2.5*10=25
    profit_and_loss = float(first_value) - float(second_value)  # 10-25=-5
    print(Total_current_cost)
    line_one = f"تكلفة الشراء الأول: {first_value}"
    line_two = f"تكلفة الشراء الثانية{second_value}"
    line_three = f"القيمة الإجمالية للأسهم: {Total_previous_cost}"
    line_for = f"اجمالي عدد الأسهم: {total_quantity}"
    line_five = f"التكلفة الحالية للسهم: {Average_price}"
# line_sex = f"اجمالي القيمة الحالية: {Total_current_cost}"
    line_seven = f" فرق سعر المشتريات: ==> (({profit_and_loss}))"

    # List Contain All Lines
    all_lines = [line_one, line_two, line_three, line_for, line_five, line_seven]

    # Message Box To Show All Lines
    messagebox.showinfo("summary", "\n\n\n".upper().join(all_lines))


# Create The Calculate Button
btn = Button(arrow_app, text="أحسب", width=13, font=('Arial', 15),
             height=1, bg="#e91e63", fg="white", borderwidth=6, command=calc).place(x=5, y=210)
clear_btn = Button(arrow_app, text="أمسح", width=13, font=('Arial', 15),
                   height=1, bg="#e91e63", fg="white", borderwidth=6, command=clear).place(x=5, y=250)

# Place Button in The Main Window
arrow_app.mainloop()
# Run App Infinitely
