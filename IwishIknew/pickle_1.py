import pickle 

def storeData(): 
    #initializing data to be sorted in db 
    Omkar = {'key' : 'Omkar', 'name': ' Omkar Pathak', 'age':21, 'pay':40000}
    Jagdish = {'key':'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000} 
    
    #database 
    db={}
    db['Omkar']= Omkar 
    db['Jagdish'] = Jagdish 
    
    #For storing
    #type(b) gives <class 'bytes'> ; 
    b= pickle.dumps(db)
    
    #For loading
    myEntry = pickle.loads (b)
    print(myEntry)    