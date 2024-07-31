# from sqlalchemy import func
from hr.app.models.Department import Department
from sqlalchemy.orm import scoped_session
# from hr.app.db import db
# from hr.app.models.BloodDonation import BloodDonation
from sqlalchemy.exc import SQLAlchemyError

class departmentRepository:
    @staticmethod
    def add_department_into_db(session:scoped_session, args:dict):
        try:
            result = Department(**args)
            session.add(result)
            session.commit()
            session.refresh(result)
            return result
        except SQLAlchemyError as e:
            session.rollback()
            raise  
        finally:
            session.remove()
    @staticmethod
    def get_department_by_id_from_db(session:scoped_session,args:dict):
        res = session.query(Department).filter(Department.department_id==args.get("department_id")).first()
        return res   
    

    @staticmethod
    def get_all_departments_from_db(session:scoped_session):
        res = session.query(Department).all()
        return res

    @staticmethod
    def update_the_department(session:scoped_session,check_department:object,args:dict):
        try:
            check_department.name = args.get("name")
            update = session.flush() 
            # session.commit()  
            return True
        except SQLAlchemyError as e:
            session.rollback()
            raise









#     @staticmethod
#     def get_single_bb_byid(session, args):
#         res = (
#             session.query(BloodBank)
#             .filter(BloodBank.BloodBankID == args.get("BloodBankID"))
#             .first()
#         )
#         return res

#     staticmethod

#     def update_bb_todb(session, args, bk):
#         bk.BloodBankName = args.get("BloodBankName")
#         bk.Location = args.get("Location")
#         bk.Email = args.get("Email")
#         bk.ContactNumber = args.get("ContactNumber")
#         session.commit()
#         res = (
#             session.query(BloodBank)
#             .filter(BloodBank.BloodBankID == args.get("BloodBankID"))
#             .first()
#         )
#         return res

#     @staticmethod
#     def getting_all_bb(session):
#         res = session.query(BloodBank).all()
#         return res

#     @staticmethod
#     def geting_available_bloods(session, args):
#         # breakpoint()
#         # res = (
#         #     session.query(BloodBank)
#         #     .filter(BloodBank.BloodBankName == args.get("BloodBankName"))
#         #     .first()
#         # )
#         # # bd = res.blooddonations
#         # # main = (
#         # #     session.query(res.blooddonations.BloodType, func.count(res.blooddonations.DonationID))
#         # #     .group_by(res.blooddonations.BloodType)
#         # #     .all()
#         # # )
#         # main = (
#         #     session.query(BloodDonation.BloodType, func.count(BloodDonation.DonationID))
#         #     .group_by(BloodDonation.BloodType)
#         #     .all()
#         # )
#         # ans = [
#         #     {
#         #         "BloodBankName": res.BloodBankName,
#         #         "ContactNumber": res.ContactNumber,
#         #         "Location": res.Location,
#         #         "BloodType": [
#         #             {
#         #                 "Type": blood,
#         #                 "TotalAvailable": count,
#         #             }
#         #             for blood, count in main
#         #         ],
#         #     }
#         # ]
#         # # if main:
#         # #     ans = {
#         # #         "BloodBankName": res.BloodBankName,
#         # #         "BloodType": [
#         # #             {
#         # #                 "Type": blood,
#         # #                 "TotalAvailable": count,
#         # #             }
#         # #             for blood, count in main
#         # #         ],
#         # #     }
#         # # else:
#         # #     ans = "No data available"
#         # return ans
#         res = (
#             session.query(BloodBank)
#             .filter(BloodBank.BloodBankName == args.get("BloodBankName"))
#             .first()
#         )

#         if res:
#             blood_types_count = {}
#             for donation in res.blooddonations:
#                 blood_type = donation.BloodType
#                 if blood_type in blood_types_count:
#                     blood_types_count[blood_type] += 1
#                 else:
#                     blood_types_count[blood_type] = 1

#                 ans = [
#                     {
#                         "BloodBankName": res.BloodBankName,
#                         "ContactNumber": res.ContactNumber,
#                         "Location": res.Location,
#                         "BloodType": [
#                             {"Type": blood, "TotalAvailable": count}
#                             for blood, count in blood_types_count.items()
#                         ],
#                     }
#                 ]
#             return ans
#         else:
#             return "Blood bank not found"

#     @staticmethod
#     def getting_all_availble_bloods(session):
#         res = session.query(BloodBank).all()
#         return res
