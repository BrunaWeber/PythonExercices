def list_multiply(list1, list2):
    
    for num1, num2 in zip(list1,list2):
        list3.append(num1*num2)

        #print(f"This is list 1: {list1}") 
        #print(f"This is list 2: {list2}")     
        print(f"This is list 3 (List that multiplys list1 and list2): {list3}")
        
list1=[1,2,3,4,5,6]    
list2=[2,4,6,8,10,12]
list3=[]
list_multiply(list1, list2)   

    