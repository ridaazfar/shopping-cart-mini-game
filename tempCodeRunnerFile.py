from tkinter import *
from tkinter import messagebox
import winsound

def pay_bill():
    # show message box first
    messagebox.showinfo("Bill Paid","Thanks for shopping!🛒")
    
    # after pressing OK, destroy basket window and main window
    if hasattr(window, "list_window"):  #hasattr means has attribute
        window.list_window.destroy()
    window.destroy()

def drag_start(event):
    canvas.startX = event.x
    canvas.startY = event.y

def drag_motion(event):
    dx = event.x - canvas.startX
    dy = event.y - canvas.startY
    canvas.move("current", dx, dy)
    canvas.startX = event.x
    canvas.startY = event.y

def drop(event):
    # Get which item was dropped
    item = canvas.find_withtag("current")[0] # the dragged item
    x, y = canvas.coords(item)  # current position of the item
    basket_width = basket_image.width()
    basket_height = basket_image.height()

    x_min = 250 - (basket_width // 2)   # left edge
    x_max = 250 + (basket_width // 2)   # right edge
    y_min = 250 - (basket_height // 2)  # top edge
    y_max = 250 + (basket_height // 2)  # bottom edge

    if x_min < x < x_max and y_min < y < y_max:
        grocery_name = item_names[item]
        if grocery_name not in basket_items:
            basket_items.append(grocery_name)

            winsound.Beep(1400, 70)
            winsound.Beep(1400, 70)
            winsound.Beep(1400, 70)


def show_list():
    if not basket_items:
        messagebox.showinfo("Basket 🛒", "Your basket is empty!")
        return
    
    # Create the window only once
    list_window = Toplevel(window)
    list_window.config(bg="white")

    label2 = Label(list_window, text="Your Basket",
                   font=("Ink Free",16,"bold"),
                   fg="#F4A6A6", bg="white")
    label2.pack()

    listbox = Listbox(list_window,
                      width=20, height=10,
                      font=("Ink Free",12,"bold"),
                      fg="#F4A6A6",
                      bg="#f7ffde")
    listbox.pack()

    # Insert all items at once
    for item in basket_items:
        listbox.insert(END, item)

    button = Button(list_window, text="Pay Bill",
                    font=("Ink Free",10,"bold"),
                    bg="#F4A6A6", fg="white",
                    command=pay_bill)
    button.pack(pady=5)

window = Tk()
window.geometry("500x500")
window.config(bg="white")

label = Label(window, text="Pick Up Groceries 🛒",
              font=("Ink Free",20,"bold"),
              fg="#EA9696", bg="white")
label.pack()

button = Button(window, text="Show Basket",
                font=("Ink Free",12,"bold"),
                bg="#F4A6A6", fg="white",
                command=show_list)
button.pack(side="bottom", pady=10)

canvas = Canvas(window, height=500, width=500, bg="white")
canvas.pack()

background_image=PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\sheet.png")
background=canvas.create_image(0,0,image=background_image)

basket_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\pink basket.png")
myimage = canvas.create_image(250,250,image=basket_image)

coke_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\coke cherry.png")
coke = canvas.create_image(44, 13, image=coke_image, anchor="nw")

macroon_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\macroon.png")
macroon = canvas.create_image(187, 22, image=macroon_image, anchor="nw")

milk_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\milk bottle.png")
milk = canvas.create_image(120, 348, image=milk_image, anchor="nw")

jam_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\jam.png")
jam = canvas.create_image(338, 20, image=jam_image, anchor="nw")

bagel_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\bagels.png")
bagel = canvas.create_image(372, 144, image=bagel_image, anchor="nw")

strawberry_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\strawberries.png")
strawberry = canvas.create_image(263, 365, image=strawberry_image, anchor="nw")

nutella_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\nutella.png")
nutella = canvas.create_image(0, 197, image=nutella_image, anchor="nw")

roll_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\rolls.png")
rolls = canvas.create_image(18, 369, image=roll_image, anchor="nw")

coffee_image = PhotoImage(file="C:\\Users\\jtees\\Documents\\Shopping Cart\\cold coffee.png")
coffee = canvas.create_image(372, 344, image=coffee_image, anchor="nw")

# Map canvas IDs to grocery names
item_names = {
    coke: "Coke Cherry",
    macroon: "Strawberry Macaron",
    milk: "Milk Bottle",
    jam: "Strawberry Jam",
    bagel: "Bagels",
    strawberry: "Strawberries",
    nutella: "Nutella",
    rolls: "Cinnamon Rolls",
    coffee: "Iced Coffee"
}
basket_items=[]
# Group all groceries
items = [coke, macroon, milk, jam, bagel, strawberry, nutella, rolls, coffee]

# Bind events
for item in items:
    canvas.tag_bind(item, "<Button-1>", drag_start)
    canvas.tag_bind(item, "<B1-Motion>", drag_motion)
    canvas.tag_bind(item, "<ButtonRelease-1>", drop)

window.mainloop()
