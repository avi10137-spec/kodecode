import logging
from logging_setup import get_loger
# # logging.basicConfig(level=logging.INFO,format="%(levelname)s|%(message)s")
# # logger=logging.getLogger(__name__)
# def process_payment(user_id, amount):
#     logger.info(f"Starting payment for user {user_id}")
#     # print(f'Starting payment for user {user_id}')
#
#     if amount <= 0:
#         logger.error(f"ERROR: Invalid amount")
#        # print('ERROR: Invalid amount')
#         return
#     if amount > 10000:
#         logger.warning(f"WARNING: Large transaction")
#        # print('WARNING: Large transaction')
#     logger.info(f"Payment of {amount} completed for user {user_id}")
#     # print(f'Payment of {amount} completed for user {user_id}')
# # process_payment(315857318,100000)
# # 7
# # logger=logging.getLogger("payment")
# # logger.setLevel(logging.DEBUG)
# # formatter=logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s")
# # file_handler=logging.FileHandler("payment.log",encoding="utf8")
# # file_handler.setFormatter(formatter)
# # logger.addHandler(file_handler)
#
# def process_payment1(user_id, amount):
#     logger.info(f"Starting payment for user {user_id}")
#     # print(f'Starting payment for user {user_id}')
#
#     if amount <= 0:
#         logger.error(f"ERROR: Invalid amount")
#        # print('ERROR: Invalid amount')
#         return
#     if amount > 10000:
#         logger.warning(f"WARNING: Large transaction")
#        # print('WARNING: Large transaction')
#     logger.info(f"Payment of {amount} completed for user {user_id}")
#     # print(f'Payment of {amount} completed for user {user_id}')
# process_payment1(315857318,100000)
# # 8.
#
# def read_config(filepath):
#     # TODO: הוסף DEBUG עם filepath הניסיון לפני
#     logger.debug("try to open file")
#     try:
#         with open(filepath) as f:
#             data = f.read()
#             logger.info(f"the open file in secsesfuli")
#         # TODO: הוסף INFO הצלחה על
#         return data
#     except FileNotFoundError:
#         logger.exception(f"file not exist")
#         # TODO: הוסף exception לוג
#         return None
# read_config("z2.txt")
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# def register_user(email, password, age):
#     has_password=bool(password)
#     logger.info(f'register{email}in  age{age}')
#     if age < 18:
#        logger.info(f'the user{email}conot to login becouse your age{age}')
#        return
#     logger.info('ok email=%s password=%s', email,has_password)
#     logger.info(f'the user{email}entry in secusefuly')
# register_user("avi",123,17)
def get_logger():
    building_loger=get_loger("building loger")
    building_loger.info("its info")
    building_loger.worning("adf")
    building_loger.error("abc")
get_logger()

