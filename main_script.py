# LMS
LMS is an environment to manage the books, issue and return data via using python.
'''
    Title                       : Library Management System 
    Name                        : Sahil Agrwal
    Date                        : 27/07/2019

'''

import functions as f
import os

def main():
    op=0
    while op != 14:
        print('---'*40)
        print('\t********Library Management System***********')
        print('---'*40)
        print('\tpress 1 for Add Student')
        print('\tpress 2 for Add Faculty')
        print('\tpress 3 for Add Book')
        print('\tpress 4 for issue book for  Student')
        print('\tpress 5 for issue book for faculty')
        print('\tpress 6 for search book')
        print('\tpress 7 for search student')
        print('\tpress 8 for search faculty')
        print('\tpress 9 for return book from  Student')
        print('\tpress 10 for return book from faculty')
        print('\tpress 11 for display information of student')
        print('\tpress 12 for display information of faculty')
        print('\tpress 13 for display information of books')
        print('\tpress 14 for Exit')
        print('---'*40)
        op=int(input('Enter choice :: '))
        print('---'*40)
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[  Please carefully filled the entry ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        if(op==1):
            f.add_student()
        elif(op==2):
            f.add_faculty()
        elif(op==3):
            f.add_books()
        elif(op==4):
           f.book_issue()
        elif(op==5):
            f.book_issue_fac()
        elif(op==6):
            if os.path.exists('Books.pkl') is True:
               with open('Books.pkl','rb') as b:
                    isbn=input('Enter book ISBN :: ').upper()
                    f.search(b,isbn,3)
            else:
                print('No any directory')
        elif(op==7):
            if os.path.exists('Student.pkl') is True:
                with open ('Student.pkl','rb') as b:
                    stu=input('Enter Student ID  :: ').upper()
                    f.search(b,stu,1)
            else:
                print('No any directory')
        elif(op==8):
            if os.path.exists('Faulty.pkl') is True:
                with open ('Faculty.pkl','rb') as b:
                    fac=input('Enter Faculty ID  :: ').upper()
                    f.search(b,fac,2)
            else:
                print('No any directory')
        elif(op==9):
            f.return_student()
        elif(op == 10):
            f.return_faculty()
        elif(op==11):
            f.display_student()
        elif(op==12):
            f.display_faculty()
        elif(op==13):
            f.display_books()
        elif(op==14):
            print("*************** Thankyou ********************")
            break
        else:
            print("Invalid choice")
            
if __name__=='__main__':
    main()
        
