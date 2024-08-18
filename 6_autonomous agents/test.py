import streamlit as st

# Başlık
st.title('Kişilik Testi')

# Sorular ve yanıt seçenekleri
sorular = [
    "Yeni insanlarla tanışmayı sever misiniz?",
    "Detaylara önem verir misiniz?",
    "Plan yapmadan seyahate çıkar mısınız?",
    "Risk almayı sever misiniz?",
    "Sanat eserlerinden etkilenir misiniz?",
    "Bir grup içinde liderlik yapmayı sever misiniz?",
    "Bilinmeyene karşı meraklı mısınız?",
    "Kuralları sorgular mısınız?",
    "Yalnız zaman geçirmekten hoşlanır mısınız?",
    "Düzenli bir yaşam tarzını tercih eder misiniz?"
]

yanit_secenekleri = [
    'Kesinlikle katılıyorum', 'Katılıyorum', 'Kararsızım', 'Katılmıyorum', 'Kesinlikle katılmıyorum'
]

# Kullanıcı yanıtlarını toplama
yanitlar = []
for soru in sorular:
    yanit = st.radio(soru, yanit_secenekleri, key=soru)
    yanitlar.append(yanit)

# Kişilik tipi hesaplama
def kisilik_tipi_hesapla(yanitlar):
    puanlar = {
        'Dışa Dönük': 0,
        'İçe Dönük': 0,
        'Pratik': 0,
        'Yenilikçi': 0,
        'Riskten Kaçınan': 0,
        'Risk Alıcı': 0
    }

    for yanit in yanitlar:
        if yanit == 'Kesinlikle katılıyorum' or yanit == 'Katılıyorum':
            puanlar['Dışa Dönük'] += 1
            puanlar['Yenilikçi'] += 1
            puanlar['Risk Alıcı'] += 1
        elif yanit == 'Kararsızım':
            puanlar['Pratik'] += 1
            puanlar['İçe Dönük'] += 1
        elif yanit == 'Katılmıyorum' or yanit == 'Kesinlikle katılmıyorum':
            puanlar['İçe Dönük'] += 1
            puanlar['Pratik'] += 1
            puanlar['Riskten Kaçınan'] += 1

    max_puan = max(puanlar.values())
    kisilik_tipleri = [k for k, v in puanlar.items() if v == max_puan]

    return ', '.join(kisilik_tipleri)

# Sonuçları gösterme
if st.button('Kişilik Tipimi Belirle'):
    sonuc = kisilik_tipi_hesapla(yanitlar)
    st.subheader('Kişilik Tipiniz:')
    st.write(sonuc)
    st.write('Not: Bu test, genel bir rehber olarak kullanılmalıdır. Kişilik, zaman içinde ve farklı durumlar altında değişebilir.')