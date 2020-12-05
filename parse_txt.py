import re

text = "the threat from China is on its doorstep, \n we need to defend ourselves and our territories very effectively. We can't stand idly by and watch as our territory is eroded and our people are displaced."

def parse_for_tweeter(string):    
    # truncate at last sentance before 250 char
    sentance_list = re.split(r'(?<=[.!?;\n]) +', string)
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
