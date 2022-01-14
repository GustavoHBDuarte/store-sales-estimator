import os
import pandas as pd
import numpy as np
import requests
from flask import Flask, request, Response

# logica utilizada pelo link do bot do Telegram:
##https://api.telegram.org/bot<token>/METHOD_NAME


# constants
# Token a ser usado na comunicacao com o Telegram
TOKEN = pd.read_csv('TOKEN.txt', header = None)
TOKEN = TOKEN.iloc[0,0]



# Informações sobre o bot - parametro getMe
#'https://api.telegram.org/bot{}/getMe'.format(TOKEN)


# Como extrair uma a mensagem recebida pelo bot? - parâmetro getUpdates
#'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN)


# Como fazer o bot retornar uma mensagem? - parametro sendMessage
#'https://api.telegram.org/bot{}/sendMessage?chat_id=1589632105&text=It worked!'.format(TOKEN)


# Conexão entre o bot e o endpoint local exposto - parametro webHook
# IMPORTANTE: para expor o localhost tive que usar o ngrok (https://dashboard.ngrok.com/get-started/setup)
# Localização ngrok na minha máquina local cd /home/gustavo/Downloads ./ngrok http 5000
#'https://api.telegram.org/bot{}/setwebHook?url=https://c396-201-71-19-91.ngrok.io'.format(TOKEN)






def send_message(chat_id, text):
    
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id) 

    # envio do texto
    response = requests.post(url, json={"text": text})
    
    print('Status Code: {}'.format(response.status_code))
    
    return None



def load_dataset(store_id):

    # Loading test dataset
    
    df_test = pd.read_csv('test.csv')
    
    
    # Choosing store for prediction (slice df)
    
    df_test = df_test[df_test['Store']==store_id]
    
    if not df_test.empty:               
        
        # Converting df to json
        
        data_json = df_test.to_json(orient='records', date_format='iso')
        
    else:
        
        data_json = 'error'
    
    return data_json


def predict(data_json):
    

    # API Call =====================================================================================
    
    # Para a call funcionar o deploy do modelo deve ter sido feito com sucesso no Heroku.
    # Se o resultado da execução dessa célula for 200 a requisição funcionou
    # Se o resultado da execução dessa célula for 503 significa que a porta não foi encontrada
    
    url = 'https://rossmann-sales-predictor.herokuapp.com/rossmann/predict' 
    
    header = {'Content-type':'application/json'} #indica para a API qual tipo de requisição se está fazendo
    
    
    
    
    
    # Fazendo a requisição
    
    response = requests.post(url=url, headers=header, json=data_json)
    
    print('Status Code: {}'.format(response.status_code))
    
    
    
    
    # Convertendo o json retornado pela requisição em um df
    
    df_predictions = pd.DataFrame(response.json(), columns=response.json()[0].keys())
    
    return df_predictions




def parse_message(message):
    
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']
    
    store_id = store_id.replace('/', '')
    
    try:
        store_id = int(store_id)
    
    except ValueError:
                
        store_id = 'error'
    
    return chat_id, store_id





# initialize API
app = Flask(__name__)

# criando o endpoint (url que receberá os dados):
@app.route( '/', methods=['GET','POST'] )


def index():
    if request.method=='POST': # condição na qual o bot recebe mensagem postada pelo usuário
        
        message = request.get_json()
        
        
        chat_id, store_id = parse_message(message)
        
        
        if store_id != 'error':
            
            # loading data
            data = load_dataset(store_id)
            
            if data != 'error':
                            
                #predict
                df_predictions = predict(data)
                
                #calculations
                
                # Grouping predictions by store

                df_predictions_grouped = df_predictions[['Store', 'Predictions']].groupby('Store').sum().reset_index()


                # Checking predictions for a specific store / send message

                msg ='Store {0} will sell €{1:.2f} in the next 6 weeks.'.format(df_predictions_grouped['Store'].values[0], df_predictions_grouped['Predictions'].values[0])
                
                #send message
                
                send_message(chat_id, msg)
                return Response('Ok', status='200')
                
                
            else:
                send_message(chat_id, 'Store ID unavailable')
                return Response('OK', status='200')
        
        else:
            
            send_message(chat_id, 'Store ID must be a valid number')
            return Response('Ok', status='200')
        
        
        
    else:
        return '<h1>Rossmann Telegram Bot</h1>' # mostrar esse texto caso o usário faça uma requisição na API sem enviar dados.
        
    

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run( '0.0.0.0', port=port )
    #      (local host)



