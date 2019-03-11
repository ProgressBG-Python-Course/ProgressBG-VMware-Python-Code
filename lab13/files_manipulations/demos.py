def read_file_demo(file_path):
  # get the File Handler
  fh = open(file_path, mode="r")

  # file manipulation (read from file)
  # content = fh.read()
  # print(content)

  # TASK: ouptut the number of lines:
  lines = fh.readlines()
  print(f'Line numbers: {len(lines)}')

  # close (release the FH)
  fh.close()


def write_file_demo(file_path):
  fh = open(file_path, mode="w")

  fh.write('One line\nSecond line\n')
  fh.close()

def write_file_task(file_name):
  '''
    TASK:
    Given the list of strings:
    lines = [
      'line 1',
      'line 2',
      'line 3',
      'line 4',
      'line 5',
      'line 6',
    ]

    create a file 'lines.txt' containing the lines from the list
  '''
  lines = [
    'line 1',
    'line 2',
    'line 3',
    'line 4',
    'line 5',
    'line 6',
  ]

  fh = open(file_name, mode='w')

  fh.writelines(lines)


def append_file_demo(file_path):
  pass

# write_file_demo('demo.txt')

write_file_task('lines.txt')