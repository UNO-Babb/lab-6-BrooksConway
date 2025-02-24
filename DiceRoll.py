#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

start = 1
end = 6

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
D1 = random.randint(start, end)
print(D1)

D2 = random.randint(start, end)
print(D2)

  #find the sum total of the two dice
sumD = D1 + D2
print(sumD)
  #print statictics for dice rolls


if __name__ == '__main__':
  main()
