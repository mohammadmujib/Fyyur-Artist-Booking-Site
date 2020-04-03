from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, AnyOf, URL, Length, NumberRange, Optional
from enum import Enum
# from models import Artist, Venue, Show


class ShowForm(FlaskForm):
    artist_id = IntegerField(
        'artist_id',
        validators=[DataRequired(), NumberRange(
            min=1, message="Please enter a numeric ID")]
    )
    venue_id = IntegerField(
        'venue_id',
        validators=[DataRequired(), NumberRange(
            min=1, message="Please enter a numeric ID")]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )

class USState(Enum):
    AL = 'Alabama'
    AK = 'Alaska'
    AZ = 'Arizona'
    AR = 'Arkansas'
    CA = 'California'
    CO = 'Colorado'
    CT = 'Connecticut'
    DE = 'Delaware'
    FL = 'Florida'
    GA = 'Georgia'
    HI = 'Hawaii'
    ID = 'Idaho'
    IL = 'Illinois'
    IN = 'Indiana'
    IA = 'Iowa'
    KS = 'Kansas'
    KY = 'Kentucky'
    LA = 'Louisiana'
    ME = 'Maine'
    MD = 'Maryland'
    MA = 'Massachusetts'
    MI = 'Michigan'
    MN = 'Minnesota'
    MS = 'Mississippi'
    MO = 'Missouri'
    MT = 'Montana'
    NE = 'Nebraska'
    NV = 'Nevada'
    NH = 'New Hampshire'
    NJ = 'New Jersey'
    NM = 'New Mexico'
    NY = 'New York'
    NC = 'North Carolina'
    ND = 'North Dakota'
    OH = 'Ohio'
    OK = 'Oklahoma'
    OR = 'Oregon'
    PA = 'Pennsylvania'
    RI = 'Rhode Island'
    SC = 'South Carolina'
    SD = 'South Dakota'
    TN = 'Tennessee'
    TX = 'Texas'
    UT = 'Utah'
    VT = 'Vermont'
    VA = 'Virginia'
    WA = 'Washington'
    WV = 'West Virginia'
    WI = 'Wisconsin'
    WY = 'Wyoming'

    # Class method bound to its class rather than its object, it doesn't require a creation of class instance much like static method
    # The parameter is the class itself (whereas a static method knows nothing about tthe class just deals with the parameters)
    @classmethod
    def choices(cls):
        return [(choice.name, choice.name) for choice in cls]


class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired(), Length(min=2, max=120)]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(min=2, max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired(), AnyOf([choice.name for choice in USState])],
        choices=USState.choices()
    )
    address = StringField(
        'address', validators=[DataRequired(), Length(min=2, max=120)]
    )
    phone = StringField(
        'phone', validators=[DataRequired(), Length(min=2, max=120)]
    )
    image_link = StringField(
        'image_link', validators=[Optional(), URL()]
    )

    genres = SelectMultipleField(
        'genres', validators=[Optional()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website_link = StringField(
        'website_link', validators=[Optional(), URL()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[Optional(), URL()]
    )
    submit = SubmitField('Add Venue')


class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired(), Length(min=2, max=120)]
    )
    city = StringField(
        'city',
    )
    state = SelectField(
        'state', validators=[Optional(), AnyOf([(choice.name) for choice in USState])],
        choices=USState.choices()
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[Optional(), URL()]
    )

    genres = SelectMultipleField(
        'genres', validators=[Optional()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    website_link = StringField(
        'website_link', validators=[Optional(), URL()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[Optional(), URL()]
    )
    available_hours = StringField(
        'available_hours', validators=[Optional(), Length(min=5, max=5)]
    )

    def validate_available_hours(self, available_hours):
        available_hours_parts = available_hours.data.split('-')
        try:
            from_hour = int(available_hours_parts[0])
        except Exception:
            raise ValidationError("Invalid format for available hours.")

        try:
            to_hour = int(available_hours_parts[1])
        except Exception:
            raise ValidationError("Invalid format for available hours.")

        try:
            from_hour = int(available_hours_parts[0])
            to_hour = int(available_hours_parts[1])

            if to_hour <= from_hour:
                raise ValidationError("Invalid format for available hours.")
        except Exception:
            raise ValidationError("Invalid format for available hours.")

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
