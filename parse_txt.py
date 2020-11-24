import re

text = """The Royal Logistics Corps is responsible for ensuring that such a plan is formulated, rehearsed and executed by all relevant commands. 'Doctrinal frameworks. UK Armed forces have traditionally used the doctrinal framework to coordinate and describe their military operations. The framework comprises four mutually-relevant and context-dependent planning steps.
a. Joint action is defined as the deliberate use and orchestration of military capabilities and activities to realise specific physical and/or psychological effects. Joint action is planned from the desired outcome back to actions, through objectives and effects, and the effects are then recognised and exploited.
b. Joint action is a unifying doctrine that guides the orchestration and execution of operations whether the task is any combination of fighting, engagement, security, support or support. It is implemented through joint action, normally executed by a single Services or Defence component. The framework is designed to be readjusted and reused for subsequent operations."""

def parse_for_tweeter(string):

    # truncate at last sentance before 250 char
    sentance_list = string.split('.')
    new_string = ""
    for sentnace in sentance_list:
        if len(new_string) + len(sentnace) <= 250:
            new_string += sentnace + '.'
        else:
            return new_string


if __name__ == "__main__":
    print(parse_for_tweeter(text))
