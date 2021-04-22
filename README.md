# 2020 - 1 빅데이터분석방법론 

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



![슬라이드1](https://user-images.githubusercontent.com/59246354/115718753-66436400-a3b6-11eb-830d-62c924df204a.PNG)
![슬라이드2](https://user-images.githubusercontent.com/59246354/115718754-67749100-a3b6-11eb-89a2-950c7592fd56.PNG)
![슬라이드3](https://user-images.githubusercontent.com/59246354/115718757-67749100-a3b6-11eb-9a4e-ec42b885a3a9.PNG)
![슬라이드4](https://user-images.githubusercontent.com/59246354/115718758-680d2780-a3b6-11eb-91bf-3da128e72af7.PNG)
![슬라이드5](https://user-images.githubusercontent.com/59246354/115718760-68a5be00-a3b6-11eb-8e39-8d1b77abde50.PNG)
![슬라이드6](https://user-images.githubusercontent.com/59246354/115718762-68a5be00-a3b6-11eb-8ee4-2028a85eba3c.PNG)
![슬라이드7](https://user-images.githubusercontent.com/59246354/115718767-693e5480-a3b6-11eb-89bf-e0ff790d2f66.PNG)
![슬라이드8](https://user-images.githubusercontent.com/59246354/115718769-693e5480-a3b6-11eb-8a9d-dcfc305a54e3.PNG)
![슬라이드9](https://user-images.githubusercontent.com/59246354/115718774-69d6eb00-a3b6-11eb-86a0-af6c9dac9f38.PNG)
![슬라이드10](https://user-images.githubusercontent.com/59246354/115718775-6a6f8180-a3b6-11eb-97cc-b89c4ee49b14.PNG)
