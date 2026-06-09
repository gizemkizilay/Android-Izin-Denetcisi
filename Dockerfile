# Temel Python imajını kullanıyoruz
FROM python:3.12-slim

# Çalışma dizinini ayarlıyoruz
WORKDIR /app

# Kaynak kodumuzu konteynere kopyalıyoruz
COPY src/ /app/src/

# Uygulamanın nasıl çalışacağını belirtiyoruz
ENTRYPOINT ["python", "src/izin_denetici.py"]