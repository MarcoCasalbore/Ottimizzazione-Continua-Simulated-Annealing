# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:34:37 2024

@author: marco
"""

import autograd.numpy as np
from autograd import grad

from constantss import *


# prob1
#dim = 2
# def dim() :
#     return DIM
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = (10**(5)*x[0]**2) + x[1]**2 - (x[0]**2 + x[1]**2)**2 + (10**(-5)*(x[0]**2 + x[1]**2)**4) 
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f

# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-20, 20))
#         pto_init[i + 1] = float(np.random.uniform(-20, 20))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init

# problem 2
#dim = 2
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-2.5, 2.5))
#         pto_init[i + 1] = float(np.random.uniform(-1.5, 1.5))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 0
#     f = (4 - 2.1*(x[0]**2) + (x[0]**4)/3)*(x[0]**2) + x[0]*x[1] + ((-4 + 4*x[1]**2)*(x[1]**2))
#     return f


#prob 3
##dim = 2
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(0, 500))
#         pto_init[i + 1] = float(np.random.uniform(0, 500))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = -x[0]*x[1]*(72 - 2*x[0] - 2*x[1])
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f


#prob4
## dim = 2
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-500, 500))
#         pto_init[i + 1] = float(np.random.uniform(-500, 500))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = 100*(x[1]-(x[0]**2))**2 + 6*(6.4*(x[1]-0.5)**2 - x[0] - 0.6)**2
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f



#prob5
## dim = 2
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#         pto_init[i + 1] = float(np.random.uniform(-10, 10))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = (x[0] - 13 + ((5-x[1])*x[1] - 2)*x[1])**2 +  (x[0]-29 + ((x[1] + 1)*x[1] - 14)*x[1])**2
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f

#prob 6

# def dim() :
#     return 4
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     #print(pto_init)
#     return pto_init
    
# def functionProblem(x, n) :
#     f = (100*(x[0]**2 - x[1])**2) + ((x[0] - 1)**2) + ((x[2] - 1)**2) + (90*(x[2]**2 - x[3])**2) + (10.1*((x[1] - 1)**2 + (x[3] - 1)**2)) + (19.8*(x[1] - 1)*(x[3] - 1))
#     #print("funzione", f)
#     return f


#problem 7
# def dim() :
#     return 10
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1000, 1000))
#         pto_init[i + 1] = float(np.random.uniform(-1000, 1000))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     c = 10**2
#     f = 0
#     for i in range(0, n - 1) :
#         f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f



# ================= JOGO STELLE DOPPIE ================



#2 MEYER - ROTH #risultati sbagliati sul file stelle doppie
# def dim() :
#     return 3
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def Y(x, i) :
#     t = np.array([1., 2., 1., 2., 0.1])
#     v = np.array([1., 1., 2., 2., 0.0])
#     return (x[0]*x[2]*t[i]) / (1 + x[0]*t[i] + x[1]*v[i])

# def functionProblem(x, n) :
#     f = 0
#     y = np.array([0.126, 0.219, 0.076, 0.126, 0.186])
#     for i in range(5) :
#         f += (Y(x, i) - y[i])**2
#     #print("funzione", f)
#     return f

#   4 OK
## Miele and Cantrell ###

# def dim() :
#     return 4
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = (np.exp(x[0]) - x[1])**4 + 100*((x[1] - x[2])**6) + (np.tan(x[2] - x[3]))**4 + x[0]**8
#     return f

  #5 OK
### WOOD FUNCTION ###

# def dim() :
#     return 4
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     #print(pto_init)
#     return pto_init
    
# def functionProblem(x, n) :
#     f = (100*(x[0]**2 - x[1])**2) + ((x[0] - 1)**2) + ((x[2] - 1)**2) + (90*(x[2]**2 - x[3])**2) + (10.1*((x[1] - 1)**2 + (x[3] - 1)**2)) + (19.8*(x[1] - 1)*(x[3] - 1))
#     #print("funzione", f)
#     return f


#   6 OK
### Six hump camel back function ###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-2.5, 2.5))
#         pto_init[i + 1] = float(np.random.uniform(-1.5, 1.5))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0
#     #for i in range(0, n - 1) :
#     f = (4 - 2.1*(x[0]**2) + (x[0]**4)/3)*(x[0]**2) + x[0]*x[1] + ((-4 + 4*x[1]**2)*(x[1]**2))
#     #print("funzione", f)
#     return f

#   7 OK
# ### 10*N MINIMI LOCALI LEONARDO###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-10., 10.))
#         pto_init[i + 1] = float(np.random.uniform(-10., 10.))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     #for i in range(0, n - 1) :
#     SOMMA = 0
    
#     for i in range(n - 1) :
#         SOMMA += ((x[i] - 1)**2)*(1 + 10*np.sin(np.pi*x[i + 1])**2)
#     f = (np.pi/n)*(10*np.sin(np.pi*x[0])**2 + SOMMA + (x[n - 1] - 1)**2)
#     #print("funzione", f)
#     return f

#   7 # OK
# ### 10*N MINIMI LOCALI NOSTRA###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10., 10.))
#     return pto_init

# def functionProblem(x, n) :
#     f = 0.
#     SOMMA = 0.
#     term1 = 10 * (np.sin(np.pi * x[0])**2)
    
    
#     for i in range(n - 1): #
#         arg1 = (x[i] - 1)**2
#         arg2 = 1 + (10 * (np.sin(np.pi * x[i+1])**2) )
#         SOMMA += arg1*arg2

#     term3 = (x[n - 1] - 1)**2 #x(n)
#     f = (np.pi/(n))*(term1+SOMMA+term3)
#     return f
    

#   8 # x(2) == 0 e != 1 (check)
### 15*N MINIMI LOCALI ###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10., 10.))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 0.
#     somma = 0
#     for i in range(DIM - 1):
#         somma += ((x[i] - 1)**2) * (1 + 10 * (np.sin(3*np.pi*x[i+1])**2))
    
#     arg1 = np.sin(3*np.pi*x[0])**2
#     elem1 = (arg1 + somma) * (1/10)

#     elem2 = (1/10)*((x[DIM-1] - 1)**2) * (1 + (np.sin(2*np.pi*x[DIM-1])**2))

#     return elem1 + elem2

# 9

# def dim() :
#     return 4
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(0., 10.))
#         pto_init[i + 1] = float(np.random.uniform(0., 10.))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
    
#     a = np.array([[4., 4., 4., 4.], 
#                   [1., 1., 1., 1.],
#                   [8., 8., 8., 8.], 
#                   [6., 6., 6., 6.], 
#                   [3., 7., 3., 7.], 
#                   [2., 9., 2., 9.], 
#                   [5., 5., 3., 3.], 
#                   [8., 1., 8., 1.], 
#                   [6., 2., 6., 2.], 
#                   [7., 3.6, 7., 3.6]])
    
#     c = np.array([.1, .2, .2, .4, .4, .6, .3, .7, .5, .5])
    
#     m = 10
#     f = 0.
#     for i in range(m) : 
#         f = f - (1 / ((np.dot((x - a[i]).T, (x - a[i]))) + c[i]))
#     #print("funzione", f)
#     return f


#   11 ok
### GOLDSTEIN AND PRICE ###

# def dim() :
#     return 2
    
# # def starting_point(n) :
# #     pto_init = np.zeros(n)
# #     for i in range(0, n, 2) :
# #         pto_init[i] = float(np.random.uniform(-2., 2.))
# #         pto_init[i + 1] = float(np.random.uniform(-2., 2.))
# #     #print(pto_init, type(pto_init), pto_init[0])
# #     return pto_init

# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-2., 2.))
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     #for i in range(0, n - 1) :
#     f = (1 + ((x[0] + x[1] + 1)**2) * (19 - 14*x[0] + 3*(x[0]**2) - 14*x[1] + 6*x[0]*x[1] +3*(x[1]**2))) * (30 + ((2*x[0] - 3*x[1])**2)*(18 - 32*x[0] + 12*(x[0]**2) + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2))
#     #print("funzione", f)
#     return f


### 12 EXPONENTIAL (sbagliata la soluzione sul file stelle doppie###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-1., 1.))
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     somma = 0
#     for i in range(0, n) :
#         somma += x[i]**2
#     f = np.exp((-0.5)*somma)
#     return f


#Only if you start near the optimal point
### 13 cosine mixture###
# def dim() :
#     return 2
    
# def starting_point(n) :
#     # return np.array([0.9, 0.9])
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-1., 1.))
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     somma_1 = 0
#     somma_2 = 0
#     for i in range(0, DIM) :
#         somma_1 += np.cos(5*np.pi*x[i])
#         somma_2 += x[i]**2
#     f = 0.1*somma_1 - somma_2
#     return f



                  ############################ PROBLEMA PER L'ESAME #############################

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(0., 500.))
#         #pto_init[i+1] = float(np.random.uniform(-2, 2))    #DA AGGIUNGERE SOLO SE NECESSARIO
#     #print(pto_init)
#     return pto_init
    
# def functionProblem(x, n) :
#     f=0
#     f = -x[0]*x[1]*(72-2*x[0]-2*x[1])
#     #print("funzione", f)
#     #f = (1 + ((x[0] + x[1] + 1)**2) * (19 - 14*x[0] + 3*(x[0]**2) - 14*x[1] + 6*x[0]*x[1] +3*(x[1]**2))) * (30 + ((2*x[0] - 3*x[1])**2)*(18 - 32*x[0] + 12*(x[0]**2) + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2))
#     return f



# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1., 1.))
#        # pto_init[i + 1] = float(np.random.uniform(-10., 10.))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     #for i in range(0, n - 1) :
#     SOMMA = 0
    
#     for i in range(1, 10) :
#         SOMMA += (2+2*i-(np.exp(i*x[0])+np.exp(i*x[1])))**2
#     f = SOMMA
#     #print("funzione", f)
#     return f


#problema 2


# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1., 1.))
#         #pto_init[i + 1] = float(np.random.uniform(-1., 1.))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     #for i in range(0, n - 1) :
#     f = (np.cos(x[0]) * np.sin(x[1])) - (x[0])/(x[1]**2 +1)
#     #print("funzione", f)
#     return f



#PROBLEMA 2 ESAME 

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1, 2))
#         pto_init[i] = float(np.random.uniform(-1, 1))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = np.cos(x[0])*np.sin(x[1]) - (x[0]/(x[1]**2 + 1))
#     return f


# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1.5, 4.))
#         pto_init[i + 1] = float(np.random.uniform(-3., 3.))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #æc = 10**3
#     f = 0.
#     #for i in range(0, n - 1) :
#     f = np.sin(x[0]+x[1]) + ((x[0]+x[1])**2) -(3/2)*x[0] + (5/2)*x[1] + 1
#     #print("funzione", f)
#     return f





#PROBLEMA 4 ESAME 

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 1 + np.sin(x[0])*2 + np.sin(x[1])2 - 0.1*np.exp(-x[0]2 - x[1]*2)
#     return f





#PROBLEMA 1 ESAME 

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-1, 1))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 0
#     for i in range(10):
#         f += (2 + 2*i - (np.exp(i*x[0]) + np.exp(i*x[1])))**2
#     return f


#PROBLEMA 2 ESAME 

def dim() :
    return 2
    
def starting_point(n) :
    pto_init = np.zeros(n)
    for i in range(0, n, 2) :
        pto_init[i] = float(np.random.uniform(-1, 2))
        pto_init[i] = float(np.random.uniform(-1, 1))
    return pto_init
    
def functionProblem(x, n) :
    f = np.cos(x[0])*np.sin(x[1]) - (x[0]/(x[1]**2 + 1))
    return f


#PROBLEMA 3 ESAME 

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-1.5, 4))
#         pto_init[i] = float(np.random.uniform(-3, 3))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - (3/2)*x[0] + (5/2)*x[1] + 1
#     return f

#PROBLEMA 4 ESAME 

# def dim() :
#     return 2
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 1 + np.sin(x[0])**2 + np.sin(x[1])**2 - 0.1*np.exp(-x[0]**2 - x[1]**2)
#     return f




#################################################################################################################














if __name__ == "__main__":
    from scipy.optimize import minimize, dual_annealing, basinhopping, differential_evolution

    def functionProblemScipy(x) :
        f = (np.exp(x[0]) - x[1])**4 + 100*((x[1] - x[2])**6) + (np.tan(x[2] - x[3]))**4 + x[0]**8
        return f
    
    n = 4

    x0 = starting_point(4)
    # bounds = [(-10, 10), (-10, 10), (-10, 10), (-10, 10)]
    bounds = [(-1, 1)  for i in range(n)]
    print(bounds)

    # ===========  LOCAL MINIMIZER  =============
    # result = minimize(functionProblemScipy, x0)

    # ===========  GLOBAL MINIMIZER  =============

    #COME IL SIMULATED ANNEALING
    # result = dual_annealing(functionProblemScipy, bounds)



    # BASINSHOPPING
    # Definisci il minimizzatore locale
    # minimizer_kwargs = {"method": "BFGS"}
    # result = basinhopping(functionProblemScipy, x0, minimizer_kwargs=minimizer_kwargs)



    # DIFFERENTIAL_EVOLUTION(sembra essere il migliore)
    result = differential_evolution(functionProblemScipy, bounds)

    print("Optimal value:", result.fun)
    print("Optimal point:", result.x)








