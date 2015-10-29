rangenum = range(1,100)
fib = [1,2,3,5]
evenfib = []

 



for i in rangenum:
     length = len(fib) -1
     sum1 = fib[length]
     lengthminus = length -1
     sum2 = fib[lengthminus]
     
     newfib = sum1+ sum2
     
     if newfib > 4000000:
         break
     
     fib.append(newfib)
     
     

for i in fib:
    if i % 2 == 0:
        evenfib.append(i)
        
        
print sum(evenfib)


   
     

     

 
   
     
    
    
    


