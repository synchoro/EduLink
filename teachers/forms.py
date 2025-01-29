import datetime
import re
from django import forms
from django.core.exceptions import ValidationError

from .models import Teacher
from grades.models import Grade


GENDER_CHOICES = [
    ('M', '男性'),
    ('F', '女性'),
]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'grade', 'phone_number', 'gender', 'birthday']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].queryset = Grade.objects.all().order_by('grade_number')
        self.fields['grade'].empty_label = 'クラスを選択してください'
        self.fields['gender'].widget = forms.Select(choices=GENDER_CHOICES)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # 去除所有非数字字符（包括 "-"）
        raw_phone_number = re.sub(r'\D', '', phone_number)

        # 验证电话号码格式是否符合要求（不带连字符的格式）
        if not re.match(r"^(070|080|090)\d{8}$", raw_phone_number):
            raise ValidationError('電話番号の形式が正しくありません。<br>正しい形式: 09012345678 または 090-1234-5678')

        # 检查是否已经存在相同的电话号码（无论是否带 `-`）
        if Teacher.objects.filter(phone_number=raw_phone_number).exclude(pk=self.instance.pk).exists():
            raise ValidationError("この電話番号を持つ教師情報は既に存在します。")

        # 将电话号码存储为无 `-` 的格式
        return raw_phone_number

    
    def clean_birthday(self):
        birthday=self.cleaned_data.get('birthday')
        if not isinstance(birthday,datetime.date):
            raise ValidationError('生年月日の形式が正しくありません。正しい形式: YYYY-MM-DD')
        if birthday > datetime.date.today():
            raise ValidationError('生年月日は現在日より前にしてください')
        return birthday

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if Teacher.objects.filter(grade=grade).exclude(pk=self.instance.pk).exists():
            raise ValidationError("このクラスを担当する教師情報は既に存在します。")
        return grade
