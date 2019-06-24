#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program contains the example in 'Introduction to Operations Research'
# by Gerald Liberman 10th edition pg 447

# The problem is to determine how many teams to deploy in each country
# to improve the health of that country, the effectiveness in each country
# is different and based on the number of teams deployed.

# This is a classic dynamic programming problem where the stage n is the country
# the state is the number of teams depolyed in each country s(n) where the sum
# of s(n) is equal to 5, the decision x(n) is how many teams are deployed in
# each country.

def get_data():
    """
    This function return the input data for the problem
    """
    # col = stages, row = number of teams at each stage
    data = {}
    data['stage'] = 3
    data['state'] = 5
    data['detail'] = [[0, 0, 0, 0],
                    [1, 45, 20, 50],
                    [2, 70, 45, 70],
                    [3, 90, 75, 80],
                    [4, 105, 110, 100],
                    [5, 120, 150, 130]]


    return data


def normal_solve(data):
    """
    This is a demonstration function that takes in the problem data
    and return the optimal solution
    """
    n = 3
    #while n > 1:
    # if it is the last stage
    current_table = [[] for row in range(data['state'] + 1)]
    if n == data['stage']:
        for row_idx in range(len(current_table)):

            current_table[row_idx].append(data['detail'][row_idx][n])

    new_table = [[] for row in range(data['state'] + 1)]
    n = 2
    stored_value = 0
    if n < data['stage'] and n > 1:
        for state_value in range(data['state'] + 1):
            for x_value in range(state_value + 1):

                current_fx = current_table[state_value - x_value][0] + \
                            data['detail'][x_value][n]

                if current_fx > stored_value:
                    stored_value = current_fx

            new_table[state_value].append(stored_value)

    n = 1
    stored_value = 0
    if n == 1:
        for x_value in range(data['state'] + 1):
            current_fx = new_table[5 - x_value][0] + \
            data['detail'][x_value][n]

            if current_fx > stored_value:
                stored_value = current_fx

    return stored_value # solution

data = get_data()

def dp_solve(data, table = None, n = data['stage'], optimal = 0):
    """
    This function solves the problem using recursive dynamic programming
    Input is the data, recursive table
    returns the solution list
    """
    if n < 1:
        return table, optimal

    if table == None:
        table = [[] for row in range(data['state'] + 1)]



    if n == data['stage']:
        for row_idx in range(len(table)):
            table[row_idx].append(data['detail'][row_idx][n])

    elif n < data['stage'] and n > 1:
        stored_value = 0
        for state_value in range(data['state'] + 1):
            for x_value in range(state_value + 1):
                current_fx = table[state_value - x_value][-1] + \
                            data['detail'][x_value][n]

                if current_fx > stored_value:
                    stored_value = current_fx

            table[state_value].append(stored_value)

    elif n == 1:
        for x_value in range(data['state'] + 1):
            current_fx = table[5 - x_value][-1] + \
            data['detail'][x_value][n]
            if current_fx > optimal:
                optimal = current_fx
                optimality = 'yes'

        #optimal = stored_value



    print('a', optimal, n)
    return dp_solve(data, table, n - 1, optimal)
    #print('n:', n)



    return table, n

def recur_try(a):
    if a > 10:
        return None

    a = a + 1
    recur_try(a)
    return a


#recur_try(8)

#dp_solve(data)

print(dp_solve(data))
