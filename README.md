# price_tracker-cron

Script to check price manually or with crontab on daily basis from webstore.
If price have dropped, new entry will be saved to file.

How to use it?

List "products" is where you input your target product url and price in the manner:

products = [
    [url, price],
    [url, price]
]


To setup script with crontab start terminal and enter:
> crontab -e

It will open config file, where we need to define our job.
Enter path to your Python version and to script tracker.

>
> 0 * * * *  /usr/bin/python3.8 ./price_tracker/tracker.py   

...And save it, this will check lowest price for products at every hour on every day in year.

Check your cron jobs with:

>crontab -l





