# 폴더 유무 확인 위함
import os

class Vibration_Anomaly_Detection:

    def __init__(self):
        # 데이터가 저장될 폴더 이름?, 경로 
        self.folder_name = "C_33_200103222_1405_D"
        self.analysis_directory_path = "./" + self.folder_name + "_A/"

        # 폴더 이름 길이를 구하는데 왜 구하는지는 모르겠음.
        self.foldername_length = len(self.folder_name)

        # 취득 데이터가 있는 폴더 경로
        # 없으면 자동으로 생성하니 그 폴더안에 취득(txt) 넣으면 됩니다.
        self.file_full_path = "./senSorData/" + self.folder_name

        # 취득 데이터 파일 개수 확인
        self.number_of_files = len(os.listdir(self.file_full_path))

        # 매트랩은 폴더 속 파일 정보를 보는데 일단 파이썬은 이름만 불러와짐
        # 이름만 사용하기 때문에 문제는 없어 보임.
        self.my_folder_info = os.listdir(self.file_full_path)



    
    def folder_create(self):
        # 결과 저장 폴더 유무 확인
        print("결과 저장 폴더 유무를 확인합니다.")
        if os.path.isdir(self.analysis_directory_path) == False:
            print("결과 저장 폴더가 없습니다.")
            os.makedirs(os.path.join(self.analysis_directory_path))
            print("결과 저장 폴더 생성 완료!!")
        else:
            print("결과 저장 폴더가 있습니다!!")

        # 취득 데이터 폴더 유무 확인
        print("취득 데이터 폴더 유무를 확인합니다.")
        if os.path.isdir(self.file_full_path) == False:
            print("취득 데이터 폴더가 없습니다.")
            os.makedirs(os.path.join(self.file_full_path))
            print("취득 데이터 폴더 생성 완료!!")
        else:
            print("취득 데이터 폴더가 있습니다!!")



    def Start(self):
        print("시작!!")

        self.folder_create()

        print(self.number_of_files)
        print(self.my_folder_info)


if __name__ == "__main__":
    Porting = Vibration_Anomaly_Detection()
    Porting.Start()
