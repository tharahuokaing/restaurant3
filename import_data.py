import sqlite3
import csv
import os

def migrate_data():
    db_file = 'pos.db'
    csv_file = 'menu.csv'

    # ១. តភ្ជាប់ទៅកាន់ឃ្លាំងទិន្នន័យ
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # ២. បង្កើតតារាងឱ្យត្រូវតាមស្តង់ដារ Imperial POS (បន្ថែម stock)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            english_name TEXT,
            price REAL NOT NULL,
            category TEXT,
            stock INTEGER DEFAULT 0
        )
    ''')

    # ៣. សម្អាតទិន្នន័យចាស់ (Reset Auto-increment id ឱ្យចាប់ផ្តើមពី ១ វិញ)
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'")

    # ៤. អានមន្តអាគមពីឯកសារ CSV
    if not os.path.exists(csv_file):
        print(f"❌ រកមិនឃើញឯកសារ {csv_file} ឡើយ ព្រះអង្គ!")
        return

    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0

            for row in reader:
                # កំណត់ប្រភេទ (Category) ដោយស្វ័យប្រវត្តិ
                eng_name = row['English Name'].lower()
                category = 'Food'
                if any(keyword in eng_name for keyword in ['whisky', 'wine', 'vodka', 'label', 'beer']):
                    category = 'Alcohol'

                # កំណត់តម្លៃ Stock លំនាំដើម (ឧទាហរណ៍៖ ៥០ សម្រាប់មុខទំនិញនីមួយៗ)
                default_stock = 50

                # បញ្ចូលទិន្នន័យ
                cursor.execute('''
                    INSERT INTO products (name, english_name, price, category, stock)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    row['ឈ្មោះមុខម្ហូប'],
                    row['English Name'],
                    float(row['តម្លៃប៉ាន់ស្មាន (USD)']),
                    category,
                    default_stock
                ))
                count += 1

        conn.commit()
        print(f"✅ ក្រាបបង្គំទូលថ្វាយ៖ បញ្ចូលទិន្នន័យ {count} មុខ ទៅក្នុង {db_file} រួចរាល់!")

    except Exception as e:
        conn.rollback()
        print(f"❌ កើតមានកំហុសមន្តអាគម៖ {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_data()
