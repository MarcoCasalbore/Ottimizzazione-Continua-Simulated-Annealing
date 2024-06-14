# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:34:04 2024

@author: marco
"""

import autograd.numpy as np
from autograd import grad
from constantss import *
from auxiliaryy import gradient_phi_dir, hessian, function
from linesearchh import linesearch_ArmijoNonMonotona, linesearch

def direction(f, nf, n, x, n_iter, eps) :
    eps_1 = 10**(-8)
    eps_2 = 10**(-3)
    p = np.zeros(n)
    s = -grad(function)(x, n, eps)
    nf += 1
    i = 0

    
    if np.dot(np.dot(s.T, hessian(x, n, s, eps)), s) < eps_1*(np.linalg.norm(s) ** 2) :
        return - grad(function)(x, n, eps)
    
    while i < MAX_ITER: 
        alpha = - np.dot(gradient_phi_dir(p, x, n, eps).T, s) / np.dot(np.dot(s.T, hessian(x, n, s, eps)), s)

        p = p + alpha*s
        
        if np.linalg.norm(gradient_phi_dir(p, x, n, eps)) <=  (eps_2 / (1 + n_iter)) * np.linalg.norm(grad(function)(x, n, eps)) :
            nf += 2
            return p
        
        i += 1
        
        beta = np.dot(np.dot(gradient_phi_dir(p, x, n, eps), hessian(x, n, s, eps)), s) / np.dot(np.dot(s.T, hessian(x, n, s, eps)), s)
        
        s = -gradient_phi_dir(p, x, n, eps) + beta*s
        nf += 1
        
        
        if np.dot(np.dot(s.T, hessian(x, n, s, eps)), s) < eps_1*(np.linalg.norm(s) ** 2) :
            return p
        
        
        if s.all() <= 10 ** (-8) : break
    
        #if np.linalg.norm(s) <= 10**(-8) : break
    
    return p
    
def troncatoMAIN(eps, delta, x0) :
    alpha = 10**(-3)
    gamma = 10**(-6)
    #if delta < 10**(-9) : delta = 10**(-9)
    #print(delta, "delta")
    n = DIM
    x = x0
    #Wtrhd = 10**(-5)

    n_iter = 0
    max_iter = 2**8 - 1
    f = function(x, n, eps)
    nf = 1
    l = []

    while True:
        norm_gradient = np.sqrt(np.dot(grad(function)(x, n, eps).T, grad(function)(x, n, eps)))
        #print(norm_gradient)
        #norm_gradient = np.sqrt(grad(function) * grad(function))
        #print("n_itert =",n_iter,"  nf =",nf,"f =",  f,"norma_grad =", norm_gradient)
        if norm_gradient <= delta:
            print("\nAlgoritmo locale terminato con un punto stazionario, valore di funzione obiettivo:", function(x, n, eps), "\n")
            for i in range(0, n) :
                print  ("\nx(",i+1,") =",x[i], "\n")
            break
            
        if n_iter > max_iter :
            print("\nAlgoritmo terminato per massimo numero di iterazioni")
            #print("\nNorma attuale del gradiente:", norm_gradient)
            for i in range(0, n) :
                print  ("\nx(",i+1,") =",x[i], "\n")
            break
        
        direct = direction(f, nf, n, x, n_iter, eps)
        #print("direction", direct)
        #if np.linalg.norm(direct) <= 10**(-9) : break
        #gradient_dir = np.dot(grad(function).T, direct)
        gradient_dir = np.dot(grad(function)(x, n, eps).T, direct)
        #print("gradient_dir", gradient_dir)
    
        # alpha, phi_alpha, nf = linesearch_ArmijoNonMonotona(l, f, function, x, n, gamma, alpha, direct, gradient_dir, nf, eps)
        alpha, phi_alpha, nf = linesearch(f, function, x, n, gamma, alpha, direct, gradient_dir, nf, eps)
        #print("alpha", alpha, "phi_alpha", phi_alpha)
        # print()
        # print(f"x: {x}, alpha: {alpha}, d: {direct}")
        # print()
        x = x + alpha*direct
        #print("x", x)
        
        
        
        # ### DA CAMBIARE OGNI VOLTA ###
        # if (x - 3 > 0).any() :
        #     break
        # if (x + 1.5 < 0).any() :
        #     break
        

        if (x > 2.).any() :
            print("troncato out of range")
            break
        if (x < -0.1).any() :
            print("troncato out of range")
            break

        
        
        
        f = phi_alpha
        l.append(f)
        #print("f", f)
    
        n_iter += 1
        #print(n_iter)
        #print("------------------- fatta iterazione", n_iter, "-------------------")
        #print("\n")
    print(function(x,n,eps))
    
    print(f"Numero Iterazioni Algoritmo Newt. Troncato: {n_iter} Norma del gradiente: {norm_gradient}")
    #file_stampe.write(f"Prima dell'accettazione del test, N° Punti Generati: {n_iter}\n")
    return x