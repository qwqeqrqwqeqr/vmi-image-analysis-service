'''
image util
'''


def set_image_dir_list(result):
    image_dir_list = [result['a_4'], result['a_5'], result['a_6'],
                      result['a_7'], result['a_8'], result['a_9'],
                      result['a_10'], result['a_11'], result['a_12'],
                      result['a_13'], result['a_14'], result['a_15'],
                      result['a_16'], result['a_17'], result['a_18'],
                      result['a_19'], result['a_20'], result['a_21'],
                      result['a_22'], result['a_23'], result['a_24'],
                      result['a_25'], result['a_26'], result['a_27'],
                      result['a_28'], result['a_29'], result['a_30']]

    return image_dir_list


'''
score util
'''


def check_score_list_length(score_list):
    if len(score_list) == 27:
        return True
    else:
        return False
