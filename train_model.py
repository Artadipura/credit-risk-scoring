import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Langsung baca data mentah asli dari Kaggle!
df = pd.read_csv('credit_risk_dataset.csv')
df = df.dropna()

# 2. Bikin tabel berisi kolom penting DAN hitung beban pinjaman di sini
df_penting = df[['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'loan_status']].copy()
df_penting['beban_pinjaman'] = df_penting['loan_amnt'] / df_penting['person_income']

# 3. Pisahkan Lembar Soal (X) dan Kunci Jawaban (Y)
X = df_penting.drop('loan_status', axis=1)
Y = df_penting['loan_status']

# 4. Potong data dan Latih AI-nya
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

# 5. Simpan Otak AI ke dalam toples
with open('model_kredit_baru.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Data sukses dibersihkan & Model AI diupdate sempurna!")