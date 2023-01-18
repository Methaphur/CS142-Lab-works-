#Problem 1     
#Finding c^m using log m number of multiplication operations
def expo(n,m):
  # When the exponent is 1 , return the base itself  
  if m == 1:
    return n
  # If exponent is even , divide it by 2 and square the base
  if m % 2 == 0:
    return expo(n**2,m/2)
  else:
    # Else make n^m as n*(n^m-1)
    return n*expo(n**2,(m-1)/2) 

# Using binary representtion to solve 

# function to return binary format of a number
def bin_conv(n):
    binary = bin(n)[2:]
    return binary

def power(n,m):
# Init a dictionary
    powers = {}
    bin = bin_conv(m)
    for i in range(len(bin)):
#       If the ith position(from right) is 1 , key i : n^(2^i) 
        if bin[len(bin)-(i+1)] == "1":
            powers[i] = n**(2**i)

    count = 1
#     Product of values return our desired product
    for value in powers.values():
        count *= value
    return count

print('1.')
print(expo(2,3))
print(power(2,43))
print()

print('2.a)')
# Find course in course list of 2n-1 elements with only 1 appearance 

input = ['B102','C102','CS142','M102','C102','M102','B102','P102','P102']
# Init an empty dictionary
courses = {}
def course_dict(input):
#   Iterating through elements in input
  for i in input:
#     If element not in dict , set a key with value 1
    if i not in courses:
      courses[i] = 1
    else:
#       If element already present , increment value of key by 1
      courses[i] += 1

#     Fidning key with value 1 
  for key,value in courses.items():
    if value == 1:
      return key

print(course_dict(input))
print()

print("2.b)")

# Same as question 1 but instead of course list we have a list of 2n-1 elements containing (1,n)
# We use properties of numbers instead of a dictionary to execute this using only one auxillary variable 
# (Lists are compound variables and can't be used)

input = [3,1,2,5,4,1,5,3,2]
def fun(input):
#   Finding sum of n numbers and doubling it 
  n = (len(input)+1)//2
  sum = n*(n+1)
#   Finding the sum of elements in the list
  l_sum = 0 
  for i in input:
    l_sum += i
#   Returning the double of sum of n elements and subtracting the sum of our given list , returning us with the element only appearing once
#   eg: Our input list is (1,1,2)
#     : (1,1,2,2) - (1,1,2) = 2
  return(sum - l_sum)

print(fun(input))
print()


#Problem 3
# Modifying the insertion sort algorithm to sort position of elements divisible by k in asccending order 
# and the rest of the elements in descending order 
# Insertion sort Algorithm provided
def insertion_sort(list1):
  for i in range(1,len(list1)):
    current = list1[i]
    j = i -1
    while j >= 0 and current < list1[j]:
      list1[j+1] = list1[j]
      j = j -1 
    list1[j+1] = current
  return list1

# Method using auxillary lists

def ins_sort(List,k):

  aux_1 = [i for i in range(k-1,len(List),k)] # Stores values of indicies in kth positions 
  aux_2 = [i for i in range(len(List)) if i not in aux_1] # Stores indices of elements other than kth 
  
#   Soting of elements in kth pos in Ascending order
  for i in range(len(aux_1)):
    current = List[aux_1[i]]
    j = i -1
    while j >= 0 and current < List[aux_1[j]]:
      List[aux_1[j+1]] = List[aux_1[j]]
      j = j -1 
    List[aux_1[j+1]] = current
  
#   Sorting of all other elements in Descending order
  for i in range(len(aux_2)):
    current = List[aux_2[i]]
    j = i -1
    while j >= 0 and current > List[aux_2[j]]:
      List[aux_2[j+1]] = List[aux_2[j]]
      j = j -1 
    List[aux_2[j+1]] = current 
  
  return List
print('3.a (Aux lists)')
n = [31,12,21,55,22,1,51,30,2,7]
k = 3
print(ins_sort(n,k))
print()


# Sorting algorithm without using auxillary lists

def my_sort(List,k):
#     Sorting in Ascending order
    for i in range(k-1,len(List),k):
        current = List[i]
        j = i-k
        while j>=0 and List[j] > current:
            List[j+k] = List[j]
            j -= k
        List[j+k]=current
        
#     Sorting in Descending order
    for i in range(len(List)):
        if (i+1)%k!=0:
            current = List[i]
            if i%k == 0:
                j = i-2
            else:
                j = i-1
            while j>=0 and List[j]<current:
                if (j+2)%k==0:
                    List[j+2]=List[j]
                else:
                    List[j+1]=List[j]
                if j%k == 0:
                    j-=2
                else:
                    j-=1
            if (j+2)%k == 0:
                List[j+2]=current
            else:
                List[j+1]=current
    
    return List

n = [31,12,21,55,22,1,51,30,2,7]
k = 3
print('3.b W/o Aux lists')
print(my_sort(n,k))
print(my_sort([10,7,9,8],3)) # Rosha, here you go <3

print()


print('4.')
# Problem 4 : Finding number of inversion pairs

# Inversion pairs are pairs of elements in list such that i < j but L[i] > L[j]
# The bigger the number of inversion pairs , the farther we are from the final sorted list
# 0 Inversion pairs indicates a totally sorted list


def inversion_pair(list1):
  # Just introduce a counter for every inversion pair "sorted"
  count = 0
  for i in range(1,len(list1)):
    current = list1[i]
    j = i -1
    while j >= 0 and current < list1[j]:
      count += 1
      list1[j+1] = list1[j]
      j = j -1 
    list1[j+1] = current
  return count

n = [31,12,21,55,14,1,51,30,2,7]
print("Inversion pairs:",end = " ")
print(inversion_pair(n))

