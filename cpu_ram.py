from tkinter import *
from tkinter import font
from psutil import disk_partitions, disk_usage, virtual_memory, cpu_percent 

window = Tk()
window.geometry("900x600")
window.title("CPU - RAM - DISK USAGE")


# Función para mostrar información de la CPU
def show_cpu_info():
    cpu_use = cpu_percent(interval=1)
    print('{} %'.format(cpu_use))
    cpu_label.config(text='{}%'.format(cpu_use))
    cpu_label.after(200, show_cpu_info)

# Function converter Bytes to Gigabytes
def conversor_bytes_to_gb(bytes_value):
    one_gigabyte = 1073741824 # Bytes
    giga = bytes_value / one_gigabyte
    giga = '{0:.1f}'.format(giga)
    return giga

# Function to display RAM information
def show_ram_info():
    ram_usage = virtual_memory()
    print(ram_usage)
    used = conversor_bytes_to_gb(ram_usage[3])
    total = conversor_bytes_to_gb(ram_usage[0])
    percent = ram_usage[2]
    ram_label.config(text='{} GB / {} GB ({} %)'.format(used, total, percent))
    ram_label.after(200, show_ram_info)

# Title program
title_program = Label(window, text='PC Performance Manager', font="arial 40 bold", fg='#14747F')
title_program.place(x=110, y=20)               
    

# CPU title
cpu_title_label = Label(window, text='CPU Usage: ', font="arial 24 bold", fg='#FA5125')
cpu_title_label.place(x=20, y=155)

# Label to show percent of CPU
cpu_label = Label(window, bg='#071C1E', fg='#FA5125', font="Arial 30 bold", width=20)
cpu_label.place(x=230, y=150)

# RAM title
ram_title_label = Label(window, text='RAM Usage: ', font="arial 24 bold", fg='#34A96C')
ram_title_label.place(x=20, y=255)

# Label to show percent of RAM
ram_label = Label(window, bg='#071C1E', fg='#FA5125', font="Arial 30 bold", width=20)
ram_label.place(x=230, y=250)


if __name__ == '__main__':
    show_cpu_info()
    show_ram_info()
    window.mainloop()
