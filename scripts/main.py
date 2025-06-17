import os
import src.data.eda_analysis as eda

def main():
   data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/raw/MachineLearningRating_v3.txt"))
   df=eda.load_data(data_path)
   eda.inspect_data(df)
   cleaned_data=eda.clean_data(df)
   eda.perform_EDA(df)

if __name__ == "__main__":
    main()
