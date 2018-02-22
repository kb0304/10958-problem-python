upper_limit = 1001
g_number_array = [1,2,3,4,5,6,7,8,9]
operator_array = ['+','-','*','/','^','']

def operate(first, second, operator):
  if(operator=='+'):
    return first+second
  elif(operator=='-'):
    return first-second
  elif(operator=='*'):
    return first*second
  elif(operator=='/'):
    return first/second
  elif(operator=='^'):
    return first**second
  elif(operator==''):
    return int(str(first)+str(second))
  else:
    print("Please define an operatoin for the operator first.")

def final_function(k):
  answer_array = []

  def check_existance(number_array, number_to_check):
    number_count = len(number_array)
    if(number_count==1):
      print number_array[0]
      if(number_array[0]==number_to_check):
        return True
      else:
        return False
 
    for i in range(0,number_count-1):
      for operator in operator_array:
        temp = number_array[:]

        execute = True
        if operator == '/' and number_array[i+1]==0:
           execute = False
        elif operator == '/' and not(number_array[i]%number_array[i+1]==0):
           execute = False
        elif operator == '' and (number_array[i]<0 or number_array[i+1]<0):
           execute = False
        elif operator == '^' and number_array[i+1]>1000:
           execute = False
        elif operator == '^' and number_array[i+1]<0:
           execute = False
        elif number_array[i]>1000000000 or number_array[i]<-1000000000 or number_array[i+1]>1000000000 or number_array[i+1]<-1000000000:
           execute = False
        elif len(number_array)!=len(g_number_array) and operator=='':
           execute = False

        if execute:
          temp[i] = operate(number_array[i],number_array[i+1], operator)
          for j in range(i+1,number_count-1):
            temp[j] = temp[j+1]
          del temp[-1]
          if(check_existance(temp, number_to_check)):
            answer_array.append([i, operator])
            return True
    return False

  check_existance(g_number_array, k)
  answer_array.reverse()

  if len(answer_array)==0:
    print str(k)+': Not found#####################################################################'
    return

  temp_array = g_number_array[:]
  for ele in answer_array:
    i = ele[0]
    number_count = len(temp_array)
    temp_array[i] = '('+str(temp_array[i])+ele[1]+str(temp_array[i+1])+')'
    for j in range(i+1,number_count-1):
      temp_array[j] = temp_array[j+1]
    del temp_array[-1]
  print str(k)+': '+temp_array[0]



final_function(67543)
