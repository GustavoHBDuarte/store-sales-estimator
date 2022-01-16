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
<ul>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
  <li><font size="3"><b>Feature - </b> description</font></li><br>
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


<h1>5- Insights</h1>

<br>
<p><font size="3">Paragrafo 1</font></p>

<p><font size="3">Paragrafo 2</font></p>


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
<p><font size="3">As the time events are important for modeling sales, the cross-validation step was carried-out taking into account this important feature. Thus,cross-validation train-test split was performed considering the date of the observations (rows). Test (validation) set had a constant width (6 weeks) starting with later dates compared to training set in which had an earlier variable range  of dates. K-fold cross-validation provided replicates that allowed standard deviation calculation of each metric evaluated (Mean Absolute Error - MAE, Mean Absolute Percentage Error - MAPE, Root Mean Squared Error- RMSE).</font></p><br>


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
<p><font size="3">Parágrafo</font></p>
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

<h1>9- Model performance to business performance</h1>

<br>
<p><font size="3">Parágrafo</font></p>

<h1>10- Model deployment</h1>

<br>
<p><font size="3">Parágrafo</font></p>

<h1>11- Conclusions</h1>

<br>
<p><font size="3">Paragrafo 1</font></p>

<p><font size="3">Paragrafo 2</font></p>


<h1>12- Next steps/Perspectives</h1>

<br>
<p><font size="3">Paragrafo 1</font></p>

<p><font size="3">Paragrafo 2</font></p>
