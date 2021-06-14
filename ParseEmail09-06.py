# Email domain name finder - version 1

#emailAddress = "username@domain.ext"
#def parseEmail(emailAddress):
       
    #username = emailAddress.split('@')[0]
    #domain = emailAddress.split('@')[1]
    
    #print("Username: " + username)
    #print("Domain: " + domain)  
    
#parseEmail("brunadaniweber@hotmail.com")
#parseEmail("cavallaro@gmail.com")
#parseEmail("vanessa@net.ie")

############################################

# Email domain name finder - version 2

def parseEmail(emailAddress):
    
    emailAddress = (input("Enter your email: "))

    username = emailAddress.split('@')[0]
    domain = emailAddress.split('@')[1]
    domain_name = domain.split('.')[0]
    extention = domain.split('.')[-1]
   
    print("Username: ", username)
    print("Domain: ", domain_name)
    print("Extention: ", extention)

parseEmail(input)

   
 

    

    

    
    

  


    
   
