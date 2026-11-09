import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_excel('data.xlsx')
X = df[['temperatura', 'presion', 'vibracion', 'tiempo_produccion']]
y = df['defectuoso']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)
kernels = ['linear', 'rbf', 'poly']
resultados = []
for kernel in kernels:
    modelo = make_pipeline(
        StandardScaler(),
        SVC(kernel=kernel)
    )
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    resultados.append({
        'Modelo SVM': kernel,
        'Accuracy': accuracy,
        'F1-score': f1
    })
tabla = pd.DataFrame(resultados)
print("\nCOMPARACIÓN DE MODELOS SVM")
print(tabla.to_string(index=False))

mejor = tabla.loc[tabla['F1-score'].idxmax()]
print("\nMEJOR MODELO:")
print("Kernel:", mejor['Modelo SVM'])
print("Accuracy:", mejor['Accuracy'])
print("F1-score:", mejor['F1-score'])