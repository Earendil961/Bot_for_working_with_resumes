import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("rezume_full_merged.csv", sep=';')

print("=== Общая информация ===")
print(f"Всего строк: {len(df)}")
print(f"Всего столбцов: {len(df.columns)}")
print("\nТипы данных:")
print(df.dtypes)

print("\n=== Пропущенные значения ===")
missing_values = df.isnull().sum()
missing_percent = (missing_values / len(df)) * 100
missing_data = pd.DataFrame({
    'Количество пропусков': missing_values,
    'Процент пропусков': missing_percent.round(2)
})
print(missing_data[missing_data['Количество пропусков'] > 0])

plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Распределение пропущенных значений')
plt.show()

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print("\n=== Описательная статистика числовых данных ===")
print(df[numeric_cols].describe())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n=== Анализ столбца '{col}' ===")
    print(f"Уникальных значений: {df[col].nunique()}")
    if df[col].nunique() < 20:
        print("Распределение значений:")
        print(df[col].value_counts())

        plt.figure(figsize=(10, 5))
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Распределение значений в столбце {col}')
        plt.xticks(rotation=45)
        plt.show()

print("\n=== Анализ целевой переменной ===")
print("Распределение значений response_type_const:")
print(df['response_type_const'].value_counts(normalize=True) * 100)

plt.figure(figsize=(8, 5))
sns.countplot(x='response_type_const', data=df)
plt.title('Распределение целевой переменной (response_type_const)')
plt.show()

date_cols = [col for col in df.columns if 'date' in col.lower()]
if date_cols:
    print("\n=== Анализ временных данных ===")
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col])
            print(f"\nСтолбец: {col}")
            print(f"Минимальная дата: {df[col].min()}")
            print(f"Максимальная дата: {df[col].max()}")

            plt.figure(figsize=(12, 5))
            df[col].dt.year.value_counts().sort_index().plot(kind='bar')
            plt.title(f'Распределение по годам для столбца {col}')
            plt.show()
        except:
            print(f"Не удалось преобразовать столбец {col} в дату")

if len(numeric_cols) > 1:
    print("\n=== Корреляционный анализ ===")
    corr_matrix = df[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Матрица корреляций')
    plt.show()

print("\n=== Анализ выбросов ===")
for col in numeric_cols:
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df[col])
    plt.title(f'Ящик с усами для {col}')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df[col], kde=True)
    plt.title(f'Гистограмма распределения {col}')
    
    plt.tight_layout()
    plt.show()
    
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\nСтолбец: {col}")
    print(f"Количество выбросов: {len(outliers)}")
    print(f"Процент выбросов: {len(outliers)/len(df)*100:.2f}%")
    if len(outliers) > 0:
        print("Примеры выбросов:")
        print(outliers[[col]].head())
