# Aim is to read the data from the source and prepare it to train, test, split 

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.exceptions import CustomException
from src.logger import logging
from src.components.datatransform import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    data_path: str=os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self):
        try:
            data = pd.read_csv('notebook/data/stud.csv')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            data.to_csv(self.ingestion_config.data_path, index=False, header=True)

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            return(self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.start_data_ingestion()

    data_transform = DataTransformation()
    data_transform.start_data_transformation(train_data, test_data)