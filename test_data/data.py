from dataclasses import dataclass
from config_path import *

@dataclass
class BaseData:
    main_url: str = "https://dev.azure.com"
    login_url: str = "https://login.microsoftonline.com/common/oauth2/authorize"
    username: str = USERNAME
    password: str = PASSWORD





