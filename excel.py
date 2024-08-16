import pandas as pd
import os

def split_csv(input_file, column_name):
    # Membaca file CSV
    df = pd.read_csv(input_file)
    
    # Mendapatkan nama file tanpa ekstensi
    file_name = os.path.splitext(input_file)[0]
    
    # Mendapatkan nilai unik dari kolom yang ditentukan
    unique_values = df[column_name].unique()
    
    # Membuat folder output jika belum ada
    output_folder = f"{file_name}_split"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Memecah file berdasarkan nilai unik
    for value in unique_values:
        # Membuat subset data untuk nilai tertentu
        subset = df[df[column_name] == value]
        
        # Membuat nama file output
        output_file = f"{output_folder}/{file_name}_{value}.csv"
        
        # Menyimpan subset ke file CSV baru
        subset.to_csv(output_file, index=False)
        
        print(f"File {output_file} telah dibuat.")

# Memanggil fungsi split_csv
input_file = "customer.csv"  
column_name = "gender"  

split_csv(input_file, column_name)