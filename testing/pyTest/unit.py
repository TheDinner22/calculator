unit_tests = {}

# dependencies
from pyLib.float import My_Float

# My_float throws when not passed None, str, or int
def test1(done):
    def yep_this_too():
        pass

    class No_data_type_is_safe:
        really = "YES"

    # put all bad inputs into a list to iterate over
    bad_inputs = [
        {"this" : "is wrong"},
        ["im a ", "bad input"],
        ("tuples", "also", "no go"),
        3.1415926535897932384626433,
        yep_this_too,
        No_data_type_is_safe,
        True,
        False,
        [],
        {},
        ()
    ]

    for bad_input in bad_inputs:
        try:
            My_Float(bad_input)

            # if it made it to this line, My_float didn't throw so the test failed
            raise AssertionError("My_Float did not throw when passed:\n" + str(bad_input))
        except TypeError:
            continue
        
    done("My_float throws when not passed None, str, or int")
unit_tests["My_float throws when not passed None, str, or int"] = test1

# My_float works with int input
def test2(done):
    # define input and expected output
    good_input = -2134
    expected_output = [2134, ".", 0]

    # define the actual output, the value property on the My_Float class
    output = My_Float(good_input).Value


    err_msg = f"expected output: {expected_output}\ndid not equal\noutput: {output}"
    assert expected_output == output, err_msg

    done("My_float works with int")
unit_tests["My_float works with int"] = test2

# My_float works with str (with/w-out dot)
def test3(done):
    # key = input
    # value = expected output
    inputs = {
        "-234" : [234, ".", 0],
        "3356.54336" : [3356, ".", 54336]
    }

    for input, expected_output in inputs.items():
        # create output
        output = My_Float(input).Value

        err_msg = f"expected output: {expected_output}\ndid not equal\noutput: {output}"
        assert expected_output == output, err_msg

    done("My_float works with str (with/w-out dot)")
unit_tests["My_float works with str (with/w-out dot)"] = test3

# My_float works with + - sign (for int and str)
def test4(done):
    # key = input
    # value = expected output
    inputs = {
        "123.123" : True,
        "-321.456" : False,
        123 : True,
        -321 : False
    }

    for input, expected_output in inputs.items():
        output = My_Float(input).Is_positive

        err_msg = f"expected output: {expected_output}\ndid not equal\noutput: {output}"
        assert expected_output == output, err_msg
    
    done("My_float works with + - sign (for int and str)")
unit_tests["My_float works with + - sign (for int and str)"] = test4

# My_float works with None
def test5(done):
    good_input = None
    expected_output = [0, ".", 0]

    output = My_Float(good_input).Value

    err_msg = f"expected output: {expected_output}\ndid not equal\noutput: {output}"
    assert expected_output == output, err_msg

    done("My_float works with None")
unit_tests["My_float works with None"] = test5

# Value setter logic throws on bad inputs 
def test6(done):
    my_float = My_Float(123)

    def yep_this_too():
        pass

    class No_data_type_is_safe:
        really = "YES"

    # put all bad inputs into a list to iterate over
    bad_inputs = [
        {"this" : "is wrong"},
        ["im a ", "bad input"],
        ("tuples", "also", "no go"),
        3.1415926535897932384626433,
        yep_this_too,
        No_data_type_is_safe,
        True,
        False,
        [],
        {},
        (),
    ]

    for bad_input in bad_inputs:
        try:
            my_float.Value = bad_input

            # if it made it to this line, My_float didn't throw so the test failed
            raise AssertionError("My_Float.Value setter function did not throw when passed:\n" + str(bad_input))
        except TypeError:
            continue

    done("Value setter logic throws on bad inputs")
unit_tests["Value setter logic throws on bad inputs"] = test6

'''
# example tests
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
unit_tests["one plus one is equal to two"] = one_plus_one_is_two

def one_plus_one_is_three(done):
    outcome = 1+1
    desired_outcome = 3
    assert outcome == desired_outcome, "1+1 was not equal to three"
    done("one plus one is equal to three")
unit_tests["one plus one is equal to three"] = one_plus_one_is_three
'''
