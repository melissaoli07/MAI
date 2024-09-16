from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Aqui estamos carregando o modelo já treinado que está no arquivo JobLib
with open('C:/Users/HP/Desktop/fiap/ai2024/sprint3/MAI/meu_modelo_serializado.pickle', 'rb') as f:
    modelo = pickle.load(f)

# Rota para receber os dados e fazer previsões
@app.route('/prever', methods=['GET'])
def prever():
    # Obter parâmetros da solicitação GET
    parametro1 = int(request.args.get('quantity'))
    parametro2 = float(request.args.get('unitPrice'))
    parametro3 = float(request.args.get('costumerId'))
    parametro4 = int(request.args.get('month'))
    parametro5 = float(request.args.get('totalSpent'))
    parametro6 = float(request.args.get('avaregePrice'))
    parametro7 = int(request.args.get('frequency'))

    # Fazer previsões usando o modelo 
    entrada = np.array([[parametro1, parametro2, parametro3, parametro4, parametro5, parametro6, parametro7]])
    resultado = modelo.predict(entrada)

    # Retornar o resultado como JSON
    return jsonify({'previsao do grupo de cliente': resultado.tolist()})

if __name__ == '__main__':
    print("Servidor Flask em execução")
    # Executar o aplicativo Flask
    app.run(debug=True)
