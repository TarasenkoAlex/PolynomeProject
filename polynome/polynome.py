class Polynome(object):
    def __init__(self, coeffs):
        if len(coeffs) == 0:
            raise Exception("Polynome don't exist without coefficients.")
        self._degree = len(coeffs) - 1
        self._coefficients = coeffs
        self.__reduce()

    def __reduce(self):
        tmp = [0] * (self._degree + 1)
        for i in range(0, self._degree + 1):
            tmp[i] = self._coefficients[self._degree - i]

        self._coefficients = tmp

    def __eq__(self, other):
        if not isinstance(other, Polynome):
            raise Exception("Other isn't polynome.")

        if self.__compare__(other) == 0:
            return True
        return False

    def __compare__(self, other):
        if not isinstance(other, Polynome):
            raise Exception("Other isn't polynome.")

        if self.degree < other.degree:
            return -1
        if self.degree > other.degree:
            return 1
        for i in range(self.degree, -1, -1):
            if self._coefficients[i] < other._coefficients[i]:
                return -1
            if self._coefficients[i] > other._coefficients[i]:
                return 1
        return 0

    def __add__(self, other):
        if isinstance(other, Polynome):
            count = max(self.degree, other.degree) + 1
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                tmp[i] = self._coefficients[i]
            for i in range(0, other.degree + 1):
                tmp[i] += other._coefficients[i]
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        elif isinstance(other, int) or isinstance(other, float):
            count = self.degree + 1
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                tmp[i] = self._coefficients[i]
            tmp[0] += other
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        else:
            raise Exception("Other isn't polynome.")

    def __sub__(self, other):
        if isinstance(other, Polynome):
            count = max(self.degree, other.degree) + 1
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                tmp[i] = self._coefficients[i]
            for i in range(0, other.degree + 1):
                tmp[i] -= other._coefficients[i]
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        elif isinstance(other, int) or isinstance(other, float):
            count = self.degree + 1
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                tmp[i] = self._coefficients[i]
            tmp[0] -= other
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        else:
            raise Exception("Other isn't polynome.")

    def __mul__(self, other):
        if isinstance(other, Polynome):
            count = self.degree + other.degree + 2
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                for j in range(0, other.degree + 1):
                    tmp[i + j] += self._coefficients[i] * other._coefficients[j]
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        elif isinstance(other, int) or isinstance(other, float):
            count = self.degree + 1
            tmp = [0] * count
            for i in range(0, self.degree + 1):
                tmp[i] = self._coefficients[i] * other
            coeff = [0] * count
            for i in range(0, count):
                coeff[i] = tmp[count - 1 - i]
            while coeff[0] == 0 and len(coeff) > 1:
                coeff.remove(coeff[0])
            return Polynome(coeff)
        else:
            raise Exception("Other isn't polynome.")

    def __str__(self):
        result = str()
        if (self.degree == 0):
            return str(self._coefficients[0])

        for i in range(self.degree, -1, -1):
            s = str()
            if i != 0:
                if self._coefficients[i] > 0:
                    if i == self.degree:
                        s = str(self._coefficients[i]) + 'x^' + str(i)
                    else:
                        s = '+' + str(self._coefficients[i]) + 'x^' + str(i)
                if self._coefficients[i] < 0:
                    s = str(self._coefficients[i]) + 'x^' + str(i)
            else:
                if self._coefficients[i] > 0:
                    if i == self.degree:
                        s = str(self._coefficients[i])
                    else:
                        s = '+' + str(self._coefficients[i])
                if self._coefficients[i] < 0:
                    s = str(self._coefficients[i])
            result += s

        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def degree(self):
        return self._degree
