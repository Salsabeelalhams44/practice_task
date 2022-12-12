import json
import requests


def register_new_student():

    fullname = input('Enter full name: ')
    age = int(input('Enter your age: '))
    level = input('choose your level A, B, C: ')
    mobile_number = input('Enter your mobile number: ')

    data = {
        'full_name': fullname,
        'age': age,
        'mobile_number': mobile_number,
        'level': level,
    }

    store_data = requests.post(
        'http://staging.bldt.ca/api/method/build_it.test.register_student',
        data=data
    )
    data = json.loads(store_data.text)
    print('Congratulation!!, Add new student done successfully')
    print(data)


def edit_student_details():

    m_id = input('Enter your id: ')
    fullname = input('Enter full name: ')
    age = int(input('Enter your age: '))
    level = input('choose your level A, B, C: ')
    mobile_number = input('Enter your mobile number: ')
    print('Your information updated successfully')
    result = requests.put(
        'http://staging.bldt.ca/api/method/build_it.test.edit_student',
        data={
          'id': m_id,
          'full_name': fullname,
          'age': age,
          'mobile_number': mobile_number,
          'level': level
        }
    )
    data = result.text
    data = json.loads(data)
    print('Update information done successfully')
    print(data)


def delete_student():
    m_id = input('Enter your id for delete: ')
    result = requests.delete(
        'http://staging.bldt.ca/api/method/build_it.test.delete_student',
        data={'id': m_id}
    )
    print('Delete done successfully')
    data = result.text
    data = json.loads(data)
    print(data)


def export_all_students_to_file():
    result = requests.get('http://staging.bldt.ca/api/method/build_it.test.get_students')
    data = result.text
    data = json.loads(data)
    file1 = open('students.text', mode='w')
    for i in range(len(data)):
        file1.write(str(data['data'][i])+'\n')
    file1.close()
    print('Export all students done successfully')


def export_student_details_to_file():
    m_id = input('Enter your id for export information to file: ')
    result = requests.get('http://staging.bldt.ca/api/method/build_it.test.get_student_details', data={'id': m_id})
    data = result.text
    data = json.loads(data)
    file2 = open('student.text', mode='w')
    file2.write(str(data['data']))
    file2.close()
    print('Export your information done successfully')


while True:
    menu = int(input(""" Enter the number of process that need to do from the menu
                     1- Register new student
                     2- Edit Student Details
                     3- Delete Student
                     4- Export Students to text file
                     5- Export Students details to text file
                     6- Exit :) 
                     """))
    if menu == 1:
        register_new_student()

    elif menu == 2:
        edit_student_details()

    elif menu == 3:
        delete_student()

    elif menu == 4:
        export_all_students_to_file()

    elif menu == 5:
        export_student_details_to_file()

    else:
        print('Thank you for using system')
        exit()
    # print(type(data))
    # print(type(data))
    # print(data['status'])
    # print(data)
    # print(data['data'][0]['full_name'])
    # context = {}
    # context['data'] = data['full_name']
    # render_template("student_template.html",**context)
    
