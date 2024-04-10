import time
import News as n
import weather as w
from tkinter import Label,Tk,Frame,Button
from tkcalendar import Calendar
import Gmail
import datetime
from threading import Thread
window = Tk()
#event=Event()
window.overrideredirect(True)
window.geometry("1920x1080")####"1920x1080"   "500x500"
window.config(bg="black")
window.resizable(False,False)
today = datetime.date.today()
count = 0

def Ctime():

    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    Time = Label(window, text=hour + " : " + minute + " : " + second, font=("Helvetica", 25), fg="white",
                 bg="black")
    Time.place(x=1540, y=20) ###### x=1540, y=20
    temperature = Label(window, text=w.T, font=("Helvetica", 14), fg="white", bg="black")
    temperature.place(x=20, y=20)
    Humidity = Label(window, text=w.H, font=("Helvetica", 14), fg="white", bg="black")
    Humidity.place(x=20, y=70)
    wind = Label(window, text=w.w_s, font=("Helvetica", 14), fg="white", bg="black")
    wind.place(x=20, y=120)
    weather = Label(window, text=w.W, font=("Helvetica", 14), fg="white", bg="black")
    weather.place(x=20, y=170)
    date = today.strftime("%B %d, %Y")
    weekdays = ("weekdays", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    weekday = (datetime.datetime.now().isoweekday())
    weak = str(weekdays[weekday])
    weakup = weak.upper()
    week = Label(window, text=weakup, font=("Helvetica", 18), fg="white", bg="black")
    week.place(x=1540, y=155)
    Date = Label(window, text=date, font=("Helvetica", 18), fg="white", bg="black")
    Date.place(x=1540, y=90)
    return Time
        #Time.config()
        #continue
    #print("black")
def v():
    while True:
        global c
        if c == 1:
            break
        Ctime()
        time.sleep(1)
        #a.after(1000,Ctime)
def N ():
    while True:
        global p
        if p == 1:
            break
        news()
        time.sleep(5)
        #g.after(5000,news)


def news():
    global count
    NEWS=n.main()
    #print(count)
    blk=Label(window, text="NEWS_12: Bollywood actress Parineeti Chopra getting engaged with "
                           "_AAP leader Raghav Chadha - Parineeti Chopra, Raghav Chadha engagement - Economic Times____",
              font=("Helvetica", 14), fg="black", bg="black")
    blk.place(x=10, y=900)
    NEWSS=Label(window, text=NEWS[count], font=("Helvetica", 13), fg="white", bg="black")
    NEWSS.place(x=20, y=900)  ###### x=20, y=900
    count+=1
    #NEWSS.after(5000,news)
    if count==15:
        count=0
    return NEWSS
def NR():
    name = Label(window, text='SORRY :(', font=("Helvetica", 20), fg="white", bg="black")
    name.place(x=830, y=70)
def calen():
    cal = Calendar(window, selectmode="day", date_pattern="d/m/yy", background="black", disabledbackground="black",
                   bordercolor="black",
                   headersbackground="black", normalbackground="black", foreground='white',
                   normalforeground='white', headersforeground='white', weekendbackground="black",
                   othermonthbackground="black", othermonthwebackground="black", othermonthweforeground="white"
                   , othermonthforeground="white", weekendforeground="white", selectbackground="white",
                   selectforeground="black")
    cal.place(x=1530, y=235)

def none():
    #window.config(bg="white")
    temperature = Label(window, text=w.T, font=("Helvetica", 14), fg="black", bg="black")
    temperature.place(x=20, y=20)
    Humidity = Label(window, text=w.H, font=("Helvetica", 14), fg="black", bg="black")
    Humidity.place(x=20, y=70)
    wind = Label(window, text=w.w_s, font=("Helvetica", 14), fg="black", bg="black")
    wind.place(x=20, y=120)
    weather = Label(window, text=w.W, font=("Helvetica", 14), fg="black", bg="black")
    weather.place(x=20, y=170)
    emoji = Label(window, text='\U0001F642', font=("Arial Black", 25), fg="black", bg="black")
    emoji.place(x=1080, y=58)
    emoji = Label(window, text='\U0001F642', font=("Arial Black", 25), fg="black", bg="black")
    emoji.place(x=1100, y=60)
    name = Label(window, text='HELLO  NISHANTH', font=("Helvetica", 20), fg="black", bg="black")
    name.place(x=810, y=70)
    heading = Label(window, text="MAIL", font=("Helvetica", 14),fg="black", bg="black")
    heading.place(x=150, y=490)
    week = Label(window, text="----------------------", font=("Helvetica", 18),fg="black", bg="black")
    week.place(x=1540, y=155)
    # week_1 = Label(window, text="----------------------", font=("Helvetica", 18), fg="white", bg="white")
    # week_1.place(x=990, y=150)
    Date = Label(window, text="----------------------", font=("Helvetica", 18), fg="black", bg="black")
    Date.place(x=1540, y=90)
    Time = Label(window, text="------------------------------", font=("Helvetica", 25), fg="black", bg="black")
    Time.place(x=1540, y=20)
    mail_1 = Label(window, text="-------------------------------------------------------------------------------------"
                                "-------------------------------------------------------------------"
                   , font=("Helvetica", 13), fg="black", bg="black")
    mail_1.place(x=20, y=560)
    mail_2 = Label(window, text="-------------------------------------------------------------------------------------"
                                "-------------------------------------------------------------------"
                   , font=("Helvetica", 13), fg="black", bg="black")
    mail_2.place(x=20, y=620)
    mail_3 = Label(window, text="-------------------------------------------------------------------------------------"
                                "-------------------------------------------------------------------"
                   , font=("Helvetica", 13), fg="black", bg="black")
    mail_3.place(x=20, y=680)
    mail_4 = Label(window, text="-------------------------------------------------------------------------------------"
                                "-------------------------------------------------------------------"
                   , font=("Helvetica", 13), fg="black", bg="black")
    mail_4.place(x=20, y=740)
    mail_5 = Label(window, text="-------------------------------------------------------------------------------------"
                                "-------------------------------------------------------------------"
                   , font=("Helvetica", 13), fg="black", bg="black")
    mail_5.place(x=20, y=800)
    blk = Label(window, text="NEWS_12: Bollywood actress Parineeti Chopra getting engaged with "
                             "_AAP leader Raghav Chadha - Parineeti Chopra, Raghav Chadha engagement - Economic Times____",
                font=("Helvetica", 14), fg="black", bg="black")
    blk.place(x=10, y=900)
    L=Label(window, text="----------------------------------------------", font=("Helvetica", 100), fg="black", bg="black")
    L.place(x=1530, y=235)
    #cal= Label(window, text="----------------------------------------------", font=("Helvetica", 50), fg="black",
              #bg="blue")
    #cal.place(x=1530, y=420)
def rishi():
    mail, sub = Gmail.main()
    emoji = Label(window, text='\U0001F642', font=("Arial Black", 25), fg="white", bg="black")
    emoji.place(x=1080, y=58)
    name = Label(window, text='HELLO  RISHI', font=("Helvetica", 20), fg="white", bg="black")
    name.place(x=810, y=70)
    cal = Calendar(window, selectmode="day", date_pattern="d/m/yy", background="black", disabledbackground="black",
                   bordercolor="black",
                   headersbackground="black", normalbackground="black", foreground='white',
                   normalforeground='white', headersforeground='white', weekendbackground="black",
                   othermonthbackground="black", othermonthwebackground="black", othermonthweforeground="white"
                   , othermonthforeground="white", weekendforeground="white", selectbackground="white",
                   selectforeground="black")
    cal.place(x=1530, y=235)


    ###########################################################################################
    heading = Label(window, text="MAIL", font=("Helvetica", 14), fg="white", bg="black")
    heading.place(x=150, y=490)
    mail_1 = Label(window, text=mail[0] + " : " + sub[0], font=("Helvetica", 13), fg="white", bg="black")
    mail_1.place(x=20, y=560)
    mail_2 = Label(window, text=mail[1] + " : " + sub[1], font=("Helvetica", 13), fg="white", bg="black")
    mail_2.place(x=20, y=620)
    mail_3 = Label(window, text=mail[2] + " : " + sub[2], font=("Helvetica", 13), fg="white", bg="black")
    mail_3.place(x=20, y=680)
    mail_4 = Label(window, text=mail[3] + " : " + sub[3], font=("Helvetica", 13), fg="white", bg="black")
    mail_4.place(x=20, y=740)
    mail_5 = Label(window, text=mail[4] + " : " + sub[4], font=("Helvetica", 13), fg="white", bg="black")
    mail_5.place(x=20, y=800)
    mail_6 = Label(window, text=mail[4] + " : " + sub[4]+"----------------------------------------------------------------------",
                   font=("Helvetica", 7), fg="black", bg="black")
    mail_6.place(x=20, y=860)



def nishanth():
    mail, sub = Gmail.nishanth()
    emoji = Label(window, text='\U0001F642', font=("Arial Black", 25), fg="white", bg="black")
    emoji.place(x=1080, y=58)
    name = Label(window, text='HELLO  RISHI', font=("Helvetica", 20), fg="white", bg="black")
    name.place(x=810, y=70)
    cal = Calendar(window, selectmode="day", date_pattern="d/m/yy", background="black", disabledbackground="black",
                   bordercolor="black",
                   headersbackground="black", normalbackground="black", foreground='white',
                   normalforeground='white', headersforeground='white', weekendbackground="black",
                   othermonthbackground="black", othermonthwebackground="black", othermonthweforeground="white"
                   , othermonthforeground="white", weekendforeground="white", selectbackground="white",
                   selectforeground="black")
    cal.place(x=1530, y=235)

    ###########################################################################################
    heading = Label(window, text="MAIL", font=("Helvetica", 14), fg="white", bg="black")
    heading.place(x=150, y=490)
    mail_1 = Label(window, text=mail[0] + " : " + sub[0], font=("Helvetica", 13), fg="white", bg="black")
    mail_1.place(x=20, y=560)
    mail_2 = Label(window, text=mail[1] + " : " + sub[1], font=("Helvetica", 13), fg="white", bg="black")
    mail_2.place(x=20, y=620)
    mail_3 = Label(window, text=mail[2] + " : " + sub[2], font=("Helvetica", 13), fg="white", bg="black")
    mail_3.place(x=20, y=680)
    mail_4 = Label(window, text=mail[3] + " : " + sub[3], font=("Helvetica", 13), fg="white", bg="black")
    mail_4.place(x=20, y=740)
    mail_5 = Label(window, text=mail[4] + " : " + sub[4], font=("Helvetica", 13), fg="white", bg="black")
    mail_5.place(x=20, y=800)
    mail_6 = Label(window, text=mail[4] + " : " + sub[
        4] + "----------------------------------------------------------------------",
                   font=("Helvetica", 7), fg="black", bg="black")
    mail_6.place(x=20, y=860)
