def longestsub(s):
  char_dict ={}
  lptr =0
  rptr =0
  sub = ""
  res = ""
  while lptr < len(s) and rptr < len(s): # n steps 
    char = s[rptr]
    if char in char_dict and lptr<(char_dict[char]+1):
      lptr = char_dict[char]+1
    sub = ""
    for i in range(lptr, rptr+1): # n steps #
      sub += s[i]
    if len(sub)> len(res):
      res = sub
    
    char_dict[char] = rptr
    rptr +=1
  return res

if __name__ == "__main__":
  print(longestsub("abcdefghijklmn"))

#   Clean Code
def longestsub(s):
  char_dict ={}
  lptr =0
  rptr =0
  #sub = ""
  res = [0,0]
  while lptr<len(s) and rptr<len(s) : # n steps 
    char = s[rptr]
    if char in char_dict and lptr<(char_dict[char]+1):
      lptr = char_dict[char]+1
      sub =s[lptr]
    if rptr -lptr> res[1] - res[0]:
      res[0], res[1] = lptr , rptr
    char_dict[char] = rptr
    rptr +=1
  return s[res[0]: res[1]]

if __name__ == "__main__":
  print(longestsub("clementisacap"))