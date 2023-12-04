class recursion:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number

        Returns:
            int: computed factorial of the specified number
        """

        # this is the stopping case
        if n == 1:
            return n
        else:
            # this is the general rule that includes the recursive call
            return n * recursion.factorial(n - 1)
        

    @staticmethod
    def power(number: int, power: int):
        """Computes the power of a specified number.

        Args:
            number (int): specified number
            power (int): specified power

        Returns:
            int: computed power of the specified number
        """

        # this is the stopping case
        if power == 0:
            return 1
        else:
            # this is the general rule that includes the recursive call
            return number * recursion.power(number, power - 1)