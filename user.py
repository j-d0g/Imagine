class User:
    skill_translations = {
            'prob_solving' : 0
            'communication' : 1
            'teamwork' : 2
            'creativity' : 3 
            'leadership' : 4
            'artistic' : 5
            'academic' : 6 
            'attention_to_detail' : 7
            'prioritisation' : 8
            'interpersonal' : 9 
            'time_management' : 10
    }

    bcg_translations = {
            'minority' : 0,
            'gender' : 1,
            'financial' : 2,
            'location' : 3,
            'education' : 4,
            'disability' : 5,
            'domestic' : 6,
            'lgbt' : 7
    }

    def __init__(self, name, skill_score, bcg_score, ):
        self.name = 
        self.id = 
        self.skill_score = skill_score
        self.bcg_score = bcg_score

class Googler(User):
    def __init__():

class Student(User):
    def __init__(self):
        self.best_match_abs = [] * self.get_total_googlers
        self.best_match_career = [] * self.get_total_googlers
        self.best_match_bcg = [] * self.get_total_googlers
    
    def get_total_googlers(self):
        return 5

    def get_best_skill(self):
        return self.best_match_skill[0]
        
    def get_best_bcg(self):
        return self.best_match_bcg[0]
        
    def get_best_abs(self):
        return self.best_match_abs[0]

new_user = User()
print(new_user.skill_score['prob_solving'])
