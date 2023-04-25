from app import app
from models import db, Production, Role, Actor
from faker import Faker

#application context - gives us access to context and data within the application we are working on as it is running 
#need to use with_context to use seeds 

with app.app_context():
    Production.query.delete()
    Role.query.delete()
    Actor.query.delete()

    #prod = Production(title='', genre='', length='', image='', language='', director='', description='')
    menu = Production(title='the menu', 
                      genre='thriller', 
                      length=107, 
                      image='https://m.media-amazon.com/images/M/MV5BMzdjNjI5MmYtODhiNS00NTcyLWEzZmUtYzVmODM5YzExNDE3XkEyXkFqcGdeQXVyMTAyMjQ3NzQ1._V1_FMjpg_UX1000_.jpg', 
                      language='english', 
                      director='mark mylod', 
                      description='Painstakingly prepared.  Brilliantly executed.', 
                      composer='colin stetson',
                      year=2022
                      )
    
    everything = Production(
        title="everything everywhere all at once",
        genre='sci-fi',
        length=139,
        image="https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyMTgtYzk5Y2M3ZDVmMDk1XkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_FMjpg_UX1000_.jpg",
        language='english, mandarin',
        director='daniel kwan',
        description='Sucked into a bagel.',
        composer='son lux',
        year=2022
    )
    guardians = Production(
        title="guardians of the galaxy vol. 2",
        genre='sci-fi',
        length=137,
        language='english',
        image='https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_FMjpg_UX1000_.jpg',
        composer='tyler bates',
        year=2017,
        director='james gunn',
        description='when things get bad, they\'ll do their worst'
    )
    budapest = Production(
        title='the grand budapest hotel',
        genre='comedy',
        length=100,
        year=2014,
        image='https://m.media-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_FMjpg_UX1000_.jpg',
        language='english',
        director='wes anderson',
        composer='alexandre desplat',
        description='keep your hands off my lobby boy!'
    )
    ind = Production(
        title='independence day',
        genre='sci-fi',
        length=145,
        image='https://m.media-amazon.com/images/M/MV5BMGQwNDNkMmItYWY1Yy00YTZmLWE5OTAtODU0MGZmMzQ1NDdkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg',
        language='english',
        director='roland emmerich',
        composer='david arnold',
        description='we\'ve always believed we weren\'t alone'
    )

    wicked = Production(
        title="wicked",
        genre="drama",
        length=1,
        image="https://m.media-amazon.com/images/I/61Dyzt7uM9L._AC_UF894,1000_QL80_.jpg",
        director='jon m chu',
        composer='stephen schwartz',
        description='it\'s just life, so keep dancing through'
    )

    shark = Production(
        title="shark tale",
        genre="childrens",
        image="https://m.media-amazon.com/images/M/MV5BMTMxMjY0NzE2M15BMl5BanBnXkFtZTcwNTc3ODcyMw@@._V1_FMjpg_UX1000_.jpg",
        length=90,
        director='vicky jenson',
        composer='hans zimmer',
        description='behind every little fish is a great white lie'
    )
    amsterdam = Production(
        title="amsterdam",
        genre="mystery",
        image="https://m.media-amazon.com/images/M/MV5BNDQwNzE0ZTItYmZjMC00NjI3LWFlNzctNTExZDY2NWE0Zjc0XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_FMjpg_UX1000_.jpg",
        length=134,
        director="david o russell",
        composer="daniel pemberton",
        description="let the love, murder, and conspiracy begin"
    )

    nope = Production (
        title='nope',
        genre='sci-fi',
        image='https://m.media-amazon.com/images/M/MV5BOGJhYzAwN2MtNjA1Ny00ZjJiLWFmNzYtMDgzNTUzYjc5NTIzXkEyXkFqcGdeQXVyMTUzOTcyODA5._V1_.jpg',
        length=130,
        director='jordan peele',
        composer='michael abels',
        description='nope'
    )

    timeToDie = Production(
        title='no time to die',
        genre='action',
        image='https://m.media-amazon.com/images/M/MV5BYWQ2NzQ1NjktMzNkNS00MGY1LTgwMmMtYTllYTI5YzNmMmE0XkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_.jpg',
        length=163,
        director='cary joji fukunaga',
        composer='hans zimmer',
        description='the mission that changes everything begins',
        year=2021,
        language='english'
    )

    knives = Production(
        title='knives out',
        genre='mystery',
        image='https://m.media-amazon.com/images/M/MV5BMGUwZjliMTAtNzAxZi00MWNiLWE2NzgtZGUxMGQxZjhhNDRiXkEyXkFqcGdeQXVyNjU1NzU3MzE@._V1_.jpg',
        length=130,
        director='rian johnson',
        composer='nathan johnson',
        description='Everyone has a motive. No one has a clue. Hell, any of them could have done it.',
        year=2019,
        language='english'
    )

    productions=[knives, timeToDie, nope, amsterdam, shark, wicked,ind, budapest, guardians,everything, menu]
    db.session.add_all(productions)
    db.session.commit()

    #actor = Actor(name='', image='', age=-1, country='')
    anya = Actor(
        name='anya taylor-joy',
        age=27,
        country="usa",
        image="https://m.media-amazon.com/images/M/MV5BMTllYmE5YTYtZGZmYy00ZTBlLWJlODEtYWQ0ZmU1YTJkMjJlXkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_FMjpg_UX1000_.jpg"
    )
    fiennes = Actor(
        name='ralph fiennes',
        age=60,
        country='england',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg/440px-Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg'
    )
    yeoh = Actor(
        name='michelle yeoh',
        age=60,
        country='malaysia',
        image='https://m.media-amazon.com/images/M/MV5BMTg0NTI0NDkzOF5BMl5BanBnXkFtZTcwMjYwMTIwNw@@._V1_FMjpg_UX1000_.jpg'
    )
    goldblum = Actor(
        name='jeff goldblum',
        age=70,
        country='usa',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Jeff_Goldblum_by_Gage_Skidmore_3.jpg/440px-Jeff_Goldblum_by_Gage_Skidmore_3.jpg'
    )
    saldana = Actor(
        name='zoe saldana',
        age=44,
        country='usa',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Avatar_The_Way_of_Water_Tokyo_Press_Conference_Zoe_Salda%C3%B1a_%2852563431865%29_%28cropped2%29.jpg/440px-Avatar_The_Way_of_Water_Tokyo_Press_Conference_Zoe_Salda%C3%B1a_%2852563431865%29_%28cropped2%29.jpg'
    )
    smith = Actor(
        name='will smith',
        age=54,
        country='usa',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/TechCrunch_Disrupt_2019_%2848834434641%29_%28cropped%29.jpg/440px-TechCrunch_Disrupt_2019_%2848834434641%29_%28cropped%29.jpg'
    )
    deniro = Actor(
        name='robert deniro',
        age=79,
        country='usa',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Robert_De_Niro_2011_Shankbone.JPG/440px-Robert_De_Niro_2011_Shankbone.JPG'
    )
    kaluuya = Actor(
        name='daniel kaluuya',
        age=34,
        country='england',
        image='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Daniel_Kaluuya_%2835411578144%29_%28cropped_2%29.jpg/440px-Daniel_Kaluuya_%2835411578144%29_%28cropped_2%29.jpg'
    )
    yeun=Actor(
        name='steven yeun',
        age=39,
        country='korea',
        image='https://flxt.tmsimg.com/assets/553525_v9_bb.jpg'
    )
    keke = Actor(
        name="keke palmer",
        age=29,
        country="usa",
        image="https://flxt.tmsimg.com/assets/302753_v9_bb.jpg"
    )

    armas = Actor(
        name='ana de armas',
        age=34,
        country='cuba',
        image='https://m.media-amazon.com/images/M/MV5BMjg5NzcwNTYyN15BMl5BanBnXkFtZTgwNTQ2NjgzNTM@._V1_FMjpg_UX1000_.jpg'
    )
    curtis = Actor(
        name='jamie lee curtis',
        age=64,
        country='usa',
        image='https://cdn.britannica.com/72/238172-050-05FB9A3C/American-actress-Jamie-Lee-Curtis-2021.jpg'
    )

    actors=[curtis, armas, keke, yeun, kaluuya, deniro, smith, saldana, goldblum, yeoh,fiennes, anya]
    db.session.add_all(actors)
    db.session.commit()

    #role = Role(role_name='', production_id=-1, actor_id=-1)
    margot = Role(
        role_name='Margot', 
        actor=anya,
        production=menu
    )
    chef = Role(
        role_name='Chef Slowik',
        actor=fiennes,
        production=menu
    )
    evelyn = Role(
        role_name='Evelyn Quan Wang',
        actor=yeoh,
        production=everything
    )
    monsieur=Role(
        role_name='Monsieur Gustave H.',
        actor=fiennes,
        production=budapest
    )
    deputy=Role(
        role_name="Deputy Vilmos Kovacs",
        actor=goldblum,
        production=budapest
    )
    aleta=Role(
        role_name='Aleta Ogord',
        actor=yeoh,
        production=guardians
    )
    gamora=Role(
        role_name='gamora',
        actor=saldana,
        production=guardians
    )
    levinson=Role(
        role_name='David Levinson',
        actor=goldblum,
        production=ind
    )
    captain=Role(
        role_name='Captain Steven Hiller',
        actor=smith,
        production=ind
    )
    wizard=Role(
        role_name="The Wonderful Wizard of Oz",
        actor=goldblum,
        production=wicked
    )
    morrible=Role(
        role_name="Madame Morrible",
        actor=yeoh,
        production=wicked
    )
    oscar = Role(
        role_name='Oscar',
        actor=smith,
        production=shark
    )
    don = Role(
        role_name='Don Lino',
        actor=deniro,
        production=shark
    )
    libby = Role(
        role_name='Libby Voze',
        actor=anya,
        production=amsterdam
    )
    irma = Role(
        role_name='Irma St. Clair',
        actor=saldana,
        production=amsterdam
    )
    gilbert = Role(
        role_name="Gilbert Dillenbeck",
        actor=deniro,
        production=amsterdam
    )
    oj = Role(
        role_name='Otis OJ Haywood Jr',
        actor=kaluuya,
        production=nope
    )
    jupe=Role(
        role_name="Ricky Jupe Park",
        actor=yeun,
        production=nope
    )
    em = Role(
        role_name="Emerald Em Haywood",
        actor=keke,
        production=nope
    )
    paloma = Role(
        role_name='Paloma',
        actor=armas,
        production=timeToDie
    )
    mallory = Role(
        role_name='Gareth Mallory / M',
        actor=fiennes,
        production=timeToDie
    )
    marta = Role(
        role_name='Marta Cabrera',
        actor=armas,
        production=knives
    )
    drysdale = Role(
        role_name="Linda Drysdale",
        actor=curtis,
        production=knives
    )
    deidre = Role(
        role_name="Deirdre Beaubeirdre",
        actor=curtis,
        production=everything
    )

    roles = [deidre, drysdale, marta, mallory, paloma, em, jupe, oj, gilbert, irma, libby, don, oscar, morrible, wizard, captain, levinson, gamora, aleta, deputy, monsieur, evelyn, chef, margot]
    db.session.add_all(roles)
    db.session.commit()