#WordIndex.py
#Name:Brooks Conway
#Date:2/26/25
#Assignment:Lab 6 Index

def main():
  textFile = open("fish.txt", 'r')
  
  wordList = {} #create an empty dictionary
  lineNum = 0

  for line in textFile:
    lineNum += 1
    words = line.split()
    for word in words:
      word = word.lower()
      word = word.replace("," , "")
      word = word.replace("." , "")
      word = word.replace("\n" , "")
      word = word.replace("!" , "")
      if word in wordList:
        wordList[word].append(lineNum)
      else:
        wordList[word] = [lineNum]

    
    for word in wordList:
      print(word, wordList[word])
  

 


if __name__ == '__main__':
  main()
