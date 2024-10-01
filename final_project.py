import pandas as pd
from time import sleep
import csv
import os
import re






class person :
    def __init__(self,name,age):
        self.name=name
        self.age =age


class athlete(person):
    def __init__(self,name,age,email,password):
        super().__init__(name,age)
        self.email=email
        self.password = password

class coachh(person) :
    def __init__(self, name, age , email , password):
        super().__init__(name, age)
        self.email=email
        self.password = password

class manager(person):
    def __init__(self, name, age,email,password):
        super().__init__(name, age)
        self.email=email
        self.password = password





class sport :
    def __init__(self,day,hours,coach) :
        self.day=day
        self.hours=hours
        self.coach=coach

class football(sport):
    def __init__(self, day, hours, coach):
        super().__init__(day, hours, coach)


class volleyball(sport):
    def __init__(self, day, hours, coach):
        super().__init__(day, hours, coach)

class basketball(sport):
    def __init__(self, day, hours, coach):
        super().__init__(day, hours, coach)

class swim(sport):
    def __init__(self, day, hours, coach):
        super().__init__(day, hours, coach)


class wallet:
    def __init__(self) :
        self.cash = 0
    def buy_football(self):
        if self.cash >=80 :
            self.cash-=80
            os.system('clear')
            print('the football paid seccessfully ')
        else:
            print('sorry you have debts')

    def add_cash(self,amount):
        self.cash += amount
        print('you added %i cash to your wallet and your currnt cash is %i ' %(amount,self.cash))

    def buy_volleyball(self):
        if self.cash >=70 :
            self.cash-=70
            os.system('clear')
            print('the volleyball paid seccessfully ' , self.cash)
        else:
            print('sorry you have debts')

    def buy_basketball(self):
        if self.cash >=60 :
            self.cash-=60
            os.system('clear')
            print('the football paid seccessfully ' , self.cash)
            
        else:
            print('sorry you have debts')

    def buy_swiming(self):
        if self.cash >=40 :
            self.cash -= 40
            os.system('clear')
            print('the football paid seccessfully ' , self.cash)
        else:
            print('sorry you have debts')
    def buy_gym(self):
        if self.cash >=100 :
            self.cash-=100
            os.system('clear')
            print('the football paid seccessfully ' , self.cash)
        else:
            print('sorry you have debts')


#///////////////////////////////////////////////////////////////////// اتمام تعریف کلاس ها 



#با استفاده از کتابخونه (pd) 
#چهار تا فایل های سی اس وی رو میخونیم

df = pd.read_csv('/Users/hamoon/Desktop/athlete.csv')
df2 = pd.read_csv('/Users/hamoon/Desktop/manager.csv')
df1 = pd.read_csv('/Users/hamoon/Desktop/reserve.csv')
df3 = pd.read_csv('/Users/hamoon/Desktop/coach.csv')
# df5 = pd.read_csv('/Users/hamoon/Desktop/facilieties_management.csv')



A1 = wallet()

#/////////////////////////////////////////////////////////////////// شروع منو اصلی با سه گزینه


while True:
    os.system('clear')
    print('Welcome to Main Menu :\n')
    print('1.Athlete')
    print('2.Coach')
    print('3.Manager\n\n')


    choice = int(input('Enter your rule \'s number : '))
    os.system('clear')

        
    #///////////////////////////////////////////////////////// شروع athlete
    if choice == 1 :       

        print('1.Sign-up')
        print('2.Loggin')
        print('3.Back\n\n\n')
        choice_100 = int(input('Enter the one you want :'))
        os.system('clear')
        if choice_100 == 3:
            pass


        if choice_100 == 1 :           #sign up

            print('Please fill the blanks corroctly to sign-up seccessfully ')

            name_of_user = input('Enter your name : ')
            age_of_user = int(input('Enter your age: '))
            email_of_user=input('Please Enter your username :')


             #//////////////////////////////////////////////////////// با استفاده از Regex درستی ایمیل واردشده رااز نظر فرمت چک میکنیم

            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            while bool(re.fullmatch(regex,email_of_user)) != True:
                email_of_user=input('Please give a valid email address :')
                
            password_of_user=int(input('Please Enter the password you want  :'))


            
            print('Successfully signed up .')

            A = athlete(name_of_user,age_of_user,email_of_user,password_of_user)
            user_profile = [A.name , A.age , A.email , A.password , 'Athlete']
            with open('/Users/hamoon/Desktop/athlete.csv' , 'a' , newline='') as f :
                writer = csv.writer(f)
                writer.writerow(user_profile)
                
            df = pd.read_csv('/Users/hamoon/Desktop/athlete.csv')
            
            os.system('clear')
                
            
            choice_101 = input('do you want to loggin ? (y/n)')
            if choice_101 == 'y':
                os.system('clear')
                email_user = input('Username : ')
                password_user = int(input('Password : '))
            
                while (df['email'] == email_user).any() and (df['password'] == password_user).any():
                    print('loggin successfully....')
                    break
                else:
                    print('loggin failed')
                    email_user = input('Username : ')
                    password_user = input('Password : ')

        if choice_100 == 2 :           #loggin

            os.system('clear')
            email_user = input('Username : ')
            password_user = int(input('Password : '))
            
            while (df['email'] == email_user).any() and (df['password'] == password_user).any():
                print('loggin successfully....')
                break
            else:
                print('loggin failed')
                email_user = input('Username : ')
                password_user = input('Password : ')
            
        
                

            sleep(2)
            os.system('clear')

            #////////////////////////////////////////////////////////  بعد از ساین اپ و لاگین میرسیم به داشبورد
            while True :
                print('Welcome to dashboard : ')
                print('1.Reservetion ')
                print('2.Change password')   
                print('3.Wallet')
                print('4.Reservetion Data')
                print('5.EXIT\n\n\n')


                choice_1 = int(input('Enter your choice :'))
                if choice_1 == 1 :
                    os.system('clear')
                    print('1.Sport field')
                    print('2.Pool')
                    print('3.GYM\n')
                    choice_2 = int(input('Enter the sport area you want to do :'))

                    if choice_2 == 1 :
                        os.system('clear')
                        print('In sport field we have 3 sport option :')
                        print('1.Football')
                        print('2.Volleyball')
                        print('3.Basketball\n\n\n')
                        choice_3 = int(input('Enter your sport do you want :'))
                        
                        #///////////////////////////////////////////////////////////////////////////////////////////////////#football

                        if choice_3 == 1 :
                            os.system('clear')

                            if A1.cash >= 80: 
                                print('These times are available for football :')
                                print('1.Monday / 4 - 6')
                                print('2.Wendsday / 4 - 6')
                                print('3.Friday / 4 - 6')

                                choice_4 = int(input('Which one is your best time in the week ?'))
                                if choice_4 == 1 :
                                    os.system('clear')
                                    day = 'monday'
                                    hours = '4/6'
                                if choice_4 == 2 :
                                    os.system('clear')
                                    day = 'wendsday'
                                    hours = '4/6'
                                if choice_4 == 3 :
                                    os.system('clear')
                                    day = 'friday'
                                    hours = '4/6'
                                
                                os.system('clear')
                                print('1.Juegen klopp')
                                print('2.Pep guardiula')
                                print('3.Zeidane')
                                choice_6 = int(input('Which coach do you want ?'))
                                if choice_6 == 1 :
                                    print('Juegen klopp selected')
                                    coach ='Juegen klopp'
                                if choice_6 == 2 :
                                    print('Pep guardiula selected')
                                    coach ='Pep guardiula'
                                if choice_6 == 3 :
                                    print('Zeidane selected')
                                    coach ='Zeidane'

                                A1.cash = A1.cash - 80
                                print('$80 was withdrawn from the account.')


                                B = football(day,hours,coach)
                                user_profile1 = [email_user , password_user ,'Football', day , hours ,coach]
                                with open('/Users/hamoon/Desktop/reserve.csv' , 'a' , newline='') as f1 :
                                    writer = csv.writer(f1)
                                    writer.writerow(user_profile1)
                                sleep(2)


                            else:
                                print('you do not have enough money')

                            #///////////////////////////////////////////////////////////////////////////////////////////////////volleyball
                            


                        if choice_3 == 2 :
                            if A1.cash >= 70:
                                os.system('clear')
                                print('These times are available for Volleyball :')
                                print('1.Monday / 2 - 4')
                                print('2.Wendsday / 2 - 4')
                                print('3.Friday / 2 - 4')

                                choice_4 = int(input('Which one is your best time in the week ?'))
                                if choice_4 == 1 :
                                    os.system('clear')
                                    day = 'monday'
                                    hours = '2/4'
                                if choice_4 == 2 :
                                    os.system('clear')
                                    day = 'wendsday'
                                    hours = '2/4'
                                if choice_4 == 3 :
                                    os.system('clear')
                                    day = 'friday'
                                    hours = '2/4'

                                os.system('clear')
                                print('1.Vellasco')
                                print('2.Kovač')
                                print('3.Rezende')
                                choice_6 = int(input('Which coach do you want ?'))
                                if choice_6 == 1 :
                                    print('Vellasco selected')
                                    coach ='Vellasco'
                                if choice_6 == 2 :
                                    print('Kovač selected')
                                    coach ='Kovač'
                                if choice_6 == 3 :
                                    print('Rezende selected')
                                    coach ='Rezende'
                                
                                A1.cash = A1.cash - 70
                                print('$70 was withdrawn from the account.')

                                C = volleyball(day,hours,coach)
                                user_profile2 = [email_user , password_user ,'Volleyball', day , hours ,coach]
                                with open('/Users/hamoon/Desktop/reserve.csv' , 'a' , newline='') as f1 :
                                    writer = csv.writer(f1)
                                    writer.writerow(user_profile2)
                                sleep(2)
                            else:
                                print('you do not have enogh money')
                                
                        
                        #///////////////////////////////////////////////////////////////////////////////////////////////////#basketball

                        if choice_3 == 3 :
                            os.system('clear')
                            if A1.cash >= 60:

                                print('These times are available for Basketball :')
                                print('1.Monday / 6 - 8')
                                print('2.Wendsday / 6 - 8')
                                print('3.Friday / 6 - 8')

                                choice_4 = int(input('Which one is your best time in the week ?'))
                                if choice_4 == 1 :
                                    os.system('clear')
                                    day = 'monday'
                                    hours = '6 - 8'
                                if choice_4 == 2 :
                                    os.system('clear')
                                    day = 'wendsday'
                                    hours = '6 - 8'
                                if choice_4 == 3 :
                                    os.system('clear')
                                    day = 'friday'
                                    hours = '6 - 8'

                                os.system('clear')
                                print('1.Phill Jackson')
                                print('2.Lenny Wilkens')
                                choice_6 = int(input('Which coach do you want ?'))
                                if choice_6 == 1 :
                                    print('Phill Jackson selected')
                                    coach ='Phill Jackson'
                                if choice_6 == 2 :
                                    print('Lenny Wilkens selected')
                                    coach ='Lenny Wilkens'

                                A1.cash = A1.cash - 60
                                print('$60 was withdrawn from the account.')

                                D = basketball(day,hours,coach)
                                user_profile3 = [email_user , password_user ,'Basketball', day , hours ,coach]
                                with open('/Users/hamoon/Desktop/reserve.csv' , 'a' , newline='') as f1 :
                                    writer = csv.writer(f1)
                                    writer.writerow(user_profile3)
                                sleep(2)
                            else : 
                                print('you do not have enogh money')




                        #////////////////////////////////////////////////////// بخش انتخاب روز و ساعت 
                    elif choice_2 == 2 :
                        os.system('clear')
                        if A1.cash >= 40:
                            print('These times are available for pool :')
                            print('1.Monday')
                            print('2.Theuseday')
                            print('3.Wendsday ')
                            print('4.Thursday')
                            print('5.Friday')

                            choice_5 = int(input('Pool is available every day at 4-10 .pm , which day is best for you?'))
                            if choice_5 == 1 :
                                os.system('clear')
                                day = 'Monday'
                            if choice_5 == 2 :
                                os.system('clear')
                                day = 'Theuseday'
                            if choice_5 == 3 :
                                os.system('clear')
                                day = 'Wendsday'
                            if choice_5 == 4 :
                                os.system('clear')
                                day = 'Thursday'
                            if choice_5 == 5 :
                                os.system('clear')
                                day = 'Friday'
                            hours = '4/10'

                            A1.cash = A1.cash - 40
                            print('$40 was withdrawn from the account.')
                            
                            os.system('clear')
                            print('We have 1 coach for swiming right now , his name is Mr.Swimmer')
                            coach = 'Mr.Swimmer'
                            
                        
                            E = swim(day,hours,coach)

                            #کل اطلاعات رزرو مثل روز و ساعت و مربی رو در فایل سی اس وی رزرو مینویسیم 

                            user_profile4 = [email_user , password_user ,'Swiming', day , hours ,coach]
                            with open('/Users/hamoon/Desktop/reserve.csv' , 'a' , newline='') as f1 :
                                writer = csv.writer(f1)
                                writer.writerow(user_profile4)
                            sleep(2)
                        else : 
                                print('you do not have enogh money')


                    elif choice_2 == 3 :
                        os.system('clear')
                        if A1.cash >= 100:

                            print('These times are available for gym :')
                            print('1.Monday')
                            print('2.Theuseday')
                            print('3.Wendsday ')
                            print('4.Thursday')
                            print('5.Friday')

                            choice_5 = int(input('GYM is available every day, which day is best for you?'))
                            if choice_5 == 1 :
                                os.system('clear')
                                day = 'Monday'
                            if choice_5 == 2 :
                                os.system('clear')
                                day = 'Theuseday'
                            if choice_5 == 3 :
                                os.system('clear')
                                day = 'Wendsday'
                            if choice_5 == 4 :
                                os.system('clear')
                                day = 'Thursday'
                            if choice_5 == 5 :
                                os.system('clear')
                                day = 'Friday'

                            A1.cash = A1.cash - 100
                            print('$100 was withdrawn from the account.')

                            os.system('clear')
                            print('We have 1 coach for gym righ now , his name is Mr.Fitman')
                            coach = 'Mr.Fitman'
                            hours = '2/10'

                            F = swim(day,hours,coach)
                            user_profile5 = [email_user , password_user ,'Gym', day , hours ,coach]
                            with open('/Users/hamoon/Desktop/reserve.csv' , 'a' , newline='') as f1 :
                                writer = csv.writer(f1)
                                writer.writerow(user_profile5)
                            sleep(2)
                        else : 
                                print('you do not have enogh money')






                if choice_1 == 2 :
                    os.system('clear')
                    old_password = int(input('Enter the OLD password : '))
                    new_password = int(input('Enter the NEW password :' ))
                    user_rows = df.loc[df['email'] == email_user]
                    df.loc[user_rows.index, 'password'] = new_password
                    df.to_csv('/Users/hamoon/Desktop/athlete.csv', index=False)
                    print('Seccessfully changed the password from %i to %i' %(old_password ,new_password))
                    sleep(3)
                







                while choice_1 == 3 :
                    os.system('clear')
                    print('1.Increase credit')
                    print('2.Credit withdrawal')
                    print('3.Credit View')
                    print('4.Receive gift credit')
                    print('5.Back')

                    choice_7 = int(input('Which one do you want to go ? '))
                    
                    

                    if choice_7 == 1 :
                        os.system('clear')
                        aded_amout = int(input('Enter the desired amount:'))
                        A1.add_cash(aded_amout)
                        

                    if choice_7 == 2 :
                        os.system('clear')
                        withdrawal_amount = int(input('Enter the desired amount:'))
                        A1.cash -= withdrawal_amount
                        print('%i money withdrawal your wallet' %(withdrawal_amount))
                

                    if choice_7 == 3 :
                        print(A1.cash)
                       
                        if A1.cash >= 100:
                            user_profile4 = [email_user , password_user ,A1.cash,'level 1']
                            with open('/Users/hamoon/Desktop/financial.csv' , 'a' , newline='') as f2 :
                                writer = csv.writer(f2)
                                writer.writerow(user_profile4)

                        if 50 < A1.cash and A1.cash < 100:
                            user_profile4 = [email_user , password_user ,A1.cash,'level 2']
                            with open('/Users/hamoon/Desktop/financial.csv' , 'a' , newline='') as f2 :
                                writer = csv.writer(f2)
                                writer.writerow(user_profile4)

                        if A1.cash <= 50 :
                            user_profile4 = [email_user , password_user ,A1.cash,'level 3']
                            with open('/Users/hamoon/Desktop/financial.csv' , 'a' , newline='') as f2 :
                                writer = csv.writer(f2)
                                writer.writerow(user_profile4)
                            
                        
                        
                        

                    if choice_7 == 4 :
                        os.system('clear')
                        if A1.cash <= 50 :
                            print('your level is 3 and you do not include gift credit')
                            A1.cash += 0

                        if  50 < A1.cash and A1.cash < 100:
                            print('your level is 2 and you will get 20 gift credits')
                            A1.cash += 20

                        if A1.cash >= 100:
                            print('your level is 1 and you will get 50 gift credits')   
                            A1.cash += 50


                    
                    sleep(4)
                    if choice_7 == 5 :
                        break
                    else :
                        print('invalid choice')

                if choice_1 == 4 :
                    
                    # print(df1[df1['email'] == email_user])
                    with pd.option_context('expand_frame_repr', False):
                        print(df1[df1['email'] == email_user])
                        sleep(5)
                
                
                if choice_1 == 5 : 
                    break
                else :
                    print('invalid choice')



        
        
        

        else :
            print('invalid choice')







    #///////////////////////////////////////////////////////// شروع Coach :

    if choice == 2 :
        os.system('clear')
        print('please loggin :')
        email_of_coach = input('Enter your email : ')
        password_of_coach = int(input('Enter your password :'))
        while (df3['email'] == email_of_coach).any() and (df3['password'] == password_of_coach).any():
            print('loggin successfully....')
            break
        else:
            print('loggin failed')
            email_of_coach = input('Username : ')
            password_of_coach = input('Password : ')

        os.system('clear')
        while True :
            os.system('clear')
            print('coach menu : ')
            print('1.Add a supplement')
            print('2.visit supplements')
            print('3.visit profile')
            print('4.Exit')

            list_supplement = []
            list_supplement_energy = []
            list_supplement_num = []



            coach_menu = int(input('select your option: '))
            
            if coach_menu == 1:
                os.system('clear')
                print('please enter the supplements feature : ')
                supplement_name = input('supplement name :')
                supplement_energy = int(input('supplement energy: '))
                supplement_number_day = int(input('Number per day:'))

                list_supplement.append(supplement_name)
                list_supplement_energy.append(supplement_energy)
                list_supplement_num.append(supplement_number_day)


            if coach_menu == 2:
                os.system('clear')
                print(list_supplement)
                print(list_supplement_energy)
                print(list_supplement_num)
                sleep(4)

            if coach_menu == 3:
                os.system('clear')
                result = df3[df3['email'] == email_of_coach]
                print(result)
                sleep(5)

            if coach_menu == 4 :
                break

        
            
            

        
        

        

            # coach کامل نیس /\








    #///////////////////////////////////////////////////////// شروع Manager :



    if choice == 3 :
        os.system('clear')
        print('please loggin :')
        email_of_manager = input('Enter your email : ')
        passwoed_of_manager = int(input('Enter your password :'))
        G = manager('alimohammadi' , 40 , email_of_manager, passwoed_of_manager)

        while (df2['email'] == email_of_manager).any() and (df2['password'] == passwoed_of_manager).any():
            print('loggin successfully....')
            break
            
        else:
            print('loggin failed')
            email_of_manager = input('Username : ')
            password_upasswoed_of_manager = input('Password : ')
            os.system('clear')
            #/////////////////////////////////////////////////////////// منوی اصلی مدیر :

        while True:
            os.system('clear')
            print('1.do you want to see anybody profile ')
            print('2.change users password ')
            print('3.Define a new user')
            print('4.All athletes')
            print('5.All coaches')
            print('6.Manpower management')
            print('7.Facilieties management')
            print('8.Inventory management')
            print('9.Delete user')
            print('10.EXIT\n')
            
            choice_9 = int(input('which one :'))
            

            if choice_9 == 1:
                os.system('clear')
                print('1.athlete info ')
                print('2.reserevetion info ')
                
                choice_10 = int(input('which one : '))
                if choice_10 == 1:    
                    os.system('clear')
                    search_user = input('please type the man s username :')
                    print(df[df['email'] == search_user])

                    back = input('Enter [y] to go back :')
                    while back != 'y' :
                        back = input('Enter [y] to go back :')
                    else :
                        pass
                if choice_10 == 2:
                    os.system('clear')
                    search_user = input('please type the man s username :')
                    print(df1[df1['email'] == search_user])
                    back = input('Enter [y] to go back :')
                    while back != 'y' :
                        back = input('Enter [y] to go back :')
                    else :
                        pass
                    
                



            if choice_9 == 2:

                os.system('clear')
                email_of_user_for_password_chang = input('Enter the email of who you want to change his password : ')
                user_rows = df.loc[df['email'] == email_of_user_for_password_chang]
                new_password = int(input('Enter the NEW password :' ))
                df.loc[user_rows.index, 'password'] = new_password
                df.to_csv('/Users/hamoon/Desktop/athlete.csv', index=False)
                os.system('clear')
                print('successfully changed the password of user ... ')
                sleep(3)

            if choice_9 == 3:
                os.system('clear')
                print('Please fill the blanks corroctly to sign-up secsesfully ')

                name_of_user_1 = input('Enter the name of new user : ')
                age_of_user_1 = int(input('Enter the age of new user : '))
                email_of_user_1 =input('Please Enter the username  :')
                
                regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                while bool(re.fullmatch(regex,email_of_user_1)) != True:
                    email_of_user_1=input('Please give a valid email address :')
                    
                password_of_user_1 =input('Please Enter the password for new user  :')

                A = athlete(name_of_user_1,age_of_user_1,email_of_user_1,password_of_user_1)
                user_profile10= [A.name , A.age , A.email , A.password,'athlete']
                with open('/Users/hamoon/Desktop/athlete.csv' , 'a' , newline='') as f :
                    writer = csv.writer(f)
                    writer.writerow(user_profile10)
                os.system('clear')
                print('Successfully created a user profile ...')
                sleep(3)
            
            if choice_9 == 4 :
                os.system('clear')
                print(df)
                sleep(5)
                
            if choice_9 == 5 :
                os.system('clear')
                print(df3)
                sleep(5)
            
            if choice_9 == 6 :
                os.system('clear')
                result = pd.concat([df2, df3 , df])
                result.to_csv('/Users/hamoon/Desktop/manpower.csv' , index=False)
                df4 = pd.read_csv('/Users/hamoon/Desktop/manpower.csv')
                print(df4)
                sleep(5)
                 
            if choice_9 == 7:
                os.system('clear')
                print('Sport Complex :')
                print(df5)
                fac1 = input('Enter [y] to go back :' )
                if fac1 == 'y':
                    pass
                else :
                    print('Invalid choice')
                    fac2 = input('Enter [y] to go back :' )
                    if fac2 == 'y':
                        pass

            if choice_9 == 8:
                os.system('clear')
                while True:
                    os.system('clear')
                    print('Welcome to inventory management :\n\n')
                    print('1.Football\n')
                    print('2.Volleyball\n')
                    print('3.Basketball\n')
                    print('4.Pool\n')

                    select1 = int (input('Choose one of them :\n'))
                    os.system('clear')

                    while select1 == 1 :
                        os.system('clear')
                        print('Football inventory management :\n')
                        print('1.Enter information')
                        print('2.Check information')
                        print('3.Report information')
                        print('4.Back\n')

                        select2 = int(input('Enter your choice :'))

                        if select2 == 1 :
                            os.system('clear')
                            print('\nEnter information\n\n')
                            print('1.Football Ball\n')
                            ball_f = int (input('Enter the number of balls in the club : '))
                            print('\n2.Football Lawn\n')
                            print('Select the lawn condition number :')
                            lawn_f = int (input('1.Usable and Healthy\t 2.Dangerous and Unhealthy\n'))
                            print('\n3.Football Goal and Net\n')
                            goal_f = int (input('Enter the number of goals in the club : '))
                            net_f = int (input("Enter the number of goal's net in the club : "))
                            

                        if select2 == 2:
                            os.system('clear')
                            print('Check information\n\n')
                            print('Football balls condition :\n')
                            if ball_f <= 2 :
                                print('!!  LACK OF FOOTBALL BALLS  !!\n\n')
                            else:
                                print('Normal\n')

                            print('Football lawn condition :\n')
                            if lawn_f == 1 :
                                print('Normal\n')
                            elif lawn_f == 2:
                                print('!!  FOOTBALL LAWN IS DANGEROUS  !!\n\n')
                            else:
                                print('invalid choice\n')
                            
                            print('Football goals condition :\n')
                            if goal_f <=2 :
                                print('!!  LACK OF FOOTBALL GOALS  !!\n\n')
                            elif goal_f > 2:
                                print('Normal\n')

                            print('Football nets condition :\n')
                            if net_f <= 2 :
                                print('!!  LACK OF FOOTBALL NETS  !!\n\n')
                            else:
                                print('Normal\n')
                            
                            select3 = input('Do you want to go back ?(y,n)')
                            while select3 == 'y':
                                break
                            else :
                                print('please enter valid ')
                                select3 = input('Do you want to go back ?')
                            

                        
                        if select2 == 3:
                            os.system('clear')
                            print('Report information\n\n')
                            print('Number of Football balls :'+ str(ball_f) +'\n')
                            if lawn_f == 1 :
                                print('The lawn condition is Usable and Healthy\n')
                            if lawn_f == 2:
                                print('The lawn condition is Dangerous and Unhealthy\n')
                            if lawn_f >= 2:
                                print('invalid choice\n')
                            print('Number of Football goals :'+ str(goal_f) +'\n')
                            print('Number of Football nets :'+ str(net_f) +'\n')

                            sleep(7)

                        if select2 == 4:
                            break
                        else:
                            print('invalid choice')


                    while select1 == 2 :
                        os.system('clear')
                        print('Volleyball inventory management :\n')
                        print('1.Enter information')
                        print('2.Check information')
                        print('3.Report information')
                        print('4.Back\n')

                        select2 = int(input('Enter your choice :'))
                        
                        
                        if select2 == 1 :
                            os.system('clear')
                            print('\nEnter information\n\n')
                            print('1.Volleyball Ball\n')
                            ball_v = int (input('Enter the number of balls in the club : '))
                            print('2.Volleyball Net\n')
                            net_v = int (input("Enter the number of nets in the club : "))
                            print('3.Select the net condition number :\n')
                            net1_v = int (input('1.Usable and Healthy\t 2.Dangerous and Unhealthy\n'))
                            
                    
                        if select2 == 2:
                            os.system('clear')
                            print('Check information\n\n')
                            print('Volleyball balls condition :\n')
                            if ball_v <= 2 :
                                print('!!  LACK OF VOLLEYBALL BALLS  !!\n\n')
                            else:
                                print('Normal\n')

                            print('Volleyball nets numbers condition :\n')
                            if net_v <= 2 :
                                print('!!  LACK OF VOLLEYBALL NETS  !!\n\n')
                            else:
                                print('Normal\n')
                            
                            print('Volleyball net condition :\n')
                            if net1_v == 1 :
                                print('Normal\n')
                            elif net1_v == 2:
                                print('!!  VOLLEYBALL NET NEEDS TO CHANGE  !!\n\n')
                            else:
                                print('invalid choice\n')

                            select3 = input('Do you want to go back ?(y,n)')
                            while select3 == 'y':
                                break
                            else :
                                print('please enter valid ')
                                select3 = input('Do you want to go back ?')
                        
                        if select2 == 3:
                            os.system('clear')
                            print('Report information\n\n')
                            print('Number of Volleyball balls :'+ str(ball_v) +'\n')
                            print('Number of Volleyball nets :'+ str(net_v) +'\n')
                            if net1_v == 1 :
                                print('The net condition is Usable and Healthy\n')
                            if net1_v == 2:
                                print('The net condition is Dangerous and Unhealthy\n')
                            if net1_v >= 2:
                                print('invalid choice\n')
                            
                            sleep(7)
                        
                        if select2 == 4 :
                            break

                        else:
                            print('invalid choice')
                            
                            
                    while select1 == 3 :
                        os.system('clear')
                        print('Basketball inventory management :\n')
                        print('1.Enter information')
                        print('2.Check information')
                        print('3.Report information')
                        print('4.Back\n')


                        select2 = int(input('Enter your choice :'))
                        
                        
                        if select2 == 1 :
                            os.system('clear')
                            print('Enter information\n\n')
                            print('1.Basketball Ball\n')
                            ball_b = int (input('Enter the number of balls in the club : '))
                            print('2.Basketball Net\n')
                            net_b = int (input("Enter the number of nets in the club : "))
                            print('3.Select the net condition number :\n')
                            net1_b = int (input('1.Usable and Healthy\t 2.Dangerous and Unhealthy\n'))
                            
                    
                        if select2 == 2:
                            os.system('clear')
                            print('Check information\n\n')
                            print('Basketball balls condition :\n')
                            if ball_b <= 2 :
                                print('!!  LACK OF BASKETBALL BALLS  !!\n\n')
                            else:
                                print('Normal\n')

                            print('Basketball nets numbers condition :\n')
                            if net_b <= 2 :
                                print('!!  LACK OF BASKETBALL NETS  !!\n\n')
                            else:
                                print('Normal\n')
                            
                            print('Basketball net condition :\n')
                            if net1_b == 1 :
                                print('Normal\n')
                            elif net1_v == 2:
                                print('!!  BASKETBALL NET NEEDS TO CHANGE  !!\n\n')
                            else:
                                print('invalid choice\n')

                            select3 = input('Do you want to go back ?(y,n)')
                            while select3 == 'y':
                                break
                            else :
                                print('please enter valid ')
                                select3 = input('Do you want to go back ?')
                        
                        
                        if select2 == 3:
                            os.system('clear')
                            print('Report information\n\n')
                            print('Number of Basketball balls :'+ str(ball_b) +'\n')
                            print('Number of Basketball nets :'+ str(net_b) +'\n')
                            if net1_b == 1 :
                                print('The net condition is Usable and Healthy\n')
                            if net1_b == 2:
                                print('The net condition is Dangerous and Unhealthy\n')
                            if net1_b >= 2:
                                print('invalid choice\n')
                            
                            sleep(7)

                        if select2 == 4:
                            break
                        
                        else:
                            print('invalid choice\n')
                            
                    
                    while select1 == 4 :
                        os.system('clear')
                        print('Pool inventory management :\n')
                        print('1.Enter information')
                        print('2.Check information')
                        print('3.Report information\n')
                        print('4.Back\n')


                        select2 = int(input('Enter your choice :'))
                        
                        
                        if select2 == 1 :
                            os.system('clear')
                            print('Enter information\n')
                            print('1.The percentage of chlorine in the pool water :\n')
                            chlorine = int (input('1.less than 2%\t 2.between 2 - 3%\t 3.more than 3%\n'))
                            print('2.Pool Slippers \n')
                            slipper = int (input("Enter the number of slippers in the pool : "))
                            print('3.Pool Life Ring and Life Jacket \n')
                            jacket = int(input("Enter the number of pool life rings and life jackets in the pool : "))
                            

                        if select2 == 2:
                            os.system('clear')
                            print('Check information\n\n')
                            print('Chlorine in the pool condition :\n')
                            if chlorine == 1 :
                                print('!!  LACK OF CHLORINE IN POOL  !!\n\n')
                            elif chlorine == 2 :
                                print('Normal\n')
                            elif chlorine == 3 :
                                print('!!  EXCESS OF CHLORINE IN POOL  !!\n\n')
                            else:
                                print('invalid choice\n')
                            
                            print('Pool slipper numbers condition :\n')
                            if slipper <= 12 :
                                print('!!  LACK OF POOL SLIPPERS  !!\n\n')
                            else:
                                print('Normal\n')
                            
                            print('Pool Life Ring and Life Jacket condition :\n')
                            if jacket <= 5 :
                                print('!!  LACK OF POOL LIFE RING AND LIFE JACKET  !!\n\n')
                            else:
                                print('Normal\n')

                            select3 = input('Do you want to go back ?(y,n)')
                            while select3 == 'y':
                                break
                            else :
                                print('please enter valid ')
                                select3 = input('Do you want to go back ?')
                    
                        if select2 == 3:
                            os.system('clear')
                            print('Report information\n\n')
                            if chlorine == 1 :
                                print('The chlorine in the pool is low(less than 2%)\n')
                            if chlorine == 2:
                                print('The chlorine in the pool is normal(between 2-3%)\n')
                            if chlorine == 3:
                                print('The chlorine in the pool is high(more than 2%)\n')
                            print('Number of Pool slippers :'+ str(slipper) +'\n')
                            print('Number of Pool Life Ring and Life Jacket :'+ str(jacket) +'\n')
                            sleep(7)

                        if select2 == 4:
                            break

                        else:
                            print('invalid choice\n')
                            

                    
                    else:
                        print('invalid choice\n')
            
            while choice_9 == 9:
                os.system('clear')
                print('1.delete reservetion')
                print('2.delete user')
                print('3.Back')
                choice_12 = int(input('which one ?'))
                if choice_12 == 2 :
                    del_username = input('Please enter the username you want to delete :')
                    del_password = int(input('Please enter the password of that username :'))
                    rows_to_delete = df[(df['email'] == del_username) & (df['password'] == del_password)].index
                    while (df['email'] == del_username).any() & (df['password'] == del_password).any() :
                        df = df.drop(rows_to_delete)
                        df.to_csv('/Users/hamoon/Desktop/athlete.csv', index=False)
                        print('secussesfully DELETED the user')
                        sleep(5)
                    else :
                        print('Cant DELETE user , the information you filled is not correct')
                        sleep(5)

                if choice_12 == 1 :
                    del_username1 = input('Please enter the username you want to delete his reservetion:')
                    del_password1 = int(input('Please enter the password of that username  :'))
                    rows_to_delete1 = df1[(df1['email'] == del_username1) & (df1['password'] == del_password1)].index
                    while (df1['email'] == del_username1).any() & (df1['password'] == del_password1).any() :
                        df1 = df1.drop(rows_to_delete1)
                        df1.to_csv('/Users/hamoon/Desktop/reserve.csv', index=False)
                        print('secussesfully DELETED the reservetion of this user')
                        sleep(5)
                    else :
                        print('Cant DELETE reservetion , the information you filled is not correct')
                        sleep(5)

                if choice_12 == 3 :
                    break

                else :
                    print('Invalid choice')

                



            if choice_9 == 10:
                break

            else :
                print('invalid choice')
            

    else :
        print('invalid choice')
