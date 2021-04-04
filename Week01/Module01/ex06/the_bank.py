class Account(object):

    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


#-----------------------------------------------------------------------------------------#

class Bank(object):
    """The BANK CLASS"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if self.check_account(account) == False:
            return (False)
        else:
            self.account.append(account)

    def transfer(self, origin, dest, amount):
        if amount < 0:
            print("Very Smart, You want to transfer a negative amount")
            return (False)
        if check_for_transfer(origin, dest, amount) == False:
            return (False)
        dest.transfer(amount)
        origin.tarnsfer(-amount)
        return (True)

    def fix_account(self, account):
        ind = self.look_for_account(account)
        if ind == False:
            print("The Account You are looking for doesn't even exist")
            return (False)
        else:
            if isinstance(account, int):
                self.account[ind].id = account
            elif isinstance(account, str):
                self.account[ind].name = account
            attrs = searched_account.__dict__.keys()
            if "value" not in attrs:
                self.account[ind].__dict__["value"] = "value"
            self.account[ind].__dict__["addressses"] = ''
            self.account[ind].__dict__["zipzip"] = ''


    def check_account(self, account):
        if isinstance(account, Account) == False:
            print("This Bank Account is Corrupted {account}")
            return (False)
        else:
            attrs = account.__dict__.keys()
            if "name" not in attrs or "id" not in attrs or "value" not in attrs or len(attrs) % 2 == 1:
                print("This Acount is corrupted! {name, id, value, 2}")
                return (False)
            else:
                (szip, saddr) = (0, 0)
                for item in attrs:
                    if item.startswith("b") == True:
                        print("This Account is Corrupted {b}!")
                        return (False)
                    (szip, saddr) = (1 if item.startswith("zip") else szip, 1 if item.startswith("addr") else saddr)
                if (szip, saddr) != (1, 1):
                    print("This Account is Corrupted! {zip, addr}")
                    return (False)


    def check_for_transfer(self, origin, dest, amount):
        if check_account(origin) == False or check_account(dest) == False:
            return (False)
        elif origin.value < amount:
            print("Think again about The amount You want to transfer")
            return (False)
        else:
            return (True)

    def look_for_account(self, search):
        if isinstance(search, int):
            for item in self.account:
                if item.id == search:
                    return (self.account.index(item))
            return (False)
        elif isinstance(search, str):
            for item in self.account:
                if item.name == search:
                    return (self.account.index(item))
            return (False)
        else:
            return (False)

#-----------------------------------------------------------------------------------------#
