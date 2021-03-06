"""
A non-python example, with tests for IRKernel (irkernel.github.io).
(Beware of python quoting/string escaping rules being different to the
language being tested)
"""

import unittest
import jupyter_kernel_test as jkt

class IRKernelTests(jkt.KernelTests):
    kernel_name = "ir"

    language_name = "R"

    file_extension = ".r"

    code_hello_world = 'print("hello, world")'

    completion_samples = [
        {
            'text': 'zi',
            'matches': {'zip'},
        },
    ]

    complete_code_samples = ['1', "print('hello, world')", "f <- function(x) {x*2}"]
    incomplete_code_samples = ["print('hello", "f <- function(x) {x"]

    code_generate_error = "raise"

    code_execute_result = [
        {'code': "1+2+3", 'result': "[1] 6"}
    ]

    code_display_data = [
        {'code': "plot(iris)", 'mime': "image/png"},
    ]


if __name__ == '__main__':
    unittest.main()
