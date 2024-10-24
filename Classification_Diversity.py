import numpy as np




def len_check(Y_model1, Y_model, Y_obs):
    try:
        len(Y_model1) == len(Y_model) == len(Y_obs)
    except ValueError:
        print('Error: The length of the arrays are not equal')
        return False
    return True

def Binary_Matix(Y_1 ,Y_2 ,Y_obs):
    BM = np.zeros((2,2))
    try:
        len(Y_1) == len(Y_2) and len(Y_2)  == len(Y_obs)

        for i in range(len(Y_1)):
            if Y_1[i] == Y_2[i] and Y_2[i] == Y_obs[i]:
                BM[0,0] += 1
            elif Y_1[i] == Y_2[i] and Y_2[i] != Y_obs[i]:
                BM[1,1] += 1
            elif Y_1[i] != Y_2[i] and Y_1[i] == Y_obs[i]:
                BM[0,1] += 1
            else :
                BM[1,0] += 1

    except ValueError:
        print('Error: The length of the arrays are not equal')
    return BM






#==================================Pairwise Diversity==================================


#Correlation Coefficient
def Correlation_Coefficient(Y_1, Y_2, Y_obs):
    try :
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        CC = (BM[0,0]*BM[1,1] - BM[0,1]*BM[1,0])/np.sqrt((BM[0,0] + BM[0,1])*(BM[1,0] + BM[1,1])*(BM[0,0] + BM[1,0])*(BM[0,1] + BM[1,1]))

    except ZeroDivisionError :
        print('Error: Division by zero')
  
    return CC

#Q-statistic

def Q_statistic(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        Q = (BM[0,0]*BM[1,1] - BM[0,1]*BM[1,0])/(BM[0,0]*BM[1,1] + BM[0,1]*BM[1,0])
        
    except ZeroDivisionError :
        print('Error: Division by zero')
    return Q


#Differences Mesure

def Differences_Mesure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        DM = (BM[0,1] + BM[1,0])/(BM[0,0] + BM[0,1] + BM[1,0] + BM[1,1])

    except ZeroDivisionError :
        print('Error: Division by zero')
    return DM

#Double Fault Measure

def Double_Fault_Measure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        DFM = BM[1,1]/(BM[0,0] + BM[0,1] + BM[1,0] + BM[1,1])

    except ZeroDivisionError :
        print('Error: Division by zero')
    return DFM


#Combination of Differences Mesure and Double Fault Measure


def D_DF_Mesure(Y_1, Y_2, Y_obs):
    try:
        len_check(Y_1, Y_2, Y_obs) == True
        BM = Binary_Matix(Y_1, Y_2, Y_obs)

        D_DF = (BM[0,1] + BM[1,0] )/(BM[1,1] )

    except ZeroDivisionError :
        print('Error: Division by zero')
    return D_DF

#==================================Non-Pairwise Diversity==================================



def Entropy(Y_Classifiers ,Y_obs):
    try:

        N = len(Y_obs)
        L = len(Y_Classifiers)

        perdictions = list(zip(*Y_Classifiers))

        E_prime=0

        for j in range(N):
            
            correct_predictions = sum([1 for i in range(L) if perdictions[j][i] == Y_obs[j]])

            min_term = min(correct_predictions, L-correct_predictions)

            E_prime += min_term/(L - L/2)

        E = E_prime/N

    except ZeroDivisionError :
        print('Error: Division by zero')

    except ValueError:
        print('Error: The length of the arrays are not equal')    

    return E


# def Kohavi_Wolpert_Variance(Y_Classifiers ,Y_obs):
#     try:

#         N = len(Y_obs)
#         L = len(Y_Classifiers)

        

        
