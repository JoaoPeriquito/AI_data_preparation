import scripts.xnat as xnat
import os
import dbdicom as db
import pipelines.rename as rename
import numpy as np
import nibabel as nib
import shutil

def main(username, password, save_path, list_of_patient_ids, chosen_series):

    for ID in list_of_patient_ids.ID:
        try:
            XNAT_dataset_name = xnat.download_study(username, password, save_path,specific_dataset=ID)
            path_scan = os.path.join(save_path, XNAT_dataset_name)
        except:
            print('Dataset name is incorrect or does NOT exist!')
            continue

        folder = db.database(path=path_scan)
        rename.main(folder)

        array_list = []
        for serie in chosen_series:
            try:
                series_temp = folder.series(SeriesDescription=serie)
                print(series_temp[0]['SeriesDescription'])
                if series_temp:
                    array_temp, _ = series_temp[0].array(['SliceLocation', 'AcquisitionTime'], pixels_first=True)
                    array_temp = np.squeeze(array_temp)
                    array_list.append(array_temp)
            except:
                print(serie + " was NOT found!")

        try:        
            stacked_array = np.stack(array_list, axis=3)
            stacked_array = np.transpose(stacked_array, (1,0,2,3))
            np.save(os.path.join(save_path, ID),stacked_array) #save in numpy file
            nifti_image = nib.Nifti1Image(stacked_array, affine=series_temp[0].affine()[0])
            nib.save(nifti_image, os.path.join(save_path, ID +'.nii.gz'))
        except:
            print('Data was NOT saved!')
            
        shutil.rmtree(path_scan)