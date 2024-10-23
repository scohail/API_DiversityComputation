




#==================================Pairwise Diversity==================================



def Correlation_Diversity(Y_1, Y_2, Y_obs):
    try:
        len(Y_1) == len(Y_2) and len(Y_2)  == len(Y_obs)
        a ,b ,c, d = 0,
        for i in len(Y_1):
            if Y_1[i] == Y_2[i] and Y_2[i] == Y_obs[i]:
                a += 1
            elif Y_1[i] == Y_2[i] and Y_2[i] != Y_obs[i]:
                d += 1
            elif Y_1[i] != Y_2[i] and Y_1[i] == Y_obs[i]:
                b += 1
            else :
                c += 1
        
        
            
    except ZeroDivisionError :
        print('Error: Division by zero')
    except ValueError:
        print('Error:  The length of the arrays are not equal')