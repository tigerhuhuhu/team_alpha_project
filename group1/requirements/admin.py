from django.contrib import admin

from requirements.models import files
from requirements.models import iteration
from requirements.models import project
from requirements.models import story
from requirements.models import story_comment
from requirements.models import story_attachment
from requirements.models import task
from requirements.models import user_association
from requirements.models import backlog

admin.site.register(files.ProjectFile)
admin.site.register(iteration.Iteration)
admin.site.register(project.Project)
admin.site.register(story.Story)
admin.site.register(story_comment.StoryComment)
admin.site.register(story_attachment.StoryAttachment)
admin.site.register(user_association.UserAssociation)
admin.site.register(backlog.Backlog)