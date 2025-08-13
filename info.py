from tkinter import *

root = Tk()
root.title('Hello World')

def showMessage():
    Label(root, text="ชื่อ สรวิชญ์ ศรีลาออน", fg="white", font=("Arial", 20), bg="black").pack()
    Label(root, text="ชั้น ม.5/8", fg="white", font=("Arial", 20), bg="black").pack()
    Label(root, text="เลขที่ 11", fg="white", font=("Arial", 20), bg="black").pack()

Button(root, text="info", command=showMessage).pack()

root.geometry("500x500")
root.mainloop()