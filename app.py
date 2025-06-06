from flask import Flask, jsonify
import requests
from datetime import datetime, date
import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
        except locale.Error:
            pass


app = Flask(__name__)

def get_liturgia_from_external_api(target_date: date):
    base_url = "https://liturgia.up.railway.app/v2/"
    api_url = f"{base_url}?dia={target_date.day}&mes={target_date.month}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        liturgia_completa = {
            "data": target_date.strftime("%d de %B de %Y"),
            "dia_da_semana": target_date.strftime("%A"),
            "titulo": data.get("liturgia", "Título não encontrado"),
            "cor_liturgica": data.get("cor", "Não informada"),
            "leituras": []
        }

        leituras_from_api = data.get("leituras", {})

        leitura_tipos_map = [
            ("primeiraLeitura", "Primeira Leitura"),
            ("salmo", "Salmo Responsorial"),
            ("segundaLeitura", "Segunda Leitura"),
            ("evangelho", "Evangelho")
        ]

        for api_field_name, display_name in leitura_tipos_map:
            list_of_leitura_dicts = leituras_from_api.get(api_field_name)
            
            if list_of_leitura_dicts and isinstance(list_of_leitura_dicts, list):
                for leitura_item in list_of_leitura_dicts:
                    if isinstance(leitura_item, dict):
                        referencia = leitura_item.get("referencia", "Não encontrada")
                        texto = leitura_item.get("texto", "Texto não disponível")
                        
                        if api_field_name == "salmo" and leitura_item.get("refrao"):
                            texto = f"Refrão: {leitura_item['refrao']}\n{texto}"

                        if texto != "Texto não disponível":
                            liturgia_completa["leituras"].append({
                                "tipo": display_name,
                                "referencia": referencia,
                                "texto": texto
                            })
        
        if leituras_from_api.get("extras") and isinstance(leituras_from_api["extras"], list):
            for extra in leituras_from_api["extras"]:
                if isinstance(extra, dict) and extra.get("tipo") and extra.get("referencia") and extra.get("texto"):
                    liturgia_completa["leituras"].append({
                        "tipo": extra["tipo"],
                        "referencia": extra["referencia"],
                        "texto": extra["texto"]
                    })

        oracoes_api = data.get("oracoes", {})
        if oracoes_api:
            if oracoes_api.get("coleta"):
                liturgia_completa["leituras"].append({
                    "tipo": "Oração da Coleta",
                    "referencia": "Não aplicável",
                    "texto": oracoes_api["coleta"]
                })
            if oracoes_api.get("oferendas"):
                liturgia_completa["leituras"].append({
                    "tipo": "Oração das Oferendas",
                    "referencia": "Não aplicável",
                    "texto": oracoes_api["oferendas"]
                })
            if oracoes_api.get("comunhao"):
                liturgia_completa["leituras"].append({
                    "tipo": "Oração da Comunhão",
                    "referencia": "Não aplicável",
                    "texto": oracoes_api["comunhao"]
                })
            if oracoes_api.get("extras") and isinstance(oracoes_api["extras"], list):
                for extra_oracao in oracoes_api["extras"]:
                    if isinstance(extra_oracao, dict) and extra_oracao.get("tipo") and extra_oracao.get("texto"):
                         liturgia_completa["leituras"].append({
                            "tipo": f"Oração Extra: {extra_oracao['tipo']}",
                            "referencia": "Não aplicável",
                            "texto": extra_oracao["texto"]
                        })

        return liturgia_completa

    except requests.exceptions.RequestException:
        return None
    except ValueError:
        return None
    except Exception:
        return None

@app.route('/liturgia', methods=['GET'])
@app.route('/liturgia/<string:data_str>', methods=['GET'])
def api_get_liturgia(data_str=None):
    if data_str:
        try:
            target_date = datetime.strptime(data_str, '%d-%m-%Y').date()
        except ValueError:
            return jsonify({"erro": "Formato de data inválido. Use DD-MM-AAAA (ex: 05-06-2025)."}), 400
    else:
        target_date = date.today()

    liturgia = get_liturgia_from_external_api(target_date)

    if liturgia:
        return jsonify(liturgia)
    else:
        return jsonify({"erro": f"Não foi possível obter a liturgia para a data {target_date.strftime('%d-%m-%Y')}."}), 500

if __name__ == '__main__':
    app.run(debug=True)