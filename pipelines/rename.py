""" 
@author: Joao Periquito 
iBEAt Rename Scrpit
2022
Pulse sequence name standardization for iBEAt MR Protcol
"""
import time

from itertools import chain

def Philips_rename(series):
        
    SeqName = series["SeriesDescription"]
    
    if SeqName is None:
        return 'Sequence not recognized'
    
    if SeqName == 'T1w_abdomen_dixon_cor_bh':
        TE = series.EchoTime

        inphase = series.subseries(EchoTime=TE[0])
        inphase.SeriesDescription = 'T1w_abdomen_dixon_cor_bh_in_phase'

        outphase = series.subseries(EchoTime=TE[1])
        outphase.SeriesDescription = 'T1w_abdomen_dixon_cor_bh_out_phase'
        
        return 'T1w_abdomen_dixon_cor_bh'
    
    if SeqName == 'PC_RenalArtery_Right_EcgTrig_fb_120':

        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'PC_RenalArtery_Right_EcgTrig_fb_120_magnitude'

        m_pca = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_PCA', 'M', 'PCA'])
        m_pca.SeriesDescription = 'PC_RenalArtery_Right_EcgTrig_fb_120_mpca'

        phase = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'PHASE CONTRAST M', 'P', 'PCA'])
        phase.SeriesDescription = 'PC_RenalArtery_Right_EcgTrig_fb_120_phase'

        return 'PC_RenalArtery_Right_EcgTrig_fb_120'
    
    if SeqName == 'PC_RenalArtery_Left_EcgTrig_fb_120':

        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'PC_RenalArtery_Left_EcgTrig_fb_120_magnitude'

        m_pca = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_PCA', 'M', 'PCA'])
        m_pca.SeriesDescription = 'PC_RenalArtery_Left_EcgTrig_fb_120_mpca'

        phase = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'PHASE CONTRAST M', 'P', 'PCA'])
        phase.SeriesDescription = 'PC_RenalArtery_Left_EcgTrig_fb_120_phase'

        return 'PC_RenalArtery_Left_EcgTrig_fb_120'

    if SeqName == 'T1map_kidneys_cor-oblique_mbh fa35':
        
        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'T1map_kidneys_cor-oblique_mbh_magnitude'

        T1map = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'T1 MAP', 'T1', 'UNSPECIFIED'])
        T1map.SeriesDescription = 'T1map_kidneys_cor-oblique_mbh_T1map'

        return 'T1map_kidneys_cor-oblique_mbh'
    
    if SeqName == 'T2star_map_pancreas_tra_mbh':

        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'T2star_map_pancreas_tra_mbh_magnitude'

        phase = series.subseries(ImageType=['ORIGINAL','PRIMARY','PHASE MAP', 'P', 'FFE'])
        phase.SeriesDescription = 'T2star_map_pancreas_tra_mbh_phase'

        return 'T2star_map_pancreas_tra_mbh'
    
    if SeqName == 'T2star_map_kidneys_cor-oblique_mbh':

        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'T2star_map_kidneys_cor-oblique_mbh_magnitude'

        phase = series.subseries(ImageType=['ORIGINAL','PRIMARY','PHASE MAP', 'P', 'FFE'])
        phase.SeriesDescription = 'T2star_map_kidneys_cor-oblique_mbh_phase'

        return 'T2star_map_kidneys_cor-oblique_mbh'

    if SeqName == 'T2map_mGRASE_kidneys_cor-oblique_mbh_TEn*10':
        
        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_SE', 'M', 'SE'])
        magnitude.SeriesDescription = 'T2map_kidneys_cor-oblique_mbh_magnitude'

        T2map = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'T2 MAP', 'T2', 'UNSPECIFIED'])
        T2map.SeriesDescription = 'T2map_kidneys_cor-oblique_mbh_T2map'

        R2map = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'R2_UNSPECIFIED', 'R2', 'UNSPECIFIED'])
        R2map.SeriesDescription = 'T2map_kidneys_cor-oblique_mbh_R2map'

        return 'T2map_kidneys_cor-oblique_mbh'
    
    if SeqName == 'DTI TEST 4 NSA1 b100 add':
        return 'DTI_kidneys_cor-oblique_fb'
    
    if SeqName == 'IVIM _kidneys_cor-oblique_fb gradient file needed':
        return 'IVIM _kidneys_cor-oblique_fb'
    
    if SeqName == 'MT_ON_kidneys_cor-oblique_bh off resonance':
        
        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'MT_ON_kidneys_cor-oblique_bh'

        phase = series.subseries(ImageType=['ORIGINAL','PRIMARY','PHASE MAP', 'P', 'FFE'])
        phase.SeriesDescription = 'MT_ON_kidneys_cor-oblique_bh_phase'
        
        return 'MT_ON_kidneys_cor-oblique_bh_mag_and_phase'
    
    if SeqName == 'MT_OFF_kidneys_cor-oblique_bh':
        
        magnitude = series.subseries(ImageType=['ORIGINAL', 'PRIMARY', 'M_FFE', 'M', 'FFE'])
        magnitude.SeriesDescription = 'MT_OFF_kidneys_cor-oblique_bh'

        phase = series.subseries(ImageType=['ORIGINAL','PRIMARY','PHASE MAP', 'P', 'FFE'])
        phase.SeriesDescription = 'MT_OFF_kidneys_cor-oblique_bh_phase'
        
        return 'MT_OFF_kidneys_cor-oblique_bh_mag_and_phase'
    
    if SeqName == 'DCE_kidneys_cor-oblique_fb_wet_pulse':
        return 'DCE_kidneys_cor-oblique_fb'
    
    if SeqName == 'T1w_abdomen_post_contrast_dixon_cor_bh':
        TE = series.EchoTime

        inphase = series.subseries(EchoTime=TE[0])
        inphase.SeriesDescription = 'T1w_abdomen_dixon_cor_bh_in_phase_post_contrast'

        outphase = series.subseries(EchoTime=TE[1])
        outphase.SeriesDescription = 'T1w_abdomen_dixon_cor_bh_out_phase_post_contrast'
        
        return 'T1w_abdomen_post_contrast_dixon_cor_bh'

    return SeqName
            

def Siemens_rename(series): 
    """
    The sequence names in Leeds have been removed by the anonymisation
    procedure and must be recovered from other attributes
    """
    SeqName = series["SequenceName"]
    print(SeqName)
    if SeqName is None:
        return 'Sequence not recognized'
    
    if SeqName == '*tfi2d1_115':
        return 'Sequence not recognized'

    if SeqName == '*tfi2d1_192':
        if series["FlipAngle"] > 30:
            return 'localizer_bh_fix'
        else: 
            return 'localizer_bh_ISO'

    if SeqName == '*h2d1_320':
        return 'T2w_abdomen_haste_tra_mbh'

    if SeqName == '*fl3d2':
        sequence = 'T1w_abdomen_dixon_cor_bh'
        imType = series["ImageType"]
        if imType[3] == 'OUT_PHASE' or imType[4] == 'OUT_PHASE': 
            return sequence + '_out_phase'
        if imType[3] == 'IN_PHASE'  or imType[4] == 'IN_PHASE': 
            return sequence + '_in_phase'
        if imType[3] == 'FAT'       or imType[4] == 'FAT': 
            return sequence + '_fat'
        if imType[3] == 'WATER'     or imType[4] == 'WATER': 
            return sequence + '_water'

    if SeqName == '*fl2d1r4': 
        if series["ImagePositionPatient"][0] < 0:
            return 'PC_RenalArtery_Right_EcgTrig_fb_120'
        else: 
            return 'PC_RenalArtery_Left_EcgTrig_fb_120'

    if SeqName == '*fl2d1_v120in':
        imType = series["ImageType"]
        if series["ImagePositionPatient"][0] < 0:
            sequence = 'PC_RenalArtery_Right_EcgTrig_fb_120'
        else:
            sequence = 'PC_RenalArtery_Left_EcgTrig_fb_120'
        if imType[2] == 'P': 
            return sequence + '_phase'
        if imType[2] == 'MAG': 
            return sequence + '_magnitude'
        
    if SeqName == '*fl2d12':
        imType = series["ImageType"]
        if series["InPlanePhaseEncodingDirection"] == 'COL':
            sequence = 'T2star_map_pancreas_tra_mbh'
        else:
            sequence = 'T2star_map_kidneys_cor-oblique_mbh'
        if imType[2] == 'M': 
            return sequence + '_magnitude'
        if imType[2] == 'P': 
            return sequence + '_phase'
        if imType[2] == 'T2_STAR MAP': 
            return sequence + '_T2star'

    if SeqName == '*fl2d1':
        imType = series["ImageType"]
        sequence = 'T1w_kidneys_cor-oblique_mbh'
        if imType[2] == 'M': 
            return sequence + '_magnitude'
        if imType[2] == 'P': 
            return sequence + '_phase'

    if SeqName == '*tfl2d1r106': 
        imType = series["ImageType"]
        sequence = 'T1map_kidneys_cor-oblique_mbh'
        res = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in imType))
        if res[2] == 'T1 MAP': 
            return sequence + '_T1map'
        if res[3] == 'MOCO': 
            return sequence + '_moco'
        if res[2] == 'M': 
            return sequence + '_magnitude'
        if res[2] == 'P': 
            return sequence + '_phase'

    if SeqName == '*tfl2d1r96':
        imType = series["ImageType"]
        sequence = 'T2map_kidneys_cor-oblique_mbh'
        if imType[-1] == 'T2': 
            return sequence + '_T2map'
        if imType[-1] == 'MOCO': 
            return sequence + '_moco'
        if imType[2] == 'M': 
            return sequence + '_magnitude'
        if imType[2] == 'P': 
            return sequence + '_phase'

    if SeqName[:5] == '*ep_b' or SeqName[0][:5] == '*ep_b':
        if len(series.files()) < 1000:
            return 'IVIM_kidneys_cor-oblique_fb'
        else:
            return 'DTI_kidneys_cor-oblique_fb'

    if SeqName == '*fl3d1':
        if series["ScanOptions"] == 'PFP': 
            return 'MT_OFF_kidneys_cor-oblique_bh'
        else:
            return 'MT_ON_kidneys_cor-oblique_bh'

    if SeqName == '*tfi2d1_154': 
        return 'ASL_planning_bh'
    
    if SeqName == 'tgse3d1_512': 
        return 'ASL_kidneys_pCASL_cor-oblique_fb'
    
    if SeqName == 'WIP_tgse3d1_512': 
        return 'ASL_kidneys_pCASL_cor-oblique_fb'
    
    if SeqName == '*tfl2d1_16': 
        return 'DCE_kidneys_cor-oblique_fb'
    
    if SeqName == 'RAVE3d1': 
        return 'RAVE_kidneys_fb'
    
    if SeqName == '*fl3d2': 
        return 'T1w_abdomen_dixon_cor_bh'

    return 'Sequence not recognized'


def main(folder):
    start_time = time.time()

    DCE_count = 0
    ASL_count = 0
    all_series = folder.series()
    Manufacturer = all_series[0]['Manufacturer']

    for i, series in enumerate(all_series):
        folder.progress(i+1, len(all_series), 'Renaming...')

        if Manufacturer == 'SIEMENS':
            imDescription = Siemens_rename(series)
            series.SeriesDescription = imDescription

            if imDescription == 'DCE_kidneys_cor-oblique_fb':
                DCE_count = 1
            if DCE_count == 1 and imDescription[0:17] == 'T1w_abdomen_dixon':
                series.SeriesDescription = imDescription + '_post_contrast'
            elif imDescription == 'ASL_kidneys_pCASL_cor-oblique_fb' and ASL_count == 0:
                series.SeriesDescription = imDescription + '_M0_moco'
                ASL_count = 1
            elif imDescription == 'ASL_kidneys_pCASL_cor-oblique_fb' and ASL_count == 1:
                series.SeriesDescription = imDescription + '_PW_moco'
                ASL_count = 2
            elif imDescription == 'ASL_kidneys_pCASL_cor-oblique_fb' and ASL_count == 2:
                series.SeriesDescription = imDescription + '_RBF_moco'
                ASL_count = 3
            elif imDescription == 'ASL_kidneys_pCASL_cor-oblique_fb' and ASL_count == 3:
                series.SeriesDescription = imDescription + '_control_moco'
                ASL_count = 4
            elif imDescription == 'ASL_kidneys_pCASL_cor-oblique_fb' and ASL_count == 4:
                series.SeriesDescription = imDescription + '_label0_moco'
                ASL_count = 0
        else:
            imDescription = Philips_rename(series)
            series.SeriesDescription = imDescription

        
        print(imDescription)

    folder.save()
    folder.log("Renaming was completed --- %s seconds ---" % (int(time.time() - start_time)))

    


