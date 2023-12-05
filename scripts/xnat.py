""" 
@author: Joao Periquito 
iBEAt XNAT import
2022  
XNAT Dataset auto-import script 
"""

import xnat
import zipfile
import datetime
import os

def XNAT_download(username,password,path,dataset_selected,specific_dataset=None):
    url = "https://qib.shef.ac.uk"

    if specific_dataset!=None:
        
        site = specific_dataset.split('_')[0]
        patient = specific_dataset.split('_')[1]
        
        if   site == '1128': #Bari
            dataset_selected[0] = 5
            dataset_selected[1] = 0
        elif site == '2128': #Bordeaux
            dataset_selected[0] = 2
            dataset_selected[1] = 1 #Baseline
        elif site == '3128': #Exeter
            dataset_selected[0] = 3
            dataset_selected[1] = 0
        elif site == '4128': #Leeds
            dataset_selected[0] = 6
            dataset_selected[1] = 0
        elif site == '5128': #Turku
            dataset_selected[0] = 4
            dataset_selected[1] = 3 #GE
        # elif site == '2178': #Sheffield
        #     dataset_selected[0] = 7
        #     dataset_selected[1] = 0


    with xnat.connect(url, user=username, password=password) as session:
        xnatProjects = [project.secondary_id for project in session.projects.values()]
        #for x in range(len(xnatProjects)):
            #print (str(x) +": " + xnatProjects[x])
        #print("Select the project:")
        #projectSelected = int(input())
        #projectSelected = 6
        projectSelected = dataset_selected[0]
        projectID = xnatProjects[projectSelected]
        #print(projectID)
        
        projectName = [project.name for project in session.projects.values() if project.secondary_id == projectID][0]
        if projectName:
            xnatSubjects = [subject.label for subject in session.projects[projectName].subjects.values()]
            #for x_2 in range(len(xnatSubjects)):
                #print (str(x_2) +": " + xnatSubjects[x_2])
            #print("Select the project:")
            #xnatSubjectsSelected = int(input())
            #xnatSubjectsSelected = 0
            xnatSubjectsSelected = dataset_selected[1]
            #print(xnatSubjects[xnatSubjectsSelected])
            subjectName = xnatSubjects[xnatSubjectsSelected]
            dataset = session.projects[projectName]

            xnatExperiments = [experiment.label for experiment in session.projects[projectName].subjects[subjectName].experiments.values()]
            if specific_dataset!=None:
                for x_3 in range(len(xnatExperiments)):
                #print(str(x_3) +": " + xnatExperiments[x_3])
                    if patient in xnatExperiments[x_3]:
                        dataset_selected[2] = x_3
                        break
                
            #print("Selected the project:")
            #xnatExperimentsSelected = int(input())
            #xnatExperimentsSelected = 14
            xnatExperimentsSelected = dataset_selected[2]
            print("Selected the project: " + str(xnatExperiments[xnatExperimentsSelected]))	
            experimentName = xnatExperiments[xnatExperimentsSelected]
            dataset = session.projects[projectName].subjects[subjectName].experiments[experimentName]
            dataset.download_dir(path)
            return experimentName

def zipFiles(listPaths):
    dt = datetime.datetime.now()
    zip_file = zipfile.ZipFile(dt.strftime('%Y%m%d') + '_xnat_upload.zip', 'w')
    for file in listPaths:
        zip_file.write(file, compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    zip_path = os.path.realpath(zip_file.filename)
    return zip_path



#####################################################
################ UPLOAD DOES NOT WORK ###############
def XNAT_upload(username,password,path):
    url = "https://qib.shef.ac.uk"

    with xnat.connect(url, user=username, password=password) as session:
        xnatProjects = [project.secondary_id for project in session.projects.values()]
        for x in range(len(xnatProjects)):
            print (str(x) +": " + xnatProjects[x])
        print("Select the project:")
        projectID = xnatProjects[9]
        print(projectID)
        #uploadPaths = [image.file for image in app.folder.instances()]
        uploadPaths = [image.file for image in path]
        uploadZipFile = zipFiles(uploadPaths)

    return
################ UPLOAD DOES NOT WORK ###############
#####################################################


def download_study(username, password, path,dataset_selected=[0,0,0],specific_dataset=None):

    if specific_dataset==None:
        experimentName = XNAT_download(username,password,path,dataset_selected)
        return experimentName

    else:
        experimentName = XNAT_download(username,password,path,dataset_selected=[0,0,0],specific_dataset=specific_dataset)
        return experimentName

    

