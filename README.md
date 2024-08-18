# Generative AI & Prompt Engineering Training Guide

This repository contains files for a training program covering Generative AI and Prompt Engineering topics. The training includes various projects and applications developed using Streamlit. Below are the main sections of the training and their descriptions.

## Table of Contents

1. **Basic Operations**  
   Basic operations and commands. This section provides information on fundamental processes and first steps related to Generative AI and prompt engineering.
   - `genai_audio101`: Basic information and examples related to audio processing.
   - `genai_code101`: Fundamentals of coding and programming.
   - `genai_image101`: Image processing and related techniques.
   - `genai_multimodality101`: Basics of working with multimodal data.
   - `genai_text101`: Text processing and language modeling topics.
   - `streamlit101`: Basics of developing applications with Streamlit.

2. **Application Project - Voicedraw**  
   A project involving a voice-based drawing application. Learn to create graphic drawings with voice commands and use related technologies. The application is developed using [Streamlit](https://streamlit.io/).
   - `app`: Core application files.
   - `painter`: Module for drawing with voice commands.
   - `recorder`: Module for recording audio.
   - `transcriptor`: Module for converting audio recordings to text.
   - `requirements.txt`: File specifying the dependencies required for the project.

3. **LangChain Framework**  
   Details on the LangChain framework. LangChain is a framework used for language models and natural language processing (NLP) applications. Applications are visualized with Streamlit.
   - `data`: Data processing and configuration.
   - `chain`: LangChain’s chaining structures and applications.
   - `loaders`: Data loaders and related tools.
   - `model`: Models and configurations used with LangChain.
   - `modelhelper`: Helper tools for working with models.
   - `rag`: Components related to Retrieval-Augmented Generation (RAG).
   - `raghelper`: Helper tools for RAG processes.
   - `requirements`: Dependencies required for LangChain applications.
   - `splitter_comparison`: Data splitting methods and comparisons.

4. **Application Project - VidChat**  
   A project involving a video chat application. Learn about video-based interactions and related application development processes. The project is presented using [Streamlit](https://streamlit.io/).
   - `img`: Images and media used in video applications.
   - `app`: Core application files.
   - `raghelper`: Helper tools for RAG processes in video-based projects.
   - `requirements`: File specifying the dependencies required for the project.
   - `videohelper`: Modules for video processing and management.
   - `youtubevideo`: YouTube video used in the application.

5. **Retrieval-Augmented Generation (RAG)**  
   Information on Retrieval-Augmented Generation (RAG) techniques. This technique allows language models to access broader information sources to produce more effective responses. Related applications are integrated with Streamlit.
   - `data`: Data configurations used in RAG processes.
   - `01_basic_rag_with_langchain.py`: Basic RAG application with LangChain.
   - `02_basic_rag_with_llama-index_local_storage.py`: RAG application using Llama Index with local storage.
   - `03_show_and_compare_embeddings.py`: Visualization and comparison of embedding vectors.
   - `04_show_similarity_scores_with_chromadb_example.py`: Display of similarity scores using ChromaDB.
   - `05_MMR_search_with_chroma.py`: MMR search method with Chroma.
   - `06_reranking_with_cohere.py`: Reranking processes with Cohere.
   - `07_hybrid_search.py`: Hybrid search methods.
   - `08_hyde.py`: Applications with the Hyde algorithm.
   - `09_multiquery_rag.py`: Multi-query RAG applications.
   - `hybridhelper.py`: Helper tools for hybrid search processes.
   - `hydehelper.py`: Helper tools for the Hyde algorithm.
   - `multiqueryhelper.py`: Helper tools for multi-query processes.
   - `relu.py`: ReLU activation function applications.
   - `requirements.txt`: Dependencies required for RAG applications.

6. **Autonomous Agents**  
   Information on autonomous agents. This section covers systems that can make and act upon decisions independently. Projects are visualized via Streamlit.
   - `img`: Images and media used in autonomous agent projects.
   - `01_react`: Basic autonomous agent applications developed with React.
   - `01_react_chat`: Chat-based autonomous agent applications developed with React.
   - `02_app_assistant`: Autonomous agents functioning as application assistants.
   - `03_crewai`: Autonomous agent applications for the CrewAI platform.
   - `04_autogen`: Autonomous generation methods and tools.
   - `assistant_helper`: Helper tools for enhancing assistant functionalities.
   - `crewhelper`: Helper tools for the CrewAI platform.
   - `customtools`: Customized tools and helper modules.
   - `requirements`: Dependencies required for autonomous agent projects.
   - `test`: Test files and scenarios used in autonomous agent projects.

7. **Fine-Tuning**  
   Tuning and customizing models. Learn how to optimize language models for specific tasks. Examples are provided with Streamlit applications.
   - `data`: Data configurations used in fine-tuning processes.
   - `00_gguf_quantization`: Information on quantizing the GGUF model.
   - `01_assign_labels`: Label assignment processes.
   - `02_prepare_ft_file`: Preparation of fine-tuning files.
   - `03_filecheck`: Checking files.
   - `04_delete_ft`: Deleting fine-tuning files.
   - `requirements`: Dependencies required for fine-tuning projects.

8. **Application Project - Data Explorer**  
   A project involving a data exploration application. Engage in practical work on data analysis and visualization. The application is developed using [Streamlit](https://streamlit.io/).
   - `data`: Data processing and configuration files.
   - `img`: Images and media used in the application.
   - `app`: Core application files.
   - `datahelper`: Helper tools for data processing and management.
   - `requirements`: File specifying the dependencies required for the project.

9. **Local Inference**  
   Performing inference locally. This section provides information on how to run models in local environments and perform inference tasks. Related applications are presented using Streamlit.
   - `local_chat`: Applications for chat-based inference in local environments.
   - `localhelper`: Helper tools for local inference processes.
   - `requirements`: File specifying the dependencies required for the projects.

## Usage Instructions

1. **Downloading Project Files:**
   You can start by cloning or downloading the project to your local machine.
   ```bash
   git clone https://github.com/username/genai_and_prompt_engineering.git
   ```

2. **Required Libraries and Dependencies:**
   Information about the required libraries and dependencies for the training projects and applications can be found in the requirements.txt or environment.yml files in each project directory. For example:
   ```bash
   pip install -r requirements.txt
   ```
3. **Running Projects:**
   Each application project may have its own run instructions. To start Streamlit applications, navigate to the relevant directory and use the following command:
   ```bash
   streamlit run app.py
   ```
   (Note: Replace app.py with the appropriate file name for your project.)

   
Feel free to customize this README file to include specific details and information about your projects and Streamlit-based applications. If you need to add any special information or details, please let me know!

---
                                                                                                                                                                                  
                                                                                                                                                                                                       
                                                                                                                                                                                                        
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
   - `youtubevideo`: Uygulamada kullanılan youtube videosu
5. **Retrieval-Augmented Generation (RAG)**  
   Retrieval-Augmented Generation (RAG) tekniği ile ilgili bilgiler. Bu teknik, dil modellerinin daha geniş bilgi kaynaklarına erişim sağlayarak daha etkili yanıtlar üretmesini sağlar. İlgili uygulamalar, Streamlit ile entegre edilmiştir.
   - `data`: RAG süreçlerinde kullanılan veri yapılandırmaları.
   - `01_basic_rag_with_langchain.py`: LangChain ile temel RAG uygulaması.
   - `02_basic_rag_with_llama-index_local_storage.py`: Llama Index ile yerel depolama kullanarak RAG uygulaması.
   - `03_show_and_compare_embeddings.py`: Gömme vektörlerinin gösterimi ve karşılaştırılması.
   - `04_show_similarity_scores_with_chromadb_example.py`: ChromaDB kullanarak benzerlik puanlarının gösterimi.
   - `05_MMR_search_with_chroma.py`: Chroma ile MMR arama yöntemi.
   - `06_reranking_with_cohere.py`: Cohere ile yeniden sıralama işlemleri.
   - `07_hybrid_search.py`: Hibrit arama yöntemleri.
   - `08_hyde.py`: Hyde algoritması ile uygulamalar.
   - `09_multiquery_rag.py`: Çoklu sorgu RAG uygulamaları.
   - `hybridhelper.py`: Hibrit arama süreçleri için yardımcı araçlar.
   - `hydehelper.py`: Hyde algoritması için yardımcı araçlar.
   - `multiqueryhelper.py`: Çoklu sorgu işlemleri için yardımcı araçlar.
   - `relu.py`: ReLU aktivasyon fonksiyonu uygulamaları.
   - `requirements.txt`: RAG uygulamalarının çalışması için gerekli bağımlılıklar.
6. **Autonomous Agents**  
   Otonom ajanlar üzerine bilgiler. Bu bölümde, kendi başına karar alabilen ve hareket edebilen ajan sistemleri hakkında bilgi bulacaksınız. Projeler, Streamlit üzerinden görselleştirilmiştir.
   - `img`: Otonom ajan projelerinde kullanılan görseller ve medyalar.
   - `01_react`: React ile geliştirilmiş temel otonom ajan uygulamaları.
   - `01_react_chat`: React ile sohbet tabanlı otonom ajan uygulamaları.
   - `02_app_assistant`: Uygulama asistanı olarak işlev gören otonom ajanlar.
   - `03_crewai`: CrewAI platformu için otonom ajan uygulamaları.
   - `04_autogen`: Otonom jenerasyon yöntemleri ve araçları.
   - `assistant_helper`: Asistanların işlevselliğini artıran yardımcı araçlar.
   - `crewhelper`: CrewAI platformu için yardımcı araçlar.
   - `customtools`: Özelleştirilmiş araçlar ve yardımcı modüller.
   - `requirements`: Otonom ajan projelerinin çalışması için gerekli bağımlılıklar.
   - `test`: Otonom ajan projelerinde kullanılan test dosyaları ve test senaryoları.
     
7. **Fine-Tuning (İnce Ayar)**  
   Modellerin ince ayar yapılması ve özelleştirilmesi. Bu bölümde, dil modellerini belirli görevler için nasıl optimize edebileceğinizi öğreneceksiniz. Streamlit uygulamaları ile örnekler sunulmuştur.
   - `data`: İnce ayar süreçlerinde kullanılan veri yapılandırmaları.
   - `00_gguf_quantization`: GGUF modelinin kuantizasyonu ile ilgili bilgiler.
   - `01_assign_labels`: Etiketlerin atanması işlemleri.
   - `02_prepare_ft_file`: İnce ayar dosyalarının hazırlanması.
   - `03_filecheck`: Dosyaların kontrol edilmesi.
   - `04_delete_ft`: İnce ayar dosyalarının silinmesi.
   - `requirements`: İnce ayar projelerinin çalışması için gerekli bağımlılıklar.
8. **Application Project - Data Explorer**  
   Veri keşfi uygulaması ile ilgili proje. Veri analizi ve görselleştirme üzerine uygulamalı bir çalışma yapabilirsiniz. Uygulama, [Streamlit](https://streamlit.io/) kullanılarak geliştirilmiştir.
   - `data`: Veri işleme ve yapılandırma dosyaları.
   - `img`: Uygulama içinde kullanılan görseller ve medya.
   - `app`: Temel uygulama dosyaları.
   - `datahelper`: Veri işleme ve yönetimi için yardımcı araçlar.
   - `requirements`: Projenin çalışması için gerekli bağımlılıkları belirten dosya.
9. **Local Inference**  
   Yerel çıkarım yapma. Bu bölüm, modellerin yerel ortamlarda nasıl çalıştırılacağı ve çıkarım işlemlerinin nasıl yapılacağı hakkında bilgi verir. İlgili uygulamalar, Streamlit ile sunulmuştur.
   - `local_chat`: Yerel ortamda sohbet tabanlı çıkarım yapma uygulamaları.
   - `localhelper`: Yerel çıkarım süreçlerini kolaylaştıran yardımcı araçlar.
   - `requirements`: Projelerin çalışması için gerekli bağımlılıkları belirten dosya.
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
