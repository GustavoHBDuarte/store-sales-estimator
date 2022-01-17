<h1><b><font color="#cc0000"><i>Store sales estimator</i></font></b></h1>





<h1>1- Overview and business problem</h1>

<br>
<p><font size="3">Rossmann operates over 3,000 drug stores in 7 European countries.</br> 
Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance.</br> Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 
</br>With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.</font></p>

<p><font size="3">For this purpose a machine learning model was implemented aimed to forecast daily sales for six weeks. The corresponding model was further sucessifully deployed in order to provide predictions to be consumed by a Telegram bot.</font></p>

<p><font size="3"><b>Disclaimer:</b> The business context herein presented is fictitious and was used only for the purpose of the development of this project.</font></p>


<p><font size="3">Datasets used in this project can be downloaded <a href="https://www.kaggle.com/c/rossmann-store-sales/data">here</a>.</font></p>









<h1>2- Assumptions</h1>

<br>
<ul>
  <li><font size="3">The information regarding the days where stores were closed were not considered.</font></li>
<br>
  <li><font size="3">For the rows where competition distance information was not available it was filled with a distance value higher than the longest distance of the dataset.</font></li>
<br>
  <li><font size="3">Rows with sales == 0 were not considered.</font></li>
</ul>






<h1>3- Data description</h1>

<br>
  <font size="3">The dataset used to build the solution has the following attributes:</font></li>
<br>
<br>
<ul>
  <li><font size="3"><b>Id - </b>an Id that represents a (Store, Date) duple within the test set</font></li><br>
  <li><font size="3"><b>Store - </b>a unique Id for each store</font></li><br>
  <li><font size="3"><b>Sales - </b>the turnover for any given day (this is what you are predicting)</font></li><br>
  <li><font size="3"><b>Customers - </b>the number of customers on a given day</font></li><br>
  <li><font size="3"><b>Open - </b>an indicator for whether the store was open: 0 = closed, 1 = open</font></li><br>
  <li><font size="3"><b>StateHoliday - </b>indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None</font></li><br>
  <li><font size="3"><b>SchoolHoliday - </b>indicates if the (Store, Date) was affected by the closure of public schools</font></li><br>
  <li><font size="3"><b>StoreType - </b>differentiates between 4 different store models: a, b, c, d</font></li><br>
  <li><font size="3"><b>Assortment - </b>describes an assortment level: a = basic, b = extra, c = extended</font></li><br>
  <li><font size="3"><b>CompetitionDistance - </b>distance in meters to the nearest competitor store</font></li><br>
  <li><font size="3"><b>CompetitionOpenSince[Month/Year] - </b>gives the approximate year and month of the time the nearest competitor was opened</font></li><br>
  <li><font size="3"><b>Promo - </b>indicates whether a store is running a promo on that day</font></li><br>
  <li><font size="3"><b>Promo2 - </b>Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating</font></li><br>
  <li><font size="3"><b>Promo2Since[Year/Week] - </b>describes the year and calendar week when the store started participating in Promo2</font></li><br>
  <li><font size="3"><b>PromoInterval - </b>describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store</font></li><br>
</ul>








<h1>4- Solution strategy</h1>

<br>
<ol>
  <li><font size="3"><b>Understanding the business and problems to be solved:</b> search for the real reasons for the need for sales forecasting and how the problem can be solved through machine learning, which aspects should be considered at the time of prediction and how better the proposal can be considering the models of prediction currently being used in the company.</font></li>
<br>
  <li><font size="3"><b>Data colection:</b> downloading the corresponding .csv files from <a href="https://www.kaggle.com/c/rossmann-store-sales/data">Kaggle</a> plattform.</font></li>
<br>
  <li><font size="3"><b>Data cleaning:</b> basic search for missing values, outliers and inconsistencies to make data suitable for further analysis. Adittionally a basic inspection including descriptive statistics (mean, standard deviation, range, skewness and kurtosis) should be also carried out.</font></li>
<br>
  <li><font size="3"><b>Feature engineering:</b> creating new features from the existing ones to assist in both exploratory data analysis (EDA) and machine learning modelling.</font></li>
<br>
  <li><font size="3"><b>Data filtering and selection:</b>  reducing the data based on business assumptions and constraints to make training set as close as possible to data in production.</font></li>
<br>
  <li><font size="3"><b>EDA:</b> exploring data to search for interesting insights and understand the impact of the features on the target variable (sales).</font></li>
<br>
  <li><font size="3"><b>Data preparation:</b> splitting the data into train/test sets and applying them scaling, encoding and transformation methods to make data suitable to machine learning.</font></li>
<br>
  <li><font size="3"><b>Feature selection:</b> selecting the most relevant attributes based on EDA results and suitable algorithm to maximize machine learning performance.</font></li>
<br>
  <li><font size="3"><b>Machine learning:</b> evaluating different algorithms (both linear and non-linear) and compare their results based on cross-validation. For the sake of this step a good candidate algorithm should perform better than the average-based baseline estimator.</font></li>
<br>
  <li><font size="3"><b>Hiperparameter fine tuning:</b> randomly test different hyperparameter values in order to find some combination that improves model performance.</font></li>
<br>
  <li><font size="3"><b>Error interpretation:</b> after choosing the best performing model, in the next step model performance needs to be translated to business results.</font></li>
<br>
  <li><font size="3"><b>Model deployment:</b> deploying the machine learning model to cloud environment so predictions can be accessed via API requests. After finishing deployment a Telegram bot is implemented to ease access to sales predictions by store number.</font></li>
<br>  
</ol>







<h1>5- Main insights</h1>

<br>
<p><font size="3">Stores with closer competitors should sell less. <b>False</b>.</font></p>


<a href="https://drive.google.com/uc?export=view&id=11jdfbBhiB-jb58-P6uAVvH4tB6p0az-Y"><img src="https://drive.google.com/uc?export=view&id=11jdfbBhiB-jb58-P6uAVvH4tB6p0az-Y" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />


<p><font size="3">Stores with larger assortments should sell more. <b>False</b>.</font></p>

<a href="https://drive.google.com/uc?export=view&id=1rZUqxyCtPqRasf-bZocgq9VZnfoL4m4d"><img src="https://drive.google.com/uc?export=view&id=1rZUqxyCtPqRasf-bZocgq9VZnfoL4m4d" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    
    

<p><font size="3">Stores should sell more over the years. <b>False</b>.</font></p>


<a href="https://drive.google.com/uc?export=view&id=1KIo6-SSSvKYsmyLyQKruOJwH1mRwUL8P"><img src="https://drive.google.com/uc?export=view&id=1KIo6-SSSvKYsmyLyQKruOJwH1mRwUL8P" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    


    
    
    
<h1>6- Machine Learning models</h1>

<br>
<p><font size="3">Models evaluated:</font></p>


<ul>
  <li><font size="3">Average (baseline)</font></li>
  <li><font size="3">Linear Regression</font></li>
  <li><font size="3">LASSO</font></li>
  <li><font size="3">Random Forest</font></li>
  <li><font size="3">XGBoost</font></li>
</ul>






<h1>7- Machine Learning performance</h1>

<br>
<p><font size="3">As the time events are important for modeling sales, the cross-validation step was carried-out taking into account this important feature. Thus, cross-validation train-test split was performed considering the date of the observations (rows). Test (validation) set had a constant width (6 weeks) starting with later dates compared to training set in which had an earlier variable range  of dates. K-fold cross-validation provided replicates that allowed standard deviation calculation of each metric evaluated (Mean Absolute Error - MAE, Mean Absolute Percentage Error - MAPE, Root Mean Squared Error- RMSE).</font></p><br>


<table border="1">
   <thead>
   <tr>
       <th><font size="3">Model name</font></th>
       <th><font size="3">MAE CV</font></th>
       <th><font size="3">MAPE CV</font></th>
       <th><font size="3">RMSE CV</font></th>
   </tr>
   </thead>
   <tbody>
   <tr>
       <td><font size="3">Random Forest</font></td>
       <td><font size="3">870.03 +/- 235.79</font></td>
       <td><font size="3">0.12 +/- 0.03</font></td>
       <td><font size="3">1314.54 +/- 344.19</font></td>
   </tr>
   <tr>
       <td><font size="3">XGBoost</font></td>
       <td><font size="3">1053.97 +/- 192.91</font></td>
       <td><font size="3">0.15 +/- 0.02</font></td>
       <td><font size="3">1509.89 +/- 268.02</font></td>
   </tr>
          <tr>
       <td><font size="3">Linear Regression</font></td>
       <td><font size="3">2105.49 +/- 303.38</font></td>
       <td><font size="3">0.31 +/- 0.02</font></td>
       <td><font size="3">2974.22 +/- 492.6</font></td>
   </tr>   
   </tbody>
   <tfoot>
       <td><font size="3">LASSO</font></td>
       <td><font size="3">2384.25 +/- 391.74</font></td>
       <td><font size="3">0.34 +/- 0.01</font></td>
       <td><font size="3">3356.23 +/- 556.83</font></td>
   </tfoot>
</table>


<br>
<p><font size="3">Although Random Forest was the best performing algorithm XGBoost also had a satisfactory besformance and was selected due to its less required space in cloud server to implement model deployment, resulting in an overall cost reduction.</font>

    
    
    
    

<h1>8- Hyperparameter fine tuning</h1>

<br>
<p><font size="3">Model hyperparameters were adjusted via fine tuning in order to improve model performance.The following table shows the metrics for the XGBoost tuned model:</font></p>
<br>

<table border="1">
   <thead>
   <tr>
       <th><font size="3">Model name</font></th>
       <th><font size="3">MAE</font></th>
       <th><font size="3">MAPE</font></th>
       <th><font size="3">RMSE</font></th>
   </tr>
   </thead>
   <tbody>
   <tr>
       <td><font size="3">XGBoost</font></td>
       <td><font size="3">1022.562838</font></td>
       <td><font size="3">0.144234</font></td>
       <td><font size="3">1454.073855</font></td>
   </tr>         
   </tbody>
</table>

<br>
<p><font size="3">Basic interpretation of model results:</font></p>
<br>

<ul>
  <li><font size="3"><b>MAE - </b>the model has an average error value of €1022.56.</font></li><br>
  <li><font size="3"><b>MAPE - </b>for each predicted value of the model it can underestimate or overestimate the result by 14%.</font></li><br>  
  <li><font size="3"><b>RMSE - </b>presents an average error of €1454.07 units, however this metric is more sensitive to outliers and, therefore, when this metric is significantly different from the MAE, other adjustments must be made to the data. However, RMSE was used as an indicador of improvement for the model.</font></li><br>
</ul>

<p><font size="3">In the following figure it is possible to visualize some interesting aspects for the trained model including mainly model predictions against true values, as well as residuals distribution where it is possible to see a gaussian distribution and the apparent evenlly distributed error of predictions.</font></p>
<br>

<a href="https://drive.google.com/uc?export=view&id=1ils8TLxWYtvTOdEHcqgX9MGP9sNO_x_1"><img src="https://drive.google.com/uc?export=view&id=1ils8TLxWYtvTOdEHcqgX9MGP9sNO_x_1" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />


    
    
    
    
    


<h1>9- Model performance to business performance</h1>

<br>
<p><font size="3">In business terms, MAE means how wrong the forecast is by setting upper and lower limits. MAPE means the percentage in which the predicted values differs from the target values, being, therefore, a metric that is easily interpreted.
The following table shows, based on MAE values, worst and best scenarios by store (where worst_scenario field is calculated by subtracting the MAE from the predictions field and the best_scenario field is calculated by adding the MAE field). It is easy to visualize that some stores are more challenging to predict (first rows) while others (last rows) are easier.</font></p>
<br>

<table border="1">
   <thead>
   <tr>
       <th><font size="3">store</font></th>
       <th><font size="3">predictions</font></th>
       <th><font size="3">worst_scenario</font></th>
       <th><font size="3">best_scenario</font></th>
       <th><font size="3">MAE</font></th>
       <th><font size="3">MAPE</font></th>
   </tr>
   </thead>
   <tbody>
   <tr>
       <td><font size="3">663</font></td>
       <td><font size="3">102145.570312</font></td>
       <td><font size="3">-24309.859375</font></td>
       <td><font size="3">228601.00000</font></td>
       <td><font size="3">126455.429688</font></td>
       <td><font size="3">0.553171</font></td>
   </tr>
   <tr>
       <td><font size="3">815</font></td>
       <td><font size="3">349864.468750</font></td>
       <td><font size="3">235080.000000</font></td>
       <td><font size="3">464648.93750</font></td>
       <td><font size="3">114784.468750</font></td>
       <td><font size="3">0.488278</font></td>
   </tr>
   <tr>
       <td><font size="3">192</font></td>
       <td><font size="3">256070.718750</font></td>
       <td><font size="3">24143.437500</font></td>
       <td><font size="3">487998.00000</font></td>
       <td><font size="3">231927.281250</font></td>
       <td><font size="3">0.475263</font></td>
   </tr>
   <tr>
       <td><font size="3">722</font></td>
       <td><font size="3">403444.906250</font></td>
       <td><font size="3">279296.000000</font></td>
       <td><font size="3">527593.81250</font></td>
       <td><font size="3">124148.906250</font></td>
       <td><font size="3">0.444507</font></td>
   </tr>
   <tr>
       <td><font size="3">839</font></td>
       <td><font size="3">199839.156250</font></td>
       <td><font size="3">138649.000000</font></td>
       <td><font size="3">261029.31250</font></td>
       <td><font size="3">61190.156250</font></td>
       <td><font size="3">0.441331</font></td>
   </tr>
   <tr>
       <td><font size="3">...</font></td>
       <td><font size="3">...</font></td>
       <td><font size="3">...</font></td>
       <td><font size="3">...</font></td>
       <td><font size="3">...</font></td>
       <td><font size="3">...</font></td>
   </tr>
   <tr>
       <td><font size="3">14</font></td>
       <td><font size="3">198669.140625</font></td>
       <td><font size="3">198522.000000</font></td>
       <td><font size="3">198816.28125</font></td>
       <td><font size="3">147.140625</font></td>
       <td><font size="3">0.000741</font></td>
   </tr>
   <tr>
       <td><font size="3">644</font></td>
       <td><font size="3">334179.156250</font></td>
       <td><font size="3">334015.312500</font></td>
       <td><font size="3">334343.00000</font></td>
       <td><font size="3">163.843750</font></td>
       <td><font size="3">0.000490</font></td>
   </tr>
   <tr>
       <td><font size="3">17</font></td>
       <td><font size="3">221930.796875</font></td>
       <td><font size="3">221844.593750</font></td>
       <td><font size="3">222017.00000</font></td>
       <td><font size="3">86.203125</font></td>
       <td><font size="3">0.000388</font></td>
   </tr>
   <tr>
       <td><font size="3">984</font></td>
       <td><font size="3">228221.359375</font></td>
       <td><font size="3">228152.000000</font></td>
       <td><font size="3">228290.71875</font></td>
       <td><font size="3">69.359375</font></td>
       <td><font size="3">0.000304</font></td>
   </tr>
   </tbody>
   <tfoot>
       <td><font size="3">748</font></td>
       <td><font size="3">209883.546875</font></td>
       <td><font size="3">209840.000000</font></td>
       <td><font size="3">209927.09375</font></td>
       <td><font size="3">43.546875</font></td>
       <td><font size="3">0.000208</font></td>
   </tfoot>
</table>
<br>

<br>
<p><font size="3">An overall view of MAE errors by store is shown in the following figure:</font></p>
<br>
    
<a href="https://drive.google.com/uc?export=view&id=1i0xh3FK-8t8VeMPgS3FqhhFaP75DOZIj"><img src="https://drive.google.com/uc?export=view&id=1i0xh3FK-8t8VeMPgS3FqhhFaP75DOZIj" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

    




<h1>10- Model deployment</h1>

<br>

<ul>
  <li><font size="3">Machine learning model was successfully deployed on Heroku cloud.Telegram bot can be accessed by clicking here: <a href="https://t.me/gustavo_rossmann_telegram_bot">t.me/gustavo_rossmann_telegram_bot</a>.</font>
      
<font size="3">To access bot predictions the user should start a chat sending a message with the store number. If the store number exists the bot will return estimated sales for the next 6 weeks, if it does not the chat will return an error message.</font>
</ul>    
    

<a href="https://drive.google.com/uc?export=view&id=17Db186L4t11K0AfBwNma_hfsrTCyGzNI"><img src="https://drive.google.com/uc?export=view&id=17Db186L4t11K0AfBwNma_hfsrTCyGzNI" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    
    
    
    
    
    

<h1>11- Conclusions</h1>

<br>
<p><font size="3">Althought the presented results is far from the best that could be achieved and there is room for model improvements decreasing its corresponding error, the proposed solution reached satisfactory results performing better than average-based sales prediction satisfying the needs of the business problem. </font></p>
<br>

    
    
    
    
<h1>12- Next steps/Perspectives</h1>

<br>
   
    
<ul>
  <li><font size="3">Develop other commands for the bot, such as showing the total sales for some specific date (within the 6 week period covered by the forecast).</font></li><br>
  <li><font size="3">Integrate sales forecasting with data visualization tools (Power BI, Tableau, etc).</font></li><br>
  <li><font size="3">Work on model improvements to reduce error metrics.</font></li>
</ul
