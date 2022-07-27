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

def Multiple_of_seventeen(num):
  # Function returns True if the input is a numper multiple of seventeen.
  if(num % 17) == 0:
    return True
  else:
    return False

    
for x in range(1,300):

  mo3_text  = Multiple_of_three(x)
  mo5_text  = Multiple_of_five(x)
  mo7_text  = Multiple_of_seven(x)
  mo11_text = Multiple_of_eleven(x)
  mo13_text = Multiple_of_thirteen(x)
  mo17_check = Multiple_of_seventeen(x)
  
  if mo11_text :
    text_list = [mo13_text, mo11_text]
    # Prints Bong if mutiplies by 11.
    # Prints FezzBong if multiplies by 11 and 13.
    if mo17_check:
      # Reverse the output of multiple of 17.
      text_list = reversed(text_list)
    
    print(''.join(text_list))
       
  elif mo3_text or mo5_text or mo7_text or mo13_text:
    text_list = [mo3_text, mo13_text, mo5_text, mo7_text]

    if mo17_check:
      text_list = reversed(text_list)

    print(''.join(text_list))
  
  else:
    print(x)
