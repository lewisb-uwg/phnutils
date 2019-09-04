import re

# validates phone numbers in any of the following formats
# (678) 839-6663
# 678.839.6663
# 678-839-6663
# 678/839/6663
# 6788396663
def isValid(phoneNum):
  regex = re.compile(r'\(\d\d\d\) \d\d\d\-\d\d\d\d|\d\d\d\.\d\d\d.\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d|\d\d\d/\d\d\d/\d\d\d\d|\d{10}')
  try:
    match = regex.fullmatch(phoneNum)
  except:
    return False
    
  if match:
    return True
  else:
    return False
    
# Attempts to write a phone number in a "normalized" form, e.g.
# '(678) 839-6663' would return as '6788396663' with the default separator,
# or, for example, '678.839.6663' if separator='.'
def normalize(phoneNum, separator=''):
  try:
    # not a strict phone number regex, but gives us matching groups
    pattern = re.compile(r'\(?(\d\d\d)\)?[ -./](\d\d\d)[-./](\d\d\d\d)')
    match = pattern.match(phoneNum)
    result = match.group(1) + separator + match.group(2) + separator + match.group(3)
    return result
  except:
    return None
