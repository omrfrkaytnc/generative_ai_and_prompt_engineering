# Generative AI & Prompt Engineering Eğitim Rehberi

Bu depo, Generative AI ve Prompt Engineering konularını kapsayan bir eğitim programına ait dosyaları içermektedir. Eğitim kapsamında çeşitli projeler ve uygulamalar Streamlit kullanılarak gerçekleştirilmiştir. Aşağıda eğitimde yer alan ana başlıklar ve her bir başlığın açıklamaları bulunmaktadır.

## İçindekiler

1. **Basic Operations**  
   Temel operasyonlar ve komutlar. Bu bölümde, Generative AI ve prompt mühendisliği ile ilgili temel işlemler ve ilk adımlar hakkında bilgi bulacaksınız.
   - `genai_audio101`: Ses işleme ile ilgili temel bilgiler ve örnekler.
   - `genai_code101`: Kodlama ve programlama temelleri.
   - `genai_image101`: Görüntü işleme ve ilgili teknikler.
   - `genai_multimodality101`: Çok modlu veri ile çalışma temelleri.
   - `genai_text101`: Metin işleme ve dil modelleme konuları.
   - `streamlit101`: Streamlit kullanarak uygulama geliştirme temelleri.

2. **Application Project - Voicedraw**  
   Ses tabanlı çizim uygulaması ile ilgili proje. Ses komutlarıyla grafik çizimleri yapmayı ve ilgili teknolojileri kullanmayı öğrenebilirsiniz. Uygulama, [Streamlit](https://streamlit.io/) kullanılarak geliştirilmiştir.
   - `app`: Temel uygulama dosyaları.
   - `painter`: Ses komutları ile çizim yapma fonksiyonlarını içeren modül.
   - `recorder`: Ses kayıt işlemleri için kullanılan modül.
   - `transcriptor`: Ses kayıtlarını metne dönüştüren modül.
   - `requirements.txt`: Projenin çalışması için gerekli bağımlılıkları belirten dosya.
3. **LangChain Framework**  
   LangChain çerçevesi üzerine detaylar. LangChain, dil modelleri ve doğal dil işleme (NLP) uygulamaları için kullanılan bir çerçevedir. Uygulamalar, Streamlit ile görselleştirilmiştir.
   - `data`: Verilerle ilgili işlemler ve yapılandırmalar.
   - `chain`: LangChain’in zincirleme yapıları ve uygulamaları.
   - `loaders`: Veri yükleyicileri ve ilgili araçlar.
   - `model`: LangChain ile kullanılan modeller ve yapılandırmaları.
   - `modelhelper`: Modellerle çalışmayı kolaylaştıran yardımcı araçlar.
   - `rag`: Retrieval-Augmented Generation (RAG) ile ilgili bileşenler.
   - `raghelper`: RAG süreçlerini kolaylaştıran yardımcı araçlar.
   - `requirements`: LangChain uygulamalarının çalışması için gerekli bağımlılıklar.
   - `splitter_comparison`: Veri bölme yöntemleri ve karşılaştırmalar.
4. **Application Project - VidChat**  
   Video sohbet uygulaması ile ilgili proje. Bu bölümde video tabanlı etkileşimler ve ilgili uygulama geliştirme süreçleri hakkında bilgi edinebilirsiniz. Proje, [Streamlit](https://streamlit.io/) kullanılarak sunulmuştur.
   - `img`: Video uygulamalarında kullanılan görseller ve medyalar.
   - `app`: Temel uygulama dosyaları.
   - `raghelper`: RAG süreçlerini video tabanlı projelerde kolaylaştıran yardımcı araçlar.
   - `requirements`: Projenin çalışması için gerekli bağımlılıkları belirten dosya.
   - `videohelper`: Video işleme ve yönetimi için kullanılan modüller.
   - `youtubevideo`: YouTube videoları ile entegre olan fonksiyonlar ve araçlar.
5. **Retrieval-Augmented Generation (RAG)**  
   Retrieval-Augmented Generation (RAG) tekniği ile ilgili bilgiler. Bu teknik, dil modellerinin daha geniş bilgi kaynaklarına erişim sağlayarak daha etkili yanıtlar üretmesini sağlar. İlgili uygulamalar, Streamlit ile entegre edilmiştir.

6. **Autonomous Agents**  
   Otonom ajanlar üzerine bilgiler. Bu bölümde, kendi başına karar alabilen ve hareket edebilen ajan sistemleri hakkında bilgi bulacaksınız. Projeler, Streamlit üzerinden görselleştirilmiştir.

7. **Fine-Tuning (İnce Ayar)**  
   Modellerin ince ayar yapılması ve özelleştirilmesi. Bu bölümde, dil modellerini belirli görevler için nasıl optimize edebileceğinizi öğreneceksiniz. Streamlit uygulamaları ile örnekler sunulmuştur.

8. **Application Project - Data Explorer**  
   Veri keşfi uygulaması ile ilgili proje. Veri analizi ve görselleştirme üzerine uygulamalı bir çalışma yapabilirsiniz. Uygulama, [Streamlit](https://streamlit.io/) kullanılarak geliştirilmiştir.

9. **Local Inference**  
   Yerel çıkarım yapma. Bu bölüm, modellerin yerel ortamlarda nasıl çalıştırılacağı ve çıkarım işlemlerinin nasıl yapılacağı hakkında bilgi verir. İlgili uygulamalar, Streamlit ile sunulmuştur.

## Kullanım Talimatları

1. **Proje Dosyalarını İndirme:**
   Bu projeyi yerel bilgisayarınıza klonlayarak veya dosyaları indirerek başlayabilirsiniz.
   ```bash
   git clone https://github.com/kullanıcı_adı/genai_and_prompt_engineering.git
   ```
2. **Gerekli Kütüphaneler ve Bağımlılıklar:**
   Eğitim projeleri ve uygulamalarının çalışması için gerekli olan kütüphaneler ve bağımlılıklar hakkında bilgiye her bir proje dizininde yer alan requirements.txt veya environment.yml dosyalarından ulaşabilirsiniz. Örnek olarak:
   ```bash
   pip install -r requirements.txt
   ```
3. **Proje Çalıştırma:**
   Her bir uygulama projesinin kendi çalıştırma talimatları olabilir. Streamlit uygulamalarını başlatmak için ilgili dizine gidip aşağıdaki komutu kullanabilirsiniz:
   ```bash
   streamlit run app.py
   ```
   (Not: app.py dosya adını projenizin dosya adını yansıtacak şekilde değiştirin.)

   
Bu README dosyasını, projelerinizin ayrıntılarını ve Streamlit tabanlı uygulamaları tanıtacak şekilde özelleştirebilirsiniz. Başka bir özel bilgi veya detay eklemek isterseniz, lütfen bana bildirin!
