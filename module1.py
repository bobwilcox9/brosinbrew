# module1 will be used to develop the gui.
# I will use it to calculate IBU's

# Utilization equations come from http://www.howtobrew.com/section1/chapter5-5.html
# Utilization = f(G) x f(T)
# G is the boil Gravity and T is the time a hop addition is in boil
# f(G) = 1.65 * 0.000125^(Gb - 1)
# f(T) = [1 - e^(-0.04 x T)] / 4.15

from Tkinter import *

fields = 'Addition', 'Hops', 'Weight (oz)', '% Alpha Acids', 'Time (min)', 'Gravity of Boil', 'Boil Volume (gal)'
additions = '1st', '2nd', '3rd', '4th', '5th', '6th'

############################
# Draw input grid
ry=7
rx=7
rows = []
for rr in range(ry):
    cols = []
    for cc in range(rx):
        if rr == 0:
            lc = Label(text=fields[cc], anchor='w')
            lc.grid(row=rr, column=cc)
        else:
            if cc == 0:
                lr = Label(text=additions[rr-1], anchor='w')
                lr.grid(row=rr, column=cc)
            else:
                e = Entry()
                e.grid(row=rr, column=cc)
#from Tkinter import *
     
rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)
     
def onPress():
    for row in rows:
        for col in row:
            print col.get(),
        print
     
Button(text='Fetch', command=onPress).grid()
mainloop()                e.insert(END, '%d,%d' % (rr, cc))
                cols.append(e)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print col.get(),
        print

Button(text='Submit', command=onPress).grid()
mainloop()
