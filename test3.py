from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_access_token = 'EAAM53NanbRoBOZBk0pKWhbv23AzCxZC2gceEZBinIvKVZCqvrL7nKq1UKVwaAMHzVCCOuZBchs4r6XD78mHeMCZAwl3di7McCqRmMOJutSElqcK8ZAsJPIOdN4PWZCG4UDsnK56HaN4yBDlhTxHtMsKn8vlluagzTWJbyLoZCQQSXrTPMYDi40BZAXm7Ubg8XwOqiB9FLfYBsb'
my_ad_account_id = 'act_2590394167795341'
my_app_secret = '8656f6fb3b4dd5f9634e694689023b5e'
my_app_id = '908045587016986'


FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(my_ad_account_id)
campaigns = my_account.get_campaigns()
print(campaigns)
print(my_account)

