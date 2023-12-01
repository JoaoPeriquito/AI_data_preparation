import scripts.xnat as xnat
import pandas as pd
import dbdicom as db
import pipelines.rename as rename
import numpy as np
import nibabel as nib
import shutil

def main(username, password, path, df, series_desc):

    for row in df.Datasets:
        try:
            ExperimentName = xnat.main(username, password, path,SpecificDataset=row)
            pathScan = path + "//" + ExperimentName
        except:
            print('Dataset name is incorrect or does NOT exist!')
            continue

        folder = db.database(path=pathScan)
        rename.main(folder)

        for dixon in series_desc:
            try:
                series_temp = folder.series(SeriesDescription=dixon)

                array_list = []
                if series_temp:
                    array_temp, header_temp = series_temp[0].array(['SliceLocation', 'AcquisitionTime'], pixels_first=True)
                    array_temp = np.squeeze(array_temp)
                    array_list.append(array_temp)
                    
                stacked_array = np.concatenate(array_list, axis=3)
                nifti_image = nib.Nifti1Image(stacked_array, affine=np.eye(4))
                nib.save(nifti_image, path + '\\' + 'row'+'.nii.gz')
            
            except:
                print(dixon + ' was NOT found!')
        
        shutil.rmtree(pathScan)