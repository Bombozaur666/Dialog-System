acts_list = {'hello': 'welcomemsg',
             'null': 'canthear'}


class Act_frame:
    text = ''
    act = []


class Dialogue_state_frame:
    state_frame = []


def NLU(text):
    user_frame = Act_frame()
    user_frame.text = text
    if text == 'Cześć, jak masz na imię?':
        user_frame.act = 'hello'
        print(user_frame.act)
    else:
        user_frame.act = 'null'
        print(user_frame.act)
    return user_frame


def DST(user_frame):
    dialogue_frame = Dialogue_state_frame()
    dialogue_frame.state_frame.append((user_frame.text, user_frame.act))
    print(dialogue_frame.state_frame)
    return dialogue_frame


def DP(dialogue_frame):
    system_frame = Act_frame()
    system_frame.act = acts_list[dialogue_frame.state_frame[-1][1]]
    print(system_frame.act)
    return system_frame


def NLG(system_frame):
    answer = ''
    if system_frame.act == 'welcomemsg':
        answer = 'Witaj, nazywam się Igrek Iksiński.'
    elif system_frame.act == 'canthear':
        answer = 'Nie zrozumiałem.'
    return answer


text = 'Cześć, jak masz na imię?'
#text = 'Niezrozumiałe'
print(NLG(DP(DST(NLU(text)))))