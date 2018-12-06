
class Polynomial(object):

    def __init__(self, coefficients):
        """
        This is constructor function.
        Takes calling object and coefficients of type list as argument
        Initializes coeffs as list of coefficients and Len as the length of the list
        returns None
        """
        self.coeffs = coefficients  # initializes attribute coeffs as list coefficients
        self.Len = len(coefficients)  # initializes attribute Len as length of list coefficients

    def add(self, other):
        """
        Function takes two objects of type Polynomial.
        Adds the polynomials (terms with same degrees together)
        returns the sum of two polynomial as a object of type Polynomial
        """
        diff = abs(
            self.Len - other.Len)  # Assigns the absolute value of the difference in highest order of both polynomial as diff

        if self.Len > other.Len:  # checks which polynomial is of higher degree
            temp1 = self.coeffs
            temp2 = [0] * diff + other.coeffs
        else:
            temp1 = [0] * diff + self.coeffs
            temp2 = other.coeffs
        # The polynomial of higher order is copied as it is in temp, the polynomial of lower order is copied to another temp with 0 preceeding to equal the length

        # Returns the sum of coefficients according to degree of both polynomial
        return Polynomial([sum(i) for i in zip(temp1, temp2)])

    def val(self, x):
        """
        Funtion takes calling object of type Polynomial and a integer as arguments.
        Replaces the integer in the Polynomial equation and finds it's value
        returns the value in type float
        """
        Value = 0
        for i in range(self.Len):
            # Replaces the variable with 'x' and finds the value of polynomial
            Value += self.coeffs[i] * x**(self.Len - (i + 1))
        return float(Value)

    def mul(self, other):
        """
        Function takes two objects of type Polynomial as argument.
        Finds the product of two polynomials
        returns the product in type Polynomial
        """
        product = [0] * (self.Len + other.Len - 1)  # Creates a list with coefficents zero
        for x in range(self.Len):
            for y in range(other.Len):
                # multplies the polynomials and adds the coefficients that have same degree
                product[x + y] += self.coeffs[x] * other.coeffs[y]
        return Polynomial(product)  # Returns the list of coefficients of multiplied polynomial

    def roots(self):
        """
        Function takes object of type Polynomial as argument.
        returns function call rootQuadratic with each element in list coeffs as argument for quadratic(Len=3) polynomial
        returns float of root for linear(Len=2) polynomial
        """
        if self.Len > 3:
            return "Order too high to solve for roots."  # does not calculate root if order greater than 2
        elif self.Len == 3:
            # Calls rootQuadratic with coeffients of polynomial as arguments, if quadratic polynomial
            return rootQuadratic(self.coeffs[0], self.coeffs[1], self.coeffs[2])
        elif self.Len == 2:
            # returns float of root if linear polynomial
            return float(self.coeffs[1] * -1 / self.coeffs[0])

    def __mul__(self, other):
        """
        Funtion takes two objects of type polynomial as argument.
        returns function call mul with both objects as thier argument
        """
        return self.mul(other)  # calls mul with same arguments as parameter

    def __call__(self, x):
        """
        Funtion takes an object of type polynomial and an integer as argument.
        returns function call val with the object and integer as argument
        """
        return self.val(x)  # Calls val with same arguments as parameter

    def __add__(self, other):
        """
        Funtion takes two objects of type polynomial as argument.
        returns function call add with both objects as thier argument
        """
        return self.add(other)  # Calls add with same arguments as parameter

    def __str__(self):
        """
        Function takes object of type Polynomial as argument.
        Creates a string of the Polynomial in printable form
        returns the string
        """
        answer = ''  # empty string
        for i in range(self.Len):
            if self.coeffs[i] == 0:
                answer += ''  # Does not concatenate anything if coefficient is zero

            elif i == self.Len - 1:
                # Concatenate coeffs without any variable if of zero'th order
                answer += str(self.coeffs[i]) + ".000"

            elif i == self.Len - 2:
                # Concatenates coeffs with variable 'z' if first order
                answer += str(self.coeffs[i]) + ".000" + "z" + " + "
            else:
                # Concatenates coeffs with variable 'z' raised to order of term for orders greater than 1
                answer += str(self.coeffs[i]) + ".000" + " z**" + str(self.Len - (i + 1)) + " + "
        return answer

    def __repr__(self):
        """
        Function takes one object of type Polynomial as argument.
        returns function call of __str__ with the object as the argument
        """
        return self.__str__()  # calls __str__


def rootQuadratic(a, b, c):
    """
    Takes three arguments of type float or integer.
    calculates root1 and root2 taking the three arguments as coefficients
    returns root1,root2 in type tuple
    """
    k = b**2 - (4 * a * c)  # b^2-4ac
    if k < 0:
        k = (k + 0j)  # Converting to complex number if k is negative
    root1 = (b * -1 - k**0.5) / (2 * a)
    root2 = (b * -1 + k**0.5) / (2 * a)  # finding first and second roots[(-b(+/-)k^1/2)/2a)]
    return root1, root2


def main():  # Test Function
    """
    This function does not take any parameters.
    It tests the various operations in the class polynomial
    Returns None
    """
    p1 = Polynomial([1, 2, 3])
    print p1
    p2 = Polynomial([100, 200])
    print p1 + p2
    print p1(1)
    print p1(-1)
    print (p1 + p2)(10)
    print p1 * p1
    print p1 * p2 + p1
    print p1.roots()
    print p2.roots()
    p3 = Polynomial([3, 2, -1])
    print p3.roots()
    print (p1 * p1).roots()


main()  # Calling the main function
