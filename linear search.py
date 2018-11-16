ourList = [1,2,3,4,5,65,6,456,325,42345,346,345,234,24,346,234,124,3245,346,457,578,68,679,79,6,4352,352,41234, 234,236,457,5856,63,1,325,45,67,865,73,4124,3123,236,4658,568,579,780,43,54124,2346,457,695,5234,235,458,69,780,780,435,23543,478,670,5465,1234534,68689,6574,534,754,679,5647463,]


#lets create a funtion that takes a list and a target to search for
def findValue(args,target):
  #let's detrmine the length of the list
  length_of_list = len(args)
  #set a counter for us to iterate throught the lsit 1 by 1
  count = 0
  #if the list is empty the function will return False
  while count < length_of_list:
    #logic to determine if we've found the target
    if args[count] == target:
      print("The target element {} was found at index {}".format(target,count))
      return True
    #keep track of count to get through ourList
    count += 1
  #worst case scenario in O(n) time .... we never found the element
  print("Value Not Found")
  return False

#test for a an element we know is in the list
print("We know 457 is in here ")
findValue(ourList,457)

#Test against an element we know is not in the list
print("we know 9999999 isn't in the list")
findValue(ourList,9999999)
