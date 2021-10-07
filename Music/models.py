from django.db import models


# Create your models here.
class Music(models.Model):

    Songs_Category=[('Musical genres','Musical genres'), ('Musical theatre' ,'Musical theatre'),
                    ('Rock','Rock '), ('Jazz','Jazz '), ('Classical music','Classical music '),
                    ('Pop music' ,'Pop music '), ('Hip hop music','Hip hop music '),
                    ('Country music','Country music' ),('Blues','Blues'),
                    ('Popular music','Popular music'),('Rhythm and blues','Rhythm and blues'),('Folk music','Folk music'),
                    ('Reggae', 'Reggae'),('Singing','Singing'),('Punk rock','Punk rock'),('Electronic dance','Electronic dance'),
                    ('Techno','Techno'),('Heavy metal','Heavy metal'),
                    ('Dance music', 'Dance music'),('Funk','Funk'),('Alternative rock','Alternative rock'),
                    ('Soul music','Soul music'),('Instrumental','Instrumental'),('Disco','Disco'),
                    ('House music','House music'),('Rapping','Rapping'),('Opera','Opera'),
                    ('Dubstep','Dubstep'),('Orchestra','Orchestra'),('Gospel music','Gospel music'),
                    ('Soundtrack','Soundtrack'),('Ambient music','Ambient music'),('Rock and roll','Rock and roll'),
                    ('Grunge','Grunge'),('Music of Latin America','Music of Latin America'),
                    ('World music', 'World music'),('Indie rock','Indie rock'),('Electro','Electro'),
                    ('Trance music','Trance music'),('Music of the United States','Music of the United States'),
                    ('New wave','New wave'),('Ska','Ska'),('Pop rock','Pop rock'),
                    ('Art music','Art music'),('Progressive rock','Progressive rock'),
                    ('Drum and bass','Drum and bass'),('Dub','Dub'),
                    ('Easy listening','Easy listening'),('Vocal music','Vocal music'),
                    ('Industrial music','Industrial music'),('Rockabilly','Rockabilly'),
                    ('Psychedelic rock','Psychedelic rock'),]

    Langauge_Choices=(
        ('Persian','Persian'),
        ('English','English'),
        ('Kurdish','Kurdish')
    )

    Status_Choices=(
        ('RA','RECENTLY ADDED'),
        ('MW','MOST PLAYED'),
        ('TR','TOP RATED')
    )

    details = models.CharField(max_length=100,blank=False)
    song = models.FileField(upload_to='songs',blank=False)
    category=models.CharField(max_length=100,choices=Songs_Category)
    language=models.CharField(max_length=100,choices=Langauge_Choices)
    status = models.CharField(blank=False,choices=Status_Choices,max_length=2)
    artistname = models.CharField(max_length=100,blank=False)
    songname=models.CharField(max_length=100,blank=False)
    duration=models.IntegerField(blank=False)
    likescount=models.IntegerField(blank=False)
    dislikescount=models.IntegerField(blank=False)
    playscount=models.IntegerField(blank=False)
    facebooklink=models.URLField(blank=False)
    instalink=models.URLField(blank=False)
    lyrics=models.TextField(blank=False)
    coverart=models.ImageField(upload_to='coverart',blank=False)
    arregment=models.CharField(max_length=100,blank=False)
    singerfacebooklinks=models.URLField(blank=False)
    singerinstalink=models.URLField(blank=False)
    musicianname=models.CharField(max_length=100,blank=False)
    songaccent=models.CharField(max_length=100,blank=False)
    tag=models.CharField(max_length=100,blank=False)
    releasedyear=models.DateField()
    license=models.CharField(max_length=100,blank=False)
    isalbume=models.BooleanField(default=True)
    albumename = models.CharField(max_length=100, blank=True)
    ispodcast=models.BooleanField(default=True)
    hasvideo=models.BooleanField(default=True)

    def __str__(self):
        return self.songname

Link_Choice=(
        ('O','ONLINE PLAY LINK'),
        ('D','DOWNLOAD LINK')
    )

class MusicLink(models.Model):
    song=models.ForeignKey(Music,related_name='Music_link',on_delete=models.CASCADE)
    type=models.CharField(choices=Link_Choice,max_length=1)
    link=models.URLField()

    def __set__(self):
        return self.song
