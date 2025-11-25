import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from logger import get_logger
from custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self,datafile_path,outputfile_path):
        self.datafile_path=datafile_path
        self.outputfile_path=outputfile_path
        os.makedirs(self.outputfile_path,exist_ok=True)
    def load_data(self):
        try:
            self.df=pd.read_csv(self.datafile_path)
            logger.info("Data loaded sucesfuly...")
            # self.df["Date"]=pd.to_datetime(self.df["Date"])
            # self.df["Year"] = self.df["Date"].dt.year
            # self.df["Month"] = self.df["Date"].dt.month
            # self.df["Day"] = self.df["Date"].dt.day
            # self.df.drop("Date" , axis=1 , inplace=True)
            # categorical=df.select_dtypes(include=["object"])
            # numerical=df.select_dtypes(include=['number'])
        except Exception as e:
            logger.error(f"Error while loading data {e}")
            raise CustomException("Failed to load data" , e)
    def preprocess(self):
        try:
            self.df["Date"]=pd.to_datetime(self.df["Date"])
            self.df["Year"] = self.df["Date"].dt.year
            self.df["Month"] = self.df["Date"].dt.month
            self.df["Day"] = self.df["Date"].dt.day
            self.df.drop("Date" , axis=1 , inplace=True)
            self.categorical=self.df.select_dtypes(include=["object"])
            self.numerical=self.df.select_dtypes(include=['number'])
            for col in self.numerical:
                self.df[col].fillna(self.df[col].mean(),inplace=True)
            for col in self.categorical:
                self.df[col].fillna(self.df[col].mode()[0],inplace=True)

                logger.info("Basic data processing done...")
        
        except Exception as e:
            logger.error(f"Error while preprocess data {e}")
            raise CustomException("Failed to preproces data" , e)
    def encode_data(self):
        try:
            label_encoder=LabelEncoder()
            for col in self.categorical:
                self.df[col]=label_encoder.fit_transform(self.df[col])
            logger.info("Label Encoding DOne....")
        except Exception as e:
            logger.error(f"Error while label encode data {e}")
            raise CustomException("Failed to label encode data" , e)
        
    def split_data(self):
        try:
            X=self.df.drop("RainTomorrow",axis=1)
            y=self.df["RainTomorrow"]
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

            joblib.dump(X_train,os.path.join(self.outputfile_path,"X_train.pkl"))
            joblib.dump(X_test,os.path.join(self.outputfile_path,"X_test.pkl"))
            joblib.dump(y_train,os.path.join(self.outputfile_path,"y_train.pkl"))
            joblib.dump(y_test,os.path.join(self.outputfile_path,"y_test.pkl"))

            logger.info("Splitted and saved sucesfully....")

        except Exception as e:
            logger.error(f"Error while splittting data {e}")
            raise CustomException("Failed to split data" , e)
    def run(self):
        self.load_data()
        self.preprocess()
        self.encode_data()
        self.split_data()
        logger.info("Data Procesing Completed....")
if __name__=="__main__":
    processor = DataProcessing("artifacts/raw/data.csv" , "artifacts/processed")
    processor.run()