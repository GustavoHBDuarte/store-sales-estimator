#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 15:43:38 2022

@author: gustavo
"""
import pickle
import pandas as pd
import numpy as np
import inflection
import datetime
import json

class Data_Prep(object):
    
    def __init__(self):
        self.competition_distance_scaler   = pickle.load(open('/home/gustavo/repos/Rossmann/competion_distance_scaler.pkl', 'rb')) # Opening scaler
        self.competition_time_month_scaler = pickle.load(open('/home/gustavo/repos/Rossmann/competition_time_month_scaler.pkl', 'rb')) # Opening scaler
        self.year_scaler                   = pickle.load(open('/home/gustavo/repos/Rossmann/year_scaler.pkl', 'rb')) # Opening scaler
        self.promo2_time_week_scaler       = pickle.load(open('/home/gustavo/repos/Rossmann/promo2_time_week_scaler.pkl', 'rb')) # Opening scalers
        self.store_type_encoder            = pickle.load(open('/home/gustavo/repos/Rossmann/store_type_encoder.pkl', 'rb')) # Opening encoders
        
        self.df_store                      = pd.read_csv('/home/gustavo/repos/Rossmann/store.csv')
    
    
    
    def data_cleaning(self, df):
        
        # Merging df_test and df_store:
        df = pd.merge(df, self.df_store, on='Store', how='left')
        
        # Dropping 'Id' column from df_test dataset:
        df = df.drop(columns='Id')
        


        # Changing column 'Date' to datetime

        df['Date'] = pd.to_datetime(df['Date'])

        # Adjusting column names

        df.columns = list(map(lambda x: inflection.underscore(x), df.columns)) #changing to underscore + lower(snakecase)



        # Filling NA's on 'competition_distance' column ===========================================


        ## LÓGICA USADA: se a distância está NA assumiu-se que a distância da loja concorrente é muita alta.
        ### então foi feito o preenchimento por um valor acima da distância mais alta do dataset

        df['competition_distance'] = df['competition_distance'].apply(lambda x: 200000.0 if pd.isna(x) else x)



        # Filling NA's on 'competition_open_since_month' column ==================================


        ## LÓGICA USADA: completou-se o valor NA usando o mês da coluna 'date' (data da venda) da respectiva linha

        df['competition_open_since_month'] = df[['date','competition_open_since_month']].apply(lambda x: x['date'].month if pd.isna(x['competition_open_since_month']) else x['competition_open_since_month'], axis=1)



        # Filling NA's on 'competition_open_since_year' column =====================================


        ## LÓGICA USADA: completou-se o valor NA usando o ano da coluna 'date' (data da venda) da respectiva linha

        df['competition_open_since_year'] = df[['date','competition_open_since_year']].apply(lambda x: x['date'].year if pd.isna(x['competition_open_since_year']) else x['competition_open_since_year'], axis=1)



        # Filling NA's on 'promo2_since_week' column =================================================

        ## LÓGICA USADA: todos os valores onde a coluna promo2 estavam 0 (não houve promoção na loja) a coluna
        ### 'promo2_since_week' estava NA, então assumiu-se que não houve promoção nessa loja e preencheu-se com 0

        df['promo2_since_week'] = df['promo2_since_week'].fillna(0)



        # Filling NA's on 'promo2_since_year' column ===================================================

        ## LÓGICA USADA: todos os valores onde a coluna promo2 estavam 0 (não houve promoção na loja) a coluna
        ### 'promo2_since_year' estava NA, então assumiu-se que não houve promoção nessa loja e preencheu-se com 0

        df['promo2_since_year'] = df['promo2_since_year'].fillna(0)




        # Filling NA's on 'promo_interval' column ========================================================

        ## LÓGICA USADA: todos os valores onde a coluna promo2 estavam 0 (não houve promoção na loja) a coluna
        ### 'promo_interval' estava NA, então assumiu-se que não houve promoção nessa loja e preencheu-se com 0

        df['promo_interval'] = df['promo_interval'].fillna(0)



        # Abaixo será criado um dicionário que auxiliará na conversão dos meses de números em letras:

        # criando mapeamento dos meses
        month_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}


        # criado a coluna 'month_map'
        ## LÒGICA: extraíu-se o mês (em número) da coluna 'date' e converteu-se em mês (em palavra) colocando em uma nova
        ### coluna

        df['month_map'] = df['date'].dt.month.map(month_map)


        # criando a coluna 'is_promo'
        # LÓGICA: Se o dia da venda (coluna 'data') estiver em um mês onde foi feita a promoção (coluna 'promo_interval')
        ## então será atribuído 1 na nova coluna 'is_promo', se não tiver promoção ou a venda tiver sido feita em um mês
        ## fora da promoção então o valor atribuído será 0

        df['is_promo'] = df[['month_map', 'promo_interval']].apply(lambda x: 0 if x['promo_interval']==0 else 1 if x['month_map'] in x['promo_interval'].split(',') else 0, axis=1)


        # Changing data types after previous columns creation

        df[['competition_open_since_month',
            'competition_open_since_year',
            'promo2_since_week',
            'promo2_since_year']] = df[['competition_open_since_month',
                                        'competition_open_since_year',
                                        'promo2_since_week',
                                        'promo2_since_year']].astype(int)
        
        return df
    
    
    def feature_engineering(self, df_1):    
    
    
        # Changing column 'assortment'

        df_1['assortment'] = df_1['assortment'].apply(lambda x:'basic' if x=='a' else 'extra' if x=='b' else 'extended')


        # Changing column 'state_holiday'

        df_1['state_holiday'] = df_1['state_holiday'].apply(lambda x:'Public holiday' if x=='a' else 'Easter' if x=='b' else 'Christmas' if x=='c' else 'regular day')


        # Derivando novas variáveis:


        # year

        df_1['year'] = df_1['date'].dt.year


        # month

        df_1['month'] = df_1['date'].dt.month


        # day

        df_1['day'] = df_1['date'].dt.day


        # week of year

        df_1['week_of_year'] = df_1['date'].dt.weekofyear


        # year week

        df_1['year_week'] = df_1['date'].dt.strftime('%Y-%W') # esse comando apenas coleta a data da venda e muda a formatação




        # competition_since (quanto tempo desde o início da competição ate a data da compra)

        # 1o passo - juntar as colunas 'competition_open_since_month' com 'competition_open_since_year'

        df_1['competition_since'] = df_1[['competition_open_since_year','competition_open_since_month']].apply(lambda x: datetime.datetime(year= x['competition_open_since_year'], month=x['competition_open_since_month'], day=1), axis=1)

        # 2o passo - subtrair as datas de 'date' e 'competition_since' e dividir 30 (granularidade mês)
        df_1['competition_time_month'] = ((df_1['date'] - df_1['competition_since'])/ 30).apply(lambda x: x.days).astype(int)




        # promo2_since (quanto tempo desde a a promoção estar ativa até a data da compra)

        # 1° passo: juntar a coluna 'promo2_since_year' com a coluna 'promo2_since_week' e armazenar em uma nova coluna
        df_1['promo2_since'] = df_1.apply(lambda x: str(x['promo2_since_year']) + '-' + str(x['promo2_since_week']),axis=1)

        # 2° passo: converter 'promo_since' de string para data
        # OBSERVAÇÃO IMPORTANTE: tive que fazer uma adaptação no código.
        # no código original a atribuição é feita sobre todas as linhas da coluna 'promo_since', no entanto o lambda
        # não estava funcionando na coluna 'promo_since' nas linhas com valores zerados '0-0' (proveniente dos valores
        # NA's que foram substituídos por 0 na etapa de preenchimento de NA's) então tive que aplicar a função no df
        # filtrado (df_1['promo_since']!='0-0')
        df_1.loc[df_1['promo2_since']!='0-0','promo2_since'] = df_1.loc[df_1['promo2_since']!='0-0','promo2_since'].apply(lambda x: datetime.datetime.strptime(x+'-1', '%Y-%W-%w') - datetime.timedelta(days=7) )

        # 3° passo: subtrair a data da coluna 'date' da coluna 'promo_since' (criada no passo acima), mantendo o filtro
        # condicional de linhas (df_1['promo_since']!='0-0') a atribuindo a uma nova coluna 'promo_time_week' mantendo
        # o filtro de linhas
        df_1.loc[df_1['promo2_since']!='0-0','promo2_time_week'] = ((df_1.loc[df_1['promo2_since']!='0-0','date'] - df_1.loc[df_1['promo2_since']!='0-0','promo2_since']) / 7).apply(lambda x: x.days).astype(int)

        # 4° passo: os filtros de linha anteriores resultaram apenas em dados preenchidos nas linhas do filtro. As linhas
        # não pertencentes ao filtro foram preenchidas com NA's. Preencher esses valores com 0
        df_1['promo2_time_week'] = df_1['promo2_time_week'].fillna(0)
        
        
        
        # Quando a loja está fechada ('open'==0) a quantidade de vendas e clientes é 0. Eliminar essas linhas.
        # eliminar também as linhas onde não houve vendas (df_2['sales']==0)

        df_1 = df_1[df_1['open']!=0]

        # Eliminar a coluna 'customers' (no momento do modelo em produção a informação sobre a quantidade
        # de clientes na loja não estará disponível).
        # coluna 'open' estará com valor constante (1 - loja aberta)
        # demais colunas são auxiliares

        df_1 = df_1.drop(['open','promo_interval','month_map'], axis=1)      
      
        
        
        return df_1
    
    
    
    def data_preparation(self, df_1):
        
        #train
        X_train = df_1


        # Atributos numéricos escolhidos para o scaling:


        # competition_distance (Robust Scaler)

        # year (MinMax Scaler)

        # competition_time_month (Robust Scaler)

        # promo2_time_week (MinMax Scaler)


        # Para decidir entre MinMaxScaler e RobustScaler os boxplots das variáveis foram inspecionados.
        # para variáveis com outiliers escolheu-se o Robust Scaler e para as demais o MinMax Scaler


        # Scaling com Robust Scaler ('competition_distance' e 'competition_time_month')

        # 'competition_distance'
        
        X_train['competition_distance'] = self.competition_distance_scaler.transform(X_train[['competition_distance']].values)

        

        # 'competition_time_month'

        X_train['competition_time_month'] = self.competition_time_month_scaler.transform(X_train[['competition_time_month']].values)

        




        # Scaling com MinMax Scaler ('year' e 'promo2_time_week')

        # 'year'

        X_train['year'] = self.year_scaler.transform(X_train[['year']].values)

        

        # 'promo2_time_week'

        X_train['promo2_time_week'] = self.promo2_time_week_scaler.transform(X_train[['promo2_time_week']].values)

        


        ## <font color="#808080">Encoding - variáveis categóricas</font>


        # state_holiday (One-Hot encoding)

        X_train = pd.get_dummies(data=X_train, columns=['state_holiday'], prefix=['state_holiday'])




        # store_type (Label encoder)

        X_train['store_type'] = self.store_type_encoder.transform(X_train['store_type'])




        # assortment (Ordinal Encoder)

        assortment_encoding_map = {'basic': 1, 'extended':2, 'extra':3}

        X_train['assortment'] = X_train['assortment'].map(assortment_encoding_map)





        ## <font color="#808080">Transformação de natureza - variáveis de natureza cíclica</font>

        # Atributos de natureza cíclica:

        # day_of_week

        # month

        # day

        # week_of_year

        # Transformando os atributos

        # day

        X_train['day_sin'] = X_train['day'].apply(lambda x: np.sin(x*(2.*np.pi/30))) 
        X_train['day_cos'] = X_train['day'].apply(lambda x: np.cos(x*(2.*np.pi/30)))

        # day_of_week

        X_train['day_of_week_sin'] = X_train['day_of_week'].apply(lambda x: np.sin(x*(2.*np.pi/7)))
        X_train['day_of_week_cos'] = X_train['day_of_week'].apply(lambda x: np.cos(x*(2.*np.pi/7)))


        # month

        X_train['month_sin'] = X_train['month'].apply(lambda x: np.sin(x*(2.*np.pi/12)))
        X_train['month_cos'] = X_train['month'].apply(lambda x: np.cos(x*(2.*np.pi/12)))


        # week_of_year

        X_train['week_of_year_sin'] = X_train['week_of_year'].apply(lambda x: np.sin(x*(2.*np.pi/52)))
        X_train['week_of_year_cos'] = X_train['week_of_year'].apply(lambda x: np.cos(x*(2.*np.pi/52)))
        
        
        # Columns selected for further analysis

        cols_selected = ['store', 
                         'promo', 
                         'store_type', 
                         'assortment', 
                         'competition_distance', 
                         'competition_open_since_month', 
                         'competition_open_since_year', 
                         'promo2_since_week', 
                         'promo2_since_year', 
                         'competition_time_month', 
                         'promo2_time_week', 
                         'day_sin', 
                         'day_cos', 
                         'day_of_week_sin', 
                         'day_of_week_cos',
                         'month_sin',
                         'month_cos',
                         'week_of_year_sin',
                         'week_of_year_cos']
        
        
        
        return X_train[cols_selected]
    
    
    def get_predictions(self, model, test_raw, df_3):
        
        #prediction
        predictions = model.predict(df_3)
        
        #join predictions into the original data        
        test_raw.loc[df_3.index, 'Predictions'] = np.expm1(predictions)
        
        
   
        return test_raw.to_json(orient='records', date_format='iso')    
         

