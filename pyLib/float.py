# my custom float class used to handle floating point numbers


class My_Float:
    def __init__(self, value):
        """validate value param and turn it into float

        Args:
            value (int, str, None): Value to be converted into a float

        Note:
            float isn't a type for the value arg here becuase it has been replaced!!
        """

        self.__is_positive = True

        # validate, and if possible update to, the given value
        self._validate_and_process_input(value)
         

    def _validate_and_process_input(self, value):
        """check that 'value' can be converted into a float, error if it cannot

        Args:
            value (str, int, None): only accepts 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, None, and '.'
            (and the string form of those ints) also positive and negative numbers are accepeted
        """
        # if its a None type, just make the value 0.0
        if value == None:
            self.__value = [0,".",0]

        # if its a string or int, check for + and - sign and then assign value
        elif type(value) == str or type(value) == int:
            value = str(value).strip()

            # if it has a length, check for + or - sign
            if len(value):
                value = self._check_and_update_sign(value)

                # check to make sure there are only numbers and optionally a "."
                ok_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
                has_a_dot = False
                for i in range(len(value)):
                    if not value[i] in ok_chars:
                        self._raise_bad_input_error()
                    elif value[i] == ".":
                        has_a_dot = True

                # add a dot and 0 to the end, if their is not already one
                if not has_a_dot:
                    value = value + ".0"

                # convert to list representation
                split_float = value.split(".")
                before = split_float[0]
                after = split_float[1] if split_float[1] != "" else "0"

                # check for more than one '.'
                if len(split_float) != 2:
                    self._raise_bad_input_error() 

                self.__value = [(before), ".", (after)]

        # raise error if its not a string, int, or None type
        else:
            raise TypeError("value must be: None, str, or int")

    def _check_and_update_sign(self, value):
        """if the first char in value is + or -, update the self.__positive attribute
        to true or false respectively

        Args:
            value (str): exactly what was passed into the __init__ function, cast to str with no whitespace

        Returns:
            [str]: [exactly what was passed into the function, possibly missing a "+" or "-" from index 0]
        """

        char = value[0]

        # check for + or -
        if char == "+":
            self.__is_positive = True
            value = value[1:]
        elif char == "-":
            self.__is_positive = False
            value = value[1:]

        return value

    @staticmethod
    def _raise_bad_input_error():
        """raise en error saying that the input passed to __init__ was bad
        """
        raise ValueError("Only numbers and one '.' are valid inputs")

    @property
    def Value(self):
        """getter for self.__value

        Returns:
            [list]: [index 0 is the whole number, index 1 is '.' index 2 is the decimal number]
        """
        return self.__value

    @Value.setter
    def Value(self, new_value):
        """setter for self.__value

        Args:
            new_value (int, str, none): Value to be converted into a float
        """
        self._validate_and_process_input(new_value)

    @property
    def Is_positive(self):
        """getter for self.__is_positive

        Returns:
            [bool]: true if the number is positive, otherwise false
        """
        return self.__is_positive

    def __repr__(self):
        """you know what this does

        Returns:
            [str]: [a string containing a float for example: "123.0"]
        """
        negative_sign = "-" if not self.__is_positive else ""
        return negative_sign + str(self.__value[0]) + self.__value[1] + str(self.__value[2]) # example output: "123.123"

    def __str__(self):
        """you know what this does

        Returns:
            [str]: [a string containing a float for example: "123.0"]
        """
        negative_sign = "-" if not self.__is_positive else ""
        return negative_sign + str(self.__value[0]) + self.__value[1] + str(self.__value[2]) # example output: "123.123"

    def __bytes__(self):
        """compute a byte-string representation of an object

        Returns:
            [bytes]: [float as a string cast to bytes type]
        """
        float_as_str = str(self.__value[0]) + self.__value[1] + str(self.__value[2])
        return bytes(float_as_str, 'utf-8')

    # TODO make me later if needed
    # def __format__(self, format_spec: str) -> str:
    #     # acceptable format specs:
    #     # "float" or "e" or "ratio" or "x.precision"
    #     pass

    # TODO add lt le etc magic methods


        


if __name__ == "__main__":
    f = My_Float("-432432.010")

    print(f)
    print(f.Is_positive)

    print(f.Value)

    # f.Value = "ahdak" # <- throws error | thats a good thing
    # print(f.Value)
