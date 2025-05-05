import os
import kagglehub
import pandas as pd

dataDir = "../Data"
os.makedirs(dataDir, exist_ok=True)

splits = {'train': 'train.csv', 'validation': 'validation.csv', 'test': 'test.csv'}

try:
    path = kagglehub.dataset_download("thedevastator/nlp-mental-health-conversations")
    print("Path to dataset files:", path)

    datasets = {
    "d1.json": pd.read_json("hf://datasets/Amod/mental_health_counseling_conversations/combined_dataset.json", lines=True),
    "d2.csv": pd.read_csv("hf://datasets/RishiKompelli/TherapyDataset/data.csv")
    ,"d3.csv": pd.read_csv("hf://datasets/Riyazmk/mentalhealth/fullMentalHealth.csv")
    ,"d4.csv": pd.read_csv("hf://datasets/Kiran2004/MentalHealthConversations/Kiran-deppression.csv")
    ,"d5.csv": pd.read_csv("hf://datasets/Mr-Bhaskar/Synthetic_Therapy_Conversations/" + splits["train"])
    ,"d6.parquet": pd.read_parquet("hf://datasets/Aarya4536/therapy-bot-data-10k/data/train-00000-of-00001.parquet")
    ,"d7.json": pd.read_json("hf://datasets/adarshxs/Therapy-Alpaca/final.json")
    ,"d8.parquet": pd.read_parquet("hf://datasets/mshojaei77/merged_mental_health_dataset/data/train-00000-of-00001.parquet")
}

    for filename, df in datasets.items():
        filePath = os.path.join(dataDir, filename)
        if filename.endswith(".csv"):
            df.to_csv(filePath, index = False)
        elif filename.endswith(".json"):
            df.to_json(filePath, orient = "records")
        elif filename.endswith(".parquet"):
            df.to_parquet(filePath, index = False)
        print(f"Saved {filename} to {filePath}")
        
    cleanDf = pd.read_csv(os.path.join(dataDir, "convoStarter - Sheet1.csv"))
    print("datasets downloaded and saved")
    
except Exception as e:
    print(f"Error occured: {str(e)}")
