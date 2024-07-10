'''from operations import app
from Models import User,AppointmentModel
import pytest

@pytest.fixture
def client():
   with app.test_client() as client: #test_client() will start the server and do the unit testing.
       with app.app_context(): #app_context will help you to access current flask application.
           yield client'''


'''def test_valid_login(client):
    response = client.post('/login', json={
        'username': 'uday123',
        'password': 'uday@123'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful"}'''

'''def test_invalid_login(client):
    response = client.post('/login', json={
        'username': 'wronguser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Username or password is incorrect"}'''

'''def test_missing_fields(client):
    response = client.post('/login', json={
        'username': 'testuser'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Username or password is missing"}'''

'''def test_successful_registration(client):
    response = client.post('/reg', json={
        'username': 'teja123',
        'firstname': 'teja1',
        'lastname': 'teja2',
        'emailid': 'uday123@gmail.com',
        'password': 'password'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "User registered successfully"}'''

"""def test_missing_details(client):
    response = client.post('/reg', json={
        'username': 'newuser1',
        'firstname': 'newuser',
        'lastname': 'lastname',
        'emailid': 'emailid@gmail.com',
        'password': 'newpassword'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Missing Details"}"""

'''def test_user_already_exists(client):
    response = client.post('/reg', json={
        'username': 'vishnu123',
        'firstname': 'vishnu',
        'lastname': 'charan',
        'emailid': 'vishnu@gmail.com',
        'password': 'vishnu@123'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Register user already exists"}'''


'''def test_get_appointments(client):
    response = client.get('/appointment')
    assert response.status_code == 200
    assert response.get_json() == [{'date': '2024-07-10',
  'id': 1,
  'name': 'uday',
  'service': 'yoga',
  'time': '08:00'},
 {'date': '2024-07-10',
  'id': 2,
  'name': 'vishnu',
  'service': 'Massage Therapy',
  'time': '10:00'},
 {'date': '2024-07-11',
  'id': 3,
  'name': 'saikumar',
  'service': 'Nutritional Counselling',
  'time': '10:00'},
 {'date': '2024-07-11',
  'id': 4,
  'name': 'pavan',
  'service': 'Fitness',
  'time': '17:30'}]'''

'''def test_book_appointment(client):
    response = client.post('/appointment', json={
        'name': 'John Doe',
        'service': 'Consultation',
        'date': '2024-07-10',
        'time': '10:00 AM'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Appointment booked successfully"}'''


'''def test_book_appointment_slot_not_available(client):
    response = client.post('/appointment', json={
        'name': 'John Doe',
        'service': 'Consultation',
        'date': '2024-07-10',
        'time': '10:00 AM'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Slot not available"}'''

'''def test_update_appointment(client):

    response = client.put(f'/appointment/2', json={
        'name': 'Jane Doe',
        'service': 'Therapy',
        'date': '2024-07-11',
        'time': '11:00 AM'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Appointment details updated successfully"}'''

'''def test_delete_appointment(client):
    response = client.delete(f'/appointment/4')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Appointment cancelled successfully"}'''
