import pickle
import os
print("--------------------------------------------------------------------------------------------------------------------------------")
print("                                               Welcome to Bosco Public School               ")
print()
print("                                             ***Library Management System***   ")
print()
print('''
                          Reading is essential for those who seek to rise above the ordinary.” – Jim Rohn

''')
print("--------------------------------------------------------------------------------------------------------------------------------")
print('''Welcome to the menu driven program (School Library Management System) ,here are list of operations you can perform:)......
            1.Read all the record in the Database
            2.Writing data in the database
            3.Searching data in the database
            4.Adding data in the database
            5.Updating data in database
            6.Deleting a record
            7.exit''')
def read():
    file=[]
    f=open('database','rb')
    while True:    
        try:
            file.append(pickle.load(f))
        except(EOFError):
            print("end of file")
            break
    f.close()
    print('''********************************************************''')
    print('''name  admission number  phone number  last book read''')
    print()
    for i in file:
        print()
        for j in i:
            print(j,end="    ")
            #print()
            
def write():
        print()
        f=open('database','wb')
        n=int(input('enter number of Students: '))
        for i in range(n):
            l=[]
            print()
            a=input("student name: ")
            b=int(input("Admission Number (Enter Number format only): "))
            while True:
                c=int(input("Phone number: "))
                if len(str(c))==10:
                    False
                    break
                else:
                    print("Enter valid Phone Number!")
            
            d=input("last book read: ")    
            l.extend([a,b,c,d])
            pickle.dump(l,f)
        print('*********Your data has been successfully added in the records*********')
        f.close()
        
def search():
        f=open('database','rb')
        data=[]
        l=[]
        while True:
            try:      
                data.append(pickle.load(f))
            except(EOFError):
                break
        f.close()
        a=int(input('''-------------------------------------------------------------------
    What do you wonna search,these are the criteri from from you can search:
        (1)Name
        (2)Admission Number
        (3)Phone Number
        (4)Last book read
        Enter you choice:
        -------------------------------------------------------------------
        '''))
        if a==1:
            b=input("Enter Name to be searched : ")
            for i in data:
                if i[0]==b:
                    l.append(i)
                    f=1
                else:
                    print("Entered Name doesn't exist!!!,try again.")
        elif a==2:
            b=int(input("Enter Name to be searched : "))
            for i in data:
                if i[1]==b:
                    l.append(i)
                    f=1
                else:
                    print("Entered Admission Number doesn't exist!!!,try again.")
        elif a==3:
            b=input("Enter Phone Number to be searched : ")
            for i in data:
                if i[2]==b:
                    l.append(i)
                    f=1
                else:
                    print("Entered phone number doesn't exist!!!,try again.")
        elif a==4:
            b=input("Enter Last book name read by the student to be searched : ")
            for i in data:
                if i[3]==b:
                    l.append(i)
                    f=1
                else:
                    print("Entered Entry doesn't exist!!!,try again.")
        if f==1:
            print()
            print('   Searched data from record is:')
            print('----------------------------------------------------------------------------------------')
            print("name, admission number, phone number, last book read")
            print('----------------------------------------------------------------------------------------')
            for i in l:
                print()
                for j in i:
                    print(j)
                    
def append():
    print()
    f=open('database','ab')
    n=int(input('enter number of Students to be added : '))
    for i in range(n):
        l=[]
        print()
        a=input('Name: ')
        b=int(input('Admission Number: '))
        c=int(input('Phone number: '))
        while True:
            c=int(input("Phone number: "))
            if len(str(c))==10:
                False
            else:
                print("Enter valid Phone Number!")
        d=input('Last book read: ')
        l.extend([a,b,c,d]) 
        pickle.dump(l,f)
        print('Record Successfuly Added!....................')
    f.close()

def update():
    print("********************************************************")   
    l=[]
    f=open('database','rb')
    g=open('temp','wb')
    while True:
        try:      
            l.append(pickle.load(f))
        except(EOFError):
            break
    f.close()
    x=int(input("Enter Admission Number: "))
    if x in l[1]:        
        y=int(input('''What do you want to update:
    (1)Name
    (2)Admission Number
    (3)Phone number
    (4)last book read
    Enter choice: '''))
        for i in l:
            z=[]
            if i[1]==x:
                if y==1:
                    n=input('Enter new name: ')
                    i[0]=n
                    z.append(i)
                elif y==2:
                    new=input('Enter new Admission Number: ')
                    i[1]=n
                    z.append(i)
                elif y==3:
                    n=input('Enter new Phone number: ')
                    i[2]=n
                    z.append(i)
                elif y==4:
                    n=int(input('Enter new Last book read: '))
                    i[3]=n
                    z.append(i)
                for p in z:
                    pickle.dump(p,g)    
                print("Record has been updated sucessfully")
        g.close()
        os.remove('database')
        os.rename('temp','database')
    else:
        print("Enter correct admission Number!")
        
def remove():
    f=open("database","rb")
    g=open("temp","wb")
    o_rec=[]
    while True:    
        try:
            o_rec.append(pickle.load(f))
        except(EOFError):
            print("end of file")
            break
    n_rec=[]
    
    a=int(input("Enter Admission Number of the student to be deleted: "))
    for i in o_rec:
        
        if i[1]!=a:
            n_rec.append(i)
    
    pickle.dump(n_rec, g)
    f.close()
    g.close()
    os.remove("database")
    os.rename("temp","database")


flag=1
while True:
    ch=int(input("enter choice: "))
    if ch==1:
        print()
        print('''********************************************************''')
        read()
        print()
        print("******SUCCESSFULLY READ!!!*********")
        k=input("if you want to continue press: y and to leave press n ")
        if k=='y' or 'Y':
            flag=1
        elif k=='n' or 'N':
            flag=0
        else:
            print("incorrect choice,try again.")
            
    if ch==2:
        print("********************************************************")
        write()
        print("********************************************************")
        k=input("if you want to continue press: y and to leave press n ")
        if k=='y' or 'Y':
            flag=1
        elif k=='n' or 'N':
            flag=0
        else:
            print("incorrect choice,try again.")
            
    if ch==3:
         print("********************************************************")
         search()
         print("********************************************************")
         k=input("if you want to continue press: y and to leave press n ")
         if k=='y' or 'Y':
             flag=1
         elif k=='n' or 'N':
             flag=0
         else:
             print("incorrect choice,try again.")
             
    if ch==4:
        print("********************************************************")
        append()
        print("********************************************************")
        k=input("if you want to continue press: y and to leave press n ")
        if k=='y' or 'Y':
            flag=1
        elif k=='n' or 'N':
            flag=0
        else:
            print("incorrect choice,try again.")
            
    if ch==5:
       update()
       print("********************************************************")
       k=input("if you want to continue press: y and to leave press n ")
       if k=='y' or 'Y':
           flag=1
       elif k=='n' or 'N':
           flag=0
       else:
           print("incorrect choice,try again.")
           
    if ch==6:
        print("********************************************************")
        remove()
        print("*************Data Successfully Removed!*******************")
        print("********************************************************")
        k=input("if you want to continue press: y and to leave press n ")
        if k=='y' or 'Y':
            flag=1
        elif k=='n' or 'N':
            flag=0
        else:
            print("incorrect choice,try again.")
    if ch==7:
        print(''' Here's a Motivational Quote for you!
“A reader lives a thousand lives before he dies . . . The man who never reads lives only one.” – George R.R. Martin ''')
        print('''thanks for visiting us...........................................
do visit again..............................................
Happy Reading! :)     ''')
        print("********************************************************") 
        print("--------------------------------------------------------------------------------------------------------------------------------")
        flag=0
        