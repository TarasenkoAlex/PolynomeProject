import unittest
import platform
from setuptools import setup, find_packages, Command
from setuptools.command.test import test


class DoTest(test):
    test_args = []
    test_suite = True

    @staticmethod
    def __generate_test_suite():
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests', pattern='*_unit_test.py')
        return test_suite

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run_tests(self):
        test_suite = self.__generate_test_suite()
        test_runner = unittest.runner.TextTestRunner(verbosity=2)
        test_runner.run(test_suite)

setup(
    packages=find_packages(exclude=['tests']),
    cmdclass={'test': DoTest}
)
