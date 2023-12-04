class loops:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number

        Returns:
            int: computed factorial of the specified number
        """

        # the counter variable i  more or less contains
        # the same value as the parameter n

        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop
        # is when i == 1 --> stopping case for the loop

        # with each iteration of the loop, 
        # we are decrementing the counter variable by 1
        i = n - 1
        while i > 1:
            n *= i
            i -= 1

        return n
    
    @staticmethod
    def power(number: int, power: int):
        """Computes the power of a specified number.

        Args:
            number (int): specified number
            power (int): specified power

        Returns:
            int: computed power of the specified number
        """

        # the counter variable i contains
        # the same value as the parameter power

        # the loop will repeat as long as i > 0
        # the condition that will cause the loop to stop
        # is when i == 0 --> stopping case for the loop

        # with each iteration of the loop, 
        # we are decrementing the counter variable by 1

        result = 1

        i = power
        while i > 0:
            result *= number
            i -= 1

        return result