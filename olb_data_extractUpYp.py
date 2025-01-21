import pandas as pd

def extract_zp_up_data(input_file, output_file):
    """
    Extract zp_0, zp_1, zp_2, up0, up1, up2 columns from the input file and save to an output file.

    Args:
        input_file (str): Path to the input data file.
        output_file (str): Path to save the extracted data.
    """
    # Load the data, skipping comments and reading specific columns
    data = pd.read_csv(input_file, delim_whitespace=True, comment='%', header=None)

    # Extract columns zp_0(4), zp_1(5), zp_2(6), up0(7), up1(8), up2(9)
    extracted_data = data[[4,5,6,7,8,9]]
    extracted_data.columns = ['zp_0', 'zp_1', 'zp_2', 'up0', 'up1', 'up2']

    # Add header row with %
    header = "% zp_0\tzp_1\tzp_2\tup0\tup1\tup2\n"

    # Save the extracted data to a new file with % in the header row
    with open(output_file, 'w') as f:
        f.write(header)
        extracted_data.to_csv(f, sep='\t', index=False, header=False)

if __name__ == "__main__":
    # Input and output file paths
    input_file = "DNS-LBMD3Q19BGK_ThirdOrder_banceBack_N96_Retau180.000000.dat"
    output_file = "extracted_zp_up_data.txt"

    # Extract and save data
    extract_zp_up_data(input_file, output_file)
    print(f"Extracted data has been saved to {output_file}")
