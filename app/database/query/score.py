from database.database import Database
from model.score import Score
from database.query.util import check_score_list_length


# evaluation_code에 맞는 환자의 점수를 업데이트 합니다.


def update_patient_score(eval_code, score_list):
    if not check_score_list_length(score_list):
        return False

    database = Database()
    score = Score(eval_code, score_list)

    query = f"""
    REPLACE INTO {'ai_eval_vmi'} (
    eval_code,
    q_4,q_5,q_6,q_7,q_8,
    q_9,q_10,q_11,q_12,q_13,q_14,
    q_15,q_16,q_17,q_18,
    q_19,q_20,q_21,q_22,q_23,q_24,q_25,q_26,q_27,q_28,q_29,q_30,total)
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
     """
    result = database.execute(query,
                              (score.evaluation_code,
                               score.q_4, score.q_5,
                               score.q_6, score.q_7,
                               score.q_8, score.q_9,
                               score.q_10, score.q_11,
                               score.q_12, score.q_13,
                               score.q_14, score.q_15,
                               score.q_16, score.q_17,
                               score.q_18, score.q_19,
                               score.q_20, score.q_21,
                               score.q_22, score.q_23,
                               score.q_24, score.q_25,
                               score.q_26, score.q_27,
                               score.q_28, score.q_29,
                               score.q_30, score.total))
    database.commit()
    database.close()
    return True

    '''
    Test Param
    score_list=[0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0]
    update_patient_score(1,score_list)
    '''
