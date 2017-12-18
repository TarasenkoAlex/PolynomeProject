class Polynome(object):
    @property
    def degree(self):
        return self._deg

    def __init__(self, coeffs):
        if len(coeffs) == 0:
            raise Exception("Coefficients must be not empty.")

        while coeffs[0] == 0 and len(coeffs) > 1:
            coeffs.remove(coeffs[0])
        self._deg = len(coeffs) - 1
        self._coeffs = coeffs

        self.__reduce()

    def __reduce(self):
        tmp = [0] * (self._deg + 1)
        for i in range(0, self._deg + 1):
            tmp[i] = self._coeffs[self._deg - i]
        self._coeffs = tmp

    def __str__(self):
        if (self.degree != 0):
            monoms = list()
            for i in range(self.degree, -1, -1):
                if isinstance(self._coeffs[i], float):
                    self._coeffs[i] = round(self._coeffs[i], 3)

                if self._coeffs[i] != 0:
                    if i != 0:
                        if i == 1:
                            xxx = 'x'
                        else:
                            xxx = 'x^' + str(i)
                    else:
                        xxx = ''

                    if self._coeffs[i] == 1 or self._coeffs[i] == -1:
                        if len(monoms) == 0:
                            if self._coeffs[i] == -1:
                                monoms.append(' - ' + xxx)
                            else:
                                monoms.append(xxx)
                        elif self._coeffs[i] == 1:
                            monoms.append(' + ' + xxx)
                        else:
                            monoms.append(' - ' + xxx)
                    else:
                        if len(monoms) == 0:
                            monoms.append(str(self._coeffs[i]) + xxx)
                        elif self._coeffs[i] > 0:
                            monoms.append(' + ' + str(self._coeffs[i]) + xxx)
                        else:
                            monoms.append(' - ' + str(self._coeffs[i].__abs__()) + xxx)

            result = str()
            for mon in monoms:
                result += mon

            return result
        else:
            return str(self._coeffs[0])

    def __eq__(self, other):
        if not isinstance(other, Polynome) and not isinstance(other, int) and not isinstance(other, float):
            raise Exception("Second polynome don't exist.")

        if self.__compare__(other) == 0:
            return True
        return False

    def __compare__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if self.degree == 0:
                if self._coeffs[0] > other:
                    return -1
                if self._coeffs[0] < other:
                    return 1
                return 0

        if isinstance(other, Polynome):
            if self.degree > other.degree:
                return 1
            if self.degree < other.degree:
                return -1
            for i in range(self.degree, -1, -1):
                if self._coeffs[i] < other._coeffs[i]:
                    return -1
                if self._coeffs[i] > other._coeffs[i]:
                    return 1
            return 0
        else:
            raise Exception("Second polynome don't exist.")

    def __lt__(self, other):
        if self.__compare__(other) == -1:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__compare__(other) == 1:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__compare__(other) == -1 or self.__compare__(other) == 0:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__compare__(other) == 1 or self.__compare__(other) == 0:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            temp = list()
            for i in range(self.degree, -1, -1):
                temp.append(self._coeffs[i])
            temp[len(temp) - 1] += other
            coeff = temp
            return Polynome(coeff)
        elif isinstance(other, Polynome):
            nums = max(self.degree, other.degree) + 1
            coeff = [0] * nums
            for i in range(0, self.degree + 1):
                coeff[i] = self._coeffs[i]
            for i in range(0, other.degree + 1):
                coeff[i] += other._coeffs[i]
            coeff.reverse()
            return Polynome(coeff)
        else:
            raise Exception("Second polynome don't exist.")

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            temp = list()
            for i in range(self.degree, -1, -1):
                temp.append(self._coeffs[i])
            temp[len(temp) - 1] -= other
            coeff = temp
            return Polynome(coeff)
        elif isinstance(other, Polynome):
            nums = max(self.degree, other.degree) + 1
            coeff = [0] * nums
            for i in range(self.degree, -1, -1):
                coeff[i] = self._coeffs[self.degree - i]
            for i in range(other.degree, -1, -1):
                coeff[i] -= other._coeffs[other.degree - i]
            return Polynome(coeff)
        else:
            raise Exception("Second polynome don't exist.")

    def __rsub__(self, other):
        if not isinstance(other, Polynome) and not isinstance(other, int) and not isinstance(other, float):
            raise Exception("Second polynome don't exist.")
        if not isinstance(other, Polynome):
            first = Polynome([0]) - self
            second = Polynome([other])
            return second.__add__(first)
        else:
            first = Polynome([0]) - self
            second = other
            return second.__add__(first)

    def __isub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            nums = self.degree + 1
            temp = [0] * nums
            for i in range(0, self.degree + 1):
                temp[i] = self._coeffs[i] * other
            coeff = [0] * nums
            for i in range(0, nums):
                coeff[i] = temp[nums - 1 - i]
            return Polynome(coeff)
        elif isinstance(other, Polynome):
            nums = self.degree + other.degree + 1
            temp = [0] * nums
            for i in range(0, self.degree + 1):
                for j in range(0, other.degree + 1):
                    temp[i + j] += self._coeffs[i] * other._coeffs[j]
            coeff = [0] * nums
            for i in range(0, nums):
                coeff[i] = temp[nums - 1 - i]
            return Polynome(coeff)
        else:
            raise Exception("Second polynome don't exist.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self = self * other
        return self
