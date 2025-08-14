# Day 2

Day 2 was about data transformation through grouping and filtering.

## Grouping

1. Used the groupby functionality ont he Date columns I added in. Can use a single ref or a combination `aapl_df.groupby(["Year", "Month"]).mean().drop(columns=["Day"])`
2. Realised that you can actually achieve the same without having the need to add in the helper columns through `pd.Grouper` - `aapl_df.groupby([pd.Grouper(freq="ME")]).mean().drop(columns=["Year", "Month", "Day"])`
3. The realised you can actually do it even simpler with `resample` - `aapl_df.resample("ME").mean().drop(columns=["Year", "Month", "Day"])`

## Filtering

1. Looked at different ways to filter data based on either the helper columns or the index DateTime column. 
2. Looked at how you can stack different conditions and also used loc second argument to only select a particular column.

## Combining

1. Combined the above grouping and filtering to transform the data from daily from 1980, to monthly / yearly, from 2020s.


----------------
[Day 1](Day1.md) | [Day 3](Day3.md)