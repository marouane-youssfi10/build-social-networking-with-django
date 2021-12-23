from .models import PostJobs

def most_viewed_this_week(request):
    jobs_most_viewed_this_week = None
    if request.user.is_authenticated:
        # sorting projects viewers from max to min
        jobs = PostJobs.objects.all()
        jobs_most_viewed_this_week = []
        cmp = 0
        for job in jobs:
            for i in job.viewers_job.all():
                cmp = cmp + 1
            jobs_most_viewed_this_week.append({
                'job_id': job.id,
                'name_jobs': job.name_jobs,
                'price': job.price,
                'description_job': job.description_job,
                'counting': cmp,
            })
            cmp = 0
        jobs_most_viewed_this_week = sorted(jobs_most_viewed_this_week, key=lambda x: x['counting'], reverse=True)

    return dict(jobs_most_viewed_this_week=jobs_most_viewed_this_week)

def top_jobs(request):
    jobs = PostJobs.objects.all()
    top_jobs = []
    cmp = 0
    for job in jobs:
        # count all viewers_job
        for i in job.viewers_job.all():
            cmp = cmp + 1
        # count all likes
        for j in job.likes.all():
            cmp = cmp + 1
        # count all comment post
        for z in job.post_job_comment.all():
            cmp = cmp + 1
        top_jobs.append({
            'job_id': job.id,
            'name_jobs': job.name_jobs,
            'price': job.price,
            'description_job': job.description_job,
            'counting': cmp,
        })
        cmp = 0
    top_jobs = sorted(top_jobs, key=lambda x: x['counting'], reverse=True)

    return dict(top_jobs=top_jobs)