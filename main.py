import django_setup

from myproject.myapp.models import Genre, Game


action = Genre.objects.create(name='Action')
rpg = Genre.objects.create(name='RPG')



game1 = Game.objects.create(
    title='Mafia II',
    release_year=2010,
    rating=9
)
game1.genres.set([action])

game2 = Game.objects.create(
    title='Dark Souls',
    release_year=2011,
    rating=8
)
game2.genres.set([rpg])

