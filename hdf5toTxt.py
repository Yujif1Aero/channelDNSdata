import h5py

# HDF5 ファイルをテキスト形式にエクスポートする関数
def export_hdf5_to_txt(file_path, output_txt_path):
    with h5py.File(file_path, "r") as f:
        with open(output_txt_path, "w", encoding="utf-8") as txt_file:
            # 再帰的にデータセットの構造とデータを取得する関数
            def write_structure_and_data(name, obj):
                if isinstance(obj, h5py.Dataset):
                    txt_file.write(f"Dataset: {name}\n")
                    txt_file.write(f"Shape: {obj.shape}\n")
                    txt_file.write(f"Data:\n{obj[:]}\n\n")
                elif isinstance(obj, h5py.Group):
                    txt_file.write(f"Group: {name}\n\n")

            # ファイル全体を訪問して出力
            f.visititems(write_structure_and_data)

# ファイルパスを指定
input_hdf5_path = "LM_Channel_0180_1d_energy_spectra.h5"  # 読み込む HDF5 ファイル
output_txt_path = "output_data.txt"  # 出力するテキストファイル

# エクスポートを実行
export_hdf5_to_txt(input_hdf5_path, output_txt_path)

print(f"HDF5 ファイルの内容を '{output_txt_path}' にエクスポートしました。")
