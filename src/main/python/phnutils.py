import re

regex = re.compile(r'678-839-6663')

def isValid(phoneNum):
  try:
    match = regex.fullmatch(phoneNum)
  except:
    return False
    
  if match:
    return True
  else:
    return False
