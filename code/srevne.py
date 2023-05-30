def srevne(phrase):
  n = len(phrase)
  esarhp = ['' for i in range(n)]
  for i in range(n):
    esarhp[n-1-i] = phrase[i]
  return esarhp

phrase = input("! tuot iom setiD\n")
print(''.join(srevne(phrase)))