student_names=["sagar","yashwanth","jashwanth","harsha","gouri","prajwal","chethan","varun","sina","guffren","suraj","karthik","punith","akhilesh","rahul","sina","bhargav","azam"];
print(student_names)
print("--------------")
print(student_names[5])
print(student_names[-1])

student_names.append("basha")
print(student_names)

student_names.remove("karthik")
print(f"remove karthik:{student_names}")

student_names.remove("punith")
print(f"remove punith:{student_names}")


student_names.insert(4,"kaju")
print(f"insert kaju:{student_names}")

student_names.insert(6,"manja")
print(f"insert manja:{student_names}")


student_names.insert(1,"kohli")
print(f"insert kohli:{student_names}")


student_names.insert(0,"RCB")
print(f"insert RCB:{student_names}")


student_names.pop(4)
print(f"pop:{student_names}")

student_names.pop(4)
print(f"length of list:{len(student_names)}")


student_names.reverse()
print(f"reverse:{student_names}")



















