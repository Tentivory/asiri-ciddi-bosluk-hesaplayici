#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Ciddi Boşluk Hesaplayıcı v1.0
Gününüzdeki boşluğu bilimsel ve bürokratik kesinlikle ölçer.
Bu program Türkiye Cumhuriyeti Boşluk Ölçüm Enstitüsü onaylıdır (hayali).
"""

import random
import time
import base64

# Gizli formül (dokunmayın, sistem çöker)
GIZLI = base64.b64decode("QnVyb2tyYXNpIGthemFuxLFybCwgYm_Fn2x1ayBkb2xtYXou").decode('utf-8')

def hesapla_bosluk(himm_sayisi, isim):
    print(f"\nSayın {isim}, boşluk ölçümü başlatılıyor...")
    print("Bürokratik onay bekleniyor...")
    time.sleep(2)
    print("Onay geldi. (Aslında gelmedi ama devam ediyoruz.)")
    
    katsayi = (himm_sayisi * random.uniform(0.1, 3.7)) + random.randint(5, 50)
    bosluk_orani = min(katsayi / 10, 99.9)
    
    print(f"\n=== RESMİ BOŞLUK RAPORU ===")
    print(f"İsim: {isim}")
    print(f"'Hımm' sayısı: {himm_sayisi}")
    print(f"Boşluk Katsayısı: {katsayi:.2f} birim")
    print(f"Boşluk Oranı: %{bosluk_orani:.1f}")
    print(f"Sonuç: Gününüz {bosluk_orani:.1f}% oranında boş.")
    
    if bosluk_orani > 70:
        print("UYARI: Boşluk kritik seviyede. Acil olarak daha fazla 'hımm' üretmeniz önerilir.")
    elif bosluk_orani < 20:
        print("Tebrikler! Boşluğunuz az. Muhtemelen çok meşgulsünüz veya program yanılıyor.")
    else:
        print("Normal boşluk seviyesi. Bürokrasi memnun.")
    
    print("\nNot: Bu ölçüm yasal olarak bağlayıcı değildir ama çok ciddidir.")
    print(f"Gizli not (kimse görmesin): {GIZLI}")

if __name__ == "__main__":
    print("Aşırı Ciddi Boşluk Hesaplayıcı'na hoş geldiniz!")
    print("Bu sistem, gününüzdeki anlamsız boşluğu ölçmek için tasarlanmıştır.")
    isim = input("Adınızı girin (ciddi olsun): ")
    try:
        himm = int(input("Bugün kaç kez 'hımm' dediniz? (sayı): "))
    except:
        himm = random.randint(1, 100)
        print(f"Geçersiz giriş. Sistem kendi başına {himm} olarak kabul etti.")
    
    hesapla_bosluk(himm, isim)
    print("\nRapor tamamlandı. Arşive kaldırılıyor...")
    time.sleep(1)
    print("Arşiv dolu. Rapor yok edildi. Ama boşluk kaldı.")
