import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#initialize the data ingestion configuration
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts', 'train.csv')
    test_data_path=os.path.join('artifacts', 'test.csv')
    raw_data_path=os.path.join('artifacts', 'raw.csv')

#create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_Config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
        
        try:
            df = pd.read_csv('https://raw.githubusercontent.com/sunnysavita10/credit_card_pw_hindi/main/creditCardFraud_28011964_120214.csv')
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_Config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_Config.raw_data_path, index=False)

            logging.info('Train Test split')
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_Config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_Config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_Config.train_data_path,
                self.ingestion_Config.test_data_path
            )

        except Exception as e:
            logging.info('Dataset read as pandas Dataframe')


