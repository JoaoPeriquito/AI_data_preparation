""" 
@author: Joao Periquito 
iBEAt CLUSTER MAIN Scrpit
2023
UNETR - DATA PREPARATION
"""
import pandas as pd
from pipelines import UNETR_data_preparation
from scripts import XNAT_credentials as XNAT_cred
from scripts import select_folder_to_save

if __name__ == '__main__':

    #XNAT Credentials
    username, password = XNAT_cred.main()

    path = select_folder_to_save.main()
    print(path)

    series_desc = [
    'T1w_abdomen_dixon_cor_bh_out_phase_post_contrast',
    'T1w_abdomen_dixon_cor_bh_in_phase_post_contrast',
    'T1w_abdomen_dixon_cor_bh_fat_post_contrast',
    'T1w_abdomen_dixon_cor_bh_water_post_contrast'
    ]

    df = pd.read_csv('unter_training_dataset.csv')

    UNETR_data_preparation.main(username, password, path, df, series_desc)