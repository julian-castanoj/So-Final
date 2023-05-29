from tkinter import *
from tkinter import font
from psutil import disk_partitions, disk_usage, virtual_memory, cpu_percent 
from tabulate import tabulate

window = Tk()
window.geometry("900x600")
window.title("CPU - RAM - DISK USAGE")


# Función para mostrar información de la CPU
def show_cpu_info():
    cpu_use = cpu_percent(interval=1)
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

data=disk_partitions(all=False)

def details(device_name):
    for i in data:
        if i.device == device_name:
            return i
        
# Function to display disk information
def disk_info(device_name):
    disk_info = {}
    try:
        usage = disk_usage(device_name)
        disk_info['Device'] = device_name
        disk_info['Total'] = f"{conversor_bytes_to_gb(usage.used + usage.free)} GB" 
        disk_info['Used'] = f"{conversor_bytes_to_gb(usage.used)} GB"
        disk_info['Free'] = f"{conversor_bytes_to_gb(usage.free)} GB"
        disk_info['Percent'] = f"{usage.percent} GB"
        
        info = details(device_name)
        if info is not None:
            disk_info.update({"Device": info.device})
            disk_info["Mount Point"] = info.mountpoint
            disk_info["FS-Type"] = info.fstype
            disk_info["Opts"] = info.opts
    except PermissionError:
        pass
    except FileNotFoundError:
        pass
    
    return disk_info

# Function that returns the disk partitions
def get_device_names():
    return [i.device for i in data] #return C:// D:// E://

def all_disk_info():
    return_all=[]
    for i in get_device_names():
        return_all.append(disk_info(i))
    return return_all



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

# Disk title
disk_title_label = Label(window, text='Disk Usage: ', font="arial 24 bold", fg='#797E1E')
disk_title_label.place(x=350,y=36)

#text area disk information
textArea=Text(window,bg="#071C1E", fg="yellow", width=85,height=6,padx=10, font=("consolas", 14))
textArea.place(x=15,y=410)

if __name__ == '__main__':
    show_cpu_info()
    show_ram_info()
    info = all_disk_info()
    _list=[i.values() for i in info]
    info_tabulated=tabulate(_list,headers=info[0].keys(),tablefmt="simple",missingval=("-"))
    textArea.insert(END,info_tabulated)
    window.mainloop()
