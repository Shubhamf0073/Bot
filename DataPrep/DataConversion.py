import pandas as pd

def ConversionJSON(jsonPath,jsonOutputPath):
    
    try: 
        jsonDf = pd.read_json(jsonPath)
        jsonDf.to_csv(jsonOutputPath, index = False)
        print(f"JSON converted: {jsonOutputPath}")
        return jsonDf
        
    except Exception as e:
        print(f"Error in json: {str(e)}")
        return None

        
def ConversionParquet(parquetPath, parquetOutputPath):
    
    try:
        parquetDf = pd.read_parquet(parquetPath)
        parquetDf.to_csv(parquetOutputPath, index = False)
        print(f"Parquet converted: {parquetOutputPath}")
        return parquetDf
    
    except Exception as e:
        print(f"Error in parquet: str{e}")
        return None
        
        
if __name__ == "__main__":
    jsonFile = "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d7.json"    
    parquetFiles = [
        "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d8.parquet",
        "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d6.parquet"
        ]
    jsonOutput = "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d7.csv"

    
    jsondf = ConversionJSON(jsonFile,jsonOutput)
    
    for idx, parquetFile in enumerate(parquetFiles):

        fileNum = parquetFile.split('/')[-1].replace('.parquet', '')
        parquetOutput = f"/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/{fileNum}_from_parquet.csv"
        parquet_df = ConversionParquet(parquetFile, parquetOutput)