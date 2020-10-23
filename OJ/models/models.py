from django.db import models

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, null=False)
    

class Institution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=100, null=False)

class Rating_Distribution(models.Model):
    rating_catagory = models.CharField(max_length=20, primary_key=True)
    maximum_rating = models.IntegerField(null=False)
    minimum_rating = models.IntegerField(null=False)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    handle = models.CharField(max_length=32, null=False, unique=True)
    user_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=500, null=False, unique=True)
    rating = models.IntegerField(default=0)
    password_hash = models.CharField(max_length=64, null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL)
    rating_catagory = models.ForeignKey(Rating_Distribution, on_delete=models.SET_NULL)

class Follow(models.Model):
    follower_id = models.IntegerField(null=False, primary_key=True)
    followee_id = models.IntegerField(null=False, primary_key=True)
    follower = models.ForeignKey(Users, on_delete=models.CASCADE)
    followee = models.ForeignKey(Users, on_delete=models.CASCADE)
    follower_id = follower.user_id
    followee_id = followee.user_id

class Message(models.Model):
    message_id = models.IntegerField(null=False, primary_key=True)
    text = models.TextField(null=False)
    file_location = models.CharField(max_length=512)
    time = models.DateField(null=False)
    seen = models.IntegerField(max_length=1, default=0)
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE)
    receiver_id = receiver.user_id
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
    sender_id = sender.user_id
    

class Problem(models.Model):
    problem_id = models.CharField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    input_description = models.TextField(null=False)
    output_description = models.TextField(null=False)
    note = models.TextField(null=False)
    timelimit = models.IntegerField(null=False)
    memorylimit = models.IntegerField(null=False)
    tutorial_link = models.CharField(max_length=2048)
    difficulty = models.IntegerField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    owner_user_id = owner.owner_user_id

class Problem_Catagory(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    problem_id = problem.problem_id
    catagory_name = models.CharField(max_length=256, primary_key=true)

class Testcase(models.Model):
    testcase_id = models.AutoField(primary_key=True, null=False)
    input_file_location = models.CharField(max_length=2048, null=False)
    output_file_location = models.CharField(max_length=2048, null=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    problem_id = problem.problem_id


class Sample_testcase(models.Model):
    testcase_id = models.AutoField(primary_key=True, null=False)
    input_file_location = models.CharField(max_length=2048, null=False)
    output_file_location = models.CharField(max_length=2048, null=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    problem_id = problem.problem_id

class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True, null=False)
    submission_time = models.DateField(null=False)
    judge_time = models.DateField()
    language = models.CharField(max_length=128)
    execution_time = models.IntegerField()
    memory_usages = models.IntegerField()
    verdict = models.CharField(max_length=32)
    raw_code = models.TextField(null=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    problem_id = problem.problem_id

class Contest(models.Model):
    contest_id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=512, null=False)
    start_time = models.DateField()
    duration = models.IntegerField()

class Clarification(models.Model):
    clarification_id = models.AutoField(primary_key=True, null=False)
    question = models.TextField(null=False)
    answer = models.TextField(null=False)
    publish_time = models.DateField()
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    contest_id = contest.contest_id

class Problem_contest(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    contest_id = models.IntegerField(primary_key=True)
    contest_id = contest.contest_id
    user_id = models.IntegerField(primary_key=True)
    user_id = user.owner_user_id

class Participant(models.Model):
    user_participant = models.ForeignKey(Users, on_delete=models.CASCADE)
    contest_participant = models.ForeignKey(Users, on_delete=models.CASCADE)
    contest_id = models.IntegerField(primary_key=True, null=False)
    user_id = models.IntegerField(primary_key=True, null=False)
    contest_id = contest_participant.contest_id
    user_id = user_participant.owner_user_id


class Manager(models.Model):
    user_manager = models.ForeignKey(Users, on_delete=models.CASCADE)
    contest_manager = models.ForeignKey(Contest, on_delete=models.CASCADE)
    contest_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    contest_id = contest_manager.contest_id
    user_id = user_manager.owner_user_id

class Contest_user_submission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    submission = models.ForeignKey(Users, on_delete=models.CASCADE)
    contest_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    submission_id = models.IntegerField(primary_key=True)
    contest_id = contest.contest_id
    user_id = user.owner_user_id
    submission_id = submission.submission_id



       




    


