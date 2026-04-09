from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

        # Create activities
        Activity.objects.create(user=ironman, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=batman, activity_type='cycle', duration=45, date=timezone.now())
        Activity.objects.create(user=superman, activity_type='swim', duration=60, date=timezone.now())
        Activity.objects.create(user=captain, activity_type='walk', duration=20, date=timezone.now())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=batman, score=90, rank=2)
        Leaderboard.objects.create(user=superman, score=80, rank=3)
        Leaderboard.objects.create(user=captain, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
