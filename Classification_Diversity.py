import numpy as np
import sys



def check_zero(terme):
    return terme == 0

def len_check(Y_model1, Y_model, Y_obs):
    return len(Y_model1) == len(Y_model) == len(Y_obs)

    
def Binary_Matix(Y_1 ,Y_2 ,Y_obs):
    
    try:
        if len(Y_1) == len(Y_2) and len(Y_2)  == len(Y_obs):
            BM = np.zeros((2,2))
            for i in range(len(Y_1)):
                if Y_1[i] == Y_2[i] and Y_2[i] == Y_obs[i]:
                    BM[0,0] += 1
                elif Y_1[i] == Y_2[i] and Y_2[i] != Y_obs[i]:
                    BM[1,1] += 1
                elif Y_1[i] != Y_2[i] and Y_1[i] == Y_obs[i]:
                    BM[0,1] += 1
                else :
                    BM[1,0] += 1

            return BM

        else:
            raise ValueError

    except ValueError:
        print('Error: The length of the arrays are not equal')

    
    




#==================================Pairwise Diversity==================================


# Correlation Coefficient
def Correlation_Coefficient(Y_1, Y_2, Y_obs):
    try :
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        print(BM)
        print("checking zero")
        if check_zero(np.sqrt((BM[0,0] + BM[0,1])*(BM[1,0] + BM[1,1])*(BM[0,0] + BM[1,0])*(BM[0,1] + BM[1,1]))):
            raise ZeroDivisionError("Denominator is zero")
            

        
        
        CC = (BM[0,0]*BM[1,1] - BM[0,1]*BM[1,0])/np.sqrt((BM[0,0] + BM[0,1])*(BM[1,0] + BM[1,1])*(BM[0,0] + BM[1,0])*(BM[0,1] + BM[1,1]))

        return CC
    except ZeroDivisionError as e :
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
  
    

# Q-statistic

def Q_statistic(Y_1, Y_2, Y_obs):
    
    try:
        if not len_check(Y_1, Y_2, Y_obs) :
             raise ValueError("Length check failed.")
        
        BM = Binary_Matix(Y_1, Y_2, Y_obs)
        print("getting matrix")
        print(BM)
        print("getting mesure")
        if check_zero((BM[0,0]*BM[1,1] + BM[0,1]*BM[1,0])):
            raise ZeroDivisionError("Denominator is zero")
        

        Q = (BM[0,0]*BM[1,1] - BM[0,1]*BM[1,0])/(BM[0,0]*BM[1,1] + BM[0,1]*BM[1,0])
        
        return Q

    except ZeroDivisionError as e :
        print(f"Error: {e}")
        return None
    except ValueError as e :
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    


# Differences Mesure

def Differences_Mesure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        DM = (BM[0,1] + BM[1,0])/(BM[0,0] + BM[0,1] + BM[1,0] + BM[1,1])

    except ZeroDivisionError :
        print('Error: Division by zero')
    return DM

# Double Fault Measure

def Double_Fault_Measure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        DFM = BM[1,1]/(BM[0,0] + BM[0,1] + BM[1,0] + BM[1,1])

    except ZeroDivisionError :
        print('Error: Division by zero')
    return DFM


# Combination of Differences Mesure and Double Fault Measure


def D_DF_Mesure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        D_DF = (BM[0,1] + BM[1,0] )/(BM[1,1] )

    except ZeroDivisionError :
        print('Error: Division by zero')
    return D_DF

#==================================Non-Pairwise Diversity==================================

# Entropy

def Entropy(Y_Classifiers ,Y_obs):
    try:

        N = len(Y_obs)
        L = len(Y_Classifiers)

        perdictions = list(zip(*Y_Classifiers))

        E_prime=0

        for j in range(N):
            
            correct_predictions = sum([1 for i in range(L) if perdictions[j][i] == Y_obs[j]])

            min_term = min(correct_predictions, L*correct_predictions)

            E_prime += min_term/(L - L/2)

        E = E_prime/N

    except ZeroDivisionError :
        print('Error: Division by zero')

    except ValueError:
        print('Error: The length of the arrays are not equal')    

    return E

# Kohavi-Wolpert Variance

def Kohavi_Wolpert_Variance(Y_Classifiers ,Y_obs):
    try:

        N = len(Y_obs)
        L = len(Y_Classifiers)
        predictions = list(zip(*Y_Classifiers))
        KW=0
        for j in range(N):
            correct_predictions = sum([1 for i in range(L) if predictions[j][i] == Y_obs[j]])
            KW += (correct_predictions * (L - correct_predictions))/L**2

        KW = KW/N

    except ZeroDivisionError :
        print('Error: Division by zero')

    except ValueError:
        print('Error: The length of the arrays are not equal')

    return KW


# Measurement Interrater Agreement

def Interrater_Agreement(Y_Classifiers ,Y_obs):
    try:

        N = len(Y_obs)
        L = len(Y_Classifiers)
        predictions = list(zip(*Y_Classifiers))
        p=0
        q=0

        for j in range(N):
            correct_predictions = sum([1 for i in range(L) if predictions[j][i] == Y_obs[j]])
            q += (correct_predictions*(correct_predictions - L))/L
            p += correct_predictions/(L*N)
        
        IA = 1 - q/(N*(L-1)*p*(1-p))        

    except ZeroDivisionError :
        print('Error: Division by zero')

    except ValueError:
        print('Error: The length of the arrays are not equal')

    return IA

# Difficulty Measure

def Difficulty_Measure(Y_Classifiers ,Y_obs):
    try:

        N = len(Y_obs)
        L = len(Y_Classifiers)
        predictions = list(zip(*Y_Classifiers))
        propotions=[]

        for j in range(N):
            correct_predictions = sum([1 for i in range(L) if predictions[j][i] == Y_obs[j]])
            propotions.append(correct_predictions/L)

        DM = np.var(propotions)

    except ZeroDivisionError :
        print('Error: Division by zero')

    except ValueError:
        print('Error: The length of the arrays are not equal')

    return DM


        
