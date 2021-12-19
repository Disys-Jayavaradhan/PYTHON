class restaurant:
    def __init__(self,rn,rp):
        self.restaurant_name=rn
        self.restaurant_phone=rp
        if type(self.restaurant_name) == str:
            if len(self.restaurant_phone) <=10:
                print("AMR")
            else:
                raise ValueError("enter vaild data")
jv=restaurant("AMR",564654)
