import win32gui, win32api, win32process, ctypes, time

from tkinter import *
from tkinter import messagebox

kernal32 = ctypes.windll.LoadLibrary(r"C:\Windows\System32\kernel32.dll")
hwnd = win32gui.FindWindow("MainWindow", "Plants vs. Zombies")
pid = win32process.GetWindowThreadProcessId(hwnd)[1]
handle = win32api.OpenProcess(0x1F0FFF, False, pid)

ba_addr = 0X00755E0C
m_offset1 = 0x868
m_offset2 = 0x5578

collection_addr = 0x0043CC72


def GetAddress(handle, BaseAddress, offset=[]):
    value = ctypes.c_long()
    kernal32.ReadProcessMemory(int(handle), BaseAddress, ctypes.byref(value), 4, None)
    for i in range(len(offset) - 1):
        kernal32.ReadProcessMemory(int(handle), value.value + offset[i], ctypes.byref(value), 4, None)
    return value.value + offset[len(offset) - 1]


address = GetAddress(handle, ba_addr, offset=[m_offset1, m_offset2])
sunNum = ctypes.c_long()
changeSun = ctypes.c_long()
collection = ctypes.c_long()
kernal32.ReadProcessMemory(int(handle), address, ctypes.byref(sunNum), 4, None)

screen = Tk()
screen.title('killOfPvz')
screen.geometry('300x330+300+300')


def changSun():
    try:
        n = int(e1.get())

        if n >= 0 and n <= 9999:
            changeSun = ctypes.c_long(n)
            kernal32.WriteProcessMemory(int(handle), address, ctypes.byref(changeSun), 4, None)
            messagebox.showinfo('Success', 'Sunshine is changed!')
        else:
            messagebox.showwarning('Tips', 'Out of range!0-9999')

    except e1:
        print(e1)
        messagebox.showwarning('Tips', 'Enter a Integer!')


def auto_collection():
    if checkVar.get() == '0':
        collection.value = 2421
        kernal32.WriteProcessMemory(int(handle), collection_addr, ctypes.byref(collection), 2, None)

    else:
        collection.value = 2422
        kernal32.WriteProcessMemory(int(handle), collection_addr, ctypes.byref(collection), 2, None)


lb1 = Label(screen, text='Sunshine:{}'.format(sunNum.value))
lb2 = Label(screen, text='I want:')
e1 = Entry(screen)
bt1 = Button(screen, text='Change', command=changSun, bg='green')
checkVar = StringVar(value="0")
c1 = Checkbutton(screen, text="Auto_Collection_Flag", variable=checkVar, command=auto_collection)

lb1.place(x=85, y=50)
lb2.place(x=85, y=80)
e1.place(x=130, y=80, width=50)
bt1.place(x=110, y=110)
c1.place(x=85, y=150)

screen.mainloop()
