import os

class Vibration_Anomaly_Detection:

    def __init__(self):
        # 데이터가 저장될 폴더 이름? 
        self.folder_name = "C_33_200103_1405_D"
        self.analysis_directory_path = "C:/Users/wlxo0/Desktop/asfs/" + self.folder_name + "_A/"

    def folder_create(self):
        if not(os.path.isdir(self.analysis_diretory_path)):
            os.makedirs(os.path.join(self.analysis_diretory_path))
