import os
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
#pc_name = input("Введите название ПК, для удаленной перезагрузки \n",)
#time = input("Введите время перезапускаБ в секундах",)
#reboot = "shutdown /m \\\\" + pc_name +" /r" + " /f" + " /t " + time
#print(reboot)
#os.system(reboot)
#input("Нажмите ЕНТЕР",)

def reboot_click(): #21334234
    pc_name = list(map(str, pc_name_win.get().split(" ")))  # получение название файла для удаления, через пробел
    if len(pc_name_win.get()) == 0:
        messagebox.showinfo("GUI Python", "Введите название ПК")
        return False
    #pc_name = pc_name_win.get() #получаем название ПК из окна
    time = time_re_win.get() #получаем время перезагрузки или выключения
    print(pc_name)
    print(time)
    for name in pc_name:
        if chk_reboot_state.get():
            reboot = "shutdown /m \\\\" + name + " /r" + " /f" + " /t " + time
            os.system(reboot)
            messagebox.showinfo("GUI Python", "ПК отправлен на перезагрузку")
        else:
            print()
        if chk_pwroff_state.get():
            reboot = "shutdown /m \\\\" + name + " /s" + " /f" + " /t " + time
            os.system(reboot)
            messagebox.showinfo("GUI Python", "ПК отправлен на выключение")
        else:
            print()
    #reboot = "shutdown /m \\\\" + pc_name + " /r" + " /f" + " /t " + time
    #print(reboot)
    #messagebox.showinfo("GUI Python", "ПК отправлен на перезагрузку")
def reboot_click_not():
    pc_name = list(map(str, pc_name_win.get().split(" ")))  # получение название файла для удаления, через пробел
    if len(pc_name_win.get()) == 0:
        messagebox.showinfo("GUI Python", "Введите название ПК")
        return False
    # pc_name = pc_name_win.get() #получаем название ПК из окна
    #time = time_re_win.get()  # получаем время перезагрузки или выключения
    for name in pc_name:
        if chk_reboot_state.get():
            reboot = "shutdown /m \\\\" + name + " /a"
            os.system(reboot)
            messagebox.showinfo("GUI Python", "Перезагрузка ПК отменена")
        else:
            print()
        if chk_pwroff_state.get():
            reboot = "shutdown /m \\\\" + name + " /a"
            os.system(reboot)
            messagebox.showinfo("GUI Python", "Выключение ПК отменено")
        else:
            print()

window = Tk()
window.title("Удаленная перезагрузка ПК")
window.geometry('600x300')
pc_name_label = Label(window, text="Введите название ПК, через пробел:")
pc_name_label.grid(column=0, row=0)
pc_name_win = Entry(window, width=30)
pc_name_win.grid(column=1, row=0)
btn_pc = Button(window, text="Выполнить", command=reboot_click)
btn_pc.grid(column=2, row=0)
btn_pc_not = Button(window, text="Отменить выполнение", command=reboot_click_not)
btn_pc_not.grid(column=2, row=1)
time_re_label = Label(window, text="Через какое время перезагрузить ПК (сек.): ")
time_re_label.grid(column=0, row =1)
time_re_win = Entry(window, width=30)
time_re_win.grid(column=1, row =1)
chk_reboot_state = IntVar()
chk_reboot = Checkbutton(window, text='Перезагрузить удаленный ПК', variable=chk_reboot_state)
chk_reboot.grid(column=0, row=2)
chk_pwroff_state = IntVar()
chk_pwroff = Checkbutton(window, text='Выключить удаленный ПК', variable=chk_pwroff_state)
chk_pwroff.grid(column=1, row=2)

window.mainloop()

# def clicked():
#     txt1.insert(INSERT, os.system("C:\PSTools\psexec \\\it15  ipconfig /all"))
# window = Tk()
# window.title("Удаление файлов из каталога")
# window.geometry('600x550')
# lbl3 = Label(window, text="Удаленныые файлы:")
# lbl3.grid(column=1, row=3)
# txt1 = scrolledtext.ScrolledText(window, width=70, height=20) # Окно с удаление
# txt1.grid(row=6,column=0,columnspan=3)
# btn = Button(window, text="OK", command=clicked)
# btn.grid(column=2, row=0)
# window.mainloop()