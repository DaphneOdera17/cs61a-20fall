def make_withdraw(balance):
    """Return a withdraw function with a starting balance"""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw