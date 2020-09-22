# Infrastructure Based on Charging Power Consumption
Data Pipeline for prototyping time series algorithms with numerous models
![](Images/EV_Charger_Data_Pipeline.png)


### Data Preprosessing
I could not find a non-stationary charging dataset, so I generated stationary time series dataset from a python script. The dataset is a seasonal dataset with assumption that EV owners will most likely charge their vehicles at 9am (before leaving for work) and 1pm (Break). Using such times as weights and using Gaussian Distributions this stationary dataset was generated.

![](Images/dataset.png)



### Models Used

1) ARIMA Model

![](Images/Arima_model_fit.png)

2) Neural Net (LSTM)
