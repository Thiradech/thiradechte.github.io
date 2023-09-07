import pandas as pd
path = "Fundscan/data/"

def clean_smart(data:str, columns_name:str, output_name:str):
    path = "Fundscan/data/"
    data = f"{path}{data}"
    columns_name = f"{path}{columns_name}"
    output_name = f"{path}{output_name}"
    
    cols_name = []
    with open(columns_name, 'r') as file:
        cols = file.read()
        
    cols_name = cols.split(",")
    for i in range(len(cols_name)):
        cols_name[i] = cols_name[i][1:len(cols_name[i])-1]
    
    df = pd.read_csv(data, names=cols_name)
    for i in range(len(df.columns)):
        df.iloc[:, i].replace(["-", "-%"], None, inplace=True)
        df.iloc[:, i].replace("ไม่มี", "No", inplace=True)
    
    df.to_csv(output_name)

if __name__ == '__main__':
    clean_smart("Fund Comparison.csv", "cols_name.txt", "cleaned_data.csv")
    print("Done! 123")