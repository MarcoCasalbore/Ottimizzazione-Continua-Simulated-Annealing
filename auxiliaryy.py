# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:29:21 2024

@author: marco
"""

import autograd.numpy as np
from autograd import grad, jacobian
from problemss import functionProblem



def hessian(x, n, direct, eps):
    g = grad(function)
    return jacobian(g)(x, n, eps)

def gradient_phi_dir(d, x, n, eps) :
    gpd =  np.dot(hessian(x, n, d, eps), d) + grad(function)(x, n, eps)
    return gpd

def function(x, n, eps) :
    return functionProblem(x, n)