#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:44:10 2022

@author: gustavo
"""
# Library imports

import sklearn
import pickle
import os
import pandas as pd
from flask             import Flask, request, Response
import json
from Rossmann_class.Data_Prep import Data_Prep # from diretório.nome_do_arquivo_classe import nome_da_classe

# loading model
model = pickle.load(open('model/model_XGBoost_tuned.pkl', 'rb')) # para o Heroku deve-se usar o caminho relativo 

# initialize API
app = Flask(__name__)

# criando o endpoint (url que receberá os dados):
@app.route( '/rossmann/predict', methods=['POST'] )


# Sempre após receber uma chamada o endpoint executa alguma função. Para esse caso ele executará a função 
## definida abaixo:

def rossmann_predict():
    test_json = request.get_json() # os dados da requisição virão na forma de json.
    
   
    if test_json: # there is data
        test_json = json.loads(test_json)
        
        if isinstance( test_json, dict ): #testar se o dado é uma requisição de apenas 1 linha (virá como dict)
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # do contrário a requisição virá na forma de lista (com cada ítem sendo um dicionario):
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        
        # Instantiate Rossmann class
        pipeline = Data_Prep()
        
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        
        # prediction
        df_response = pipeline.get_predictions( model, test_raw, df3 )
        
        return df_response
        
        
    else: # se o dado não existir
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # Heroku não sabe qual é a porta padrão. Usar a biblioteca os. para informar a porta usando variáveis de ambiente
    app.run( host='0.0.0.0', port=port, debug=False )
    #      (local host)
