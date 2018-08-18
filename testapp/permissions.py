from models import Post
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


_content_type = ContentType.objects.get_for_model(Post)
perm_post = Permission.objects.create(
    codename='can_post',
    name="Can Publish Posts",
    content_type=_content_type,
)
perm_del_ipost = Permission.objects.create(
    codename='can_del_ipost',
    name="Can Delete Self's Posts",
    content_type=_content_type,
)
perm_del_all_post = Permission.objects.create(
    codename='can_del_all_post',
    name="Can Delete All Posts",
    content_type=_content_type,
)
perm_del_icomment = Permission.objects.create(
    codename='can_del_icomment',
    name="Can Delete Self's Comments",
    content_type=_content_type,
)
perm_del_all_comment = Permission.objects.create(
    codename='can_del_all_comment',
    name="Can Delete All Comments",
    content_type=_content_type,
)
