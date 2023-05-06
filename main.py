from UserActType import UserActType
from nlu import nlu
from dst import DST
from dp import DP
from nlg import NLG

if __name__ == '__main__':

    dst = DST()
    dp = DP()
    nlg = NLG()

    print("Witamy w restauracji πzza. W czym mogę pomóc?")

    while True:
        user_input = input("$")
        # get user act frame from user input with Natural Language Understanding
        user_act_frame = nlu(user_input)
        # print('NLU', user_act_frame)
        # update Dialogue State Tracker with new user act frame
        dst.update(user_act_frame)
        state, last_user_act, last_system_act, slots = dst.get_dialogue_state_tracker_state()
        # print('state', state)
        # print('last_user_act', last_user_act)
        # print('last_system_act', last_system_act)
        # print('slots', slots)

        # get system act frame which decides what's next from Dialogue Policy
        system_act_frame = dp.update_system_action(state, last_user_act, last_system_act, slots)
        dst.update_last_system_act(system_act_frame)
        # print('system_act_frame', system_act_frame)

        # generate response based on system act frame
        system_response = nlg.generate_response(state, last_user_act, last_system_act, slots, system_act_frame)
        print('BOT:', system_response)

        if user_act_frame['act'] == UserActType['bye']:
            break
