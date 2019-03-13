# https://www.utf8-chartable.de/unicode-utf8-table.pl?start=1071
# CYRILLIC CAPITAL LETTER YA
# codepoint: U+042F
# UTF-8    : d0af

# print("\u042F")
# print('Я'.encode())


def string_vs_byte_string():
  string = "123абв"
  print(len(string))
  print(type(string))

  byte_string = string.encode()
  print(len(byte_string))
  print(type(byte_string))


def convert_to_window1251(string, file_name):
  encoded_str = string.encode(encoding='cp1251')

  with open(file_name, mode='wb') as fh:
    fh.write(encoded_str)



convert_to_window1251("з", 'win1251.txt')


# TASK: read the text in "win1251.txt" and print it with uppercase letter using the print(str.upper())
# result: ЗДРАВЕЙТЕ


# TODO: why prints '\xe7'
def upper_win1251(file_name):
  with open(file_name, mode="rb") as fh:
    bytes = fh.read()
    # 0417
    print(bytes)

upper_win1251('win1251.txt')

