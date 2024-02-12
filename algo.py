# package import statement
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger

api_key = 'AbDrcREU '
username = 'SMHJA1042'
pwd = '1435'
smartApi = SmartConnect(api_key)
try:
    token = "6XFPBPRHK5SM4QH5AJ53EM3JB4"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

correlation_id = "abcde"
data = smartApi.generateSession(username, pwd, totp)

if data['status'] == False:
    logger.error(data)
    
else:
    # login api call
    # logger.info(f"You Credentials: {data}")
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    # fetch the feedtoken
    feedToken = smartApi.getfeedToken()
    # fetch User Profile
    res = smartApi.getProfile(refreshToken)
    smartApi.generateToken(refreshToken)
    res=res['data']['exchanges']

   

    #Historic api
    try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": "14366",
        "interval": "ONE_MINUTE",
        "fromdate": "2024-01-25 09:15", 
        "todate": "2024-01-25 09:20"
        }
        print(smartApi.getCandleData(historicParam))
    except Exception as e:
        logger.exception(f"Historic Api failed: {e}")
   


