from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_h.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_h.after(200,date_time)
#root
clock = Tk()
clock.title('......Digital Clock......')
clock.geometry("700x350")
clock.config(bg='#1C1C1C')
clock.resizable(False,False)
#creating hour
lab_h = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_h.place(x=35,y=40)
lab_h_txt = Label(text='::',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_h_txt.place(x=135,y=35)
#creating minutes
lab_min = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_min.place(x=200,y=40)
lab_min_txt = Label(text='::',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_min_txt.place(x=300,y=35)
#creating second
lab_sec = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_sec.place(x=360,y=40,)
lab_sec_txt = Label(text='::',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_sec_txt.place(x=450,y=35)
#creating am / pm
lab_am = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_am.place(x=510,y=40)
#creating current date
lab_date = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_date.place(x=35,y=160)
lab_date_txt = Label(text='/',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_date_txt.place(x=145,y=160)
#creating month
lab_month = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_month.place(x=200,y=160)
lab_month_txt = Label(text='/',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_month_txt.place(x=315,y=160)
# creating year
lab_year = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_year.place(x=360,y=160)
lab_year_txt = Label(text='/',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_year_txt.place(x=470,y=160)
# creating day
lab_day = Label(text='00',font=('Arial',60,'bold'),bg='#1C1C1C',fg ='#690C6E')
lab_day.place(x=510,y=160)
# calling the main function
date_time()
clock.mainloop()