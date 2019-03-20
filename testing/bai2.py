dayso=[128,2,4,16,2,128,64,4,7,4,64]

print(dayso)
for i in range(len(dayso)):
    for j in range(len(dayso)):
        tich=dayso[i]*dayso[j]

        if tich ==256:    
            print(dayso[i],"va",dayso[j],"vi tri" , i+1, "va ",j+1)



