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
        if check_account(account) == False:
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



    def check_account(self, acount):
        if not account.id or not account.name or not account.value:
            print("This Bank Acouunt is Corrupted")
            return (False)
        elif isinstance(account, Account) == False or len(account.__dict__) % 2 != 0:
            print("This Bank Account is Corrupted")
            return (False)
        else:
            name = account.name
            if name.startswith("b") or name.startswith("zip") or name.startswith("addr"):
                print("This Bank Account is Corrupted")
                return (False)
            else:
                for attr in account.__dict__:
                    if attr.startswith("b") or attr.startswith("zip") or attr.starts_with("addr"):
                        print("This Bank Account is Corrupted")
                        return (False)
                return (True)

    def check_for_transfer(self, origin, dest, amount):
        if check_account(origin) == False or check_account(dest) == False:
            return (False)
        elif origin.value < amount:
            print("Think again about The amount You want to transfer")
            return (False)
        else:
            return (True)

#-----------------------------------------------------------------------------------------#
