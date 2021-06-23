def list_multiply(list1, list2):
       
    list3=[]

    list3 = [list1[num] * list2[num] for num in range(len(list1 and list2))]
    print(f"This is list 1: {list1}") 
    print(f"This is list 2: {list2}")       
    print(f"This is list 3 (List that multiplys list1 and list2): {list3}")

list1=[1,2,3,4,5,6]
list2=[3,6,9,12,15,18]
list_multiply(list1, list2)

#Reference: https://www.geeksforgeeks.org/python-multiply-two-list/
  
print("###################################################")
print("###################################################\n\n")

def multiply(list1,list2):

    list3=[] 

    for num in range(0,6):
        list3=(list1[num]*list2[num])
        print(list3)

list1=[1,2,3,4,5,6]
print(list1)    
    
list2=[1,6,7,8,9,10]
print(list2)  
    
multiply(list1, list2)