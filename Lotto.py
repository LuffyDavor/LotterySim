import tkinter as tk
import Functions
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


def numberOfBets():
    x_right_entries = 50
    for i in range(1, 7):
        if x.get() == 0:
            window.geometry("380x720")
            lblWelcome.place(x=80, y=20)
            lblWarning.place_forget()
            userNumbers[i].place(x=x_right_entries, y=150, height=30, width=30)
            userNumbersBet2[i].place_forget()
            userNumbersBet3[i].place_forget()
            userNumbersBet4[i].place_forget()
            x_right_entries += 50
            for j in range(1, 46):
                lbl2[j].place_forget()
                lbl3[j].place_forget()
                lbl4[j].place_forget()
        elif x.get() == 1:
            window.geometry("720x720")
            lblWelcome.place(x=260, y=20)
            lblWarning.place_forget()
            lblTipp[2].place(x=395, y=120)
            userNumbers[i].place(x=x_right_entries, y=150, height=30, width=30)
            userNumbersBet2[i].place(x=350+x_right_entries, y=150, height=30, width=30)
            userNumbersBet3[i].place_forget()
            userNumbersBet4[i].place_forget()
            x_right_entries += 50
            for j in range(1, 46):
                lbl3[j].place_forget()
                lbl4[j].place_forget()
        elif x.get() == 2:
            window.geometry("1080x720")
            lblWelcome.place(x=440, y=20)
            lblWarning.place_forget()
            lblTipp[2].place(x=395, y=120)
            lblTipp[3].place(x=745, y=120)
            userNumbers[i].place(x=x_right_entries, y=150, height=30, width=30)
            userNumbersBet2[i].place(x=350+x_right_entries, y=150, height=30, width=30)
            userNumbersBet3[i].place(x=700+x_right_entries, y=150, height=30, width=30)
            userNumbersBet4[i].place_forget()
            x_right_entries += 50
            for j in range(1, 46):
                lbl4[j].place_forget()
        elif x.get() == 3:
            window.geometry("1440x720")
            lblWelcome.place(x=605, y=20)
            lblWarning.place_forget()
            lblTipp[2].place(x=395, y=120)
            lblTipp[3].place(x=745, y=120)
            lblTipp[4].place(x=1095, y=120)
            userNumbers[i].place(x=x_right_entries, y=150, height=30, width=30)
            userNumbersBet2[i].place(x=350+x_right_entries, y=150, height=30, width=30)
            userNumbersBet3[i].place(x=700+x_right_entries, y=150, height=30, width=30)
            userNumbersBet4[i].place(x=1050+x_right_entries, y=150, height=30, width=30)
            x_right_entries += 50


def resetColor():
    for i in range(1, 46):
        lbl[i].config(bg='#f0f0f0')
        lbl2[i].config(bg='#f0f0f0')
        lbl3[i].config(bg='#f0f0f0')
        lbl4[i].config(bg='#f0f0f0')


def clearResults():
    lblWinningNumbers.place_forget()
    for i in range(1, 46):
        lbl[i].place_forget()
        lbl2[i].place_forget()
        lbl3[i].place_forget()
        lbl4[i].place_forget()


def checkInput(uNumbers, userNumbers):
    counterBadInput = 0
    allowed = [str(i) for i in range(1, 46)]
    for i in range(1, 7):
        if not userNumbers[i].get().isnumeric():
            counterBadInput += 1
            userNumbers[i].delete(0, 'end')
            #break
        elif userNumbers[i].get() not in allowed:
            counterBadInput += 1
            userNumbers[i].delete(0, 'end')
            #break
        elif len(uNumbers) != len(set(uNumbers)):
            counterBadInput += 1
            break
    return counterBadInput


def display(wNumbers, uNumbers, lbl, position):
    uNumbers = [int(i) for i in uNumbers]
    lblWinningNumbers.config(text="JACKPOT : " + str(wNumbers), fg='green')

    intersect = set(uNumbers).intersection(set(wNumbers))
    intersect = list(intersect)

    right_x = 0
    counter = 1
    down_y = 0
    while counter <= 45:
        if counter in wNumbers and counter in uNumbers:
            lbl[counter].config(bg='green')
        elif counter in uNumbers and counter not in wNumbers:
            lbl[counter].config(bg='red')
        if counter == 7 or counter == 13 or counter == 19 or counter == 25 or counter == 31 or counter == 37 or counter == 43:
            down_y += 30
            right_x -= 180
        lbl[counter].place(x=position+right_x, y=250+down_y, width=25, height=25)
        counter += 1
        right_x += 30
    return intersect


def myTip():
    wNumbers = Functions.winningNumbers()
    uNumbers = [str(userNumbers[i].get()) for i in userNumbers]
    uNumbers2 = [str(userNumbersBet2[i].get()) for i in userNumbersBet2]
    uNumbers3 = [str(userNumbersBet3[i].get()) for i in userNumbersBet3]
    uNumbers4 = [str(userNumbersBet4[i].get()) for i in userNumbersBet4]
    resetColor()

    if x.get() == 0:
        counterBadInput = checkInput(uNumbers, userNumbers)
        if counterBadInput == 0:
            lblWarning.place_forget()
            lblWinningNumbers.place(x=50, y=200)
            display(wNumbers, uNumbers, lbl, 90)
        else:
            clearResults()
            lblWarning.place(x=50, y=220)
    elif x.get() == 1:
        counterBadInput = checkInput(uNumbers, userNumbers)
        counterBadInput2 = checkInput(uNumbers2, userNumbersBet2)
        if counterBadInput == 0 and counterBadInput2 == 0:
            lblWarning.place_forget()
            lblWinningNumbers.place(x=250, y=200)
            display(wNumbers, uNumbers, lbl, 90)
            display(wNumbers, uNumbers2, lbl2, 440)
        else:
            clearResults()
            lblWarning.place(x=240, y=220)
    elif x.get() == 2:
        counterBadInput = checkInput(uNumbers, userNumbers)
        counterBadInput2 = checkInput(uNumbers2, userNumbersBet2)
        counterBadInput3 = checkInput(uNumbers3, userNumbersBet3)
        if counterBadInput == 0 and counterBadInput2 == 0 and counterBadInput3 == 0:
            lblWarning.place_forget()
            lblWinningNumbers.place(x=410, y=200)
            display(wNumbers, uNumbers, lbl, 90)
            display(wNumbers, uNumbers2, lbl2, 440)
            display(wNumbers, uNumbers3, lbl3, 790)
        else:
            clearResults()
            lblWarning.place(x=410, y=220)
    elif x.get() == 3:
        counterBadInput = checkInput(uNumbers, userNumbers)
        counterBadInput2 = checkInput(uNumbers2, userNumbersBet2)
        counterBadInput3 = checkInput(uNumbers3, userNumbersBet3)
        counterBadInput4 = checkInput(uNumbers4, userNumbersBet4)
        if counterBadInput == 0 and counterBadInput2 == 0 and counterBadInput3 == 0 and counterBadInput4 == 0:
            lblWarning.place_forget()
            lblWinningNumbers.place(x=590, y=200)
            display(wNumbers, uNumbers, lbl, 90)
            display(wNumbers, uNumbers2, lbl2, 440)
            display(wNumbers, uNumbers3, lbl3, 790)
            display(wNumbers, uNumbers4, lbl4, 1140)
        else:
            clearResults()
            lblWarning.place(x=590, y=220)


window = tk.Tk()

x = tk.IntVar()
userNumbers, userNumbersBet2, userNumbersBet3, userNumbersBet4 = {}, {}, {}, {}
options = ["1 Tipp", "2 Tipps", "3 Tipps", "4 Tipps"]
lbl, lbl2, lbl3, lbl4 = {}, {}, {}, {}
lblTipp = {}
x_right_entries = 50

window.geometry("380x720")  # set window size
window.title("Lotto 6 aus 45")  # set title
icon = tk.PhotoImage(file="LOTTO6aus45-logo.png")  # create icon
window.iconphoto(False, icon)    # set icon

# ENTRIES
for i in range(1, 7):
    userNumbers[i] = tk.Entry(window)
    userNumbersBet2[i] = tk.Entry(window)
    userNumbersBet3[i] = tk.Entry(window)
    userNumbersBet4[i] = tk.Entry(window)

    userNumbers[i].place(x=x_right_entries, y=150, height=30, width=30)
    x_right_entries += 50
# LABELS NUMBERS 1 to 45
for i in range(1, 46):
    lbl[i] = tk.Label(window, text=i, bg='#f0f0f0', font=('Calibri', 13, 'bold'))

    lbl2[i] = tk.Label(window, text=i, bg='#f0f0f0', font=('Calibri', 13, 'bold'))
    lbl3[i] = tk.Label(window, text=i, bg='#f0f0f0', font=('Calibri', 13, 'bold'))
    lbl4[i] = tk.Label(window, text=i, bg='#f0f0f0', font=('Calibri', 13, 'bold'))
# LABELS
lblWelcome = tk.Label(window,
                   text="Willkommen zu \nLotto 6 aus 45",
                   font=('Times New Roman', 20, 'bold'),
                   fg='#007b63')
lblWelcome.place(x=80, y=20)

for i in range(1, 5):
    lblTipp[i] = tk.Label(window,
                                text="Tipp " + str(i) + ":",
                                font=('Calibri', 12, 'bold'),
                                fg='blue')
lblTipp[1].place(x=45, y=120)

lblAttempts = tk.Label(window,
                       text="Wie oft wollen sie Tippen ? (MAX 4)",
                       font=('Calibri', 12, 'bold'),
                       fg='black')
lblAttempts.place(x=40, y=550)

lblBet = tk.Label(window,
                        text="",
                        font=('Calibri', 12, 'bold'),
                        fg='black')
lblBet.place(x=350, y=100)

lblWinningNumbers = tk.Label(window,
                  text="",
                  font=('Calibri', 12, 'bold'),
                  fg='black')
lblWinningNumbers.place(x=50, y=200)

lblWarning = tk.Label(window,
                      text="Nur Zahlen zwischen 1 und 45!\nKeine doppelten Zahlen!!!",
                      font=('Calibri', 12, 'bold'),
                      fg='red')
# BUTTONS
btnOK = tk.Button(window, text="Auswerten",
                  command=myTip,
                  padx=50, pady=20,
                  relief=tk.RIDGE)
btnOK.place(x=160, y=600)
# RADIO BUTTONS
for i in range(len(options)):
    radiobutton = tk.Radiobutton(text=options[i], variable=x, value=i, command=numberOfBets).place(x=40, y=580+i*30)

tk.mainloop()
