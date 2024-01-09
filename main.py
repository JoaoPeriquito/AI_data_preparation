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

    save_path = select_folder_to_save.main() #Select save folder

    username, password = XNAT_cred.main() #XNAT Credentials

    series = [ #select series using standardize names
    'T1w_abdomen_dixon_cor_bh_out_phase_post_contrast',
    'T1w_abdomen_dixon_cor_bh_in_phase_post_contrast',
    'T1w_abdomen_dixon_cor_bh_fat_post_contrast',
    'T1w_abdomen_dixon_cor_bh_water_post_contrast'
    ]

    list_of_patients = pd.read_csv('unter_training_dataset.csv')

    UNETR_data_preparation.main(username, password, save_path, list_of_patients, series)