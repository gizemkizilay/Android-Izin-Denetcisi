import xml.etree.ElementTree as ET
import sys
import os

TEHLIKELI_IZINLER = [
    "android.permission.READ_CONTACTS", "android.permission.WRITE_CONTACTS",
    "android.permission.CAMERA", "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION", "android.permission.RECORD_AUDIO",
    "android.permission.READ_PHONE_STATE", "android.permission.CALL_PHONE",
    "android.permission.SEND_SMS", "android.permission.RECEIVE_SMS",
    "android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"
]

def analiz_et(dosya_yolu):
    try:
        agac = ET.parse(dosya_yolu)
        kok = agac.getroot()
    except Exception as e:
        print("Hata: XML okunamadi.")
        return

    izinler = []
    for etiket in kok.findall('uses-permission'):
        izin_adi = etiket.get('{http://schemas.android.com/apk/res/android}name')
        if izin_adi:
            izinler.append(izin_adi)

    tehlikeli = [i for i in izinler if i in TEHLIKELI_IZINLER]
    normal = [i for i in izinler if i not in TEHLIKELI_IZINLER]
    
    risk_puani = (len(tehlikeli) * 10) + (len(normal) * 1)
    
    print("\n" + "="*50)
    print(" [!] ANDROID MANIFEST IZIN DENETCISI RAPORU")
    print("="*50)
    print(f"Toplam Izin Sayisi  : {len(izinler)}")
    print(f"Normal Izinler      : {len(normal)}")
    print(f"Tehlikeli Izinler   : {len(tehlikeli)}")
    print(f"[*] RISK PUANI      : {risk_puani}")
    print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analiz_et(sys.argv[1])