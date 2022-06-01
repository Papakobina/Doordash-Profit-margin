class Doordash:

  
  def __init__(self, distance, pay, time, gas, action, wageperhour):
    self.distance = distance
    self.pay = pay
    self.time = time

    used_gas = (((distance)/ 100) * 12) * 1.399
    self.gas = used_gas
    profit = pay - used_gas
    self.action = profit
    self.wageperhour = (profit/time)
    

    

results = Doordash(19, 12, 20, True, True, True )
if results.wageperhour < 0.25:
  Wage = "below"
else:
  Wage = "above"
  
print(f"You will spend {results.gas} in gas and make {Wage} minimum wage")


