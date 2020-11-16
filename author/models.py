from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='author_profile/default.jpeg',upload_to='author_profile')
    phone_regex=RegexValidator(regex=r'^\ ?1?\d{9,15}$',message="Phone no must be entered in format: Up to 10 digits allowed.")
    phone=models.CharField(validators=[phone_regex],max_length=10,default=None,null=True)
    address=models.TextField(default=None,null=True)
    city=models.CharField(max_length=50,default=None,null=True)
    '''state_choices=[('N/A','None'),('AP','Andhra Pradesh'),('AR','Arunachal Pradesh'),('AS','Assam'),('BR','Bihar'),('CT','Chhattisgarh'),
    ('GA','Goa'),('GJ','Gujarat'),('HR','Haryana'),('HP','Himachal Pradesh'),('JK','Jammu and Kashmir'),('JH','Jharkhand'),
    ('KA','Karnataka'),('KL','Kerala'),('MP','Madhya Pradesh'),('MH','Maharashtra'),('MN','Manipur'),('ML','Meghalaya'),('MZ','Mizoram'),
    ('NL','Nagaland'),('OR','Odisha'),('PB','Punjab'),('RJ','Rajasthan'),('SK','Sikkim'),('TN','Tamil Nadu'),('TG','Telangana'),
    ('TR','Tripura'),('UT','Uttarakhand'),('UP','Uttar Pradesh'),('WB','West Bengal'),('AN','Andaman and Nicobar Islands'),
    ('CH','Chandigarh'),('DN','Dadra and Nagar Haveli'),('DD','Daman and Diu'),('DL','Delhi'),('LD','Lakshadweep'),('PY','Puducherry')]'''
    state=models.CharField(max_length=50,default=None,null=True)
    country_choices=[('N/A','None'),('AF','Afghanistan'),('AX','Åland Islands'),('AL','Albania'),('DZ','Algeria'),('AS','American Samoa'),
    ('AD','Andorra'),('AO','Angola'),('AI','Anguilla'),('AQ','Antarctica'),('AG','Antigua and Barbuda'),('AR','Argentina'),
    ('AM','Armenia'),('AW','Aruba'),('AU','Australia'),('AT','Austria'),('AZ','Azerbaijan'),('BS','Bahamas (the)'),('BH','Bahrain'),
    ('BD','Bangladesh'),('BB','Barbados'),('BY','Belarus'),('BE','Belgium'),('BZ','Belize'),('BJ','Benin'),('BM','Bermuda'),
    ('BT','Bhutan'),('BO','Bolivia (Plurinational State of)'),('BQ','Bonaire, Sint Eustatius and Saba'),('BA','Bosnia and Herzegovina'),
    ('BW','Botswana'),('BV','Bouvet Island'),('BR','Brazil'),('IO','British Indian Ocean Territory (the)'),('BN','Brunei Darussalam'),
    ('BG','Bulgaria'),('BF','Burkina Faso'),('BI','Burundi'),('CV','Cabo Verde'),('KH','Cambodia'),('CM','Cameroon'),('CA','Canada'),
    ('KY','Cayman Islands (the)'),('CF','Central African Republic (the)'),('TD','Chad'),('CL','Chile'),('CN','China'),
    ('CX','Christmas Island'),('CC','Cocos (Keeling) Islands (the)'),('CO','Colombia'),('KM','Comoros (the)'),
    ('CD','Congo (the Democratic Republic of the)'),('CG','Congo (the)'),('CK','Cook Islands (the)'),('CR','Costa Rica'),
    ('CI',"Côte d'Ivoire"),('HR','Croatia'),('CU','Cuba'),('CW','Curaçao'),('CY','Cyprus'),('CZ','Czech Republic (the)'),
    ('DK','Denmark'),('DJ','Djibouti'),('DM','Dominica'),('DO','Dominican Republic (the)'),('EC','Ecuador'),('EG','Egypt'),
    ('SV','El Salvador'),('GQ','Equatorial Guinea'),('ER','Eritrea'),('EE','Estonia'),('ET','Ethiopia'),
    ('FK','Falkland Islands (the) [Malvinas]'),('FO','Faroe Islands (the)'),('FJ','Fiji'),('FI','Finland'),('FR','France'),
    ('GF','French Guiana'),('PF','French Polynesia'),('TF','French Southern Territories (the)'),('GA','Gabon'),('GM','Gambia (the)'),
    ('GE','Georgia'),('DE','Germany'),('GH','Ghana'),('GI','Gibraltar'),('GR','Greece'),('GL','Greenland'),('GD','Grenada'),
    ('GP','Guadeloupe'),('GU','Guam'),('GT','Guatemala'),('GG','Guernsey'),('GN','Guinea'),('GW','Guinea-Bissau'),('GY','Guyana'),
    ('H','Haiti'),('HM','Heard Island and McDonald Islands'),('VA','Holy See (the)'),('HN','Honduras'),('HK','Hong Kong'),
    ('HU','Hungary'),('IS','Iceland'),('IN','India'),('ID','Indonesia'),('IR','Iran (Islamic Republic of)'),('IQ','Iraq'),
    ('IE','Ireland'),('IM','Isle of Man'),('IL','Israel'),('IT','Italy'),('JM','Jamaica'),('JP','Japan'),('JE','Jersey'),
    ('JO','Jordan'),('KZ','Kazakhstan'),('KE','Kenya'),('KI','Kiribati'),('KP',"Korea (the Democratic People's Republic of)"),
    ('KR','Korea (the Republic of)'),('KW','Kuwait'),('KG','Kyrgyzstan'),('LA',"Lao People's Democratic Republic (the)"),
    ('LV','Latvia'),('LB','Lebanon'),('LS','Lesotho'),('LR','Liberia'),('LY','Libya'),('LI','Liechtenstein'),('LT','Lithuania'),
    ('LU','Luxembourg'),('MO','Macao'),('MK','Macedonia (the former Yugoslav Republic of)'),('MG','Madagascar'),('MW','Malawi'),
    ('MY','Malaysia'),('MV','Maldives'),('ML','Mali'),('MT','Malta'),('MH','Marshall Islands (the)'),('MQ','Martinique'),
    ('MR','Mauritania'),('MU','Mauritius'),('YT','Mayotte'),('MX','Mexico'),('FM','Micronesia (Federated States of)'),
    ('MD','Moldova (the Republic of)'),('MC','Monaco'),('MN','Mongolia'),('ME','Montenegro'),('MS','Montserrat'),
    ('MA','Morocco'),('MZ','Mozambique'),('MM','Myanmar'),('NA','Namibia'),('NR','Nauru'),('NP','Nepal'),
    ('NL','Netherlands (the)'),('NC','New Caledonia'),('NZ','New Zealand'),('NI','Nicaragua'),('NE','Niger (the)'),
    ('NG','Nigeria'),('NU','Niue'),('NF','Norfolk Island'),('MP','Northern Mariana Islands (the)'),('NO','Norway'),
    ('OM','Oman'),('PK','Pakistan'),('PW','Palau'),('PS','Palestine, State of'),('PA','Panama'),
    ('PG','Papua New Guinea'),('PY','Paraguay'),('PE','Peru'),('PH','Philippines (the)'),('PN','Pitcairn'),
    ('PL','Poland'),('PT','Portugal'),('PR','Puerto Rico'),('QA','Qatar'),('RE','Réunion'),('RO','Romania'),
    ('RU','Russian Federation (the)'),('RW','Rwanda'),('BL','Saint Barthélemy'),
    ('SH','Saint Helena, Ascension and Tristan da Cunha'),('KN','Saint Kitts and Nevis'),('LC','Saint Lucia'),
    ('MF','Saint Martin (French part)'),('PM','Saint Pierre and Miquelon'),('VC','Saint Vincent and the Grenadines'),
    ('WS','Samoa'),('SM','San Marino'),('ST','Sao Tome and Principe'),('SA','Saudi Arabia'),('SN','Senegal'),
    ('RS','Serbia'),('SC','Seychelles'),('SL','Sierra Leone'),('SG','Singapore'),('SX','Sint Maarten (Dutch part)'),
    ('SK','Slovakia'),('SI','Slovenia'),('SB','Solomon Islands'),('SO','Somalia'),('ZA','South Africa'),
    ('GS','South Georgia and the South Sandwich Islands'),('SS','South Sudan'),('ES','Spain'),('LK','Sri Lanka'),
    ('SD','Sudan (the)'),('SR','Suriname'),('SJ','Svalbard and Jan Mayen'),('SZ','Swaziland'),('SE','Sweden'),
    ('CH','Switzerland'),('SY','Syrian Arab Republic'),('TW','Taiwan (Province of China)'),('TJ','Tajikistan'),
    ('TZ','Tanzania, United Republic of'),('TH','Thailand'),('TL','Timor-Leste'),('TG','Togo'),('TK','Tokelau'),
    ('TO','Tonga'),('TT','Trinidad and Tobago'),('TN','Tunisia'),('TR','Turkey'),('TM','Turkmenistan'),
    ('TC','Turks and Caicos Islands (the)'),('TV','Tuvalu'),('UG','Uganda'),('UA','Ukraine'),
    ('AE','United Arab Emirates (the)'),('GB','United Kingdom of Great Britain and Northern Ireland (the)'),
    ('UM','United States Minor Outlying Islands (the)'),('US','United States of America (the)'),('UY','Uruguay'),
    ('UZ','Uzbekistan'),('VU','Vanuatu'),('VE','Venezuela (Bolivarian Republic of)'),('VN','Viet Nam'),
    ('VG','Virgin Islands (British)'),('VI','Virgin Islands (U.S.)'),('WF','Wallis and Futuna'),
    ('EH','Western Sahara*'),('YE','Yemen'),('ZM','Zambia'),('ZW','Zimbabwe')]
    country=models.CharField(max_length=50,default='None',choices=country_choices)
    pincode_regex=RegexValidator(regex=r'^[1-9][0-9]{5}$',message="Pincode must be entered in format: Up to 6 digits allowed.")
    pincode=models.CharField(validators=[pincode_regex],max_length=6,default=None,null=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.MyImageFieldName != self.MyImageFieldName:
                this.MyImageFieldName.delete()
        except: pass
        super(Profile, self).save(*args, **kwargs)