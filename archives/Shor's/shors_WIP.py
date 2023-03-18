import numpy as np
import random

def shors_algorithm(N, g):
    '''
    

    Parameters
    ----------
    N : Integer
        large number we want to factor.
    g : Integer 
        guess thats a factor of N.

    Returns
    -------
    n_1 : Integer
        Cofactor of N.
    n_2 : Integer
        Cofactor of N.

    '''
    states = np.arange(N)
    remainders = np.zeros(N)
    g_powers = np.zeros(N)
    #initialises our quantum register
    original_states = states
    for i in range(N):
        #generates a list of our guess to the power of the state
        g_powers[i] = g**(states[i])
    for i in range(N):
        remainders[i] = (g_powers[i]) % N
        #finds the remainder of the division with our large number N
    choice = random.randint(0,N) #randomly selects one of the remainder values
    r = remainders[choice]
    i_values = []
    for i in range(N):
        if remainders[i] == r:
            i_values.append(i)
            #finds each value in the remainders array equal to the choice
            #and saves the corresponding position in the array
        else:
            continue
    power_values = np.zeros(len(i_values))
    for i in range(len(i_values)):
        power_values[i] = original_states[(i_values[i])]
        #saves the relevant values of powers in a list from which p can be
        #calculated
    print(power_values)
    p = power_values[1] - power_values[0]
    p_2 = power_values[(len(power_values)-1)] - power_values[(len(power_values)-2)]
    odd_even = p%2
    if p != p_2:
        print("differences not equal error in algorithm")
    elif odd_even != 0:
        print("p is odd try another guess")
    elif p == p_2 and odd_even == 0:
        print('p = ', p)
    
    n_1 = g**(p/2) + 1
    n_2 = g**(p/2) - 1
    if (n_1 % N) == 0 or (n_2 % N) == 0:
        print("one factor is a multiple of N make another guess")
    return n_1, n_2
    
def euclids_algorithm(n_1, n_2, N):
    M = N
    if n_1 > N:
        r_1 = n_1%N
        while r_1:
            n_1=N
            N=r_1
            r_1=n_1%N
    elif n_1 < N:
        r_1 = N%n_1
        while r_1:
            N = n_1
            n_1 = r_1
            r_1 = N%n_1
    GCD_1 = N
    
    if n_2 > M:
        r_2 = n_2%M
        while r_2:
            n_2=M
            M=r_2
            r_2=n_2%M
    elif n_2 < M:
        r_2 = M%n_2
        while r_2:
            M = n_2
            n_2 = r_2
            r_2 = M%n_2
    GCD_2 = M
    return GCD_1, GCD_2

def main(N,g):
    n_1, n_2 = shors_algorithm(N, g)
    GCD_1, GCD_2 = euclids_algorithm(n_1, n_2, N)
    print("the factors are:", GCD_1, "and", GCD_2)
    
main(274,3)