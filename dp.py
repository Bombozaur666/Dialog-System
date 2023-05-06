from SystemActType import SystemActType
from UserActType import UserActType


class DP:
    def update_system_action(self, state, last_user_act, last_system_act, slots):
        if state == UserActType['order']:
            if 'kind' not in slots[state]:
                return {'act': SystemActType['request'], 'slot': 'kind'}
            elif 'size' not in slots[state]:
                return {'act': SystemActType['request'], 'slot': 'size'}
            elif 'plates' not in slots[state]:
                return {'act': SystemActType['request'], 'slot': 'plates'}
            else:
                return {'act': SystemActType['confirm_domain']}

        else:
            if last_user_act == UserActType['hello']:
                return {'act': SystemActType['welcomemsg']}
            elif last_user_act == UserActType['bye']:
                return {'act': SystemActType['bye']}
            else:
                return {'act': SystemActType['canthelp']}




