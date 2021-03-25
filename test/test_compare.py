# -*- coding: utf-8 -*-
from .helper import check_evaluation

def test_compare():
    for str_expr, str_expected in (
        (
            '"4" == 4',
            "False",
        ),
        (
            '4 == "4"',
            "False",
        ),
        (
            'a == "4"',
            'a == "4"',
        ),            
        (
            "I == I",
            "True",
        ),
        (
            "I == 0",
            "False",
        ),
        (
            "I + 0 == 1 I - 0",
            "True",
        ),
        (
            "I + 5 == I",
            "False",
        ),
    ):
        check_evaluation(str_expr, str_expected)
