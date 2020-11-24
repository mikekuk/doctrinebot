import re

text = "the threat from China is on its doorstep, we need to defend ourselves and our territories very effectively. We can't stand idly by and watch as our territory is eroded and our people are displaced."

def parse_for_tweeter(string):
    # truncate at last sentance before 250 char
    sentance_list = string.split('.')
    new_string = ""
    for sentnace in sentance_list:
        if len(sentnace) > 249:
            return sentnace[0:249]
        else:
            if len(new_string) + len(sentnace) <= 250:
                new_string += sentnace + '.'            
            return new_string
    


if __name__ == "__main__":
    print(parse_for_tweeter(text))
