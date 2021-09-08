# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np



def cropper(box_text, path):
    # box_text = './test\아이유31.png,197,1270,569,899'
    box = box_text.split(',')
    print('box:', box)
    filename = box[0].split('\\')[-1]
    print('filename:', filename)

    y_top = int(box[1])
    y_bottom = int(box[3])
    x_left = int(box[4])
    x_right = int(box[2])

    width = x_right - x_left
    height = y_bottom - y_top
    margin = 0.4

    print(width, height)

    if width < 256 or height < 256:
        print(f'X: low resolution ({width}x{height})')
        pass

    else:
        print('O: enough resolution!')
        ff = np.fromfile(f"./data/{box[0].lstrip('.')}", np.uint8)
        img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

        y_bottom = int(box[3])
        
        try:
            img_crop = img[(y_top - int(height*margin)):(y_bottom + int(height*margin)), (x_left - int(width*margin)):(x_right + int(width*margin))]
            print('O: enough margin!')

            cv2.imwrite(f'./data/{path}/{filename}', img_crop)   # 한글은 또 안받아주는듯? ㅠ / 파일 형식은 크게 상관 없는듯? 원본대로 저장!
            print('O: saved!')

            # cv2.imshow('window', img)
            # cv2.waitKey(0)
            # cv2.imshow('window_crop', img_crop)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        except:
            print('X: not enough margin...')




def main(txt, path):
     # 폴더 없으면 일단 생성
    try: 
        os.makedirs(f'./data/{path}') 
    except OSError: 
        if not os.path.isdir(f'./data/{path}'): 
            raise

    with open(f'./data/{txt}', 'r') as file:
        for text in file:
            print('\n')
            line = text.strip('\n')    # 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
            print('line:', line)
            cropper(line, path)



### 실행! ###
# data 폴더 안에 원본 폴더랑 동명의 txt가 들어있어야 함!
main('idol_girl_large.txt', 'idol_girl_large_cropped')  # txt 파일명, 저장 경로
main('idol_girl_medium.txt', 'idol_girl_medium_cropped')  # txt 파일명, 저장 경로
