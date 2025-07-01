from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    exam_name = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text[:50]

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_label = models.CharField(max_length=1)  # A, B, C, D
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.option_label}. {self.option_text[:30]}"
