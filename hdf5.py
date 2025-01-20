import h5py

file_path = "LM_Channel_0180_1d_energy_spectra.h5"  # ファイルパスを指定
with h5py.File(file_path, "r") as f:
    def print_structure(name, obj):
        print(name)

    # ファイル構造を表示
    f.visititems(print_structure)
