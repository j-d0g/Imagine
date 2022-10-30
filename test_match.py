from user import Student, Googler
roles = [
                {
                        'prob_solving' : 5,
                        'communication' : 3,
                        'teamwork' : 3,
                        'creativity' : 1, 
                        'leadership' : 1,
                        'artistic' : 0,
                        'academic' : 3, 
                        'prioritisation' : 3,
                        'interpersonal' : 1,
                        'handle_pressure' : 3
                },
                {
                        'prob_solving' : 2,
                        'communication' : 2,
                        'teamwork' : 2,
                        'creativity' : 4, 
                        'leadership' : 1,
                        'artistic' : 3,
                        'academic' : 1,
                        'prioritisation' : 2,
                        'interpersonal' : 2,
                        'handle_pressure' : 2
                },
                {
                        'prob_solving' : 2,
                        'communication' : 3,
                        'teamwork' : 2,
                        'creativity' : 1, 
                        'leadership' : 3,
                        'artistic' : 1,
                        'academic' : 1, 
                        'prioritisation' : 3,
                        'interpersonal' : 3,
                        'handle_pressure' : 3
                }
            ]
bcgs = [
                {
                        'african' : 1,
                        'asian' : 0,
                        'financial' : 1,
                        'gender' : 0, 
                        'lgbt' : 0,
                        'disability' : 0,
                        'domestic' : 0, 
                },
                {
                        'african' : 0,
                        'asian' : 1,
                        'financial' : 0,
                        'gender' : 1, 
                        'lgbt' : 0,
                        'disability' : 0,
                        'domestic' : 0, 
                },
                {
                        'african' : 0,
                        'asian' : 0,
                        'financial' : 0,
                        'gender' : 1, 
                        'lgbt' : 1,
                        'disability' : 0,
                        'domestic' : 0, 
                },
                {
                        'african' : 0,
                        'asian' : 0,
                        'financial' : 0,
                        'gender' : 0, 
                        'lgbt' : 0,
                        'disability' : 1,
                        'domestic' : 1, 
                },
                {
                        'african' : 1,
                        'asian' : 1,
                        'financial' : 1,
                        'gender' : 1, 
                        'lgbt' : 1,
                        'disability' : 1,
                        'domestic' : 1, 
                },
                {
                        'african' : 0,
                        'asian' : 1,
                        'financial' : 1,
                        'gender' : 1, 
                        'lgbt' : 1,
                        'disability' : 1,
                        'domestic' : 0, 
                },
            ]

student_swe_1 = Student('Jordan', 'jordan_tran1@hotmail.com', roles[0], bcgs[0])
student_swe_2 = Student('Tenishka', 'jordan_tran1@hotmail.com', roles[0], bcgs[1])

student_ux_1 = Student('Fara', 'jordan_tran1@hotmail.com', roles[1], bcgs[2])
student_ux_2 = Student('Azim', 'jordan_tran1@hotmail.com', roles[1], bcgs[3])

student_pm_1 = Student('Edwin', 'jordan_tran1@hotmail.com', roles[2], bcgs[4])
student_pm_2 = Student('Michael', 'jordan_tran1@hotmail.com', roles[2], bcgs[5])

googlers = []

googlers.append(Googler('Swe1', '@hotmail.com', roles[0], bcgs[0], 0))
googlers.append(Googler('Swe2', '@hotmail.com', roles[0], bcgs[1], 0))
googlers.append(Googler('Ux1', '@hotmail.com', roles[1], bcgs[2], 1))
googlers.append(Googler('Ux2', '@hotmail.com', roles[1], bcgs[3], 1))
googlers.append(Googler('Pm1', '@hotmail.com', roles[2], bcgs[4], 2))
googlers.append(Googler('Pm2', '@hotmail.com', roles[2], bcgs[5], 2))

print(student_swe_1.get_best_role_match(googlers)['best_googler'].name)
print(student_swe_2.get_best_role_match(googlers)['best_googler'].name)
print(student_ux_1.get_best_role_match(googlers)['best_googler'].name)
print(student_ux_2.get_best_role_match(googlers)['best_googler'].name)
print(student_pm_1.get_best_role_match(googlers)['best_googler'].name)
print(student_pm_1.get_best_role_match(googlers)['best_googler'].name)

print(student_swe_1.calculate_bcg(googlers)['best_googler'].name)
print(student_swe_2.calculate_bcg(googlers)['best_googler'].name)
print(student_ux_1.calculate_bcg(googlers)['best_googler'].name)
print(student_ux_2.calculate_bcg(googlers)['best_googler'].name)
print(student_pm_1.calculate_bcg(googlers)['best_googler'].name)
print(student_pm_1.calculate_bcg(googlers)['best_googler'].name)