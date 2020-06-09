import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

index_list = list(range(1, 10001))
header_list = []
header_list_plus_name = []
for i in index_list:
    header_list.append('col' + str(i))
    header_list_plus_name.append('col' + str(i))

header_list_plus_name.append('name')

# pca 를 위한 data frame 을 만들어준다.
df_ = pd.read_csv('hog_img_data.csv', names=header_list_plus_name)
# print(df_)


# pca 전에 정규화를 한다.
x = df_.loc[:, header_list].values
y = df_.loc[:, ['name']].values
x = StandardScaler().fit_transform(x)

# 10000 --> 130 feature 로 줄어든다.
# 원래 모델을 95%의 설명가능한 feature 들을 뽑아낸다.

pca = PCA(n_components=0.95)

pca_index = list(range(1, 111))
pca_column = []
for i in pca_index:
    pca_column.append('pc' + str(i))

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data=principalComponents, columns=pca_column)
finalDf = pd.concat([principalDf, df_[['name']]], axis=1)

# print(type(pca_column))
# print(pca_column)
print("number of PCs " + str(len(pca_column)))

# 각 pc 들이 얼마만큼의 variance 를 설명하는지 알 수 있다.
print(pca.explained_variance_ratio_)

# 175 개의 데이터 110 개의 feature 로 이루어진 matrix 이다.
print(finalDf.head(5))

# label 과 데이터를 분리
X = finalDf.drop(['name'], axis=1)
Y = finalDf['name']

# steps = [('scl', StandardScaler()), ('SVM', SVC(random_state=1))]
# # define the pipeline object
# pipeline = Pipeline(steps)
pipeline = Pipeline([('scl', StandardScaler()), ('clf', SVC(random_state=1))])

# 다양한 kernel function 을 사용해본다.
param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [
    {'clf__C': param_range, 'clf__kernel': ['linear']},
    {'clf__C': param_range, 'clf__gamma': param_range, 'clf__kernel': ['poly']},
    {'clf__C': param_range, 'clf__gamma': param_range, 'clf__kernel': ['sigmoid']},
    {'clf__C': param_range, 'clf__gamma': param_range, 'clf__kernel': ['rbf']}
]

gs = GridSearchCV(estimator=pipeline, param_grid=param_grid,
                  scoring='accuracy', cv=10, n_jobs=1)

gs = gs.fit(X, Y)

# GirdSearchCV 를 통해서 가장 좋은 kernel function 과 parameter 를 구할 수 있다.
for i in range(0, 144):
    print(str(i + 1) + "번째 -- ")
    print(gs.cv_results_["params"][i])
    print(gs.cv_results_["mean_test_score"][i])

# print(gs.cv_results_["params"])
# print(gs.cv_results_["mean_test_score"])
print(gs.best_score_)
print(gs.best_params_)

# # stratify : 저장된 데이터 비율만큼 나눈다.
# # train_test_split 을 통해, 효율적으로 학습 데이터를 설정한다.
# x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=30, stratify=Y)
#
# # GridSearchCV
# # 그리드를 사용한 복수 하이퍼 파라미터 최적화를 위한 parameter 를 정의한다.
# # 최적의 파라미터를 찾아주고
# # 교차 검증(cross validation)도 한다.
#
# # 'rbf' kernel 의 경우 gamma 값이 클 수록 훈련 샘플의 영향력이 증가하고, 영역이 조금 부드러워진다.
# parameters = {'SVM__C': [0.001, 0.1, 10, 100, 10e5], 'SVM__gamma': [0.1, 0.01, 0.005, 0.001]}
#
# # cv=5, 5 fold 교차 검증 (cross validation) 을 수행한다.
# grid = GridSearchCV(pipeline, param_grid=parameters, cv=5)
#
# grid.fit(x_train, y_train)
#
# print("train feature shape: ", x_train.shape)
# print("test feature shape: ", x_test.shape)
#
# print("score = %3.2f" % (grid.score(x_test, y_test)))
# print(grid.best_params_)
#
#
# # x_2 = finalDf.loc[:, ['pc1','pc2']]
# # y_2 = finalDf.loc[:, 'name']
# # df_2 = pd.concat([x_2, y_2], axis=1)
# # print(x_2)
# # print(y_2)
#
# # data 2차원 plot 을 통해 시각화를 한다.
# # 2 차원 plot 을 위해 pc1 ,pc2 를 뽑아낸다.
# sns.scatterplot(x='pc1',
#                 y='pc2',
#                 hue='name',
#                 data=finalDf)
# plt.show()
#
