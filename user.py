from collections import namedtuple
class User:
    def __init__(self, name, email, skill_score, bcg_score):
        # roles[0] = Software Engineer, roles[1] = UX/UI Design, roles[2] = Product Manager
        self.roles = [
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
        self.name = name
        self.id = email
        self.skill_score = skill_score
        self.bcg_score = bcg_score

        def get_name(self):
            return self.name

        def get_email(self):
            return self.email
        
        def get_skill_score(self):
            return self.skill_score
        
        def get_bcg_score(self):
            return self.bcg_score

class Googler(User):
    def __init__(self, name, email, skill_score, bcg_score, role):
        super().__init__(name, email, skill_score, bcg_score)
        self.role = role

class Student(User):
    def __init__(self, name, email, skill_score, bcg_score):
        super().__init__(name, email, skill_score, bcg_score)
        self.best_role_match = None

    def calculate_role(self):
        best_role = {
            'role_id' : -1,
            'score_diff' : 99
        }
        # for each role, compare the difference against students skills, and update if diff < best_diff
        for role_id, role_score in enumerate(self.roles):
            diff = 0
            # print(f'role: {role_id}')
            for attribute in role_score.keys():
                diff += abs(self.skill_score[attribute] - role_score[attribute])
                # print(f'attribute: {attribute}\nstudent score: {self.skill_score[attribute]},\nrole score: {role_score[attribute]},\ndiff: {diff}')
            if diff < best_role['score_diff']:
                best_role['role_id'], best_role['score_diff'] = role_id, diff
        return best_role

    def calculate_bcg(self, googlers):
        best_bcg = {
            'best_googler' : None,
            'score_diff' : 99
        }
        for googler in googlers:
            diff = 0
            for attribute in googler.bcg_score.keys():
                diff += abs(self.bcg_score[attribute] - googler.bcg_score[attribute])
            if diff < best_bcg['score_diff']:
                best_bcg['best_googler'], best_bcg['score_diff'] = googler, diff
        return best_bcg
    
    def get_best_role_match(self, googlers):
        best_googler = {
            'best_googler' : None,
            'score_diff' : 99
        }
        best_role_match = self.calculate_role()
        diff, candidate_googler_matches = 0, []

        # from googlers, select those that match the role the student has matched with
        for googler in googlers:
            if googler.role == best_role_match['role_id']:
                candidate_googler_matches.append(googler)

        # from role-matching googlers, find the best background match
        return self.calculate_bcg(candidate_googler_matches)
        
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