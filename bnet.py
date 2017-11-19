import sys

#Computes dependent probabilities
def calculate_dependent_probability(element,row):
    match_string = ''
    if element == "At" or "Af":
        for r in row:
            if r == "Bf" or r == "Bt" or r == "Ef" or r == "Et":
                match_string = match_string + r
        return eval(match_string)

def calculate_dependent_probability_for_mary(element,row):
    for r in row:
        if r == "At":
            #print Jt
            return Mt
        elif r == "Af":
            return Mf


def calculate_dependent_probability_for_john(element,row):
    for r in row:
        if r == "At":
            #print Jt
            return Jt
        elif r == "Af":
            return Jf



#Compute probability for all variables
def calculate_probability(all_variables):
    #print "cool"

    final_sum = 0
    for row in all_variables:
        sum = 1
        for element in row:
            if element == "At":
                dependent_probability = calculate_dependent_probability(element,row)
                dependent_probability = float("{0:.9f}".format(dependent_probability))
                sum = sum * dependent_probability
            elif element == "Af":
                dependent_probability = calculate_dependent_probability(element, row)
                dependent_probability = float("{0:.9f}".format(dependent_probability))
                sum = sum * (1-dependent_probability)

            elif element == "Jt" or element == "Jf":
                dependent_probability = calculate_dependent_probability_for_john(element, row)
                dependent_probability = float("{0:.9f}".format(dependent_probability))
                sum = sum * dependent_probability
            elif element == "Mt" or element == "Mf":
                dependent_probability = calculate_dependent_probability_for_mary(element, row)
                dependent_probability = float("{0:.9f}".format(dependent_probability))
                sum = sum * dependent_probability
            else:
                #print eval(element)
                prob = float("{0:.9f}".format(eval(element)))
                sum = float(sum * prob)
        sum = float("{0:.8f}".format(float(sum)))
        #print('%.08f' % sum)
        final_sum = final_sum + sum
        #print final_sum
    return final_sum

#This will give the product of variables
def product(*args):
    if not args:
        return iter(((),)) # yield tuple()
    return (items + (item,)
            for items in product(*args[:-1]) for item in args[-1])

def find_combination_using_truth_table(missing_variables):
    length_of_missing_variable = len(missing_variables)
    if length_of_missing_variable == 1:
        return missing_variables
    elif length_of_missing_variable == 2:
        return list(product(missing_variables[0],missing_variables[1]))
    elif length_of_missing_variable == 3:
        return list(product(missing_variables[0], missing_variables[1],missing_variables[2]))
    elif length_of_missing_variable == 4:
        return list(product(missing_variables[0], missing_variables[1],missing_variables[2],missing_variables[3]))
    elif length_of_missing_variable == 5:
        return list(product(missing_variables[0], missing_variables[1],missing_variables[2],missing_variables[3],missing_variables[4]))
    elif length_of_missing_variable == 6:
        return list(product(missing_variables[0], missing_variables[1],missing_variables[2],missing_variables[3],missing_variables[4],missing_variables[5]))



#This method will give the list of all probabilities including the
#missing probabilities
def get_all_probabilities(all_variables,missing_variables,reset_variable):
    formatted_list = []
    #temp_variable = []
    #temp_variable.append(all_variables)
    #temp_variable = all_variables
    for row in missing_variables:
        for variable in row:
            all_variables.append(variable)
        formatted_list.append(all_variables)
        #Reset the list to get the next combination
        all_variables = reset_variable[:]
    return formatted_list




def find_missing_variables(variables):
    add_missing_variables_into_a_stack = []
    for v in list_of_all_variables:
        if v not in variables:
            add_missing_variables_into_a_stack.append([v+"t",v+"f"])
            #add_missing_variables_into_a_stack.append(v+"f")
    return add_missing_variables_into_a_stack


#It will tell the length of the variables
def baysian_network(input_variables):
    get_length_of_variables = []
    for v in input_variables:
        if v in get_length_of_variables:
            pass
        else:
            get_length_of_variables.append(v[0])

    if len(get_length_of_variables) == 5:
        print "here calculate the probability directly"
        row_probability = []
        #row_probability.append(calculate_row_probability(input_variables))
    else:
        #First Calculate Numerator
        missing_variables = find_missing_variables(get_length_of_variables)
        missing_variables_combination = find_combination_using_truth_table(missing_variables)
        reset_variable = input_variables[:]
        all_probability = get_all_probabilities(input_variables,missing_variables_combination,reset_variable)
        probability = calculate_probability(all_probability)
        return probability




#decalare all variables given in the problem

list_of_all_variables = ["B","M","A","E","J"]

Bt = 0.001
Bf = 0.999

Et = 0.002
Ef = 0.998

BtEt = 0.95
BtEf = 0.94
BfEt = 0.29
BfEf = 0.001

Jt = 0.9
Jf = 0.05

Mt = 0.70
Mf = 0.01

add_variables_to_a_list = []
position_of_given = 0
for i in range(0,len(sys.argv)):
    if i == 0:
        pass

    elif sys.argv[i] == "given":
        position_of_given = i

    else:
        #Adding all the arguments from shell
        add_variables_to_a_list.append(sys.argv[i])

#This should give the final computed probability from the baysian network
compute_probability_from_baysian_network_for_numerator = baysian_network(add_variables_to_a_list)
print "This is the numerator"
print compute_probability_from_baysian_network_for_numerator

if position_of_given == 0:
    print "No denominator"
else:
    pos = 0
    denominator_list = []
    for i in range(position_of_given+1,len(sys.argv)):
        denominator_list.append(sys.argv[i])
    compute_probability_from_baysian_network_for_denominator = baysian_network(denominator_list)
    print "This is the denominator"
    print compute_probability_from_baysian_network_for_denominator


print "Final probability is = "+str(compute_probability_from_baysian_network_for_numerator/compute_probability_from_baysian_network_for_denominator)





