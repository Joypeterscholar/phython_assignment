from _decimal import Decimal

from python_files.Account import Account

account1 = Account("JOY", Decimal(1000.00))

if __name__ == '__main__':
    print(account1)