import pandas as pd

# Load the uploaded files
kx_file_path = 'kx.dat'
euu_kx_file_path = 'Euu_kx.dat'

# Read the kx.dat file
kx_data = pd.read_csv(kx_file_path, header=None, names=['kx'])

# Read the Euu_kx.dat file
euu_kx_data = pd.read_csv(euu_kx_file_path,sep='\s+', header=None)

# Insert the kx data as the first column in Euu_kx.dat
euu_kx_data.insert(0, 'kx', kx_data['kx'])

# Save the updated data back to a new file
output_file_path = './output/LM_Euu_kx_with_kx.dat'
euu_kx_data.to_csv(output_file_path, sep='\t', index=False, header=False)

output_file_path
