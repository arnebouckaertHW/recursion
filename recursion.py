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
        
    @staticmethod
    def computeMin(nums, i: int, min: int):
        """Computes the minimum value of a list of numbers.

        Args:
            nums: list of numbers
            i (int): index
            min (int): minimum value

        Returns:
            int: minimum value of the list of numbers
        """

        # this is the stopping case
        if i == len(nums):
            return min
        else:
            # this is the general rule that includes the recursive call
            if nums[i] <= min:
                min = nums[i]
            return recursion.computeMin(nums, i + 1, min)
        
    @staticmethod
    def reverse(s: str, i: int):
        """Displays the reverse of a string.
        
        Args:
            s (str): specified string
            i (int): index
        """

        # this is the stopping case
        if i == 0:
            print(" is the reverse of %s using recursion." % s)
        else:
            # this is the general rule that includes the recursive call
            print(s[i - 1], end = "")
            recursion.reverse(s, i - 1)

    @staticmethod
    def search(a, first: int, size: int, target, i: int, found: bool):
        """Searches for a desired element in a list of elements starting at a[first].

        Args:
            a: the list to search
            first (int): the list index at which the search will start
            size (int): the number of elements to search
            target: the element to search for
            i: the counter variable used to iterate through list
            found: the variable used to denote if the target has been found
        Returns:
            int: If target appears in the list, index of the element
            that contains the target, else -1.
        """

        # this is the stopping case
        if i == size or found or (i + first >= len(a)):
            if found:
                return first + i - 1
            else:
                return -1
        else:
            # this is the general rule that includes the recursive call
            if a[first + i] == target:
                found = True
            return recursion.search(a, first, size, target, i + 1, found)