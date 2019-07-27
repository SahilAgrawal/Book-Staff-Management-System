from Student import *
from Faculty import *
from Books import *
import pickle
import os



##################################################################################################################################################
'''


            Student Field
            
            :   add_student()
            
            :   student_entry()

            :  display_student()

            
'''
##################################################################################################################################################
def add_student():
        year=int(input("Student Admission year :: "))
        if year > 2000 and year < 2020:
            adm_id=input("Enter 4 digit (integer) Admission id :: ")
            if len(adm_id) == 4:
                    if os.path.exists('Student.pkl') is True:
                    with open('Student.pkl','rb') as f:
                        while True:
                            try:
                                obj = pickle.load(f)
                                #for student in obj:
                                if  obj == adm_id:
                                    print("Already exist ")
                                    print("_"*60)
                                    break
                            except EOFError:
                                student_entry(year,adm_id)
                                
                                break
                else:
                    student_entry(year,adm_id)
                   
            else:
                print("Invalid Entry")
               
        else:
            print("Invalid Year Entry")

##################################################################################################################################################

def student_entry(year,adm_id):
   
    name=input("Enter student name :: ").upper()
    branch=input("*** Branchs ***::\n 1.Computer Science / CS\n 2.Civil Engineering / CE\n 3.Mechanical Branch / ME\n 4.Electronics and Communication / EC \n 5.Electrical and electronics engineering / EX\n branch :: ").upper()
    s_id=('0187'+branch+str(year)[2:]+str(adm_id))
    with open ('Student.pkl','ab') as f:
       temp=Student(name,branch,year,s_id,adm_id)
       pickle.dump(temp,f)
       print('*************Successfully Student add**********************')
        
   
##################################################################################################################################################
def display_student():
    if os.path.exists('Student.pkl') is True:
        with open ("Student.pkl",'rb') as s:
            print('__'*50)
            print('\t\t\t STUDENT DETAILS')
            print('__'*50)
            print("\n\tName\t\t Branch\tEnroll No.\t\t Year\tBooks\n")
            while True:
                try:
                    obj = pickle.load(s)
                    obj.display()
                except EOFError:
                    break
    else:
        print('*************No such directory***********')
   
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
'''


            Faculty Field
            
            :   add_faculty()
            
            :   faculty_entry()

            :  display_faculty()

            
'''
##################################################################################################################################################
def add_faculty():

    year=int(input("Faculty admission year :: "))
    if year > 1950 and year < 2020:
        fac_id=input("Enter 6 digit  Faculty id :: ")
        if len(fac_id) == 6:
            if os.path.exists('Faculty.pkl') is True:
                with open('Faculty.pkl','rb') as f:
                    while True:
                        try:
                            data = pickle.load(f)
                            if  data.f_id == fac_id:
                                print("Already exist")
                                break
                        except EOFError:
                            faculty_entry(year,fac_id)
                            break
            else:
                faculty_entry(year,fac_id)
               
        else:
            print("Invalid Entry")
           
    else:
        print("Invalid Year Entry")
   
##################################################################################################################################################

def faculty_entry(year,fac_id):

    with open ('Faculty.pkl','ab') as f:
        name=input("Enter Faculty name :: ").upper()
        pickle.dump(Faculty(name,fac_id,year),f)
        print('*************Successfully Faculty add**********************')
        


##################################################################################################################################################

def display_faculty():
    if os.path.exists('Faculty.pkl') is True:
        with open ("Faculty.pkl",'rb') as s:
            print('__'*50)
            print('\t\t\t FACULTY DETAILS ')
            print('__'*50)
            print("\n\t Name\t\t ID\tYear\tBooks\n")
            while True:
                try:
                    obj = pickle.load(s)
                    obj.display()
                except EOFError:
                    break
    else:
            print('*********No such directory*************')
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
'''

             Book Field

            :   add_books()
            
            :   books_entry()

            :  display_books()



'''        
##################################################################################################################################################

def add_books():
   
    year=int(input("Book Publication year :: "))
    if year > 1990 and year < 2020:
        isbn=input("Enter 8 digit ISBN number of book :: ")
        if len(isbn) == 8:
            if os.path.exists('Books.pkl') is True:
                with open('Books.pkl','rb') as f:
                    while True:
                        try:
                            obj = pickle.load(f)
                            if  obj.isbn== isbn:
                                print("Already exist ")
                                print("_"*60)
                                break
                        except EOFError:
                            books_entry(year,isbn)
                            break
            else:
                books_entry(year,isbn)
               
        else:
            print("Invalid Entry")
           
    else:
        print("Invalid Year Entry")
   
##################################################################################################################################################

def books_entry(year,isbn):
    
        with open ('Books.pkl','ab') as f:
            name=input("Enter Book name :: ").upper()
            publication=input("Neme of publication :: ").upper()
            copies=int(input("Number of copies of books :: "))
            pickle.dump(Books(name,publication,isbn,year,copies),f)
            print('*************Successfully Book add in library **********************')
        
        

##################################################################################################################################################

def display_books():
    if os.path.exists('Books.pkl') is True:
        with open ("Books.pkl",'rb') as s:
            print('__'*50)
            print('\t\t\t BOOK DETAILS')
            print('__'*50)
            print("\tName\t Publication\tYear\tISBN\tNo. of copies")
            while True:
                try:
                    book_data = pickle.load(s)
                    book_data.display()
                except EOFError:
                    break
    else:
        print('***********No such directory************')
    print('__'*50)

##################################################################################################################################################
'''
                    book_issue()

                    issue()

'''

##################################################################################################################################################
def book_issue():
    if os.path.exists('Student.pkl') is True:
        stu=input("Enter Student ID :: ").upper()
        with open ("Student.pkl",'rb') as s:
            while True:
                try:
                    obj = pickle.load(s) 
                    if  obj.s_id== stu:
                        if len(obj.book) > 5:
                            print("Maximum limit of books are issued ...")
                        else:
                            book_isbn=input("Enter 8 digit book ISBN number :: ")
                            with open ('Books.pkl','rb') as b:
                                while True:
                                    try:
                                        data=pickle.load(b)
                                        if data.isbn==book_isbn:
                                            issue(book_isbn,stu,data.name)
                                            return
                                    except EOFError:
                                        break
                                    
                 
                except EOFError:
                    print('No student')
                    break
    else:
        print('*************No such directory ******************')
                

##################################################################################################################################################

def issue(book_isbn,s_id,book_name):
    lis=[]
    with open ('Student.pkl','rb') as f1:
        while True:
             
                try:
                  lis.append(pickle.load(f1))
                except EOFError:
                    break
    for _ in lis:
        if s_id ==_.s_id:
            _.book[book_isbn]=book_name
        f1.close()
    with open('Student.pkl','wb') as f:
        for _ in lis:
            pickle.dump(_,f)
    book_list=[]    
    with open ('Books.pkl','rb') as b:
        while True:
            try:
              book_list.append(pickle.load(b))
            except EOFError:
                break
        for _ in book_list:
            if _.isbn==book_isbn:
                if _.copies > 0:
                    _.copies-=1
                    print('************Successful Issue Book************')
                    break
                else:
                    print('No any book')
                    break
    with open('Books.pkl','wb') as f:
        for _ in book_list:
            pickle.dump(_,f)
##################################################################################################################################################
'''

                book_issue_fac()

                issue_fac()

'''
##################################################################################################################################################
def book_issue_fac():
    if os.path.exists('Faculty.pkl') is True:
        fac=input("Enter Faculty ID :: ").upper()
        with open ("Faculty.pkl",'rb') as s:
            while True:
                try:
                    obj = pickle.load(s)
                    print(obj.f_id)
                    if  obj.f_id== fac:
                        if len(obj.f_book) > 5:
                            print("Maximum limit of books are issued ...")
                        else:
                            book_isbn=input("Enter 8 digit book ISBN number :: ")
                            with open ('Books.pkl','rb') as b:
                                while True:
                                    try:
                                        data=pickle.load(b)
                                        if data.isbn==book_isbn:
                                            issue_fac(book_isbn,fac,data.name)
                                            return
                                    except EOFError:
                                        break
                                    
                 
                except EOFError:
                    print('No faculty')
                    break
    else:
        print('**************No such directory**************')
                
                

##################################################################################################################################################

def issue_fac(book_isbn,fac,book_name):
    lis=[]
    with open ('Faculty.pkl','rb') as f1:
        while True:
             
                try:
                  lis.append(pickle.load(f1))
                except EOFError:
                    break
    for _ in lis:
        if fac ==_.f_id:
            _.f_book[book_isbn]=book_name
        f1.close()
    with open('Faculty.pkl','wb') as f:
        for _ in lis:
            pickle.dump(_,f)
    book_list=[]    
    with open ('Books.pkl','rb') as b:
        while True:
            try:
              book_list.append(pickle.load(b))
            except EOFError:
                break
        for _ in book_list:
            if _.isbn==book_isbn:
                if _.copies > 0:
                    _.copies-=1
                    print('************Successful Issue Book for Faculty************')
                    break
                else:
                    print('No any book')
                    break
    with open('Books.pkl','wb') as f:
        for _ in book_list:
            pickle.dump(_,f)
##################################################################################################################################################
##################################################################################################################################################
'''
        return_student()

'''
##################################################################################################################################################
def return_student():
    if os.path.exists('Student.pkl') is True:
        stu=input("Enter student ID :: ").upper()
        with open ("Student.pkl",'rb') as s:
            while True:
                try:
                    obj = pickle.load(s) 
                    if  obj.s_id== stu:
                        if len(obj.book) <=  0:
                            print("No book issued....")
                        else:
                            book_isbn=input("Enter 8 digit book ISBN number :: ")
                            try:
                                for i in obj.book.keys():
                                    if i == book_isbn:
                                        print(i)
                                        ret_stu(stu,book_isbn)
                                        return
                            except EOFError:
                                print('Book not issued..')
                                break
                except EOFError:
                    print('No student')
                    break
    else:
        print('********************No such directory***********************')
##################################################################################################################################################
def ret_stu(stu,book_isbn):
    lis=[]

    # student object append into list
    
    with open ('Student.pkl','rb') as f1:
        while True:
                try:
                    lis.append(pickle.load(f1))
                except EOFError:
                    break
        # find student object into list
        
    for _ in lis:
        if stu ==_.s_id:
            del _.book[book_isbn]
            print('delete student')
        f1.close()
    book_list=[]

        # return book from student

    with open('Student.pkl','wb') as f:
        for _ in lis:
            pickle.dump(_,f)

        # append book object into list 

    with open ('Books.pkl','rb') as b:
        while True:
            try:
              book_list.append(pickle.load(b))
            except EOFError:
                break

        # list of books dump into book database

        for _ in book_list:
            if _.isbn==book_isbn:
                    _.copies+=1
                    print('************Successful Return Book by Student************')
                    break
    with open('Books.pkl','wb') as f:
        for _ in book_list:
            pickle.dump(_,f)
##################################################################################################################################################
'''
        return_faculty()
        return fac()
'''
##################################################################################################################################################
def return_faculty():
    if os.path.exists('Faculty.pkl') is True:
        fac=input("Enter Faculty ID :: ").upper()
        with open ("Faculty.pkl",'rb') as s:
            while True:
                try:
                    obj = pickle.load(s) 
                    if  obj.f_id== fac:     #FIND FACULTY
                        if len(obj.f_book) <=  0:   # CHECK TOTAL NUMBER OF ISSUE BOOK OF A PARTICULAR FACULTY
                            print("No book issued....")
                        else:
                            book_isbn=input("Enter 8 digit book ISBN number :: ")
                            try:
                                for i in obj.f_book.keys():
                                    if i == book_isbn:
                                        ret_stu(fac,book_isbn)
                                        return
                            except EOFError:
                                print('Book not issued..')
                                break
                except EOFError:
                    print('No faculty')
                    break
    else:
        print('*********************No such directory****************************')
##################################################################################################################################################
def ret_fac(fac,book_isbn):
    lis=[]
    with open ('Faculty.pkl','rb') as f1:
        while True:
                try:
                    lis.append(pickle.load(f1))
                except EOFError:
                    break
    for _ in lis:
        if fac ==_.f_id:
            del _.f_book[book_isbn]
        f1.close()
    book_list=[]
    with open('Faculty.pkl','wb') as f:
        for _ in lis:
            pickle.dump(_,f) 
    with open ('Books.pkl','rb') as b:
        while True:
            try:
              book_list.append(pickle.load(b))
            except EOFError:
                break
        for _ in book_list:
            if _.isbn==book_isbn:
                    _.copies+=1
                    print('************Successful Return Book by Student************')
                    break
    with open('Books.pkl','wb') as f:
        for _ in book_list:
            pickle.dump(_,f)
################################################################################################################################################
'''
        search(file_name,id)
'''
################################################################################################################################################
def search(s,ide,num):
    while True:
        try:
            obj = pickle.load(s)
            if num == 3:
                if  obj.isbn== ide:
                    print("\tName\t Publication\tYear\tISBN\tNo. of copies")
                    obj.display()
                    return
            if num == 2:
                if  obj.f_id== ide:
                    print("\n\t Name\t\t ID\tYear\tBooks\n")
                    obj.display()
                    return
            if num == 1:
                print(obj.name)
                if  obj.s_id == ide:
                    print("\n\tName\t\t Branch\tEnroll No.\t\t Year\tBooks\n")
                    obj.display()
                    return
        except EOFError:
            print('\t\tNo such record of  '+ide)
            break
###############################################################################################################################################

     
