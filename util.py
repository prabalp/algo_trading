from fyers_api import accessToken


def send_email():
    client_id="KPQVRS7JKZ-100"
    secret_key="V6KIXYPM5V"
    # redirect_uri="https://trade.fyers.in/api-login/redirect-uri/index.html"
    redirect_uri="http://43.204.35.208/"

    response_type="code"
    grant_type="authorization_code"
    state=""
    scope=""
    nonce=""


    session=accessToken.SessionModel(client_id=client_id,
    secret_key=secret_key,redirect_uri=redirect_uri, 
    response_type=response_type, grant_type=grant_type)

    response = session.generate_authcode()