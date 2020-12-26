import re

text = """Are you plotting the Matrix?
• Are you using proxies?
• Are there any other themes or issues?
• How is the audience relevant to the outcome of the operation?
• How is the environment varied?
• How is the threat equivalent to the threat of a counter-active act?
• How is the experience of violent conflict measured and managed and at what levels of command do various people fall?
• How is the context of the operation defined?
• How is the threat defined?
• What is the gain/loss balance?
• How is the environment varied?
• How is the threat measured and managed?
• How is the environment varied?
• How is the threat measured and managed?
• How is the environment varied?
• How is the threat measured and managed?
• How is the environment varied?
• How is the threat measured and managed?
• How is the environment varied?
• How is the threat measured and managed?"""


def parse_for_tweeter(string):    
    # truncate at last sentance before 250 char
    sentance_list = re.split(r'(?<=[.!?;:\n]) +', string)
    # sentance_list = string.split('.')
    if len(sentance_list[0]) > 249:
            return sentance_list[0][0:249]
    else:
        new_string = ""
        for sentnace in sentance_list:
            if len(new_string) + len(sentnace) <= 250:
                new_string += sentnace + " "
        return new_string

if __name__ == "__main__":
    print(parse_for_tweeter(text))
