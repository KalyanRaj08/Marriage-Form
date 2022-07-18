from tkinter import *
import sqlite3
import time as times
import math
from datetime import date, time

db = sqlite3.connect('Marriageinfo.sqlite')
dbh = db.cursor()

dbh.executescript('''
CREATE TABLE IF NOT EXISTS info(
sno INTEGER PRIMARY KEY,
name TEXT NOT NULL,
dob date,
tob time,
study TEXT,
job TEXT,
salary REAL,
father TEXT,
mother TEXT,
city TEXT,
div TEXT,
age INTEGER,
phone INTEGER NOT NULL,
photo TEXT);
''')

ch=0
def closet1():
    t1.destroy()


def inp1():
    try:
        dbh.execute('SELECT * FROM info')
        r = dbh.fetchall()
        na = na1.get()
        d = date.fromisoformat(d1.get())
        ti = time.fromisoformat(ti1.get())
        st = st1.get()
        jo = jo1.get()
        sal = sal1.get()
        fa = fa1.get()
        mo = mo1.get()
        ci = ci1.get()
        di = di1.get()
        today = date.today()
        a = today.year - d.year
        ph = int(ph1.get())
        li = li1.get()
        for i in r:
            if (str(na).lower() == str(i[1]).lower()) and (str(fa).lower() == str(i[7]).lower()) and ((int(ph) == int(i[12])) or (str(li) == str(i[13])) and (len(str(mo)) != 10)):
                label = Label(t1, text="THIS USER ALREADY EXISTS!!!", bg="white",
                              fg="black").grid(row=100, column=0)
                raise()
        dbh.execute(
            "INSERT INTO info(name, dob, tob, study, job, salary, father, mother, city, div, age, phone, photo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (na, d.strftime('%Y-%m-%d'), ti.strftime('%H:%M:%S'), st, jo, sal, fa, mo, ci, di, a, ph, li))
        db.commit()
        label = Label(t1, text="DETAILS UPLOADED SUCCESSFULLY!!!", bg="white",
                      fg="black").grid(row=100, column=0)
    except:
        label = Label(t1, text="WRONG INPUT!! COULDN'T UPLOAD!! TRY AGAIN.", bg="white",
                      fg="black").grid(row=101, column=0)


def inp():
    global t1
    t1 = Tk()
    t1.geometry("800x450")
    t1.title("MARRIAGE INFO DATABASE")
    t1.configure(bg="YELLOW")
    label = Label(t1, text="பெயர் : ", bg="white",
                  fg="black").grid(row=1, column=0)
    global na1
    na1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    na1.grid(row=1,column=1,columnspan=25)

    label = Label(t1, text="பிறந்த தேதி(YYYY-MM-DD) : ", bg="white",
                  fg="black").grid(row=2, column=0)
    global d1
    d1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    d1.grid(row=2, column=1, columnspan=25)

    label = Label(t1, text="பிறந்த நேரம்(HH:MM:SS) : ", bg="white",
                  fg="black").grid(row=3, column=0)
    global ti1
    ti1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    ti1.grid(row=3, column=1, columnspan=25)

    label = Label(t1, text="கல்வி : ", bg="white",
                  fg="black").grid(row=4, column=0)
    global st1
    st1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    st1.grid(row=4, column=1, columnspan=25)

    label = Label(t1, text="வேலை : ", bg="white",
                  fg="black").grid(row=5, column=0)
    global jo1
    jo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    jo1.grid(row=5, column=1, columnspan=25)

    label = Label(t1, text="சம்பளம் : ", bg="white",
                  fg="black").grid(row=6, column=0)
    global sal1
    sal1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    sal1.grid(row=6, column=1, columnspan=25)

    label = Label(t1, text="தந்தை : ", bg="white",
                  fg="black").grid(row=7, column=0)
    global fa1
    fa1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    fa1.grid(row=7, column=1, columnspan=25)

    label = Label(t1, text="தாய் : ", bg="white",
                  fg="black").grid(row=8, column=0)
    global mo1
    mo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    mo1.grid(row=8, column=1, columnspan=25)

    label = Label(t1, text="ஊர் : ", bg="white",
                  fg="black").grid(row=9, column=0)
    global ci1
    ci1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    ci1.grid(row=9, column=1, columnspan=25)

    label = Label(t1, text="பிரிவு : ", bg="white",
                  fg="black").grid(row=10, column=0)
    global di1
    di1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    di1.grid(row=10, column=1, columnspan=25)

    label = Label(t1, text="அலைபேசி : ", bg="white",
                  fg="black").grid(row=11, column=0)
    global ph1
    ph1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    ph1.grid(row=11, column=1, columnspan=25)

    label = Label(t1, text="ஜாதகம் : ", bg="white",
                  fg="black").grid(row=12, column=0)
    global li1
    li1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    li1.grid(row=12, column=1, columnspan=25)

    button = Button(t1, text="SUBMIT", padx=20, width=1, bg="red", command=lambda: inp1()).grid(column=0, row=13,columnspan=75)
    button = Button(t1, text="CLOSE", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0, row=14,columnspan=75)
    t1.mainloop()


def out():
    dbh.execute('SELECT * FROM info')
    l = dbh.fetchall()
    c=0
    for i in l:
        c = c + 1
    k = 0
    for i in l:
        global t1
        t1 = Tk()
        t1.geometry("800x450")
        t1.title("MARRIAGE INFO DATABASE")
        t1.configure(bg="YELLOW")
        label = Label(t1, text="பதிவு என் : ", bg="white",
                      fg="black").grid(row=1, column=0)
        na1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        na1.grid(row=1, column=1, columnspan=25)
        na1.insert(0,str(i[0]))

        label = Label(t1, text="பெயர் : ", bg="white",
                      fg="black").grid(row=2, column=0)
        d1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        d1.grid(row=2, column=1, columnspan=25)
        d1.insert(0,str(i[1]))

        label = Label(t1, text="பிறந்த தேதி : ", bg="white",
                      fg="black").grid(row=3, column=0)
        ti1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        ti1.grid(row=3, column=1, columnspan=25)
        ti1.insert(0,str(i[2]))

        label = Label(t1, text="பிறந்த நேரம் : ", bg="white",
                      fg="black").grid(row=4, column=0)
        st2 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        st2.grid(row=4, column=1, columnspan=25)
        st2.insert(0,str(i[3]))

        label = Label(t1, text="கல்வி : ", bg="white",
                      fg="black").grid(row=5, column=0)
        st1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        st1.grid(row=5, column=1, columnspan=25)
        st1.insert(0,str(i[4]))

        label = Label(t1, text="வேலை : ", bg="white",
                      fg="black").grid(row=6, column=0)
        jo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        jo1.grid(row=6, column=1, columnspan=25)
        jo1.insert(0,str(i[5]))

        label = Label(t1, text="சம்பளம் : ", bg="white",
                      fg="black").grid(row=7, column=0)
        sal1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        sal1.grid(row=7, column=1, columnspan=25)
        sal1.insert(0,str(i[6]))

        label = Label(t1, text="தந்தை : ", bg="white",
                      fg="black").grid(row=8, column=0)
        fa1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        fa1.grid(row=8, column=1, columnspan=25)
        fa1.insert(0,str(i[7]))

        label = Label(t1, text="தாய் : ", bg="white",
                      fg="black").grid(row=9, column=0)
        mo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        mo1.grid(row=9, column=1, columnspan=25)
        mo1.insert(0,str(i[8]))

        label = Label(t1, text="ஊர் : ", bg="white",
                      fg="black").grid(row=10, column=0)
        ci1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        ci1.grid(row=10, column=1, columnspan=25)
        ci1.insert(0,str(i[9]))

        label = Label(t1, text="பிரிவு : ", bg="white",
                      fg="black").grid(row=11, column=0)
        di1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        di1.grid(row=11, column=1, columnspan=25)
        di1.insert(0,str(i[10]))

        label = Label(t1, text="வயது : ", bg="white",
                      fg="black").grid(row=12, column=0)
        ph2 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        ph2.grid(row=12, column=1, columnspan=25)
        ph2.insert(0,str(i[11]))

        label = Label(t1, text="அலைபேசி : ", bg="white",
                      fg="black").grid(row=12, column=0)
        ph1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
        ph1.grid(row=12, column=1, columnspan=25)
        ph1.insert(0,str(i[12]))
        if k + 1 < c:
            button = Button(t1, text="NEXT", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0,
                                                                                                         row=13,
                                                                                                         columnspan=75)
        else:
            button = Button(t1, text="EXIT", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0,
                                                                                                         row=13,
                                                                                                         columnspan=75)

        label = Label(t1, text=str(k + 1) + "/" + str(c), bg="white",
                      fg="black").grid(row=14, column=0, columnspan=75)
        k = k + 1
        t1.mainloop()


def search1():
    try:
        s=s1.get()
        dbh.execute('SELECT * FROM info')
        r = dbh.fetchall()
        c = 0
        for i in r:
            if i[1].lower() == s.lower():
                c = c + 1
        if c == 0:
            raise ()
        k=0
        global t1
        t1.destroy()
        for i in r:
            if i[1].lower() == s.lower():
                t1 = Tk()
                t1.geometry("800x450")
                t1.title("MARRIAGE INFO DATABASE")
                t1.configure(bg="YELLOW")
                label = Label(t1, text="பதிவு என் : ", bg="white",
                              fg="black").grid(row=1, column=0)
                na1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                na1.grid(row=1, column=1, columnspan=25)
                na1.insert(0, str(i[0]))

                label = Label(t1, text="பெயர் : ", bg="white",
                              fg="black").grid(row=2, column=0)
                d1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                d1.grid(row=2, column=1, columnspan=25)
                d1.insert(0, str(i[1]))

                label = Label(t1, text="பிறந்த தேதி : ", bg="white",
                              fg="black").grid(row=3, column=0)
                ti1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                ti1.grid(row=3, column=1, columnspan=25)
                ti1.insert(0, str(i[2]))

                label = Label(t1, text="பிறந்த நேரம் : ", bg="white",
                              fg="black").grid(row=4, column=0)
                st2 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                st2.grid(row=4, column=1, columnspan=25)
                st2.insert(0, str(i[3]))

                label = Label(t1, text="கல்வி : ", bg="white",
                              fg="black").grid(row=5, column=0)
                st1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                st1.grid(row=5, column=1, columnspan=25)
                st1.insert(0, str(i[4]))

                label = Label(t1, text="வேலை : ", bg="white",
                              fg="black").grid(row=6, column=0)
                jo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                jo1.grid(row=6, column=1, columnspan=25)
                jo1.insert(0, str(i[5]))

                label = Label(t1, text="சம்பளம் : ", bg="white",
                              fg="black").grid(row=7, column=0)
                sal1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                sal1.grid(row=7, column=1, columnspan=25)
                sal1.insert(0, str(i[6]))

                label = Label(t1, text="தந்தை : ", bg="white",
                              fg="black").grid(row=8, column=0)
                fa1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                fa1.grid(row=8, column=1, columnspan=25)
                fa1.insert(0, str(i[7]))

                label = Label(t1, text="தாய் : ", bg="white",
                              fg="black").grid(row=9, column=0)
                mo1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                mo1.grid(row=9, column=1, columnspan=25)
                mo1.insert(0, str(i[8]))

                label = Label(t1, text="ஊர் : ", bg="white",
                              fg="black").grid(row=10, column=0)
                ci1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                ci1.grid(row=10, column=1, columnspan=25)
                ci1.insert(0, str(i[9]))

                label = Label(t1, text="பிரிவு : ", bg="white",
                              fg="black").grid(row=11, column=0)
                di1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                di1.grid(row=11, column=1, columnspan=25)
                di1.insert(0, str(i[10]))

                label = Label(t1, text="வயது : ", bg="white",
                              fg="black").grid(row=12, column=0)
                ph2 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                ph2.grid(row=12, column=1, columnspan=25)
                ph2.insert(0, str(i[11]))

                label = Label(t1, text="அலைபேசி : ", bg="white",
                              fg="black").grid(row=12, column=0)
                ph1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
                ph1.grid(row=12, column=1, columnspan=25)
                ph1.insert(0, str(i[12]))
                if k+1 < c:
                    button = Button(t1, text="NEXT", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0,
                                                                                                                 row=13,
                                                                                                              columnspan=75)
                else:
                    button = Button(t1, text="EXIT", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0,
                                                                                                                 row=13,
                                                                                                                 columnspan=75)

                label = Label(t1, text=str(k + 1) + "/" + str(c), bg="white",
                              fg="black").grid(row=14, column=0, columnspan=75)
                k = k + 1

    except:
        label = Label(t1, text='No one exist in that name!!!', bg="white",fg="black").grid(row=15, column=0)
        button = Button(t1, text="EXIT", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0,
                                                                                                     row=15,
                                                                                                     columnspan=75)
    t1.mainloop()


def search():
    global t1
    t1 = Tk()
    t1.geometry("800x450")
    t1.title("MARRIAGE INFO DATABASE")
    t1.configure(bg="YELLOW")
    label = Label(t1, text='Enter the பெயர் to be searched: ', bg="white",
                  fg="black").grid(row=0, column=0)
    global s1
    s1 = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    s1.grid(row=0, column=1, columnspan=25)
    button = Button(t1, text="SEARCH", padx=20, width=1, bg="red", command=lambda : search1()).grid(column=0, row=14,columnspan=75)
    t1.mainloop()

def deleted1():
    try:
        d2=d.get()
        dbh.execute('SELECT * FROM info WHERE sno=?', (d2,))
        check = dbh.fetchone()[0]
        dbh.execute('DELETE FROM info WHERE sno=?', (d2,))
        db.commit()
        label = Label(t1, text='DELETED SUCCESSFULLY!!', bg="white",
                      fg="black").grid(row=12, column=0)
    except:
        label = Label(t1, text='ERROR DELETING! ' + d.get() + ' DOESNT EXISTS!!', bg="white",
                      fg="black").grid(row=12, column=0)



def deleted():
    global t1
    t1 = Tk()
    t1.geometry("800x450")
    t1.title("MARRIAGE INFO DATABASE")
    t1.configure(bg="YELLOW")
    label = Label(t1, text='Enter the பதிவு என் to be deleted: ', bg="white",
                      fg="black").grid(row=1, column=0)
    global d
    d = Entry(t1, width=50, borderwidth=5, bg="white", fg="black")
    d.grid(row=1, column=1, columnspan=25)
    button = Button(t1, text="DONE", padx=20, width=1, bg="red", command=lambda: deleted1()).grid(column=0, row=2, columnspan=75)
    button = Button(t1, text="CLOSE", padx=20, width=1, bg="red", command=lambda: closet1()).grid(column=0, row=3, columnspan=75)
    t1.mainloop()

def submit():
    global ch
    ch = fill.get()
    try:
        ch = int(ch)
        if ch == 1:
            t.destroy()
            inp()
        elif ch == 2:
            t.destroy()
            search()
        elif ch == 3:
            t.destroy()
            deleted()
        elif ch == 4:
            t.destroy()
            out()
        elif ch == 5:
            label = Label(t, text="TERMINATED!!", bg="white",
                          fg="black").grid(row=10, column=0)
            t.destroy()

        else:
            label = Label(t, text="INVALID OPTION!!", bg="white",
                          fg="black").grid(row=10, column=0)
    except:
        label = Label(t, text="INVALID OPTION!!", bg="white",
                      fg="black").grid(row=10, column=0)


while ch != 5 :
    t = Tk()
    t.geometry("800x450")
    t.title("MARRIAGE INFO DATABASE")
    t.configure(bg="YELLOW")
    la = Label(t, borderwidth=5, text="MENU", pady=2, padx=2, bg="white",fg="black").grid(row=0, column=0, columnspan=50)
    label = Label(t, text="1.UPLOAD NEW மருமகன்/மருமகள்", bg="white",
                  fg="black").grid(row=1, column=0)
    label = Label(t, text="2.SEARCH EXISTING மருமகன்/மருமகள்", bg="white",
                  fg="black").grid(row=2, column=0)
    label = Label(t, text="3.DELETE EXISTING மருமகன்/மருமகள்", bg="white",
                  fg="black").grid(row=3, column=0)
    label = Label(t, text="4.SEE ALL மருமகன்/மருமகள்", bg="white",
                  fg="black").grid(row=4, column=0)
    label = Label(t, text="5.EXIT", bg="white",
                  fg="black").grid(row=5, column=0)
    label = Label(t, text="ENTER YOUR CHOICE : ", bg="white",
                  fg="black").grid(row=6, column=0)
    fill = Entry(t,width=50,borderwidth=5,bg="white",fg="black")
    fill.grid(row=6,column=1,columnspan=25)
    button = Button(t,text="SUBMIT",padx=20,width=1,bg="red",command=lambda : submit()).grid(column=0,row=7,columnspan=75)

    t.mainloop()
