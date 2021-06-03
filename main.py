
def last2(str):
  return len([i for i in range(len(str) - 2) if str[i:i+2] == str[-2:]])
str=input()
print(last2(str))