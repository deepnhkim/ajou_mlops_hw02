# ajou_mlops_hw02
아주대학교 AI대학원
AI융합실전프로젝트3 HW02를 위한 저장소

## 과제 목적
실제 데이터 구조에서의 설계 능력 평가
- 타이타닉 데이터를 사용하여 전처리, 모델, 버전 관리를 포함하여 재현 가능한 ML 실험 수행

## 과제 목표
1. Git + DVC 기반 재현 가능한 실험 구조
2. KNN vs SVM 성능 비교
3. Scaling + Encoding 영향 이해
4. Pipeline / ColumnTransformer 구조 표현

## 실험
1. SVM(No Scaling)
2. StandardScaler + SVM
3. StandardScaler + KNN
4. MinMaxScaler 비교(선택)

## 권장 전처리 구조
1. 수치형 -> 결측치 대체 + Scaling
2. 범주형 -> 결측치 대체 + One-hot Encoding
3. ColumnTransformer
4. KNN / SVM

## 리포트 구성
1. 데이터 개요 - Titanic 데이터 설명
2. 전처리 구조 - ColumnTransformer 설명
3. 성능 비교 - 모델별 결과
4. 전처리 영향 - scaling / encoding 영향
5. 모델 해석 - KNN vs SVM
6. MLOps 회고 - Git/DVC

## 체크포인트

- Titanic에서 왜 ColumnTransformer가 필요한가?
- Scaling이 SVM/KNN에 어떤 영향을 주었는가?
- KNN vs SVM 중 어떤 모델이 더 적합한가?
- Git + DVC로 무엇이 달라졌는가?


