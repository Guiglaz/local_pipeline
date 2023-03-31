import os
import datetime


class Experiment:
    root = os.path.normpath(".")
    
    def __init__(self,exp_name):
    
        self.exp_name         = get_exp_name(exp_name)
        
        self.exp_folder       = os.path.normpath(os.path.join(root,self.exp_name))
        self.recording_folder = os.path.normpath(os.path.join(self.exp_folder,'Recordings'))
        self.raw_folder       = os.path.normpath(os.path.join(self.exp_folder,'Raw'))
        self.notes_folder     = os.path.normpath(os.path.join(self.exp_folder, "Notes")
        self.pictures_folder  = os.path.normpath(os.path.join(self.notes_folder,'Pics'))       
        self.analysis_folder  = os.path.normpath(os.path.join(self.exp_folder, "Analysis")
        self.pipeline_folder  = os.path.normpath(os.path.join(self.exp_folder, "Standard_analysis_pipeline"))
        self.sorting_folder   = os.path.normpath(os.path.join(self.exp_folder, "Sorting"))

        self.log_name           = self.exp_name + "_log.txt"
        self.circus_params_name = "recording_00.params"
        self.prb_file_name      = "mcs_256_30_8iR_ITO.prb"
        self.binary_checkerboard_file_name = "binarysource1000Mbits"
        
        
        
    def get_exp_name(self, exp_name):
        exp = exp_name
        date = datetime.date.today()
        return "{}_{}_GGU".format(exp,date)
        
        
    def build_folders(self):
        
        