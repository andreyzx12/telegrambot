import wmi
import psutil


computer = wmi.WMI()


def proc_load():
    try:
        for pr in computer.Win32_Processor():
            return pr.LoadPercentage
    except:
        print("CPU Error")
        return 0


def ram_size():
    try:
        return psutil.virtual_memory().total, psutil.virtual_memory().used, psutil.virtual_memory().percent
    except:
        return 0, 0, 0


def gpu_name():
    try:
        for gp in computer.Win32_VideoController():
            name = gp.Name
            status = gp.Status
    except:
        status = "Error"
    return name, status
