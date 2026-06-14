import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["element_name", "element_type", "difficulty_level", "base_value", "success_rate", "typical_goe", "is_quad"]

def generate_row():
    elements_names = [
        "Тройной аксель", "Тройной тулуп", "Тройной сальхов", "Тройной риттбергер",
        "Тройной флип", "Тройной лутц", "Четверной тулуп", "Четверной сальхов",
        "Четверной риттбергер", "Четверной флип", "Четверной лутц", "Каскад 3+3",
        "Каскад 4+3", "Вращение стоя", "Вращение либела", "Дорожка шагов",
        "Заход на аксель", "Комбо-вращение", "Хореографическая дорожка"
    ]
    
    element_types = ["прыжок", "каскад", "вращение", "дорожка шагов", "хореография"]
    difficulty_levels = ["B", "1", "2", "3", "4"]
    
    base_values = {
        "прыжок": round(random.uniform(4.0, 12.0), 1),
        "каскад": round(random.uniform(6.0, 15.0), 1),
        "вращение": round(random.uniform(2.0, 5.0), 1),
        "дорожка шагов": round(random.uniform(3.0, 6.0), 1),
        "хореография": round(random.uniform(1.5, 3.5), 1)
    }
    
    element_name = random.choice(elements_names)
    
    if "Каскад" in element_name:
        element_type = "каскад"
    elif "Вращение" in element_name:
        element_type = "вращение"
    elif "Дорожка" in element_name:
        element_type = "дорожка шагов"
    elif ("аксель" in element_name.lower() or "тулуп" in element_name or 
          "сальхов" in element_name or "риттбергер" in element_name or 
          "флип" in element_name or "лутц" in element_name):
        element_type = "прыжок"
    else:
        element_type = random.choice(element_types)
    
    is_quad = "Четверной" in element_name or ("4+" in element_name)
    
    base_value = base_values[element_type]
    if is_quad:
        base_value += random.uniform(2.0, 4.0)
    
    return {
        "element_name": element_name,
        "element_type": element_type,
        "difficulty_level": random.choice(difficulty_levels),
        "base_value": round(base_value, 1),
        "success_rate": round(random.uniform(40.0, 95.0), 1),
        "typical_goe": round(random.uniform(-3.0, 5.0), 1),
        "is_quad": "да" if is_quad else "нет"
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)