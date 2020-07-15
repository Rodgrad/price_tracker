# price_tracker-cron-mailgun

Script to check webstore prices with cron automatization or manually on daily base.

If price have dropped, new entry will be saved to file.

#How to use it?

Keep script in folder  /price_tracker/ best placed as home/price_tracker/tracker.py 


Indide tracker.py is List "products", it is where you input your target product urls and price in the manner:

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


And then it will send results to email, with match or null value(null value is just to verify script execution.) 

![GitHub Logo](/email_result_list.png)
Format: ![Alt Text](url)

![GitHub Logo](/email_result.png)
Format: ![Alt Text](url)









