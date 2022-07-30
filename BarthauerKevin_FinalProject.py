'''
BarthauerKevin_FinalProject.py
7/30/22
Written in Python 3.10

Security Operations Center Reimage And Tracking Evaluation System (S.O.C.R.A.T.E.S.)

This application provides a single place to store and use data collected in the course
of end-point device security investigations for the State of Indiana Office of
Technology Security Opperations Center.  

Information captured is recorded for later reference and is concatenated into a
reimage text in case of the need to remediation.

Files that must be included with this program in the same folder are:
record.csv
reimage.txt
BarthauerKevin_FinalProject.py
'''
from tkinter import *
from tkinter import ttk
from datetime import *
from csv import writer

#### Declarations ####
attribs = []

#### Modules ####

def WinDT(x):
    '''
    Generates Date and Time Stamp as zero position of attribs
    '''
    ##Modules
    def startClick():
        startTime = Label(DT, text=comm1)
        startTime.pack()
        x.append(nowString)
        x.append(analysts[Combo.current()])
        DT.destroy()
        return
    ##Variables
    DT = Tk()
    now = datetime.now()
    analysts = ['K. Barthauer', 'J. Zwarycz']
    nowString = now.strftime("%d/%m/%Y %H:%M:%S")
    startButton = Button(DT, text = 'Begin Investigation', padx = 50, pady = 25, command = startClick)
    frame = Frame(DT, padx = 10, pady = 10)
    Combo = ttk.Combobox(frame, values = analysts)
    comm1 = 'Investigation initiated at: ' + nowString

    DT.title('S.O.C.R.A.T.E.S.')

    frame.pack()
    Combo.set('Analyst Name')
    Combo.pack(padx = 5, pady = 5)

    startButton.pack()
    DT.mainloop()
    return x

def WinReimage():
    '''
    generates reimage notification text
    '''
    global attribs
    def done():
        reimage.destroy()
        return
    f = open("reimage.txt", "w")

    f.write(f'Machine:  {attribs[2]}\n')
    f.write('\n')
    f.write(f'User: {attribs[3]}\n')
    f.write('\n')
    f.write(f'Last logged on user: {attribs[4]}\n')
    f.write('\n')
    f.write(f'Manager: {attribs[6]}\n')
    f.write('\n')
    f.write(f'Source: {attribs[7]}\n')
    f.write('\n')
    f.write(f'{attribs[9]}\n')
    f.write('\n')
    f.write(f'Severe Virus infection, warranting notification of reimage. Ticket number {attribs[10]} has been entered by IOT. Due to the severity of virus activity the machine will be/n')
    f.write('reimaged.  Internet traffic patterns suggest it is infected with a virus that cannot be cleaned by FireEye.  Any user of this computer should reset their network password\n')
    f.write('immediately. (Password should be changed to something completely different from their old password -  ie, Do not simply append a number to the old password).\n')
    f.write(f'(A support tech will be in contact with the user to have the machine reimaged under the request ticket number {attribs[10]})\n')
    f.write('\n')
    f.write('Please speak with the employee in an attempt to discover the source of this infection.  Actions should be taken to remove this source.   Actions to be considered:\n')
    f.write('1.            Restrict internet activity\n')
    f.write('2.            Do not allow USB drives to be used on the machine\n')
    f.write('3.            Education of employees on identification of spam email messages\n')
    f.write('4.            Review of appropriate internet use\n')
    f.write('5.            Discourage use of personal email (hotmail, gmail etc.) on state computers.\n')
    f.write('\n')
    f.write('Thank you for your assistance in this matter.\n')
    f.write('\n')
    f.write('IOT Security\n')
    f.close()


    reimage = Tk()
    reimage.title('S.O.C.R.A.T.E.S.')
    notice = Label(reimage, text="your reimage email has been generated and saved to the file reimage.txt")
    notice.pack()
    finishbut = Button(reimage, text="Click here to Exit", command=done)
    finishbut.pack()
    return

def WinAttribs():
    ''' Collect attribs list and choose course '''
    global attribs
    collector = Tk()
    collector.title()
    collector.geometry('500x700')
    
    host = Entry(collector, width=50, borderwidth=20)
    host.pack()
    host.insert(0,"Host name")

    user = Entry(collector, width=50, borderwidth=20)
    user.pack()
    user.insert(0,"User")

    uname = Entry(collector, width=50, borderwidth=20)
    uname.pack()
    uname.insert(0,"Username")

    agency = Entry(collector, width=50, borderwidth=20)
    agency.pack()
    agency.insert(0,"Agency")

    superv = Entry(collector, width=50, borderwidth=20)
    superv.pack()
    superv.insert(0,"Supervisor")

    source = Entry(collector, width=50, borderwidth=20)
    source.pack()
    source.insert(0,"Alert Source")

    vnotice = Entry(collector, width=50, borderwidth=20)
    vnotice.pack()
    vnotice.insert(0,"Virus Notification Contacts")

    descrip = Text(collector, width=50, height=8)
    descrip.pack()
    descrip.insert('end', "Description: ")



    def myClick():
        '''
        Button click on collector menu
        populates attribs list with investigation records
        '''
        attribs.append(host.get())
        attribs.append(user.get())
        attribs.append(uname.get())
        attribs.append(agency.get())
        attribs.append(superv.get())
        attribs.append(source.get())
        attribs.append(vnotice.get())
        attribs.append(descrip.get(1.0,'end'))
        collector.destroy()
        return attribs
        
    myButton = Button(collector, text="Record and Resolve", command=myClick)
    myButton.pack()
    collector.mainloop()
    return attribs

def resolve():
    global attribs
    res = Tk()
    res.geometry = ('500x700')
    res.title('S.O.C.R.A.T.E.S.')
    ticket = Entry(res, width=50, borderwidth=20)
    ticket.pack()
    ticket.insert(0,"ASM Ticket Number")
    def Click1():
        attribs.append(ticket.get())
        record()
        res.destroy()
        WinReimage()
        return
    def Click2():
        attribs.append('False Positive')
        record()
        res.destroy()
        return
    But1 = Button(res, text="Generate Reimage File", command=Click1)
    But1.pack()
    But2 = Button(res, text="Record as False Positive / exit", command=Click2)
    But2.pack()
    return
    
def record():
    '''
    creates file record of investigation
    '''
    global attribs
    with open('record.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(attribs)  
        f_object.close()
    return



#### Main Body ####

WinDT(attribs)
attribs = WinAttribs()
resolve()


