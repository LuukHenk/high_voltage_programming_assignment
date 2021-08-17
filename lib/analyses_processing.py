#!/usr/bin/env python3
"""
    Title:          Python programming test
    Description:    Process 'analyses' subsection of .ams measurement files

    Author:         Luuk Perdaems
    Emails:         Luukperdaems@hotmail.com
    Websites:       https://github.com/LuukHenk
"""

### Import functions {{{

import math
import sys
import argparse

### }}}



### Formulas used for processing {{{

def summing(val):
    "Sum"
    return val + (0.01 * val)

def devision(val):
    "Devision"
    return 1 / val

def multiplication(val):
    "Multiplication"
    return val * val * 0.2

def square_root(val):
    "Square root"
    return math.sqrt(val)

def subtraction(val):
    "Subtraction"
    return val - (0.01 * val)

def natural_log(val):
    "Natural logarithm"
    return math.log(val)

FORMULAS = {
    "sum": {
        "function": summing,
        "str_format": "++{}++"
    },
    "devision": {
        "function": devision,
        "str_format": "//{}//"
    },
    "multiplication": {
        "function": multiplication,
        "str_format": "**{}**"
    },
    "square_root": {
        "function": square_root,
        "str_format": "##{}##"
    },
    'subtraction': {
        "function": subtraction,
        "str_format": "--{}--"
    },
    "natural_logarithm": {
        "function": natural_log,
        "str_format": "..{}.."
    }
}
### }}}



### Input arguments {{{

def argument_handler(formulas):
    """
        Handles input arguments
        formula == the selected formula used for processing
        ams_file_path == Path to the ams file

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "formula",
        type=str,
        choices=formulas,
        help="Math formula to be applied to the data records"
    )
    parser.add_argument(
        "ams_file_path",
        type=str,
        help="Path to .ams file"
    )
    parser.add_argument(
        "--out",
        type=str,
        default="processed_analysis.html",
        help="Output file path"
    )
    return parser.parse_args()

### }}}



### Load and save file functions {{{

def load_file(filename):
    "Load a file"
    try:
        with open(filename, 'r') as myfile:
            inp = myfile.read()
        print("Opened '{}' ...".format(filename))
    except IOError:
        print("Unable to locate the input file '{}'".format(filename))
        sys.exit()

    return inp

def save_file(filename, output):
    "Save data to a file"
    with open(filename, "w") as myfile:
        myfile.write(output)
        print("Saved output in '{}' ...".format(filename))

### }}}



### Main function {{{

def main(mode="normal"):
    """
        Main function of the script
            1. Handle input arguments
            2. Load analysis section from file (data formatting)
            3. write the processed data to an HTML table
            4. Save / return output
    """



    ### 1. INPUT ARGUMENT HANDLING ###
    # Check if we are running a test file
    if mode == "unittest":
        formula_id = "devision"
        ams_file_path = "./test.ams"
    else:
        # Load input arguments if not testing
        # (formula, input file path and the optional output file path)
        arguments = argument_handler(list(FORMULAS.keys()))
        formula_id = arguments.formula
        ams_file_path = arguments.ams_file_path
        out_file_path = arguments.out

    # Load selected formula and open input file
    formula = FORMULAS[formula_id]
    data = load_file(ams_file_path)



    ### 2. DATA FORMATTING ###
    # Try to find Analysis section in file,
    # raise error and exit if not found.
    try:
        data = data.split("# Analyses")[1].split("#")[0]
    except IndexError:
        print(f"Unable to find '# Analyses' records in '{ams_file_path}'")
        sys.exit()

    # Format the Analyses data rows to a 2d table
    data = [x.split("\t") for x in data.split("\n")[:-1]]



    ### 3. TABLE FORMATTING ###
    # Generate the basic table setup
    table_out = "".join([
        "<html><body><table><tr>",
        "".join(["<th>{}</th>".format(x) for x in data[1]]),
        "</tr>"
    ])

    # Loop over the data rows and add the numerical values to a table
    for row_id, row in enumerate(data[2:]):
        # Loop over the values in the data rows and add data to the html row
        table_out += "<tr>"

        # Only process the even rows
        row_processing = row_id % 2 == 0

        for value in row:
            table_out += "<td>"

            # Only edit the values if the row is allowed to be processed
            if row_processing:
                # Check if the value can be a float
                # if so, apply the formula and format to the desired string format
                try:
                    if value in ["inf", "nan"]:
                        raise ValueError

                    out_value = float(value)
                    if out_value != 0:
                        out_value = formula["function"](out_value)
                    table_out += formula["str_format"].format(out_value)

                except ValueError:
                    table_out += value
            # Just add the values to the output if the row should not be processed
            else:
                table_out += value

            table_out += "</td>"
        table_out += "</tr>"
    table_out += "</table></body></html>"



    ### 4. SAVE OR RETURN OUTPUT ###
    # save if not running a test
    if mode != "unittest":
        save_file(out_file_path, table_out)
    return table_out

### }}}
