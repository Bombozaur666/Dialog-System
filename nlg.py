from SystemActType import SystemActType
from UserActType import UserActType


class NLG:
    def generate_response(self, state, last_user_act, last_system_act, slots, system_act):
        if state == UserActType['order']:
            if system_act['act'] == SystemActType['request']:
                if system_act['slot'] == 'kind':
                    return 'Jaką pizzę chcesz zamówić?'
                elif system_act['slot'] == 'size':
                    return 'Jakiego rozmiaru chcesz pizzę?'
                elif system_act['slot'] == 'plates':
                    return 'Dla ilu osób ma to być?'
            elif system_act['act'] == SystemActType['confirm_domain']:
                return 'Czy mam dodać tę pizzę do zamówienia?\nPizza: {}\nRozmiar: {}\nIlość osób: {}'.\
                    format(slots['order']['kind'], slots['order']['size'], slots['order']['plates'])
        elif last_user_act == UserActType['hello']:
            return 'Dzień dobry, w czym mogę pomóc?'
        else:
            return 'Przepraszam. Zdanie nie jest mi zrozumiałe. Spróbuj je sformułować w inny sposób.'