#-------------------- Windows code --------#

import tkinter
from turtle import bgcolor

window = tkinter.Tk()
window.title("Windows")
window.wm_geometry("500x500")
window["bg"] = "#900C3F"


#---------- class ------
class Animals:
    animal = "Dog"
    age = 4
    name = "Luis"
    sexo = "Male"
    color = "brown"

dog = Animals()



hea = tkinter.Label(window, text = "The animals is a? " + dog.animal).pack()


window.mainloop()

