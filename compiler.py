import sys
import re
def main(arguments):
  file = open(arguments[1], "r")
  lines = file.readlines()
  program = []
  for line in lines:
    fractions = re.findall("\d+/\d+(?: +|$)", line)
    for fraction in fractions:
      [a,b] = fraction.split("/")
      program.append((int(a), int(b)))
  print("Found programm: " + str(program))
  print("Result:\n" + str(compute(program, int(arguments[2]))))

def compute(program, inp):
  numbers = [inp]
  output = 0
  index = 0
  while output is not None:
    output = program[index][0]*inp
    if output % program[index][1] != 0:
      index = index + 1
      if index > len(program):
        output = None
        print ("Stopped")
    else:
      inp = output/program[index][1]
      index = 0
      
      if numbers in numbers:
        output = None
      else:
        print(inp)
        input()
      


if __name__ == "__main__":
    main(sys.argv)