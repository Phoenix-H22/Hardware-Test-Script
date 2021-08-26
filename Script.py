import cv2
import time
import sys
import psutil
import platform
from datetime import datetime
from tabulate import tabulate
import win32com.client
import shutil
import netifaces
import os
import psutil
import webbrowser
from pygame import mixer
os.system('color FF')
def start():
    print("\n")
    print("="*40, "Full Hardware Test Script", "="*40)
    print("""                                                                  
   @@@@@@@@@@@@@@@@@@@@@@@@@*****************************@@@@@@@@@@@@@@@@@@@@@  
   @@@@@@@@@@@@@@@@@@@@@@@@**************************************@@@@@@@@@@@@@  
   @@@@@@@@@@@@@@@@@@@@@@@**********@*******************************/@@@@@@@@@  
   @@@@@@@@@@@@@@@@@@@@@@*********@@***********************************@@@@@@@  
   @@@@@@@@@@@@@@@@@@@@@**********@@@@@@*********************************@@@@@  
   @@@@@@@@@@@@@@@@@@@@***********/@@@@@@@@@@@@@@@@@@@@@@@@@%**************@@@  
   @@@@@@@@@@@@@@@@@@@************@@@@@@@@@@@@@@@@*****@@@@@@@@@************@@  
   @@@@@@@@@@@@@@@@@@************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/***********@  
   @@@@@@@@@@@@@@@@@************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***********  
   @@@@@@@@@@@@@@@@************/@@@@@@@@@@@@@@@@@@/***************************  
   @@@@@@@@@@@@@@@*************@@@@@@@@@@@@@@@@*******************************  
   @@@@@@@@@@@@@@*************@@@@@@@@@@@@@@@*********************************  
   @@@@@@@@@@@@@*************@@@@@@@@@@@@@@@*********************************&  
   @@@@@@@@@@@@*************@@@@@@@@@@@@@@@%****************@@@&*************@  
   @@@@@@@@@@@*************@@@@@@@@@@@@@@@@***************@@@@@@@@**********@@  
   @@@@@@@@@@*************@@@@@@@@@@@@@@@@@&**************@@@@@@@@********#@@@  
   @@@@@@@@@*************@@@@@@@@@@@@@@@@@@@***************@@@@@@@@******@@@@@  
   @@@@@@@@*************@@@@@@@@@@@@@@@@@@@@@**************@@@@@@@@****@@@@@@@  
   @@@@@@@*************@@@@@@@@@@@@@@@@@@@@@@@**************@@@@@@@/@@@@@@@@@@  
   @@@@@@*************@@@@@****************@@@@**************@@@@@@@@@@@@@@@@@  
   @@@@@*************%@@@@@@**************@@@@@@**************@@@@@@@@@@@@@@@@  
   @@@@**************@@@@@@@@***********@@@@@@@@@**************@@@@@@@@@@@@@@@  
   @@@**************@@@@@@@@@@@********@@@@@@@@@@@**************@@@@@@@@@@@@@@  
   @@**************@@@@@@@@@@@@@******@@@@@@@@@@@@@**************@@@@@@@@@@@@@  
   @**************@@@@@@@@@@@@@@@****@@@@@@@@@@@@@@@**************@@@@@@@@@@@@  
   **************@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@**************@@@@@@@@@@@
    \n

                        Made by : Abdalrhman M. Alkady

                        Check >> https://alkady.phoenix-fire.tech                                                                                                                                                                                 
    """)
def cam_test():
    print("="*40, "Camera test", "="*40)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    t_end = time.time() + 3 * 1
    while time.time() < t_end:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        
        c = cv2.waitKey(1)
        if c == 27:
            break
    time.sleep(1)
    print("Camera Is fine")
    print("="*40, "Done", "="*40)
    cv2.destroyAllWindows()
    


def sound_test():
    print("="*40, "Sound Test", "="*40)

    mixer.init()
    mixer.music.load("'test.mp3")
    mixer.music.play()
    time.sleep(3)
    print('Speakers are fine')
    
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_info():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    # Boot Time
    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def cpu_info():
    # let's print CPU information
    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def Memory_use():
    # Memory Information
    print("="*40, "RAM Information", "="*40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")

def disk_use():
    # Disk Information
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")

def net_info():
    # Network information
    print("="*40, "Network Information", "="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")

def usb_info():
    print("="*40, "USB Ports", "="*40)
    try:
        usb_list = []
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            print(usb.DeviceID)
            print(usb.description)
            usb_list.append(usb.description)

        print(usb_list)
        return usb_list
    except Exception as error:
        print('error', error)
def battery():
    print("="*40, "Battery test", "="*40)   
    stream = os.popen('powercfg /batteryreport')
    output = stream.read()
    time.sleep(3)
    url = "battery-report.html"
    input("Press Enter to open Battrey Report")
    webbrowser.open(url)

def enter_exit():
    print("="*40, "Test Done!!", "="*40)
    input("Press Enter to close")

start()
system_info()
cpu_info()
Memory_use()
disk_use()
net_info()
usb_info()
sound_test()
cam_test()
battery()
enter_exit()

