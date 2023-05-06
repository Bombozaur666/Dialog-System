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
        user_act_frame = nlu(user_input)
        if user_act_frame['act'] == UserActType['bye']:
            print('Dziękujemy za skorzystanie z naszych usług')
            break
        dst.update(user_act_frame)
        state, last_user_act, last_system_act, slots = dst.get_dialogue_state_tracker_state()
        system_act_frame = dp.update_system_action(state, last_user_act, last_system_act, slots)
        dst.update_last_system_act(system_act_frame)
        system_response = nlg.generate_response(state, last_user_act, last_system_act, slots, system_act_frame)
        print('BOT:', system_response)
