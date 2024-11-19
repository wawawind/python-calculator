class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if a==0 or b==0:
            return 0
        atemp = abs(a)
        btemp = abs(b)
        result = 0
        for i in range(btemp):
            result = self.add(result, atemp)
        if a<0 and b<0:
            return result
        if a<0 and b>0:
            return -result
        if a>0 and b<0:
            return -result
        else:
            return result

    def divide(self, a, b):
        atemp = abs(a)
        btemp = abs(b)
        if btemp==0:
            print("error")
            return
        result = 0
        while atemp >= btemp:
            atemp = self.subtract(atemp, btemp)
            result += 1
        if a<0 and b<0:
            return result
        if a<0 and b>0:
            return -result
        if a>0 and b<0:
            return -result
        else:
            return result
    
    def modulo(self, a, b):
        if b<0:
            b = -b
        if a>=0:
            while a >= b:
                a = a-b
        else:
            while a<0:
                a = a+b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))