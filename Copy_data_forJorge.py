import os
import shutil
import filecmp

def find_last_MR_dir(subject_dir):
    mr_dir = [ d for d in os.listdir(subject_dir) if d.startswith('MR')]
    mr_dir = sorted( d for d in mr_dir
                     if os.path.isdir(os.path.join(subject_dir, d)))[-1]
    return os.path.join(subject_dir, mr_dir, 'outputs/suvr/WBM/')

def get_files(subject_dir):
    mr_dir = find_last_MR_dir(subject_dir)
    return [ os.path.join(mr_dir, f) for f in os.listdir(mr_dir) ]

def copy_files(orig_dir, dest_dir, check_missing_only=False):
    '''
    To check if there are missing files but not copy:
    copy_files(orig_dir_pib, dest_dir_pib, check_missing_only=True)
    '''

    old_file_rh = 'ss8_FS_MGX_SUVR_fsaverage_rh.nii'

    for d in os.listdir(dest_dir):
        subject_dir = os.path.join(orig_dir, d)
        if os.path.isdir(subject_dir):

            files = get_files(subject_dir)
            if not files:
                print('Missing files for {}'.format(subject_dir))

            dest_subject_dir = os.path.join(dest_dir, d)

            if (not check_missing_only
                and files
                and filecmp.cmpfiles(dest_subject_dir, os.path.dirname(files[0]),
                                     old_file_rh)):
                                     for f in files:
                                         shutil.copy(f, dest_subject_dir)

dest_dir = '/autofs/cluster/sperling/UserSpace/clois/Data_for_Jorge/from_Cristina'

orig_dir_pib = '/autofs/space/rincewind_001/users/PET/PIB/Sessions2'
dest_dir_pib = os.path.join(dest_dir,'PiB')
copy_files(orig_dir_pib, dest_dir_pib)

orig_dir_tau = '/autofs/space/rincewind_001/users/PET/TAU/Sessions2'
dest_dir_tau = os.path.join(dest_dir,'tau')
copy_files(orig_dir_tau, dest_dir_tau)
