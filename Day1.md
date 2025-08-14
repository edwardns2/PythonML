# Day 1

Day 1 was all about setting things up in VSCode and getting a virtual environment created and up and running.

## Virtual Environment

To create a new virtual env, I did the following:

1. VSCode - open Terminal
2. While in the directory run `uv init` and then run `uv run main.py` - this creates the virtual environment
3. Run `source .venv/bin/activate` to activate the virtual env. To deactivate, run `deactivate`.
4. Addes Dependencies / Libraries - For example, to add Pandas, run `uv add pandas numpy ipykernel`
5. Let it rip and off we go.

## GitHub

To add files to the GitHub repo, I ran:

1. `git status` - see the status of the files
2. `git add .` - add files to the staging area
3. `git commit -m "Initial Commit"` 
4. `git remote add origin https://github.com/yourusername/your-repo-name.git`
5. `git branch -M main`
6. `git push -u origin main`

For the next few commits, I just used the Source Control window in VSCode.

Everything seems to be set up and running as it should be - which is a relief.

## Obtaining Data

getting set up with `yfinance` and downloading some daily stock data. Used Apple and Tesla for ease. 

1. Installed `yfinance` through `uv` (`uv add yfinance`)
2. Ran the API to obtain stock data for apple - had to check the docs (`https://ranaroussi.github.io/yfinance/`) on how to do this, but was simple enough in the end.
3. Saved the data to a .csv file just to have something to play around with.

## EDA

1. Imported the cvs from above into a pandas dataframe. 
2. `stock_df.info()` - snapshot of the columns and data
3. `stock_df.describe()` - snapshot of some data stats
4. `stock_df.head()` / `stock_df.head()` - First / Last rows of the data
5. `stock_df.isna().sum()` - see how many na / null values in the data set. Got none, as expected. 
6. Did some Visual representations of the data 

I am not a big fan of how the numbers are presented so I ran `pd.set_option('display.float_format', lambda x: '{:,.2f}'.format(x))` to make my life a little easier as we start.

----------------
[Day 2](Day2.md)





