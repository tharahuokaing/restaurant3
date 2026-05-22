import sqlite3
import pandas as pd
import os

def imperial_migration():
    csv_file = 'menu.csv'
    db_file = 'pos.db'

    if not os.path.exists(csv_file):
        print(f"❌ រកមិនឃើញឯកសារ {csv_file} ឡើយ ព្រះអង្គ!")
        return

    try:
        # ១. អានឯកសារ CSV
        df = pd.read_csv(csv_file)

        # ២. បង្កើត Column 'category' និង 'stock' ដោយប្រើ Logic របស់ Pandas (Vectorization)
        # នេះលឿនជាងការប្រើ iterrows() ១០ ដង
        alcohol_keywords = ['Whisky', 'Wine', 'Vodka', 'Label', 'Beer', 'Bottle']

        # កំណត់ប្រភេទ Alcohol ប្រសិនបើឈ្មោះមានពាក្យក្នុងបញ្ជី
        df['category'] = df['English Name'].apply(
            lambda x: 'Alcohol' if any(k in str(x) for k in alcohol_keywords) else 'Food'
        )

        # កំណត់ស្តុកដំបូង (ឧទាហរណ៍៖ ៨៨ សម្រាប់គ្រប់មុខទំនិញ ដើម្បីសិរីសួស្តី)
        df['stock'] = 88

        # ៣. តភ្ជាប់ទៅកាន់ Database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # ៤. រៀបចំតារាង (Schema) ឱ្យបានត្រឹមត្រូវ
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

        # ៥. សម្អាតទិន្នន័យចាស់ និង Reset ID
        cursor.execute("DELETE FROM products")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'")

        # ៦. បាញ់ទិន្នន័យចូល Database ក្នុងពេលតែមួយ (Bulk Insert)
        # យើងរើសយកតែ Column ណាដែលត្រូវគ្នានឹង Table ក្នុង DB
        final_df = df[['ឈ្មោះមុខម្ហូប', 'English Name', 'តម្លៃប៉ាន់ស្មាន (USD)', 'category', 'stock']]

        final_df.to_sql('products', conn, if_exists='append', index=False,
                       dtype={
                           'ឈ្មោះមុខម្ហូប': 'TEXT',
                           'English Name': 'TEXT',
                           'តម្លៃប៉ាន់ស្មាន (USD)': 'REAL',
                           'category': 'TEXT',
                           'stock': 'INTEGER'
                       })

        conn.commit()
        conn.close()

        print(f"✅ ក្រាបបង្គំទូលថ្វាយ៖ ទិន្នន័យ {len(df)} មុខ ត្រូវបានបញ្ចូលក្នុងមហាកំផែងទិន្នន័យជោគជ័យ!")

    except Exception as e:
        print(f"❌ កើតមានកំហុសមន្តអាគម៖ {e}")

if __name__ == "__main__":
    imperial_migration()
