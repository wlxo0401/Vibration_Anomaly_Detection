#-*- coding:utf-8 -*-
# 폴더 유무 확인 위함
import os
import numpy as np
import pandas as pd
import math
import acc_int as acc_int

class Vibration_Anomaly_Detection:

    def __init__(self):
        # 데이터가 저장될 폴더 이름?, 경로 
        self.folder_name = "C_33_200103_1405_D"
        self.analysis_directory_path = "./analysisData/" + self.folder_name + "_A/"

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

        # 변수 초기화


    
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

    def main_tool(self):
        # i를 취득 데이터 수 만큼 돌립니다.
        for i in range(0, self.number_of_files):
            # 불러올 취득 파일 이름 입니다. 
            Data_file_name = self.my_folder_info[i]
            # 취득 파일 이름 길이 
            Data_file_name_name_length = len(Data_file_name)

            print(Data_file_name)
            print(Data_file_name_name_length)
            # 취득 파일 이름 길이가 25 넘으면 작동
            if Data_file_name_name_length > 25:
                # 취득 파일 경로 + 이름 합체
                open_file_name = self.file_full_path + "/" + Data_file_name

                # 결과 저장 파일 이름
                analysis_file_name_v = "./analysisData/" + self.folder_name + "_A/" + Data_file_name[:Data_file_name_name_length-8] + "_A.txt"
                print(analysis_file_name_v)
                # 파일 불러오기
                #with open(open_file_name,'r') as file_id:               
                file_id = open(open_file_name)
                #sensor_separator에 Data_file_name에 특정 위치 사이 값을 저장한다 
                sensor_separator = Data_file_name[Data_file_name_name_length-11:Data_file_name_name_length-10]
                #s1에 sensor_separator 저장
                s1=sensor_separator
                #s1을 문자열로 저장
                s1_1=str(s1)
                #센서 데이터 확인
                sensor_num = Data_file_name[Data_file_name_name_length-24:Data_file_name_name_length-23]
                sn_1=str(sensor_num)
                # s1_1 = 'V'
                # sn_1 = '1'
                print(s1_1)
                print(sn_1)
                #s1_1이 진동이면
                if s1_1=='V':
                    #happy_go_v에 데이터를 읽어드린다.
                    # happy_go_v = np.loadtxt(file_id, 
                    # delimiter=' ', 
                    # dtype={'names': ('col1', 'col2', 'col3'),
                    # 'formats': ('i4', 'i4', 'i4')}
                    # , skiprows=1)
                    happy_go_v = pd.read_csv(file_id, delimiter=' ', names=["X","Y","Z"])

                    happy_go_v_x1 = happy_go_v["X"].values.tolist()
                    happy_go_v_y1 = happy_go_v["Y"].values.tolist()
                    happy_go_v_z1 = happy_go_v["Z"].values.tolist()
                    

                    x1 = acc_int.acc_int(happy_go_v_x1, 2000)
                    y1 = acc_int.acc_int(happy_go_v_y1, 2000)
                    z1 = acc_int.acc_int(happy_go_v_z1, 2000)
                    
                    

                    x1 = x1 * 30
                    y1 = y1 * 30
                    z1 = z1 * 30

                    # X축 overall 계산식
                    x2 = x1[10:1000]
                    sumX = np.sum(np.power(x2, 2))/1.5
                    resultX = round(math.sqrt(sumX), 3)
                    # Y축 overall 계산식
                    y2 = y1[10:1000]
                    sumY = np.sum(np.power(y2, 2))/1.5
                    resultY = round(math.sqrt(sumY), 3)
                    # Z축 overall 계산식
                    z2 = z1[10:1000]
                    sumZ = np.sum(np.power(z2, 2))/1.5
                    resultZ = round(math.sqrt(sumZ), 3)

                    # overall 등급
                    gradeX = 'A'
                    gradeY = 'A'
                    gradeZ = 'A'

                    

                    if sn_1 == '1': # 전동기 기준 등급
                        if resultX >= 2.3 and resultX < 4.5:
                            gradeX = 'B'
                        elif resultX >= 4.5 and resultX < 7.1:
                            gradeX = 'C'
                        elif resultX >= 7.1:
                            gradeX = 'D'

                        if resultY >= 2.3 and resultY < 4.5:
                            gradeY = 'B'
                        elif resultY >= 4.5 and resultY < 7.1:
                            gradeY = 'C'
                        elif resultY >= 7.1:
                            gradeY = 'D'

                        if resultZ >= 2.3 and resultZ < 4.5:
                            gradeZ = 'B'
                        elif resultZ >= 4.5 and resultZ < 7.1:
                            gradeZ = 'C'
                        elif resultZ >= 7.1:
                            gradeZ = 'D'

                    else: # 축베어링 및 팬 기준 등급
                        if resultX >= 4.5 and resultX < 7.1:
                            gradeX = 'B'
                        elif resultX >= 7.1 and resultX < 9.0:
                            gradeX = 'C'
                        elif resultX >= 9.0:
                            gradeX = 'D'

                        if resultY >= 4.5 and resultY < 7.1:
                            gradeY = 'B'
                        elif resultY >= 7.1 and resultY < 9.0:
                            gradeY = 'C'
                        elif resultY >= 9.0:
                            gradeY = 'D'

                        if resultZ >= 4.5 and resultZ < 7.1:
                            gradeZ = 'B'
                        elif resultZ >= 7.1 and resultZ < 9.0:
                            gradeZ = 'C'
                        elif resultZ >= 9.0:
                            gradeZ = 'D'
                    
                    
                    
                    # write text file
                    with open(analysis_file_name_v, "w") as fid:
                        fid.write('overall\n')
                        fid.write('{0:4.3f}\t{0:4.3f}\t{0:4.3f}\n'.format(resultX, resultY, resultZ))
                        fid.write('{}\t\t{}\t\t{}\n'.format(gradeX, gradeY, gradeZ))
                        fid.write('\nrow\n')
                        #resultNumArray = np.transpose(np.arange[1:1000])
                        #catXYZ1 = np.concatenate((resultNumArray, x1, y1, z1), axis=1)
                        for row in range(10, 1000):
                            fid.write('%d\t%6.5f\t%6.5f\t%6.5f\n' % (row,x1[row],y1[row],z1[row]))
                        fid.write('EOF')


                

    def Start(self):
        print("시작!!")

        self.folder_create()
        self.main_tool()



if __name__ == "__main__":
    Porting = Vibration_Anomaly_Detection()
    Porting.Start()
