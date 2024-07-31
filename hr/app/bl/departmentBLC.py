# from itertools import count
from hr.app.repositories.departmentRepository import departmentRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class departmentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_department(args:dict):
        session = departmentBLC.get_session()
        res = departmentRepository.add_department_into_db(session, args)
        return res

    @staticmethod
    def getting_department_by_id(args):
        session  = departmentBLC.get_session()
        department = departmentRepository.get_department_by_id_from_db(session,args)
        if department:
            return department
        raise Exception("department not found")
    

    @staticmethod
    def getting_all_department():
        session = departmentBLC.get_session()
        departments = departmentRepository.get_all_departments_from_db(session)
        if departments:
            return departments
        raise Exception("departments are not exist plz add departments")
    
    @staticmethod
    def updating_the_department(args:dict):
        session = departmentBLC.get_session()
        check_department = departmentRepository.get_department_by_id_from_db(session,args)
        if check_department:
            updated =departmentRepository.update_the_department(session,check_department,args)
            if updated:
                session.commit()
                return check_department
            else:
                raise Exception("department is not updated")

        else:
            raise Exception("department_id not found")

    @staticmethod
    def deleting_the_department(args:dict):
        session = departmentBLC.get_session()
        check_department = departmentRepository.get_department_by_id_from_db(session=session,args=args)
        if check_department:
            session.delete(check_department)
            session.commit()
            return f"department_id {args.get('department_id')} is deleted successfully"
        raise Exception("department_id not found")



#     @staticmethod
#     def get_single_bb(args):
#         session = BloodBankBLC.get_session()
#         res = BloodBankRepository.get_single_bb_byid(session, args)
#         return res

#     @staticmethod
#     def updating_bloodbank(args):
#         session = BloodBankBLC.get_session()
#         bk = BloodBankRepository.get_single_bb_byid(session, args)
#         if bk:
#             res = BloodBankRepository.update_bb_todb(session, args, bk)
#             return res

#     @staticmethod
#     def get_all_bb():
#         session = BloodBankBLC.get_session()
#         res = BloodBankRepository.getting_all_bb(session)
#         return res

#     @staticmethod
#     def delete_bloodbank(args):
#         session = BloodBankBLC.get_session()
#         bb = BloodBankRepository.get_single_bb_byid(session, args)
#         if not bb:
#             return (
#                 jsonify({"message": "bloodbank not found"}),
#                 HTTPStatus.UNPROCESSABLE_ENTITY,
#             )
#         session.delete(bb)
#         session.commit()
#         return jsonify(
#             {"message": f"bloodbank{args.get('BloodBankID')} is deleted successfully"}
#         )

#     @staticmethod
#     def get_availble_bloods(args):
#         session = BloodBankBLC.get_session()
#         res = BloodBankRepository.geting_available_bloods(session, args)

#         if res:
#             return res

#     @staticmethod
#     def gets_all_availble_bloods():
#         session = BloodBankBLC.get_session()
#         res = BloodBankRepository.getting_all_availble_bloods(session)
#         if res:
#             ans = []
#             for bank in res:
#                 avail = {}
#                 for donor in bank.blooddonations:
#                     bloodtype = donor.BloodType
#                     if bloodtype in avail:
#                         avail[bloodtype] += 1
#                     else:
#                         avail[bloodtype] = 1

#                 bank_info = {
#                     "BloodBankName": bank.BloodBankName,
#                     "ContactNumber": bank.ContactNumber,
#                     "Location": bank.Location,
#                     "BloodType": [
#                         {"Type": blood, "TotalAvailable": count}
#                         for blood, count in avail.items()
#                     ],
#                 }
#                 ans.append(bank_info)

#             return ans
