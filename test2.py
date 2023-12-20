
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

# access_token = '<ACCESS_TOKEN>'
# app_secret = '<APP_SECRET>'
# app_id = '<APP_ID>'
# id = '<AD_ACCOUNT_ID>'

access_token = 'EAAaD8rGzbZBoBO5BBMl7uZBTVSC7RcLHnCx4MfZAVaX6ZA2hPZBw1O8V1L3rqURnHJs2aZAufIaMb4J5Myb6JnKGdAtwj5Sdy0WFSbIoUBjMeFwGeoxbTK06J2YQBNpp0pLWKw4ZAKSxHdWkYvK9iGLSuBvFf3AkQwqYWZAfFcWN1aBO1oGEPJJ6ZCmcxvZBaKFhrzrt8pVdfa'
id = 'act_897221598226099'
app_secret = '08b0b9eb74647094209f67220bd7cfde'
app_id = '1833928246915050'


FacebookAdsApi.init(access_token=access_token)

fields = [
]

params = {
  'name': 'My campaign',
  'objective': 'OUTCOME_TRAFFIC',
  'status': 'PAUSED',
  'special_ad_categories': [],
}

print(AdAccount(id).create_campaign(
    fields=fields,
    params=params,
    )
)

