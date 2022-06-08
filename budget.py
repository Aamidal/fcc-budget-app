class Category:
  """Define a budget category class, named by user. Basic deposit, withdrawal, transfer and balance checking functionality."""
  def __init__(self, category):
      self.category = category
      self.balance = 0
      self.ledger = []

  def __repr__(self):
      title = self.category.center(30, "*") + '\n'
      transactions = ""
      total = f'Total: {self.balance}'
      for i in self.ledger:
          desc, amt = str(i['description']), "{:.2f}".format(i['amount'])
          line = desc[0:23].ljust(23) + amt.rjust(7) + "\n"
          transactions += line

      return title + transactions + total
  
  def check_funds(self, amount):
      if amount > self.balance:
          return False
      else:
          return True

  def deposit(self, amount, description = ""):
      self.balance += amount
      self.ledger.append(
          {"amount": amount, "description": description}
      )

  def withdraw(self, amount, description = ""):
      if self.check_funds(amount) == True:
          self.balance -= amount
          self.ledger.append(
          {"amount": -amount, "description": description}
          )
          return True
      else: 
          return False

  def get_balance(self):
      return self.balance
  
  def transfer(self, amount, destination):
      if self.check_funds(amount) == True:
          self.withdraw(amount, f"Transfer to {str(destination.category)}")
          destination.deposit(amount, f"Transfer from {self.category}")
          return True
      else:
          return False



def create_spend_chart(categories):
  """Create bar graph using passed categories, displaying percentage of total spending per category"""

  # Find total lines
  items = len(categories)
  if items == 0:
      return 'Invalid input. Provide at least 1 category.'
  chart = 'Percentage spent by category\n'
  data = []
  lines = 0
  total = 0.00

  # Calculate total spend across categories
  for c in categories:
      if lines < len(c.category): lines = len(c.category)

      spent=0.00
      for spend in c.ledger:
          if spend['amount']<0:
              spent += spend['amount']
      total += spent
      data.append([c.category, abs(spent)])

  total = abs(total)
  
  # Percentage of total spend per category
  for d in data:
      percent = d[1] / total * 100
      d [1] = percent
    
  # Formatting the chart
  for n in reversed(range(11)):
      n = n * 10
      num = str(n)
      line = str()
      if num == '0':
          line += ' '
      if num != '100':
          line += ' '
      line += num + '|'

      for d in data:
          if n < d[1]:
              line += ' o '
          else:
              line += '   '

      chart += line + ' \n'
  
  chart += '    -'
  
  for n in range(items):
      chart += '---'
  
  for n in range(lines):
      chart += '\n    '
      for d in data:
          try:
              chart += ' ' + d[0][n]+ ' '
          except:
              chart += '   '
      chart += ' '

  return chart