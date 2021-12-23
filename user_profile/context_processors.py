from accounts.models import UserProfile

def most_viewed_people(request):
    user_profile = UserProfile.objects.all()
    # sorting user_profile viewers from max to min
    most_viewed_user_people = []
    cmp = 0
    for profile in user_profile:
        for i in profile.viewers.all():
            cmp = cmp + 1
        most_viewed_user_people.append({
            'profile_id': profile.id,
            'user': profile.user,
            'title': profile.title,
            'counting': cmp,
        })
        cmp = 0
    most_viewed_user_people = sorted(most_viewed_user_people, key=lambda x: x['counting'], reverse=True)

    return dict(most_viewed_user_people=most_viewed_user_people[0:5])