from database.database import Database
from model.image import Image
from database.query.util import set_image_dir_list, map_to_dir


# evaluation_code에 맞는 환자의 이미지를 불러옵니다,


def get_patient_image(evaluation_code):
    database = Database()
    query = "SELECT * FROM ai_ans_vmi_dir_crop where eval_code = %s"
    result = database.executeOne(query, evaluation_code)
    image = Image(evaluation_code, set_image_dir_list(result))
    database.close()

    return image


def set_patient_image(evaluation_code):
    database = Database()
    query = f"""
      REPLACE INTO {'ai_ans_vmi_dir_crop'} (
      eval_code,
      a_4,a_5,a_6,a_7,a_8,
      a_9,a_10,a_11,a_12,a_13,a_14,
      a_15,a_16,a_17,a_18,
      a_19,a_20,a_21,a_22,a_23,a_24,a_25,a_26,a_27,a_28,a_29,a_30)
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
       """
    result = database.execute(query,
                              (evaluation_code,
                               map_to_dir(evaluation_code,4),
                               map_to_dir(evaluation_code,5),
                               map_to_dir(evaluation_code, 6),
                               map_to_dir(evaluation_code, 7),
                               map_to_dir(evaluation_code, 8),
                               map_to_dir(evaluation_code, 9),
                               map_to_dir(evaluation_code, 10),
                               map_to_dir(evaluation_code, 11),
                               map_to_dir(evaluation_code, 12),
                               map_to_dir(evaluation_code, 13),
                               map_to_dir(evaluation_code, 14),
                               map_to_dir(evaluation_code, 15),
                               map_to_dir(evaluation_code, 16),
                               map_to_dir(evaluation_code, 17),
                               map_to_dir(evaluation_code, 18),
                               map_to_dir(evaluation_code, 19),
                               map_to_dir(evaluation_code, 20),
                               map_to_dir(evaluation_code, 21),
                               map_to_dir(evaluation_code, 22),
                               map_to_dir(evaluation_code, 23),
                               map_to_dir(evaluation_code, 24),
                               map_to_dir(evaluation_code, 25),
                               map_to_dir(evaluation_code, 26),
                               map_to_dir(evaluation_code, 27),
                               map_to_dir(evaluation_code, 28),
                               map_to_dir(evaluation_code, 29),
                               map_to_dir(evaluation_code, 30)))
    database.commit()
    database.close()
    return True


