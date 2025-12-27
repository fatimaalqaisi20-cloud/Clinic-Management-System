print(' ')
print('created by Fatima & Raghad')
print ('==============================')
import datetime
class PatientProfile:
    #كلاس يمثل بيانات المريض الأساسية
   def __init__(self, full_name, birth_date, contact_number):
       self.full_name = full_name
       self.birth_date = birth_date
       self.contact_number = contact_number
class MedicalAppointment:
    #كلاس يمثل تفاصيل الموعد الطبي
   def __init__(self, patient, date, time, status):
       self.patient = patient
       self.date = date
       self.time = time
       self.status = status
class AppointmentManager:
    #كلاس يمثل ادارة المواعيد الطبية
   def __init__(self):
       self.appointments = []
   def add_appointment(self, appointment):
       self.appointments.append(appointment)
   def list_appointments(self):
       for appointment in self.appointments:
           print(f"Patient: {appointment.patient.full_name}")
           print(f"Date: {appointment.date}")
           print(f"Time: {appointment.time}")
           print(f"Status: {appointment.status}")
           print("-------------------------")
# الوظيفة لتحديث الموعد الطبي
def update_appointment(manager, appointment_id):
   for appointment in manager.appointments:
       if appointment.id == appointment_id:
           print("Current appointment details:")
           print(f"Patient: {appointment.patient.full_name}")
           print(f"Date: {appointment.date}")
           print(f"Time: {appointment.time}")
           print(f"Status: {appointment.status}")
           print("Enter new details (leave empty to keep current value):")
           full_name = input(f"Enter new patient's name [{appointment.patient.full_name}]: ") or appointment.patient.full_name
           birth_date = input(f"Enter new patient's date of birth [{appointment.patient.birth_date}]: ") or appointment.patient.birth_date
           contact_number = input(f"Enter new patient's contact number [{appointment.patient.contact_number}]: ") or appointment.patient.contact_number
           date = input(f"Enter new appointment date [{appointment.date}]: ") or appointment.date
           time = input(f"Enter new appointment time [{appointment.time}]: ") or appointment.time
           status = input(f"Enter new status [{appointment.status}]: ") or appointment.status
           appointment.patient.full_name = full_name
           appointment.patient.birth_date = birth_date
           appointment.patient.contact_number = contact_number
           appointment.date = date
           appointment.time = time
           appointment.status = status
           print("Appointment updated successfully.")
           return
   print(f"No appointment found with ID {appointment_id}.")
# الوظيفة لالغاء الموعد الطبي
def cancel_appointment(manager, appointment_id):
   for appointment in manager.appointments:
       if appointment.id == appointment_id:
           print(f"Cancelling appointment with ID {appointment_id}:")
           print(f"Patient: {appointment.patient.full_name}")
           print(f"Date: {appointment.date}")
           print(f"Time: {appointment.time}")
           print(f"Status: {appointment.status}")
           manager.appointments.remove(appointment)
           print("Appointment cancelled successfully.")
           return
   print(f"No appointment found with ID {appointment_id}.")
# الوظيفة لحفظ المواعيد الطبية فيملف نصي
def save_appointment_data(manager, filename):
   try:
       with open(filename, 'w') as file:
           for appointment in manager.appointments:
               file.write(f"{appointment.patient.full_name},{appointment.patient.birth_date},{appointment.patient.contact_number},"
                          f"{appointment.date},{appointment.time},{appointment.status}\n")
       print("Appointment data saved to", filename)
   except Exception as e:
       print("Error saving appointment data:", str(e))
# الوظيفة للتعامل مع تعارض المواعيد
def handle_conflicts(manager, appointment):
   conflicts = [appt for appt in manager.appointments if appt.date == appointment.date and appt.time == appointment.time]
   return conflicts
# الوظيفة الرئيسية لتعديل البرنامج
def main():
   manager = AppointmentManager()
   appointment_id_counter = 1
   while True:
       print("\nOptions:")
       print("1. Schedule Appointment")
       print("2. List Appointments")
       print("3. Update Appointment")
       print("4. Cancel Appointment")
       print("5. Save Appointment Data to File")
       print("6. Exit")
       choice = input("Enter your choice: ")
       if choice == '1':
           full_name = input("Enter patient's full name: ")
           birth_date = input("Enter patient's date of birth (YYYY-MM-DD): ")
           contact_number = input("Enter patient's contact number: ")
           date = input("Enter appointment date (YYYY-MM-DD): ")
           time = input("Enter appointment time: ")
           status = "Scheduled"
           appointment = Appointment(Patient(full_name, birth_date, contact_number), date, time, status)
           conflicts = handle_conflicts(manager, appointment)
           if not conflicts:
               appointment.id = appointment_id_counter
               appointment_id_counter += 1
               manager.add_appointment(appointment)
               print("Appointment scheduled successfully.")
           else:
               print("Scheduling conflict detected! Cannot schedule.")
       elif choice == '2':
           manager.list_appointments()
       elif choice == '3':
           appointment_id = int(input("Enter the appointment ID to update: "))
           update_appointment(manager, appointment_id)
       elif choice == '4':
           appointment_id = int(input("Enter the appointment ID to cancel: "))
           cancel_appointment(manager, appointment_id)
       elif choice == '5':
           filename = input("Enter the filename to save appointment data: ")
           save_appointment_data(manager, filename)
       elif choice == '6':
           print("Exiting the program.")
           break

if __name__ == "__main__":
   main()
