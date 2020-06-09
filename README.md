# bigdata_skku
image classification using PCA &amp; SVM

## crawling.py  

GoogleImageCrawler를 이용해서 이미지 크롤링 
you can create file dir by yourself. 

## oepn_cv_crop_image.py 

opencv 라이브러리를 이용해, 얼굴인식 후 crop(100*100*3 # color image, 100*100pixel size ) 
--> 차원을 줄이기 위해, grey 로 변환 #grey color, 100*100 pixel size 

## hog_example.py 

grey image 들의 hog features 를 계산후 csv 파일에 저장

## pca_svm.py 

100*100 의 features 에서 pca 를 통해 110 개의 pc 들을 뽑아내고, svm 을 통해 classification 한다. 
