<<<<<<< HEAD
# 🏥 Phân Loại Bệnh Tiểu Đường (Diabetes Classification)

## 📋 Giới Thiệu

Dự án này sử dụng **Machine Learning** để phân loại và dự đoán **Bệnh Tiểu Đường** dựa trên **Pima Indians Diabetes Dataset**. Bộ dữ liệu chứa thông tin y tế của 768 bệnh nhân nữ người Ấn Độ Pima có độ tuổi từ 21 trở lên.

## 📊 Thông Tin Dữ Liệu

- **Tổng số mẫu**: 768
- **Số đặc trưng**: 8 (tất cả là số)
- **Biến mục tiêu (Target)**: Outcome (0 = Không bệnh, 1 = Có bệnh)
- **Phân bố lớp**: 
  - Không bệnh: 500 mẫu (65.1%)
  - Có bệnh: 268 mẫu (34.9%)

### 8 Đặc Trưng (Features)

| Thứ tự | Tên Tiếng Anh | Tên Tiếng Việt | Giải Thích |
|--------|---|---|---|
| 1 | Pregnancies | Số lần mang thai | Số lần mang thai của bệnh nhân |
| 2 | Glucose | Glucose máu | Nồng độ glucose trong máu (mg/dL) |
| 3 | BloodPressure | Huyết áp | Huyết áp tâm trương (mmHg) |
| 4 | SkinThickness | Độ dày da | Độ dày da tại cơ ba đầu (mm) |
| 5 | Insulin | Insulin | Nồng độ insulin 2 giờ sau (µU/mL) |
| 6 | BMI | Chỉ số khối cơ thể | BMI = weight(kg) / height(m)² |
| 7 | DiabetesPedigreeFunction | Hàm lịch sử gia đình | Nguy cơ di truyền bệnh tiểu đường |
| 8 | Age | Tuổi | Tuổi của bệnh nhân (năm) |

## 🔧 Công Nghệ Sử Dụng

- **Python 3.9+**
- **Libraries chính**:
  - `pandas`: Xử lý dữ liệu
  - `numpy`: Tính toán số học
  - `scikit-learn`: Machine Learning
  - `matplotlib` & `seaborn`: Biểu đồ
  - `joblib`: Lưu/tải mô hình

## 📈 Quy Trình Thực Hiện

### 1. **Tải Dữ Liệu** 
- Đọc file CSV
- Kiểm tra kích thước và loại dữ liệu

### 2. **Khám Phá Dữ Liệu (EDA)**
- Phân tích thống kê cơ bản
- Vẽ biểu đồ phân bố
- Tính ma trận tương quan

### 3. **Tiền Xử Lý Dữ Liệu**
- Xử lý giá trị 0 không hợp lý
- Chuẩn hóa dữ liệu (StandardScaler)
- Chia tập huấn luyện/kiểm tra (80/20)

### 4. **Xây Dựng Mô Hình**
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

### 5. **Đánh Giá Mô Hình**
- Độ chính xác (Accuracy)
- Precision, Recall, F1-Score
- AUC-ROC
- Ma trận nhầm lẫn

### 6. **Dự Đoán Trên Dữ Liệu Mới**
- Tự động chuẩn hóa dữ liệu
- Dự đoán kết quả
- Tính xác suất

### 7. **Lưu Mô Hình**
- Lưu mô hình (.joblib)
- Lưu scaler
- Lưu thông tin mô hình (JSON)

## 🎯 Kết Quả Chính

### Độ Chính Xác (Accuracy)

| Mô Hình | Train | Test |
|---------|-------|------|
| Logistic Regression | 79.15% | 71.43% |
| **Random Forest** ⭐ | 99.35% | **75.32%** |
| SVM | 83.55% | 75.32% |

### AUC-ROC Score

| Mô Hình | AUC |
|---------|-----|
| Logistic Regression | 0.8230 |
| **Random Forest** ⭐ | **0.8194** |
| SVM | 0.7924 |

### Tầm Quan Trọng Đặc Trưng (Random Forest)

```
Glucose:                    28.84% ⭐⭐⭐ (Quan trọng nhất)
BMI:                        16.80% ⭐⭐
DiabetesPedigreeFunction:   12.10% ⭐
Age:                        12.09% ⭐
Pregnancies:                 8.30%
BloodPressure:               7.85%
Insulin:                     7.29%
SkinThickness:               6.72%
```

## 📁 Cấu Trúc File

```
diabetes_results/
├── models/                              # Các mô hình được lưu
│   ├── logistic_regression_model.joblib (0.91 KB)
│   ├── random_forest_model.joblib       (1389.38 KB)
│   ├── svm_model.joblib                 (30.50 KB)
│   ├── scaler.joblib                    (1.10 KB)
│   └── model_info.json                  (Thông tin mô hình)
│
├── plots/                               # Biểu đồ kết quả
│   ├── 01_class_distribution.png        (Phân bố lớp)
│   ├── 02_correlation_matrix.png        (Ma trận tương quan)
│   ├── 03_feature_distribution.png      (Phân bố đặc trưng)
│   ├── 04_feature_by_outcome.png        (So sánh đặc trưng)
│   ├── 05_model_comparison.png          (So sánh mô hình)
│   ├── 06_confusion_matrices.png        (Ma trận nhầm lẫn)
│   ├── 07_roc_curves.png                (Đường cong ROC)
│   └── 08_feature_importance.png        (Tầm quan trọng)
│
├── diabetes_classification.py           (File code chính)
└── README.md                            (File này)
```

## 🚀 Cách Sử Dụng

### Option 1: Chạy File Python

```bash
python diabetes_classification.py
```

Điều này sẽ:
- Tải dữ liệu
- Tiền xử lý
- Huấn luyện 3 mô hình
- Vẽ biểu đồ
- Lưu kết quả

### Option 2: Sử Dụng Jupyter Notebook

```bash
jupyter notebook diabetes_classification_complete.ipynb
```

### Option 3: Tải Mô Hình Đã Huấn Luyện

```python
import joblib
import pandas as pd

# Tải mô hình và scaler
model = joblib.load('diabetes_results/models/random_forest_model.joblib')
scaler = joblib.load('diabetes_results/models/scaler.joblib')

# Tạo dữ liệu bệnh nhân mới
new_patient = pd.DataFrame({
    'Pregnancies': [2],
    'Glucose': [125],
    'BloodPressure': [78],
    'SkinThickness': [32],
    'Insulin': [88],
    'BMI': [27.5],
    'DiabetesPedigreeFunction': [0.35],
    'Age': [45]
})

# Chuẩn hóa dữ liệu
scaled_data = scaler.transform(new_patient)

# Dự đoán
prediction = model.predict(scaled_data)[0]
probability = model.predict_proba(scaled_data)[0]

print(f"Dự đoán: {'Có bệnh' if prediction == 1 else 'Không bệnh'}")
print(f"Xác suất: {probability}")
```

## 📊 Giải Thích Các Biểu Đồ

### 01_class_distribution.png
- Biểu đồ cột và tròn hiển thị tỷ lệ bệnh nhân có bệnh vs không bệnh
- Nhận xét: Dữ liệu không cân bằng (65% không bệnh, 35% có bệnh)

### 02_correlation_matrix.png
- Ma trận tương quan giữa tất cả các biến
- Glucose có tương quan cao nhất với Outcome (0.47)
- BMI cũng có tương quan đáng kể (0.29)

### 03_feature_distribution.png
- Phân bố của từng đặc trưng
- Giúp hiểu rõ các chỉ số y tế

### 04_feature_by_outcome.png
- So sánh phân bố đặc trưng giữa nhóm bệnh và không bệnh
- Nhận xét sự khác biệt rõ ràng giữa 2 nhóm

### 05_model_comparison.png
- So sánh độ chính xác của 3 mô hình
- Random Forest và SVM có kết quả tương tự, tốt hơn Logistic Regression

### 06_confusion_matrices.png
- Ma trận nhầm lẫn của 3 mô hình
- Hiển thị True Positive, False Positive, True Negative, False Negative

### 07_roc_curves.png
- Đường cong ROC của 3 mô hình
- Logistic Regression có AUC cao nhất (0.8230)
- Random Forest AUC = 0.8194

### 08_feature_importance.png
- Tầm quan trọng của từng đặc trưng (Random Forest)
- Glucose (28.84%) là quan trọng nhất
- SkinThickness (6.72%) là ít quan trọng nhất

## ⚙️ Tham Số Mô Hình

### Logistic Regression
```python
LogisticRegression(max_iter=1000, random_state=42)
```

### Random Forest
```python
RandomForestClassifier(
    n_estimators=100,      # 100 cây quyết định
    random_state=42,       # Cố định random state
    n_jobs=-1,             # Sử dụng tất cả CPU cores
    max_depth=10           # Độ sâu tối đa của cây
)
```

### SVM
```python
SVC(
    kernel='rbf',          # Kernel hàm cơ sở bán kính
    probability=True,      # Tính xác suất
    random_state=42,
    gamma='scale'          # Tham số kernel
)
```

## 💡 Nhận Xét & Đề Xuất

Điểm Mạnh
- Glucose là chỉ số rất quan trọng → Kiểm tra thường xuyên
- Random Forest cân bằng tốt giữa độ chính xác và tổng quát hóa
- AUC = 0.8194 cho thấy mô hình khác biệt tốt giữa hai lớp

Điểm Cần Cải Thiện
- Dữ liệu không cân bằng (65% vs 35%) → Có thể sử dụng SMOTE
- Một số giá trị 0 có thể không phải thiếu dữ liệu thực sự
- Precision cho lớp "có bệnh" là 66% → Còn cải thiện được

### Đề Xuất Tương Lai
1. **Tối ưu hóa siêu tham số** (Hyperparameter Tuning)
   - GridSearch hoặc RandomSearch
   - Cross-validation

2. **Xử lý dữ liệu không cân bằng**
   - SMOTE (Synthetic Minority Oversampling Technique)
   - Weighted loss function

3. **Thêm mô hình**
   - Gradient Boosting
   - XGBoost
   - Neural Network

4. **Kiểm định chéo** (Cross-Validation)
   - K-Fold Cross-Validation
   - Stratified K-Fold

LƯU Ý
- Mô hình này KHÔNG CÓ THỂ thay thế chẩn đoán y tế chuyên nghiệp
- Độ chính xác 75% có nghĩa là ~25% trường hợp có thể dự đoán sai
- Luôn tham khảo bác sĩ chuyên khoa trước khi đưa ra quyết định y tế
- Dữ liệu này từ những nữ bệnh nhân người Ấn Độ Pima, có thể không áp dụng cho các quần thể khác

Tài Liệu Tham Khảo

   - Source: UCI Machine Learning Repository
   - Link: https://www.kaggle.com/uciml/pima-indians-diabetes-database

   - Smith, J. W., et al. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.

   - Link: https://scikit-learn.org/


=======
# sgu2526k1_csttnt_btnhom
Doanh ngu
>>>>>>> 5ca1df1fc5765992d5dc6161c59429f2f93e0325
