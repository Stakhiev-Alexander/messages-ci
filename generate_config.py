import os
from collections import OrderedDict

import messages._config as cfg


PROFILE_NAME = 'integration_tester'

# # ---------------------------------------------------------------------
# Email
data = {
    'from_': os.getenv('EMAIL_EMAIL'),
    'server': 'smtp.gmail.com',
    'port': 465
}
auth = {
    'auth': os.getenv('EMAIL_PASSWORD')
}

cfg.configure_profile(
    msg_type='email',
    profile_name=PROFILE_NAME,
    data=data,
    auth=auth
)


# ---------------------------------------------------------------------
# Telegram
data = {'channel_id': os.getenv('TELEGRAM_CHANNEL_ID')}
auth = {'auth': os.getenv('TELEGRAM_TOKEN')}

cfg.configure_profile(
    msg_type='telegrambot',
    profile_name=PROFILE_NAME,
    data=data,
    auth=auth
)


# ---------------------------------------------------------------------
# Twilio
data = {
    'from_': os.getenv('TWILIO_NUMBER')
}
auth = OrderedDict(
    [
        ("auth_sid", os.getenv('TWILIO_SID')),
        ("auth_token", os.getenv('TWILIO_TOKEN')),
    ]
)

cfg.configure_profile(
    msg_type='twilio',
    profile_name=PROFILE_NAME,
    data=data,
    auth=auth
)


# ---------------------------------------------------------------------
# Whatsapp
data = {
    'from_': os.getenv('WHATSAPP_NUMBER')
}
auth = OrderedDict(
    [
        ("auth_sid", os.getenv('WHATSAPP_SID')),
        ("auth_token", os.getenv('WHATSAPP_TOKEN')),
    ]
)
cfg.configure_profile(
    msg_type='whatsapp',
    profile_name=PROFILE_NAME,
    data=data,
    auth=auth
)
