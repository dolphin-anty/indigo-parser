from library import Indigo, Dolphin
from config import INDIGO_TOKEN, INDIGO_PORT, DOLPHIN_TOKEN
from datetime import datetime
from termcolor import colored

indigo = Indigo(INDIGO_TOKEN, INDIGO_PORT)
indigo_profiles = indigo.get_profiles()
for profile in indigo_profiles['value']:
    indigo_profile_data_dict = indigo.get_profile_info(profile['uuid'])
    dolphin = Dolphin(DOLPHIN_TOKEN)
    response = dolphin.create_profile(indigo_profile_data_dict)
    if response['success'] == 1:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Profile {indigo_profile_data_dict["name"]} - '
              f'{colored("successfully created", "green")}')
    else:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Profile {indigo_profile_data_dict["name"]} - '
              f'{colored("Opps! Something went wrong!", "red")}')

print(f'\n\n{colored("Congratulations! Migration process successfully completed!", "green")}')
