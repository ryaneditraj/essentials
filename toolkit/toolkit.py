print("RYANS PERSONAL HACKER TOOLKIT")

def add_https(input_file, output_file):
  """Reads lines from a file, prepends https://, and writes to another file.

  Args:
      input_file: Path to the file containing URLs.
      output_file: Path to write the modified URLs.
  """

  with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
      out_file.write("https://" + line)

  print(f"Lines modified and saved to {output_file}")

def add_http(input_file, output_file):
  """Reads lines from a file, prepends https://, and writes to another file.

  Args:
      input_file: Path to the file containing URLs.
      output_file: Path to write the modified URLs.
  """

  with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
      out_file.write("http://" + line)

  print(f"Lines modified and saved to {output_file}")
no = int(input("""
           [1] Add Https:// to domain list
           [2] Add Http:// to domain list
               
               >"""))

if no == 1:
    input_file = input("Input File: ")
    output_file = input("Output File: ")

    add_https(input_file, output_file)

elif no == 1:
    input_file = input("Input File: ")
    output_file = input("Output File: ")

    add_http(input_file, output_file)