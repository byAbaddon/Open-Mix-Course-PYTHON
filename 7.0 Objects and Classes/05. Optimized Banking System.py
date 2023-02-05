class BankAccount:
    def __init__(self, ):
        self.lst = []

    def add_data(self, bank, name, balance):
        self.lst.append({'bank': bank, 'name': name, 'balance': float(balance)})

    def result(self):
        sort_lst = sorted(self.lst, key=lambda x: (-x['balance'], len(x['bank'])))
        [print(f"{x['name']} -> {x['balance']:.2f} ({x['bank']})") for x in sort_lst]


account = BankAccount()
while True:
    try:
        bank_name, user_name, user_balance = input().split(' | ')
        account.add_data(bank_name, user_name, user_balance)
    except:
        account.result()
        break

'''
input:
DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
end

output:
Aleksander -> 20000.00 (DSK)
Aleksander -> 20000.00 (Piraeus)
Pesho -> 2000.40 (DSK)
Ivan -> 504.40 (DSK)
Ivan -> 504.40 (Piraeus)
'''
