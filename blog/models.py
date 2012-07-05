from django.db import models
from django.contrib import admin
class Post(models.Model):
    title= models.CharField(max_length=60)
    body= models.TextField()
    created= models.DateField()
    updated= models.DateField()
    

    def __unicode__(self):
	return self.title 


class Comment(models.Model):
    body= models.TextField()
    author= models.CharField(max_length=60)
    created= models.DateField()
    updated= models.DateField()
    post= models.ForeignKey(Post)
    
    def body_first_60(self):
	return self.body[:60]

    def __unicode__(self):
	return self.body
class CommentInline(admin.TabularInline):
    model= Comment

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','created','updated')
    search_fields=('title','body')
    list_filter=('created',)
    inlines =[
	CommentInline,
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display =('author','body_first_60','created','updated')
    list_filter=('created', 'author')

# Create your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
