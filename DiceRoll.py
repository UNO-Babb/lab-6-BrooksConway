#DiceRoll.py
#Name: Brooks Conway
#Date: 2/26/25
#Assignment: Lab 6 Dice
import random

start = 1
end = 6

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numRolls = 1000000
  for count in range(numRolls):
    D1 = random.randint(start, end)

    D2 = random.randint(start, end)

    #find the sum total of the two dice
    sumD = D1 + D2

    rolls[sumD -2] = rolls[sumD -2]+1

    #print statictics for dice rolls
  
  num = 2
  for r in rolls:
    percent = round(r/ numRolls * 100, 1)
    print(num, ":", r)
    num = num + 1
if __name__ == '__main__':
  main()
