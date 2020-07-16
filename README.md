# PriceTracker with cron and Mailgun

Script to check webstore prices by cron automatization or manually at chosen time.

If price have dropped, new entry will be saved to file and sent to email address.

# How to use it?

Keep script in folder  /price_tracker/ best placed as home/user/price_tracker/tracker_public.py .

Inside tracker_public.py is List "products", it is where you input your target product urls and price in the manner:

>products = [
>    [url, price],
>    [url, price]
>]


# Price_tracker-cron

To setup script with crontab start terminal and enter:
> crontab -e

It will open config file, where we need to define our job.

Enter path to your Python version and to script tracker.

>
> 0 * * * *  /usr/bin/python3.8 ./price_tracker/tracker_public.py   

...And save it, this will check lowest price for products at every hour on every day in year.

Check your cron jobs with:
>crontab -l

# File and MailGun 

On first match it will create file price_tracker.html, we use this file to compare current data with data in file so
we avoid duplicates.


And then it will send results to email, with match or null value(null value is just to verify script execution.) 

![GitHub Logo](/email_result_list.png)
Format: ![Alt Text](url)

![GitHub Logo](/email_result.png)
Format: ![Alt Text](url)



And this is how it looks in file price_tracker.html, I chose .html file to keep browser only app I need to check all data.

![GitHub Logo](/price_tracker_file.png )
Format: ![Alt Text](url)








