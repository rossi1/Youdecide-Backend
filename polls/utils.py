import cloudinary
from django_celery_beat.models import  PeriodicTask, ClockedSchedule


def filter_votes(instance):
    """ 
    Custom function to filter related voters ids 
    And return list of voters username on a poll 
       
    """
    voter_list = []

    for voter_id in instance:
            for voters_name in voter_id.values():
                if voters_name is None:
                    continue
                else:
                    voter_list.append(voters_name)
    
    return voter_list


def schedule_task(date):
    schedule = ClockedSchedule.objects.create(clocked_time=date)

    return schedule


def create_task(schedule, id):
    task =''

    print(task)

    return task

def cloudinary_upload_image(file):
    upload = cloudinary.uploader.upload(file, resource_type = "video")
    return upload['secure_url']


def cloudinary_upload_video(file):
    upload = cloudinary.uploader.upload(file, resource_type = "video")
    return upload['secure_url']

    