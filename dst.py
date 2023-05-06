from UserActType import UserActType

class DST:
    def __init__(self):
        self.state = None
        self.last_user_act = None
        self.last_system_act = None
        self.slots = self.init_slots()

    def update(self, user_act=None):
        act = user_act['act']
        self.last_user_act = act
        if not self.state:
            if act in [UserActType['order'],
                       UserActType['delivery'],
                       UserActType['payment'],
                       UserActType['price']]:
                self.state = act

        for slot, value in user_act['slots']:
            slot = slot.lower()
            value = value.lower()

            self.slots[act][slot] = value

        return self.state

    def get_dialogue_state_tracker_state(self):
        return self.state, self.last_user_act, self.last_system_act, self.slots

    def get_state(self):
        return self.state

    def get_last_user_act(self):
        return self.last_user_act

    def get_last_system_act(self):
        return self.last_system_act

    def get_slots(self):
        return self.slots

    def update_last_user_act(self, new_user_act):
        self.last_user_act = new_user_act

    def update_last_system_act(self, new_system_act):
        self.last_system_act = new_system_act

    def init_slots(self):
        return dict(order={}, delivery={}, payment={}, price={})

