Project Name : 
  albums 

Application Functionality :
  - users could create User account and Profile account (accounts app)
    (photo could belong to one or more tag)
  - users could upload photos and do crud applications on their own photo
  - users could comment, like and dislike photos 
  - users see their own uploaded photos
  - users see uploaded photos by specific user
  - users see mose liked photos
  - users see uploaded photos by specific user

  Functionality to add in future:
  - Following system to allow users to follow each other (search for third party app)
  - Add Groups to allow users to bellong to one or many group (search for third party app)



Applications: 
  accounts
  album  

Models:
  album models:
    post:
      title
      image
      likes
      dislikes
      created_date
      updated_date
      comments
      author
    comment:
      body
      created_date
      updated_date
      author

Urls:
  path('accounts', include( ... ))
  path('albums', include( ... ))

  accouts.urls :
    custum urls of the official documentations
  album.urls :
    path('', views.index, name='blog-index'),
    # posts urls for crud operations
    path('posts/', views.PostList.as_view(), ... ),
    path('posts/<int:tag_id>', views.PostListByTag.as_view(), ... ),
    path('post/add/', views.PostCreate.as_view(), ...),
    path('post/<int:pk>/detail/', views.PostDetail.as_view(), ...),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), ...),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), ...),

Views:
  album.views:
    PostList: retrieve post_list
    PostListByTag: retrieve post_list filtred by tags
    PostCreate: create post
    PostDetail: retrieve post detail
    PostUpdate: update post
    PostDelete: delete post

    
Templaest:
  templates/albums/:
    album_list.html
    album_detail.html
    album_create_form.html
    album_update_form.html
    album_confirm_delete.html
    pagination.html

