from django import forms 

HALLS = [
    'Patel',
    'Azad',
    'Nehru',
    'RP',
    'RK',
    'MMM',
    'LBS',
    'BC Roy',
    'BRH',
    'Gokhale',
    'HJB',
    'JCB',
    'MS',
    'MT',
    'SNVH',
    'RLB',
    'SAM',
    'SNIG',
    'VS'
]

HALL_TUPLES = [(x,x) for x in HALLS]

class Info(forms.Form):
    name = forms.CharField(label="Your Name", max_length=30)
    email = forms.CharField(label="Your Email-ID", max_length=30)
    roll = forms.CharField(label="Roll Number", max_length=10)
    hall = forms.CharField(label = "Hall of Residence", widget=forms.Select(choices=HALL_TUPLES))
    contact = forms.IntegerField(label="Contact Number")
    exp = forms.CharField(label="Write about your experience in Soft Skills", widget=forms.Textarea(attrs={'rows':1, 'cols':35}))