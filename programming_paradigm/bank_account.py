class BankAccount:
  def __init__(self, initial_balance=0):
    """Initialize the bank account with an optional initial balance."""
    self.account_balance = initial_balance


  def deposit(self, amount):
    """Add the specified amount to the account balance."""
    if amount < 0:
      raise ValueError("Deposit amount must be non-negative")
    self.account_balance += amount


  def withdraw(self, amount):
    """Withdraw the specified amount if sufficient funds exist.
    Returns True if successful, otherwise False.
    """
    if amount < 0:
      raise ValueError("Withdrawal amount must be non-negative")
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    return False


  def display_balance(self):
    """Print the current account balance."""
    print(f"Current Balance: ${self.account_balance:.2f}")
