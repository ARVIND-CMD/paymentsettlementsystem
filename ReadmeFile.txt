Django Setup:
1. Clone the project from the git repository.
git clone ""
2. Run the command in the terminal(make sure requirements.txt lies in the same directory) : pip install -r requirements.txt



MongoDB Setup:
1. Create an account on https://www.mongodb.com/cloud/atlas/register?utm_content=rlsavisitor&utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_general_retarget-brand_gic-null_apac-all_ps-all_desktop_eng_lead&utm_term=cloud%20mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=14412646479&adgroup=131761130852&cq_cmp=14412646479&gad=1&gclid=CjwKCAjwsKqoBhBPEiwALrrqiDDV_k2E63xKyxNpVlTX72dDvJPJ4ttiCBgpAQJCYJsAB05eE7Tt5BoCzFQQAvD_BwE
2. Create the cluster
3. Add username : test_user
4. Its password : BydxRm6az8YZ1lHi
5. You will get the connection string e.g: "mongodb+srv://test_user:<password>@cluster0.nfztvrp.mongodb.net/"
(Replace the password with your own password)
6. Create databae with name : settlement_data
7. Create collection with name : settlement_records

Redis SETUP:
1. pip install django-redis redis

MYSQL SETUP:
1. Install mysql from https://dev.mysql.com/downloads/installer/ 
2. Save the password for the root user.
3. Create one database with name "payment_records"
4. In the paymentsettlesystem/settings.py file change the password to your password
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payment_records',
        'USER': 'root',
        'PASSWORD': 'Ouattwac@4321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
























