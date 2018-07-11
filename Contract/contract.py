class Contract:
    def __init__(self, name, phone, email, addr):
        self.name = name;
        self.phone = phone;
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name : ", self.name)
        print("phone: ", self.phone)
        print("email : ", self.email)
        print("addr : ", self.addr)



def run():
    kim = Contract('kim', '0101234123', 'est@test.com', "인천")
    kim.print_info()

if __name__ == '__main__':
    run()
