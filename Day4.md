# Day 4

[Working file](files/customer_complaints.ipynb)

Using some example customer complaint data to bring everything learned so far together.

## Modelling

1. Using the compliaints data set, we will try to predict the next wuarter (13 weeks) and compare that to what actually happened.
2. Used `from statsmodels.tsa.holtwinters import SimpleExpSmoothing` - if using this one, you will get the same value for each forecasted point.
3. Went on to use double and truple (or Holt Winters) methods of forecasting.
4. Played around with the graphs - matplotlib seems easy and straightfoward, but plotly has so much power behind it. Just a bit more verbose to code.
5. Mean Absolute Error (MAE) and RSME testing
6. Learned how to predict future results and plot them on a graph. I think I should now be able to do what I want which was to see predictions and comprare them to actuals over time. 




----------------
[Day 3](Day3.md) | [Day 5](Day5.md)