
ADDRESSES = 'addresses'
CONTACTS = 'contacts'
EMPLOYMENT_DETAILS = 'employment_details'
ADDRESS = 'address'
ADDRESS_TYPE = 'address_type'
DEPARTMENT = 'department'
DESIGNATION = 'designation'
STATE_PROVINCE = 'state_province'
COUNTRY = 'country'
EMPLOYEE = 'employee'
CONTACT_TYPE = 'contact_type'
MARITAL_STATUS = 'marital_status'
GENDER = 'gender'

# json fields for testing

ZERO_ADDRESS_CONTACT_EMPLOYMENT_DETAILS = \
    {
        "employee_id": "E0003",
        "first_name": "aabcd",
        "middle_name": "efgh",
        "last_name": "abcd",
        "date_of_birth": "2019-01-22",
        "marital_status": 1,
        "marital_status_name": "single",
        "gender": 1,
        "gender_name": "MALE",
        "address_list": [],
        "contact_list": [],
        "employment_details_list": [],
        "created_by": "system",
        "last_updated_by": "system",
        "deleted_status": False,
        "last_updated_date": "2019-01-22",
        "deleted_date": None,
        "created_date": "2019-01-22"
    }

ZERO_ADDRESS_EMPLOYMENT_DETAILS = \
    {
            "employee_id": "E0004",
            "first_name": "aabcd",
            "middle_name": "efgh",
            "last_name": "abcd",
            "date_of_birth": "2019-01-22",
            "marital_status": 1,
            "marital_status_name": "single",
            "gender": 1,
            "gender_name": "MALE",
            "address_list": [],
            "contact_list": [
                {
                    "contact_type": 1,
                    "contact_type_name": "Work",
                    "contact_value": "svijaykashyap65@gmail.com",
                    "created_by": "system",
                    "last_updated_by": "system",
                    "deleted_status": False,
                    "last_updated_date": "2019-01-22",
                    "deleted_date": None,
                    "created_date": "2019-01-22"
                }
            ],
            "employment_details_list": [],
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-22",
            "deleted_date": None,
            "created_date": "2019-01-22"
    }

ZERO_ADDRESS = \
    {
"employee_id": "E0005",
            "first_name": "aabcd",
            "middle_name": "efgh",
            "last_name": "abcd",
            "date_of_birth": "2019-01-22",
            "marital_status": 1,
            "marital_status_name": "single",
            "gender": 1,
            "gender_name": "MALE",
            "address_list": [],
            "contact_list": [
                {
                    "contact_type": 1,
                    "contact_type_name": "Work",
                    "contact_value": "svijaykashyap65@gmail.com",
                    "created_by": "system",
                    "last_updated_by": "system",
                    "deleted_status": False,
                    "last_updated_date": "2019-01-22",
                    "deleted_date": None,
                    "created_date": "2019-01-22"
                }
            ],
            "employment_details_list": [
                {
                    "department": 1,
                    "department_name": "IT",
                    "designation": 1,
                    "designation_name": "SE",
                    "employment_start_date": "2019-01-23",
                    "employment_end_date": None,
                    "created_by": "system",
                    "last_updated_by": "system",
                    "deleted_status": False,
                    "last_updated_date": "2019-01-22",
                    "deleted_date": None,
                    "created_date": "2019-01-22"
                }
            ],
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-22",
            "deleted_date": None,
            "created_date": "2019-01-22"
    }

EMPLOYEE_COMPOSITE_CREATE = \
    {
            "employee_id": "E0006",
            "first_name": "aabcd",
            "middle_name": "efgh",
            "last_name": "abcd",
            "date_of_birth": "2019-01-22",
            "marital_status": 1,
            "marital_status_name": "single",
            "gender": 1,
            "gender_name": "MALE",
            "address_list": [
                {
                    "address_type": 1,
                    "address_type_name": "2222",
                    "address": {
                        "addr_line_one": "2422",
                        "addr_line_two": "one",
                        "addr_line_three": "two",
                        "locality": "three",
                        "city": "Bengaluru",
                        "state_province": 1,
                        "state_name": "Karnataka",
                        "country": 1,
                        "country_name": "India",
                        "postal_code": "55555",
                        "created_by": "system",
                        "last_updated_by": "system",
                        "deleted_status": False,
                        "last_updated_date": "2019-01-23",
                        "deleted_date": None,
                        "created_date": "2019-01-23"
                    }
                }
            ],
            "contact_list": [
                {
                    "contact_type": 1,
                    "contact_type_name": "Work",
                    "contact_value": "svijaykashyap65@gmail.com",
                    "created_by": "system",
                    "last_updated_by": "system",
                    "deleted_status": False,
                    "last_updated_date": "2019-01-22",
                    "deleted_date": None,
                    "created_date": "2019-01-22"
                }
            ],
            "employment_details_list": [
                {
                    "department": 1,
                    "department_name": "IT",
                    "designation": 1,
                    "designation_name": "SE",
                    "employment_start_date": "2019-01-23",
                    "employment_end_date": None,
                    "created_by": "system",
                    "last_updated_by": "system",
                    "deleted_status": False,
                    "last_updated_date": "2019-01-22",
                    "deleted_date": None,
                    "created_date": "2019-01-22"
                }
            ],
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-22",
            "deleted_date": None,
            "created_date": "2019-01-22"
    }