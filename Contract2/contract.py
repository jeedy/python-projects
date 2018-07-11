class Contract:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print("name: ", self.name)
        print("Phone Number: ", self.phone)
        print("email: ", self.email)
        print("addr: ", self.addr)


def set_contract():
    name = input("name: ")
    phone = input("phone: ")
    email = input("email: ")
    addr = input("address: ")
    contract = Contract(name, phone, email, addr)
    return contract


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def print_contract(contract_list):
    for contract in contract_list:
        contract.print_info()


def delete_contract(contract_list, name):
    for i, contract in enumerate(contract_list):
        if contract.name == name:
            del contract_list[i]


def store_contract(contract_list):
    f = open("contract_db.txt", "wt")
    for contract in contract_list:
        f.write(contract.name + "\n")
        f.write(contract.phone + "\n")
        f.write(contract.email + "\n")
        f.write(contract.addr + "\n")
    f.close()


def load_contract(contract_list):
    f = open("contract_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip('\n')
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        addr = lines[4 * i + 3].rstrip('\n')
        contract = Contract(name, phone, email, addr)
        contract_list.append(contract)
    f.close()


def run():
    contract_list = []
    load_contract(contract_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contract = set_contract()
            contract_list.append(contract)
        elif menu == 2:
            print_contract(contract_list)
        elif menu == 3:
            name = input("삭제할 이름: ")
            delete_contract(contract_list, name)
        elif menu == 4:
            store_contract(contract_list)
            break


if __name__ == "__main__":
    run()
