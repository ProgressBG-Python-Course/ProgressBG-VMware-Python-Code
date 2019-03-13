import re

def simple_demo():
  string = ".comgmail.com"

  pattern = r'\.com'

  regex = re.compile(pattern)
  res = regex.search(string)


  if res:
    print(f"Match: {res.group(0)}")
  else:
    print("No")

def metachar_demo():
  """
  "ala@hjdshfjds.com"   - > valid
  "ala23@hjdshfjds.com" - > not valid
  valid email is : sequence of lattin letters, followed by '@', followed by letters, followed '.', followed by 3, 4, 5,6 letters
  """

  strings = [
    "ala@hjdshfjds.com",
    "ala23@hjdshfjds.com",
    "a@.com"
  ]
  regex = re.compile(r'[a-z]+@[a-z]*\.[a-z]{3,6}')

  for string in strings:
    if not regex.search(string):
      print(f'{string} does not match!')

def demo2():
  string = "ababab"
  regex = re.compile( r"(?:(?:ab)|(?:cd)){3}" )


  res = regex.search(string)
  if res:
    print(res.group(0))
    # print(res.grup(2))




demo2()