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

    def calculate_best_match(self):
        best_match = {
            'role_id' : -1,
            'score_diff' : 99
        }
        for role_id, role_score in enumerate(self.roles):
            diff = 0
            print(f'role: {role_id}')
            for attribute in role_score.keys():
                diff += abs(self.skill_score[attribute] - role_score[attribute])
                print(f'attribute: {attribute}\nstudent score: {self.skill_score[attribute]},\nrole score: {role_score[attribute]},\ndiff: {diff}')
            if diff < best_match['score_diff']:
                best_match['role_id'], best_match['score_diff'] = role_id, diff
        return best_match

student_1 = User('Jordan', 'jordan_tran1@hotmail.com', user_score, None)
print(student_1.calculate_best_match())