# Python programming test
File processing engine that is able to process the 'analyses' sub-section of  data (results) from the input file.

## Usage
Run the main script using python using the desired input arguments
`$ python main.py <formula> <ams_file_path>`

### Positional arguments
* `<formula>`: str - The formula we want to use on all the numerical values in the analyses table (options: sum, devision, multiplication, square_root, subtraction, natural_logarithm)
* `<ams_file_path>`: str - Path to the ams file containing an analyses subsection

### Optional arguments
* `--out`: Output file path (default: `./processed_analysis.html`)
