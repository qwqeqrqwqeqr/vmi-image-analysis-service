from database.database import Database
from model.image import Image
from database.query.util import set_image_dir_list


# evaluation_code에 맞는 환자의 이미지를 불러옵니다,


def get_patient_image(evaluation_code):
    database = Database()
    query = "SELECT * FROM ans_vmi_dir_crop where eval_code = %s"
    result = database.executeOne(query, evaluation_code)
    image = Image(evaluation_code, set_image_dir_list(result))
    database.close()

    return image









