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
input = []
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
                e.insert(END, '%d' % ((rx-1)*(rr-1)+cc))
                cols.append(e)
    rows.append(cols)

############################
# Define functions

# def onPress():
#     for row in rows:
#         for col in row:
#             print col.get(),
#         print

def submit_output():
    input = []
    # read data. Increments left to right
    for row in rows:
        for col in row:
          input.append(col.get())
    # manipulate data
    output.config(text=input[0])

############################
# Arrange buttons and output

output = Label()
output.grid(row=8, column=2)
#Button(text='Submit', command=onPress).grid(row=8, column=0)
Button(text='Submit', command=submit_output).grid(row=8, column=0)
Button(text="Quit", command=quit).grid(row=8, column=1)

mainloop()
