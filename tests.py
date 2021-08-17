#!/usr/bin/env python3
"""
    Title:          Python programming test, test script
    Description:    Test functions for the Python programming analyses (lib/analyses_processing)

    Author:         Luuk Perdaems
    Emails:         Luukperdaems@hotmail.com
    Websites:       https://github.com/LuukHenk
"""


### Import functions {{{

import unittest
from lib import analyses_processing as analyses

### }}}



###  Tests {{{

EXPECTED_TEST_OUT = "".join([
    "<html><body><table>",
    "<tr><th>Analysis</th><th>Sample ID</th><th>Sample Description</th>",
    "<th>Measurement</th><th>Start Time</th><th>Accumulated Block Time</th>",
    "<th>Excluded Ratio</th><th>C12 Charge</th><th>C13 Charge</th><th>C14 Counts</th>",
    "<th>C12 Time</th><th>Stop Conditions</th><th>Stop Time</th></tr>",
    #
    "<tr><td>//1.0//</td><td>'7'</td><td>'1,3mm Graphite'</td><td>//1.0//</td>",
    "<td>'2020-May-07 17:06:03.544941'</td><td>//0.008333333333333333//</td><td>nan</td>",
    "<td>inf</td><td>//2057469.2305476568//</td><td>//0.002932551319648094//</td>",
    "<td>//0.8333333333333333//</td><td>['Time limit']</td><td>'2020-May-07 17:08:18.325870'</td>",
    "</tr>",
    #
    "<tr><td>2</td><td>'8'</td><td>'1,3mm Graphite'</td><td>1</td>",
    "<td>'2020-May-07 17:08:18.325870'</td><td>120.0</td><td>nan</td><td>inf</td>",
    "<td>4.884520000000001e-07</td><td>366</td><td>1.2000000000000002</td><td>['Time limit']</td>",
    "<td>'2020-May-07 17:10:33.077671'</td></tr>",
    #
    "<tr><td>//0.3333333333333333//</td><td>'9'</td><td>'1,3mm Graphite'</td><td>//1.0//</td>",
    "<td>'2020-May-07 17:10:33.077671'</td><td>//0.008333333333333333//</td><td>//0.0//</td>",
    "<td>//23494.88257962533//</td><td>//2161554.5900611714//</td>",
    "<td>//0.0024630541871921183//</td><td>//0.8333333333333333//</td><td>['Time limit']</td>",
    "<td>'2020-May-07 17:12:47.869253'</td></tr>",
    #
    "<tr><td>4</td><td>'10'</td><td>'1,3mm Graphite'</td><td>1</td>",
    "<td>'2020-May-07 17:12:47.869253'</td><td>120.0</td><td>0.0</td><td>4.252458e-05</td>",
    "<td>4.6171900000000006e-07</td><td>3109</td><td>1.2000000000000002</td>",
    "<td>['Time limit']</td><td>'2020-May-07 17:15:02.701415'</td></tr>",
    "</table></body></html>"
])

class TestStringMethods(unittest.TestCase):
    """ Test cases for the processing analysis """

    def test_sum(self):
        " Tests if the sum function gives the desired output"
        self.assertEqual(analyses.summing(100), 101)

    def test_devision(self):
        " Tests if the devision function gives the desired output"
        self.assertEqual(analyses.devision(100), 0.01)

    def test_multiplication(self):
        " Tests if the mulitplication function gives the desired output"
        self.assertEqual(analyses.multiplication(100), 2000)

    def test_square_root(self):
        " Tests if the square root function gives the desired output"
        self.assertEqual(analyses.square_root(100), 10)

    def test_subtraction(self):
        " Tests if the subtraction function gives the desired output"
        self.assertEqual(analyses.subtraction(100), 99)

    def test_natural_log(self):
        " Tests if the natural log function gives the desired output"
        self.assertEqual(round(analyses.natural_log(2.7183)), 1)

    def test_main_success(self):
        """
        Test if the main function succeeds with an input file that should be working
        Fails if the output file is not what is expected
        """
        self.assertEqual(analyses.main("unittest"), EXPECTED_TEST_OUT)

### }}}

if __name__ == '__main__':
    unittest.main()
