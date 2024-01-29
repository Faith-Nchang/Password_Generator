import random
from tkinter import *
from tkinter import messagebox

def password_generator():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!@#$%^&*(){}?/><;"
    # ensures the user inputed a number for each entry
    try:
       required_numbers = int(number_input.get())
       required_letters = int(letter_input.get())
       required_special_characters = int(special_character_input.get())
    except:
        messagebox.showerror("Please enter a value for all the fields")
        return
    # generates random letters
    password_letters = [random.choice(letters) for i in range(required_letters)]
    # generates random numbers
    password_numbers = [random.choice(numbers) for i in range(required_numbers)]
    # generates random characters
    password_special_characters = [random.choice(special_characters) for i in range(required_special_characters)]


    # concatenates all generated letters, numbers, and characters
    list = password_letters + password_numbers + password_special_characters
    random.shuffle(list)

    # converts characters to string
    password =' '.join([str(i) for i in list])
    password = "Password: " + str((password))
    password_string = StringVar()
    password_string.set(password)

    # displays the generated password
    password_input = Label(window, textvariable=password_string, font=('Arial',10,'normal'), bg="black", fg="blue")
    password_input.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
    password_input.bind("<Return>")


window = Tk()
window.title("Password Generator")
window.geometry("300x300")
window.configure(bg="black")

# header for the password generator
label = Label(window, text="Password Generator", font=('Arial', 13, 'bold'), fg="green", background="black")
label.grid(row=0, column=0, padx=10, pady = 10, columnspan=2)

# prompt the user for the number of letters
label = Label(window, text="Enter number of letters in password", font=('Arial', 10), background="black", fg ="white")
label.grid(row=1, column=0)
letter_input = Entry(window, width =5)
letter_input.grid(row = 1, column = 1, padx=5, pady=10)

# prompt the user for number of digits to include
numbers = Label(window, text="How many digits in password: ", font=('Arial', 10), background="black", fg ="white")
numbers.grid(row=2, column=0)
number_input = Entry(window, width =5)
number_input.grid(row = 2, column = 1, padx=6, pady=15)

# prompts the user for special characters to include
characters = Label(window, text="Number of other characters in password: ", font=('Arial', 10), background="black", fg ="white")
characters.grid(row=3, column=0)
special_character_input = Entry(window, width=5)
special_character_input.grid(row=3, column=1, padx=5, pady=10)

# calls the password_generator function when clicked
button = Button(window, text="Generate password", command=password_generator)
button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()