from django.db import models
from app.cores.date import get_today_datetime


class TagManager(models.Manager):

    def get_all_tag(self):
        return self.get_queryset().all().values().order_by('-create_at')

    def get_tag_by_id(self, id):
        return self.get_queryset().filter(id=id).values().first()

    def get_tag_by_slug(self, slug):
        return self.get_queryset().filter(slug=slug).values().first()

    def create_tag(self, name, slug):
        return self.create(name=name, slug=slug)

    def update_tag_by_id(self, data, id):
        return self.get_queryset().filter(id=id).update(**data, update_at=get_today_datetime())

    def delete_tag_by_id(self, id):
        return self.get_queryset().get(id=id).delete()


class Tag(models.Model):
    class Meta:
        db_table = 'tag'
        default_related_name = 'tag'

    name = models.CharField(max_length=250, null=False, blank=False)
    slug = models.CharField(max_length=250, unique=True, null=False, blank=False)
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = TagManager()
