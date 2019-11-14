import unittest
import test_planday
import os

# Import the HTMLTestRunner Module
import HtmlTestRunner

# Get the Present Working Directory since that is the place where the report
# would be stored

current_directory = os.path.dirname(os.path.realpath(__file__))


class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_Planday(self):
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_planday.TestPayday)
        ])

        output_file = open(current_directory + "\\reports\Planday.html", "w+")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
