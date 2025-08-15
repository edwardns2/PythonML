# Day 3

[Working file](files/apple_stock.ipynb)

A bit of tidying up and adding a couple of new things.

1. Added some rolling averages to the data set. Should really have throught of this one in the initial EDA section. 
2. Find out that can just use `.plot()` to show a quick graph of the data.
3. Added daily returns to the data set `aapl_df["daily_returns"] = aapl_df["Close"].pct_change() * 100`. 
4. Had a wuick peek at the `corr()` to see if the volume and price was correlated - it was not.

## Seasonal Decomposition

- Trend
- Seasonality (additive / multiplicative)
- Error (what is not explained by trend or seasonality)

1. Used `statsmodels` to easily show some seasonality on a monthly and quarterly basis.




----------------
[Day 2](Day2.md) | [Day 4](Day4.md)