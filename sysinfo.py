#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made with <3 and License under the GNU GPLv3 




import os 
import subprocess 
import psutil
import platform
import distro
import threading
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime
from datetime import date
from colorama import init
from colorama import Fore, Back, Style
from psutil import virtual_memory

os.system("clear")

init() # spawn colorama


# get some basic system information 
user = os.getenv("USER")
home = os.getenv("HOME")
uid = os.geteuid()
system =  distro.name()
arch = platform.architecture() 
code = distro.codename()
version = distro.version()
cpucount = os.cpu_count()
threadcount = threading.active_count()
cpu_frequency = psutil.cpu_freq()
vmem = psutil.virtual_memory()

# No longer needed in the code but kept for reffrence later on 
#mem_byt = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # doesnt work on mac but apple can suck my di- big toe 
#mem_gb = mem_byt/(1024.**4)  # very sloppy way of doing this 

date = date.today() 

f = Figlet(font="cybermedium") #figlet font 

def get_size(bytes, suffix="B"):
    #Scale bytes to its proper format
        #1253656 => '1.20MB'
       #1253656678 => '1.17GB'
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# This seems to cause a hang no clue why got nothing from debugger
#proc0 = subprocess.Popen(["cat", "/etc/issue"], stdout=subprocess.PIPE, shell=True, close_fds=True)
#os_name = proc0.communicate()   
#print (f.renderText(os_name))


print(Fore.GREEN, Style.BRIGHT, "─" * 47, "Sys_Info", "─" * 47)
print(Fore.CYAN + f.renderText(" " + system + " " + code))
print("   OS Version: " + version)
print("")
print (Fore.GREEN , "─" * 105)
#print(Style.RESET_ALL) # dont need this anymore
print("""
""")
print('[ User Info ]'.center(105, '─'))
print(
  """
  """ +
  Back.GREEN + Fore.BLACK + Style.BRIGHT + "Date:" + Style.RESET_ALL + Fore.GREEN ,  date ,  "     " + Back.GREEN + Fore.BLACK + Style.BRIGHT + "User:" + Style.RESET_ALL + Fore.GREEN , user , "      "
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Home:" + Style.RESET_ALL + Fore.GREEN , home , "   " 
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Uid:" + Style.RESET_ALL + Fore.GREEN , uid , " "

 
 
)
print("""
""")
print(Style.BRIGHT)
print('[ System Info ]'.center(105, '─'))
print(
  """
  """ +
  Back.GREEN + Fore.BLACK + Style.BRIGHT + "CPU Count:" + Style.RESET_ALL + Fore.GREEN ,  cpucount ,  "     " + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Running Threads:" + Style.RESET_ALL + Fore.GREEN , threadcount , "      "
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "CPU freq:" + Style.RESET_ALL + Fore.GREEN , cpu_frequency.current , "MHZ ", "   " 
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Arch:" + Style.RESET_ALL + Fore.GREEN , arch , " " + """
 
  """ +
 Back.GREEN + Fore.BLACK + Style.BRIGHT + "MEM Total:" + Style.RESET_ALL + Fore.GREEN , get_size(vmem.total)  ,  "          " + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Used:" + Style.RESET_ALL + Fore.GREEN , get_size(vmem.percent), "   "
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Available:" + Style.RESET_ALL + Fore.GREEN , get_size(vmem.total),"      " 
 + Back.GREEN + Fore.BLACK + Style.BRIGHT + "Free:" + Style.RESET_ALL + Fore.GREEN , get_size(vmem.free) , " "
 )
 # needed one more line of code to hit 100 wich is where i told myself i will stop for the night
