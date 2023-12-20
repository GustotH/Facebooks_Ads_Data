from datetime import datetime, date, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adaccountuser import AdAccountUser
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.campaign import Campaign

account_id = 1133145350148237
app_id = '908045587016986'
app_secret = '8656f6fb3b4dd5f9634e694689023b5e'
access_token = 'EAAM53NanbRoBO3ZAcngIjvNgDULI6uJ8KhfALkzol5mGzwLMZAgZC3y4S1q7prtFzFOVYwCx6soQ8YjVH1s0KPCe95WfHoczZAHKHhp8rYCjy6MVOUdyMvTw17FFSWi48ZCyZBf5T2TTOkbwRdKADuaCY7QXAV7hPZCmDM5fLNg5OugZBChirmwuMREaFxP77C5l'

FacebookAdsApi.init(app_id, app_secret, access_token)

yesterday = date.today() - timedelta(1)

account = AdAccount('act_'+str(account_id))
insights = account.get_insights(fields=[
        AdsInsights.Field.account_id,
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.adset_id,
        AdsInsights.Field.ad_name,
        AdsInsights.Field.ad_id,
        AdsInsights.Field.spend,
        AdsInsights.Field.impressions,
        AdsInsights.Field.clicks,
        AdsInsights.Field.actions,
        AdsInsights.Field.conversions
], params={
    'level': 'ad',
    'time_range': {
        'since':  yesterday.strftime("%Y-%m-%d"),
        'until': yesterday.strftime("%Y-%m-%d")
    },'time_increment': 1
})

print(type(insights))

print(insights[0])

print(len(insights))

for item in insights:
    print(str(item['campaign_name']))



with open('insights.txt', 'w') as f:
    for index, item in enumerate(insights):
        f.write(str(index))
        f.write('\n')
        # print(index, item)

# with open('insights.txt', 'w') as f:
#     f.write(insights)