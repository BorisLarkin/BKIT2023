import sys
import math

def get_coef(index, prompt):
    '''
    Reads a coefficient, be it KBM or console

    Args:
        index (int): Number of the parameter in the console string
        prompt (str): Suggests an input

    Returns:
        float: coefficient of the biquadratic equation
    '''
    try: #to get a coeff from cmd
        coef_str = sys.argv[index]
    except:
        # KBM input
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Solving a biquadratic equation

    Args:
        a (float): coef А
        b (float): coef B
        c (float): coef C

    Returns:
        list[float]: root list
    '''
    q_roots = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        q_roots.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        q_roots.append(root1)
        q_roots.append(root2)
    biq_roots = []
    for i in q_roots:
        if i == 0.0:
            biq_roots.append(0)
        elif i>0:
            biq_roots.append(math.sqrt(i))
            biq_roots.append(-math.sqrt(i))
    return biq_roots


def main():
    '''
    Main function
    '''
    a = get_coef(1, 'Enter coefficient А:')
    b = get_coef(2, 'Enter coefficient B:')
    c = get_coef(3, 'Enter coefficient C:')
    # Calculating roots
    roots = get_roots(a,b,c)
    # Roots output
    len_roots = len(roots)
    if len_roots == 0:
        print('No roots')
    elif len_roots == 1:
        print('One root: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Two roots: {} & {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Three roots: {} & {} & {}'.format(roots[0], roots[1], roots[2], ))
    elif len_roots == 4:
        print('Four roots: {} & {} & {} & {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# If executed from cmd
if __name__ == "__main__":
    main()
