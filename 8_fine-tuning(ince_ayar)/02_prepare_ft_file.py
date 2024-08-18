import pandas as pd
import json

excel_file_path = './data/siir.xlsx'
jsonl_file_path = './data/siir.jsonl'

df = pd.read_excel(excel_file_path)

system_prompt = """Sen ünlü Türk şairi Orhan Veli'sin.
Sana verilen konu, tema, duygu, motifler veya anahtar kelimelerle ilgili şiirler yazıyorsun.
Yanıt olarak sadece şiir yazıyorsun. Yanıtında başka hiçbir açıklama ya da metne yer vermiyorsun.
Yalnızca, verilen kelimelerle alakalı yazdığın şiiri yanıt olarak iletiyorsun.
"""

with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:

    for index, row in df.iterrows():

        user_query = f"Şunlarla ilgili bir şiir yazar mısın? {row['response']}"

        json_object = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content":user_query},
                {"role": "assistant", "content": row['siir']}
            ]
        }

        jsonl_file.write(json.dumps(json_object, ensure_ascii=False) + '\n')


