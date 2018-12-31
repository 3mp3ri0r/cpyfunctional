import unittest

import cpyfunctional


class TestFuncCurry(unittest.TestCase):
    """
    Test func_curry function able to make callable accept parameters.
    """

    def test_func_curry_able_to_make_callable_accept_params(self):
        """
        func_curry given callable that given multiple params, able to return value from them.
        """
        def add(number1: int, number2: int, prev_number: int) -> int:
            return number1 + number2 + prev_number
        result = cpyfunctional.compose(cpyfunctional.func_curry(add)(5, 7), lambda number: number ** 2)(3)
        self.assertEqual(result, 21)
