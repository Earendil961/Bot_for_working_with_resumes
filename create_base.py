import pandas as pd
import numpy as np
import gc

edu = pd.read_csv("C:\R_dp\R_Data\hse\hse_project_2025\edu.csv", sep=';')
edu_sorted = edu.sort_values('id_cv')

addedu = pd.read_csv("C:\R_dp\R_Data\hse\hse_project_2025\ddedu.csv", sep=';')
addedu_sorted = addedu.sort_values('id_cv')

eda_full = pd.merge(edu_sorted, addedu_sorted, how='inner', on='id_cv')
print(eda_full.head(10))

print(f"Размер таблицы edu: {edu_sorted.shape} (строк, столбцов)")
print(f"Размер таблицы addedu: {addedu_sorted.shape} (строк, столбцов)")
print(f"Размер объединенной таблицы eda_full: {eda_full.shape} (строк, столбцов)")

eda_full.to_csv("eda_full.csv", sep=';', index=False, encoding='utf-8-sig')
print("\nТаблица сохранена в файл: eda_full.csv")

def load_large_csv(filepath, chunksize=10000):
    """Постепенная загрузка больших CSV файлов"""
    chunks = []
    for chunk in pd.read_csv(filepath, sep=';', chunksize=chunksize):
        chunks.append(chunk)
    return pd.concat(chunks, ignore_index=True)

try:
    print("1. Загрузка workexp...")
    workexp = pd.read_csv("C:\R_dp\R_Data\hse\hse_project_2025\workexp.csv", sep=';', nrows=1000000)
    print(f"Загружено строк workexp: {len(workexp)}")
    
    print("2. Сортировка workexp...")
    workexp = workexp.sort_values('id_cv')
    
    print("3. Загрузка eda_full...")
    eda_full = pd.read_csv("eda_full.csv", sep=';', nrows=1000000) 
    print(f"Загружено строк eda_full: {len(eda_full)}")
    
    print("4. Объединение таблиц...")
    merged_chunks = []
    for i in range(0, len(eda_full), 50000):
        chunk = eda_full.iloc[i:i+50000]
        merged = pd.merge(chunk, workexp, how='inner', on='id_cv')
        merged_chunks.append(merged)
        print(f"Обработано {min(i+50000, len(eda_full))}/{len(eda_full)} строк")
        gc.collect() 
    
    id_full = pd.concat(merged_chunks, ignore_index=True)
    print(f"5. Итоговый размер объединенной таблицы: {len(id_full)} строк")
    
    id_full.to_csv("id_full_merged.csv", sep=';', index=False)
    print("6. Результат сохранен в id_full_merged.csv")

except Exception as e:
    print(f"Ошибка: {str(e)}")
    print("Попробуйте уменьшить объем данных или увеличить ресурсы системы")
try:
    id_full_merged = pd.read_csv("id_full_merged.csv", sep=';', nrows=1000000)  
    print(f"Загружено строк id_full_merged: {len(id_full_merged)}")
except Exception as e:
    print(f"Ошибка при загрузке id_full_merged.csv: {e}")
    exit()

try:
    print("Загрузка responses...")
    responses = pd.read_csv("C:\R_dp\R_Data\hse\hse_project_2025\esponses.csv", sep=';', low_memory=False)
    print(f"Загружено строк responses: {len(responses)}")
    
    print("Сортировка responses...")
    responses = responses.sort_values('id_cv')
    
    print("Уникальные значения response_type:")
    print(responses["response_type"].unique())
    
    print("Создание response_type_const...")
    responses["response_type_const"] = np.where(
        responses["response_type"] == "Принятие", 1, 0
    )
    responses_2 = responses[['response_type_const', 'id_cv']].copy()
    
except Exception as e:
    print(f"Ошибка при обработке responses: {e}")
    exit()

try:
    print("Объединение таблиц...")
    rezume_full = pd.merge(
        responses_2, 
        id_full_merged, 
        how='inner', 
        on='id_cv'
    )
    
    rezume_full = rezume_full.drop_duplicates(subset='id_cv', keep='first')

    print("Размер итоговой таблицы:", len(rezume_full), rezume_full)
    
    rezume_full = rezume_full.head(900000)
    
    print("\nТипы данных в итоговой таблице:")
    print(rezume_full.dtypes)
    
    print("\nРазмер итоговой таблицы:")
    print(rezume_full.shape)
    
    print("\nКоличество уникальных id_cv:")
    print(rezume_full['id_cv'].nunique())
    
    print("\nПервые 10 строк:")
    print(rezume_full.head(10))
    
    rezume_full.to_csv(
        "rezume_full_merged.csv", 
        sep=';', 
        index=False, 
        encoding='utf-8-sig'
    )
    print("\nТаблица успешно сохранена в файл: rezume_full_merged.csv")
    
except Exception as e:
    print(f"Ошибка при объединении таблиц: {e}")
    exit()
