class facebook:

    friendlist={}
    Login={}
    database={}
    groups=[]
    common=[]

    def __init__(self):
        print("***************LOGIN TO FACEBOOK************** ")
        print()
        self.enter=input("sign in or sign up: ")
        if self.enter == "sign in" :
            print("************************sign in to facebook*************************** ")
            print()
            self.user_name=input("Enter your Mail Id: ")
            self.password=input("Enter your password: ")
            if isinstance(self.user_name,str) and isinstance(self.password,str):
                if self.user_name in database and self.database(self.user_name
                elif self.enter == "sign up":
            print("************************* sign up to facebook************************** ")
            print()
            self.user_name=input("Enter your Name: ")
            self.E_mail=input("Enter your mail ID: ")
            self.password=input("Enter you password; ")
            if isinstance(self.user_name,str) and isinstance(self.E_mail,str) and isinstance(self.password,str):
                if self.E_mail[-10:] == "@gmail.com" and self.password.isalnum(self.password) == True:
                    self.database[self.user_name]=self.password
                elif:
                    raise TypeError("Invalid Datatype")
                print(self.database)
                    
        #self.name=input("Enter your friend's name  : ")
        #self.id=input("Enter your friend's id: ")
        #self.add()
        
    def add(self):
        self.friendlist[self.name]=self.id
        print(self.friendlist)

jv=facebook()

