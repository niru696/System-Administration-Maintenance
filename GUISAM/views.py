from __future__ import unicode_literals

import subprocess
import os

import pandas as pd
import matplotlib.pyplot as plt

import Tkinter as tk
#from Tkinter import filedialog
import tkFileDialog as filedialog
from tkFileDialog import *


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return render(request, 'GUISAM/index.html')

def assignment3(request):
    return render(request, 'GUISAM/assignment3.html')

def assignment4(request):
    return render(request, 'GUISAM/assignment4.html')

def assignment5(request):
    return render(request, 'GUISAM/assignment5.html')

def assignment6(request):
    return render(request, 'GUISAM/assignment6.html')

def assignment7(request):
    return render(request, 'GUISAM/assignment7.html')



#def grub(request):
    #command = "gedit /etc/default/grub".split(" ")
    #subprocess.Popen(command, stdout=subprocess.PIPE)
    #return redirect('GUISAM:index')

def grub_order(request):
    value = request.POST.get('number')
    if value not in ['0','1','2']:
        messages.error(request, 'Enter a value among 0, 1 or 2')
    else:
        change_default="sudo -S sed -i s/GRUB_DEFAULT=.*/GRUB_DEFAULT={}/ /etc/default/grub".format(value)

        os.system(change_default)

    return redirect('GUISAM:index')

def grub_timeout(request):
    value = request.POST.get("timeout")
    if value:
        timeout="sudo -S sed -i s/GRUB_TIMEOUT=.*/GRUB_TIMEOUT={}/ /etc/default/grub".format(value)
        # print(timeout)
        os.system(timeout)
        os.system("cat /etc/default/grub")
    else:
        messages.error(request, 'enter time!')
    return redirect('GUISAM:index')

def change_screen(request):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    splash_path = "sudo cp {} /boot/grub".format(file_path)
  
    os.system(splash_path)
        
    return redirect('GUISAM:index')

def shutdown(request):
    value = request.POST.get('timeout')
    command = "shutdown -h +"+value
    print(command)
    # subprocess.Popen(command, stdout=subprocess.PIPE)
    os.system(command)
    return redirect('GUISAM:index')

def cancel_shutdown(request):
    command = "shutdown -c".split(" ")
    subprocess.Popen(command, stdout=subprocess.PIPE)
    return redirect('GUISAM:index')

def logout(request):
    subprocess.call('gnome-session-quit')
    return redirect('GUISAM:index')

def restart(request):
    value = request.POST.get('timeout')
    command = 'shutdown -r +'+value
    # subprocess.Popen(['reboot'], stdout=subprocess.PIPE)
    os.system(command)
    return redirect('GUISAM:index')

def force_restart(request):
    os.system('sudo shutdown -r now')
    return redirect('GUISAM:index')

def Add_user(request):
    value = request.POST.get("timeout")
    
    value = "sudo useradd "+ value
    print(value)
    userid = request.POST.get("timeout")
    #print (userid)
    userid = "sudo useradd -u "+ userid +" "+ value
    #print (userid)
    
    login_shell = request.POST.get("timeout")
    login_shell = "sudo useradd -s "+login_shell+" "+ value
    os.system(value)
    os.system(userid)
    os.system(login_shell)
    #print(login_shell)
    os.system('less >5 /etc/passwd')
    return redirect("GUISAM:index")

def delete_user(request):
    user_name = request.POST.get("timeout")
    #print(user_name)
    user_name = "sudo userdel "+ user_name
    os.system(user_name)
    os.system('less  >5 /etc/passwd')
    return redirect('GUISAM:index')

def Add_group(request):
    group_name = request.POST.get("timeout")
    print(group_name)
    group_name = "sudo groupadd "+ group_name
    groupid = request.POST.get("timeout")
   # print (groupid)
    groupid = "sudo groupadd -g "+ groupid +" "+ group_name
   # print (groupid)
    os.system(group_name)
    os.system(groupid)
    os.system('less >5 /etc/group')
    return redirect("GUISAM:index")

def delete_group(request):
    group_name = request.POST.get("timeout")
    #print(user_name)
    group_name = "sudo groupdel "+ group_name
    os.system(group_name)
    os.system('less >5 /etc/passwd')
    return redirect("GUISAM:index")

def add_users_list(request):
    file_path = os.path.dirname(os.path.dirname(__file__))
    users_list = open(os.path.join(file_path, 'batch.txt'), 'r')
    print(users_list)
    users_arr = []

    for i in users_list.readlines():
        temp = i.split(" ")
        cmd_1 = "sudo useradd -m {} -s {}".format(temp[0], temp[2])
        cmd_2 = "{}:{}| sudo chpasswd".format(temp[0], temp[1])
        # cmd = "sudo deluser --remove-home {}".format(temp[0])
        # os.system(cmd)
        os.system(cmd_1)
        os.system(cmd_2)
    return redirect("GUISAM:index")

#ass5

def memory_usage(request):
   #os.system(cmd)
   os.system("for USER in $(ps haux | awk '{print $1}' | sort -u) ; do  ps haux | awk -v user=$USER '$1 ~ user { sum += $4} END { print user, sum; }' >> memory.csv  ; done")
   file_path=os.path.dirname(os.path.dirname(__file__))
   csv_path = os.path.join(file_path, 'memory.csv')
   df =  pd.read_csv(csv_path)
   print(df)
   df2 = pd.DataFrame(columns=['users','usage'])
   split = df.ix[:,0].str.split(" ")
   df2.ix[:,0] = split.str[0]
   df2.ix[:,1] = split.str[-1]
   user_data = df2.ix[:, 0]
   #print(user_data)
   usage_data = df2.ix[:, 1]
   #print(usage_data)
   plt.pie(usage_data, labels=user_data,autopct='%1.1f%%', startangle=140)
   plt.show()
   os.system("sudo rm memory.csv")
   return redirect('GUISAM:index')


def CPU_usage(request):
   os.system("for USER in $(ps haux | awk '{print $1}' | sort -u) ; do  ps haux | awk -v user=$USER '$1 ~ user { sum += $3} END { print user, sum; }' >> cpu.csv  ; done")
   file_path=os.path.dirname(os.path.dirname(__file__))
   csv_path = os.path.join(file_path, 'cpu.csv')
   df =  pd.read_csv('cpu.csv')
   print(df)
   df2 = pd.DataFrame(columns=['users','usage'])
   split = df.ix[:,0].str.split(" ")
   df2.ix[:,0] = split.str[0]
   df2.ix[:,1] = split.str[-1]
   user_data = df2.ix[:, 0]
   #print(user_data)
   usage_data = df2.ix[:, 1]
   #print(usage_data)
   plt.pie(usage_data, labels=user_data,autopct='%1.1f%%', startangle=140)
   plt.show()
   os.system("sudo rm cpu.csv")
   return redirect('GUISAM:index')

def plot_data(data):
    dat_list = {}

    for i in data.readlines():
        split_list = i.split()
        dat_list[split_list[0]] = split_list[1]

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(dat_list.values(), labels=dat_list.keys(), colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

def renice(request):
    top_list = "ps -eo ni,pid --sort=-pcpu | head -n 6 > nice.txt"
    os.system(top_list)

    file_path = os.path.dirname(os.path.dirname(__file__))
    top_list = open(os.path.join(file_path, 'nice.txt'), 'r')
    dat_arr = []

    for i in top_list.readlines():
        dat_list = {}
        split_list = i.split()
        dat_list["ni"] = split_list[0]
        dat_list["pid"] = split_list[1]
        os.system("sudo renice 4 -p " + str(split_list[1]) + " >> renice.output.txt")
        dat_arr.append(dat_list)
    print(dat_arr)

    top_list_renice = "ps -eo ni,pid --sort=-pcpu | head -n 6 > renice.txt"
    os.system(top_list_renice)

    return redirect('GUISAM:index')

#Assign6

def set_perm(request):
    value = request.POST.get("number")
    if value:
        print(value)
        filename = check_value(request, value)
        print(filename)
        cmd = "sudo chmod " + str(value) + " " + filename
        print(cmd)
        os.system(cmd)

    else:
        messages.error(request, 'Enter a Number')
    return redirect("GUISAM:index")    


def umask_cal(request):
    value = request.POST.get("number")
    if value:
        filename = check_value(request, value)
        print(filename)
        pass
    else:
        messages.error(request, 'Enter a Number')
    print(value)
    return redirect("GUISAM:index")

def acl_user_perm(request):
    name = request.POST.get("name")
    value = request.POST.get("number")
    if value:
        file_name = check_acl_value(request, value)
        # filename = check_value(value)
        cmd = "sudo -S setfacl -m u:{}:{} {}".format(name, value, file_name)
        print(cmd)
        os.system(cmd)
    else:
        messages.error(request, 'Enter a Number')
    # print(value)
    return redirect("GUISAM:index")

def acl_group_perm(request):
    name = request.POST.get("name")
    value = request.POST.get("number")
    if value:
        file_name = check_acl_value(request, value)
        # filename = check_value(value)
        cmd = "sudo -S setfacl -m g:{}:{} {}".format(name, value, file_name)
        # print(cmd)
        os.system(cmd)
    else:
        messages.error(request, 'Enter a Number')
    print(value)
    return redirect("GUISAM:index")

def check_acl_value(request, value):
    root = tk.Tk()
    root.withdraw()
    file_name = askopenfilename(parent=root)

    if not file_name:
        messages.error(request, 'Please select a file')
        return redirect("GUISAM:index")

    if len(value) not in range(1,4):
        messages.error(request, 'Length should be max. 3 characters long')
        return redirect("GUISAM:index")
    return file_name

def check_value(request, value):
    root = tk.Tk()
    root.withdraw()
    file_name = askopenfilename(parent=root)

    if not file_name:
        messages.error(request, 'Please select a file')
        return redirect("GUISAM:index")

    if len(value) != 3:
        messages.error(request, 'Please enter a 3 digit number')
        return redirect("GUISAM:index")
    value_int = int(value)
    i=1
    if value != '000':
        while value_int > 0:
            temp = value_int%10
            print(temp)
            value_int= value_int/10
            if temp not in range(0,8):
                messages.error(request, 'value should be in range 0 - 7')
                return redirect("GUISAM:index")
            temp_new = 6-temp
            newNumber = temp_new * i
            i*=10
    root.destroy()
    print(newNumber)
    return newNumber


# Lab 7

def rsyslog(request):
    return render(request, 'GUISAM/rsyslog.html')


def log_rotate(request):
    return render(request, 'GUISAM/log-rotate.html')


def rsyslog_form(request):
    facility = request.POST.get("facility")
    level = request.POST.get("level")
    symbol_1 = ''
    symbol_2 = ''
    print(level)
    
    if request.POST.get("symbol_1"):
        print(request.POST.get("symbol_1"))

    if request.POST.get("symbol_2"):
        pass
    

    root = tk.Tk()
    root.withdraw()
    file_name = askopenfilename(parent=root)
    cmd2  = "sudo chmod 777 /etc/rsyslog.d/50-default.conf"
    subprocess.Popen(cmd2.split())
    cmd = "echo '{}.{}{}{}    {}' >> /etc/rsyslog.d/50-default.conf".format(facility, symbol_1, symbol_2, level, file_name)
    os.system(cmd)
    root.destroy()
    return redirect("GUISAM:index")


def log_rotate_form(request):
    symbol_1 = request.POST.gett("symbol_1")
    symbol_2 = request.POST.get("symbol_2")
    # facility = request.GET['facility']
    # level = request.GET['level']
    # symbol_1 = request.GET['symbol_1']
    # symbol_2 = request.GET['symbol_2']
    # root = Tk()
    # root.withdraw()
    # file_name = askopenfilename(parent=root)

    # root.destroy()
    return HttpResponse("Successful!")

