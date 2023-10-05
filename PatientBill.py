import PatientClass as A
import ProcedureClass as B
total=0
name=input("Please Enter the Patient's name ")
Id=input("Please Enter the Patient's ID ")
phone=input("Please Enter teh Patient's phone number ")
vet_stats=input("Is the patient a veteran? Y/N ")
vet_stat=vet_stats.lower()
address=input("Please enter the Patient's address ")
patient=A.Patient(Id,name,phone,vet_stat,address)
procedure_Physical=B.Procedure('Physical Exam','2/15/2022','Dr. Irvine',250,'1')
procedure_MRI=B.Procedure('MRI','2/15/2022','Dr. Hamilton',1500,'1')
procedure_CT=B.Procedure('CT Scan','2/17/2022','Dr.Drey',1200,'2')

print()
print("*** Patient Bill ***")
print(f'Name: {patient.get_name()}')
print(f'Adress: {patient.get_address()}')
print(f'Phone: {patient.get_phone()}')
print()

if procedure_Physical.get_Id() == patient.get_id():
    print(f'Procedure: {procedure_Physical.get_procedure()}')
    print(f'Date: {procedure_Physical.get_date()}')
    print(f'Practitioner: {procedure_Physical.get_pract()}')
    print(f'Charge: {procedure_Physical.get_charge()}')
    total+=procedure_Physical.get_charge()
    print()
if procedure_MRI.get_Id() == patient.get_id():
    print(f'Procedure: {procedure_MRI.get_procedure()}')
    print(f'Date: {procedure_MRI.get_date()}')
    print(f'Practitioner: {procedure_MRI.get_pract()}')
    print(f'Charge: {procedure_MRI.get_charge()}')
    print()
    total+=procedure_MRI.get_charge()
if procedure_CT.get_Id() == patient.get_id():
    print(f'Procedure: {procedure_CT.get_procedure()}')
    print(f'Date: {procedure_CT.get_date()}')
    print(f'Practitioner: {procedure_CT.get_pract()}')
    print(f'Charge: {procedure_CT.get_charge()}')
    total+=procedure_CT.get_charge()
    print()

if patient.get_vet_stat()=='y':
    total=total*.6
    print(f'Total Charge: $'+str(total))
else:
    print(f'Total Charge: $'+str(total))
#40% off total, not individual