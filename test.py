from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_access_token = 'EAAaD8rGzbZBoBO5BBMl7uZBTVSC7RcLHnCx4MfZAVaX6ZA2hPZBw1O8V1L3rqURnHJs2aZAufIaMb4J5Myb6JnKGdAtwj5Sdy0WFSbIoUBjMeFwGeoxbTK06J2YQBNpp0pLWKw4ZAKSxHdWkYvK9iGLSuBvFf3AkQwqYWZAfFcWN1aBO1oGEPJJ6ZCmcxvZBaKFhrzrt8pVdfa'
my_ad_account_id = 'act_897221598226099'
my_app_secret = '08b0b9eb74647094209f67220bd7cfde'
my_app_id = '1833928246915050'

# my_app_id = '{app-id}'
# my_app_secret = '{appsecret}'
# my_access_token = '{access-token}'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(my_ad_account_id)
campaigns = my_account.get_campaigns()
print(campaigns)

fields = [
]
params = {
  adobjects.Campaign.Field.name : 'Conversions Campaign',
  adobjects.Campaign.Field.configured_status: adobjects.Campaign.Status.paused,
}
campaign = AdAccount(id).create_campaign(fields, params)
