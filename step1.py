def Multiple_of_three(num):
  # Function returns Fizz if the input is a numper multiple of three.
  if(num % 3) == 0:
    return "Fizz"
  else:
    return ""

def Multiple_of_five(num):
  # Function returns Buzz if the input is a numper multiple of five.
  if(num % 5) == 0:
    return "Buzz"
  else:
    return""


for x in range(1,101):

  mo3_text = Multiple_of_three(x)
  mo5_text = Multiple_of_five(x)

  if mo3_text or mo5_text:
    print(mo3_text + mo5_text)
  else:
    print(x)
