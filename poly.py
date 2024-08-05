def store_pol(n):
    poly = [0] * (n + 1)
    while True:
        x = int(input("If done, give -1. To continue, give 1: "))
        if x == -1:
            break
        elif x == 1:
            degree = int(input("Enter the degree of the term to be entered: "))
            if degree <= n:
                coeff = int(input("Enter its coefficient: "))
                poly[degree] = coeff
        else:
            print("Invalid input. Please enter 1 to continue or -1 to finish.")
    return poly

def display_pol(poly):
    terms = []
    degree = len(poly) - 1
    for i in range(degree, -1, -1):
        coeff = poly[i]
        if coeff != 0:
            if i == 0:
                term = f"{coeff}"
            elif i == 1:
                term = f"{coeff}x"
            else:
                term = f"{coeff}x^{i}"
            terms.append(term)
    polynomial_str = " + ".join(terms).replace('+ -', '- ')
    print(polynomial_str if polynomial_str else "0")

def add_poly(poly1, poly2):
    n = max(len(poly1), len(poly2))
    add = [0] * n
    for i in range(n):
        if i < len(poly1):
            add[i] += poly1[i]
        if i < len(poly2):
            add[i] += poly2[i]
    return add

def multiply_poly(poly1, poly2):
    n = len(poly1) + len(poly2) - 1
    prod = [0] * n
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            prod[i + j] += poly1[i] * poly2[j]
    return prod

print("Enter coefficients for the first polynomial:")
n = int(input("Enter the highest power: "))
poly1 = store_pol(n)

print("Enter coefficients for the second polynomial:")
poly2 = store_pol(n)

result_add = add_poly(poly1, poly2)
print("Resultant polynomial after addition:")
display_pol(result_add)

result_multiply = multiply_poly(poly1, poly2)
print("Resultant polynomial after multiplication:")
display_pol(result_multiply)
