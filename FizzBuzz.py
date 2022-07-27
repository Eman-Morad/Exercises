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

def Multiple_of_seven(num):
  # Function returns Bang if the input is a numper multiple of seven.
  if(num % 7) == 0:
    return "Bang"
  else:
    return"" 

def Multiple_of_eleven(num):
  # Function returns Bong if the input is a numper multiple of eleven.
  if(num % 11) == 0:
    return "Bong"
  else:
    return"" 

def Multiple_of_thirteen(num):
  # Function returns Fezz if the input is a numper multiple of thirteen.
  if(num % 13) == 0:
    return "Fezz"
  else:
    return"" 
    
for x in range(1,300):

  mo3_text  = Multiple_of_three(x)
  mo5_text  = Multiple_of_five(x)
  mo7_text  = Multiple_of_seven(x)
  mo11_text = Multiple_of_eleven(x)
  mo13_text = Multiple_of_thirteen(x)
  
  if mo11_text :
    # Prints Bong if mutiplies by 11.
    # Prints FezzBong if multiplies by 11 and 13.
    print(mo13_text + mo11_text)      
  elif mo3_text or mo5_text or mo7_text or mo13_text:
    print(mo3_text + mo13_text + mo5_text + mo7_text)
  else:
    print(x)
