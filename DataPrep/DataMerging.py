import pandas as pd

filePaths = [
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d0.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d1.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d2.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d3.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d4.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d5.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d6_from_parquet.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d7.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/d8_from_parquet.csv",
    "/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/convoStarter - Sheet1.csv"
]

dfs = [pd.read_csv(filePath) for filePath in filePaths]

mergedDf = pd.concat(dfs, ignore_index = True)

print(f"Merged df shape: {mergedDf.shape}")
print(f"Merged df columns: {mergedDf.columns}")
print(f"Merged df head: {mergedDf.head()}")

mergedDf.to_csv("/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/final.csv", index = False)

print("Merged data saved as final.csv")