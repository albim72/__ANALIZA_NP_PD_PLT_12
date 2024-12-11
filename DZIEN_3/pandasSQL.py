import pandas as pd
from sqlalchemy import create_engine

# Konfiguracja połączenia do bazy MySQL
DATABASE_URL = 'mysql+pymysql://root:abc123@localhost/zaawansowana_baza'

# Tworzenie silnika (engine) połączenia
engine = create_engine(DATABASE_URL)

# Odczyt danych z tabeli 'users' za pomocą pandas
df_users = pd.read_sql("SELECT * FROM users", con=engine)

# Wyświetlenie DataFrame z użytkownikami
print("Użytkownicy:")
print(df_users)

# Odczyt danych z tabeli 'posts' za pomocą pandas
df_posts = pd.read_sql("SELECT * FROM posts", con=engine)

# Wyświetlenie DataFrame z postami
print("\nPosty:")
print(df_posts)
