import csv
from tkinter import *
from tkinter import ttk


def main():
        createLabels(selection, labels, listboxes)
        create_ok(selection)

        root.mainloop()

def loadCsvMeta():
        residence = {}
        age = {}
        sex = {}
        cause = {}
        year = {}

        with open('./data/13100394_MetaData.csv', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                        match row['Cube Title']:
                                case '1':
                                        residence[row['Product Id']] = 0
                                case '2':
                                        age[row['Product Id']] = 0
                                case '3':
                                        sex[row['Product Id']] = 0
                                case '4':
                                        cause[row['Product Id']] = 0
                                case '6':
                                        year[row['Product Id']] = 0
                
        return residence, age, sex, cause, year

def multi (src,f,data,x,y):
        f=ttk.Frame(src)
        scrollbar = Scrollbar(f, orient="vertical")
        listbox = Listbox(f, bg='#e0bbe4', fg='#534d6b',selectbackground='#fec8d8', selectforeground='#fb6f92',selectmode = "multiple", width=50, height=1, yscrollcommand=scrollbar.set, exportselection=0)
        scrollbar.config(command=listbox.yview, highlightbackground='#fff1f5')
        scrollbar.grid(row=y, column=x+1, sticky="ns")
        listbox.grid(row=y, column=x, sticky="nsew")
        dataHolder = data
        for i in dataHolder:
                dataHolder[i] = StringVar()
                listbox.insert(END , i)
        f.grid(column=x, row=y)
        listbox.grid(column=x, row=y)
        return listbox

def single (src,f,data,x,y):
        f=ttk.Frame(src)
        scrollbar = Scrollbar(f, orient="vertical")
        listbox = Listbox(f,bg='#e0bbe4',fg='#534d6b',selectbackground='#fec8d8', selectforeground='#fb6f92', selectmode = "single", width=50, height=1, yscrollcommand=scrollbar.set, exportselection=0)
        scrollbar.config(command=listbox.yview)
        scrollbar.grid(row=y, column=x+1, sticky="ns")
        listbox.grid(row=y, column=x, sticky="nsew")
        dataHolder = data
        for i in dataHolder:
                dataHolder[i] = StringVar()
                listbox.insert(END , i)
        f.grid(column=x, row=y)
        listbox.grid(column=x, row=y)
        return listbox

def label(src,v,x,y,lb):
        var = StringVar()
        l= Label(src, bg='#957dad', fg='white', textvariable=var, cursor='heart')
        var.set(v)
        l.grid(column=x,row=y)
        label_bind(l,lb)

def counter(lb):
        global click
        global residence, age, sex, cause

        for i in lb.curselection():
                print(lb.get(i))

        if click % 2 == 0:
                lb.config(height=20)
        else: 
                lb.config(height=1)
        click += 1
        
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        items = list(map(int, w.curselection()))
        print('------------------------------------')
        for i in range(len(items)):
                index = int(w.curselection()[i])
                value = w.get(index)
                print('You selected item %d: "%s"' % (index, value))
        print('------------------------------------')

def label_bind(l,lb):
        l.bind("<Button-1>",lambda e: counter(lb))
        lb.bind('<<ListboxSelect>>', onselect)

def createLabels(src, labels, listboxes):
        for i in range(len(labels)):
                label(src, labels[i], 0, i*2, listboxes[i])


def create_ok(src):
        ok=Button(src, bg='#fec8d8',fg='#534d6b', text='Submit',command=lambda:[create_tree()])
        ok.grid(column=0,row=20)

#-------------------------------------------------------------------------------------------------------------------------------
#Post-Selection
#-------------------------------------------------------------------------------------------------------------------------------
def get_values(lb):
        values=[]
        items = list(map(int, lb.curselection()))
        for i in range(len(items)):
                index = int(lb.curselection()[i])
                value = lb.get(index)
                values.append(value)
        return values

def display(x):
        message=Label(selection,text=x,fg='#fec8d8', bg='#d291bc')
        message.grid(column=0,row=25)

def loadCsv():
        percent=[]
        num=[]
        rank=[]
        ten_thou=[]
        v1=get_values(lb1)
        v2=get_values(lb2)
        v3=get_values(lb3)
        v4=get_values(lb4)
        if len(v1)!=0:
                for i in range(len(v1)):
                        rows=[]
                        rows2=[]
                        rows3=[]
                        rows4=[]
                        with open('./data/13100394.csv', encoding='utf-8-sig') as file:
                                reader=csv.DictReader(file)
                                for row in reader:
                                        if v1[i] in row['Leading causes of death (ICD-10)']:
                                                rows.append(row)
                        if len(v2)!=0:
                                for k in rows:
                                        for j in range(len(v2)):
                                                if v2[j] in k['Age at time of death']:
                                                        rows2.append(k)
                        else:
                                for k in rows:
                                        if 'all ages' in k['Age at time of death']:
                                                rows2.append(k)
                        if len(v3)!=0: 
                                for m in rows2:
                                        for l in range(len(v3)):
                                                if v3[l] in m['Sex']:
                                                        rows3.append(m)
                        else:
                                for m in rows:
                                        if 'Both sexes' in m['Sex']:
                                                rows3.append(m)
                        if len(v4)!=0:                        
                                for j in rows3:
                                        for n in range(len(v4)):
                                                if v4[n] in j['REF_DATE']:
                                                        rows4.append(j)
                        else:
                                return display('Please select one or more year(s)')                   
                        for row in rows4:
                                match row['Characteristics']:
                                        case 'Rank of leading causes of death':
                                                rank.append(row['VALUE'])
                                        case 'Number of deaths':
                                                num.append(row['VALUE'])
                                        case 'Percentage of deaths':
                                                percent.append(row['VALUE'])
                                        case 'Age-specific mortality rate per 100,000 population':
                                                ten_thou.append(row['VALUE'])
        else:
                return display('Please select one or more cause(s)')
        return percent, num, rank, ten_thou, v1, v2, v4

def singleLabel(frame, x):
        label = Label(frame, text=x) 
        label.pack(side=TOP)

def year_Label(frame, x):
        label = Label(frame,bg='pink',font=("Calibri Light", 15), text=x) 
        label.pack(side=TOP)

def create_tree():
        global root
        if loadCsv() is not None:
                percent, num, rank, ten_thou, values, ages, years=loadCsv()
                if len(ages)!=0:
                        for k in range(len(years)):
                                fr=ttk.Frame(root, padding=10)
                                fr.pack(side=TOP,fill=NONE)
                                year_Label(fr,years[k])
                                for i in range(len(ages)):
                                        v=values.copy()
                                        frame = ttk.Frame(fr, padding=10)
                                        frame.pack(side=LEFT, anchor=NW, fill=NONE)
                                        singleLabel(frame,ages[i])
                                        if i==0:
                                                v.insert(0,'Type')
                                        tv = ttk.Treeview(
                                        frame,  
                                        columns=v, 
                                        show='headings', 
                                        height=5
                                        )
                                        pva=[]
                                        nva=[]
                                        rva=[]
                                        ttva=[]
                                        if i==0:
                                                pva.append('Percentage Deaths')
                                                nva.append('Number of Deaths')
                                                rva.append('Rank')
                                                ttva.append('Mortality per 100k')
                                        for j in range(len(values)):
                                                tv.heading(values[j],text=values[j])
                                                pva.append(percent[(i+(k*(len(ages))))+(j*((len(years))*len(ages)))])
                                                nva.append(num[(i+(k*(len(ages))))+(j*((len(years))*len(ages)))])
                                                rva.append(rank[(i+(k*(len(ages))))+(j*((len(years))*len(ages)))])
                                                ttva.append(ten_thou[(i+(k*(len(ages))))+(j*((len(years))*len(ages)))])

                                        tv.pack(side=LEFT, fill=BOTH, pady=20)
                                        tv.insert(parent='', index=0, iid=0, values=pva)
                                        tv.insert(parent='', index=1, iid=1, values=nva)
                                        tv.insert(parent='', index=2, iid=2, values=rva)
                                        tv.insert(parent='', index=3, iid=3, values=ttva)
                else:
                        tv = ttk.Treeview(
                        root, 
                        columns=values, 
                        show='headings', 
                        height=5
                        )
                        for j in range(len(values)):
                                tv.heading(values[j],text=values[j])
                        tv.pack(side=LEFT, anchor=NW, fill=NONE, pady=20)
                        tv.insert(parent='', index=0, iid=0, values=percent)
                        tv.insert(parent='', index=1, iid=1, values=num)
                        tv.insert(parent='', index=2, iid=2, values=rank)
                        tv.insert(parent='', index=3, iid=3, values=ten_thou)


#-------------------------------------------------------------------------------------------------------------------------------
#END
#-------------------------------------------------------------------------------------------------------------------------------

residence, age, sex, cause, year = loadCsvMeta()

click=0
root = Tk()
root.configure(bg='#e0bbe4')
frm = ttk.Frame(root, padding=10)
frm.pack(side=LEFT,fill=BOTH)
s = ttk.Style()

selection = ttk.Frame(frm, padding=10)
selection.grid()
s.configure('TFrame', background='#d291bc')
labels=['Cause of Death','Age','Sex', 'Year']

lb1 = multi(selection,'frm1', cause,0,1)
lb2 = multi(selection,'frm2', age,0,3)
lb3 = single(selection,'frm3', sex,0,5)
lb4 = multi(selection,'frm4', year,0,7)

listboxes = [lb1, lb2, lb3, lb4]




if __name__ == "__main__":
    main()
