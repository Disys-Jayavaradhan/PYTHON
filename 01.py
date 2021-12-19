class phone_contacts:

    Phonecontacts={}
    Phone={}
          


    def __init__ (self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):
        print("*****************************phone Contact*************************")
        self.Firstname=input("First Name: ")
        self.Lastname=input("Last Name: ")
        self.Phone_number=input("Phone Number: ")
        self.Email_ID=input("E-mail  ID: ")
        self.Groups=input("Groups: ")
        self.DOB=input("DOB: ")

    def open_phone_contact(self):
        print("PHONE CONTACTS")

    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 20:
                print("Groups Verified")
            else:
                raise ValueError("First Name should contain lesser than or equal to 15 letters")
        else:
                raise TypeError("First Name should contain letters only")

    def phonenumber_verificatio(self):
        if len(self.phonenumber) == 10:
            if type(self.phonenumber)==int:
                print("Phone Number verified")
            else:
                raise TypeError("Phone number should contain only integers")
        else:
                raise ValueError("Phone number should not be greater than or lesser than 10")

    def emailid_verification(self):
        if type(self.emailid) == str:
            if len(self.emailid) <=25:
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
                raise TypeError("Invalid E-mail ID")

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <=20:
                print("Groups Verified" )
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
                raise TypeError("Groups should contain letter only")

    def dob_verification(self):
        if isinstance(self.dob,str) and isinstance(self.dob,str):
            print("DOB verified")

        else:
            raise ValueError("DOB should contain lesser than or equal to 10 letters")
    


JV=phone_contacts("First Name""Jaya","Lastname""Varadhan","Phone Number""9361486028","Email_ID""jayavaradhan07@gmail.com","Group""Family","DOB""06/04/2007")
JV.open_phone_contacts()
JV.firstname_verification()
JV.lastname_verification()
JV.phonenumber_verification()
JV.emailid_verification()
JV.groups_verification()
JV.dob_verification()
JV.view_contact()


phone=[{"First Name":"Abi","Last Name":"Rithinyaa","Phone Number":9854268725,"Email_id":"abi@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  #DICTIONARY INSIDE LIST
           {"Firstname":"Anu","Lastname":"priyaa","Phno":9987968725,"Email_id":"anu@gmail.com","Groups":"Friends","DOB":"03/05/2001"},]


for i in phone:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                     #KEY VALUES LOOPING
        print(f"{j}:{k}")
