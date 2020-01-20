# test

1- installation de djnago

2- Creation du projet "django-project"
	```> django-admin startproject django-admin django-project```

3- Lancer le serveur
	```> py manage.py runserver```

4- Ajouter une applicatoon blog 
	```> py manage.py startapp blog```
	cette application doit etre créer dans le meme niveau que manage.py pour qu’elle puisse être importée comme module.

5- Pour la partie Front-end

	- j'ai créé un ficher main.css qui contient le style des pages
	- j'ai créé un repértoire template qui contient les pages .html

6- Les templates

	- Afin d'éviter la répétition de code dans les fichiers .html, j'ai créé un fichier base.html qui contient la base du site web (la partie inchangeable du site web)


	
7- Article

	- Le fichier Models contient les champs et le comportement essentiels des données que vous stockez
	
	- J'ai créé une classe Post a comme attributs: titre, texte, image et tags

	- ```Post.objects.all()```=> retourne les articles dans la base de données

	

8- Database : sqlite

9- Lister les articles

	- créer un URL qui permet de lister les articles dans le fichier urls.py
	  path('', PostListView.as_view(), name='blog-home')

	- créer une classe PostListView permet de lister les articles et les envoyer a la template home.html dans le fichier views.py

	- Lister les articles : 
	  {% for post in posts %}
	  	{{ post.title }}
	  {% endfor %}

10- Afficher le Détail d'un article

	- créer un URL qui permet de lister les articles dans le fichier urls.py
	  path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),

	- créer une classe PostDetailView dans le fichier views.py permet de afficher un article dans la template post_detail.html 

	- Lister l'article : 
	  {{ object.title }}

11- Ajouter un article

	- créer un URL dans le fichier urls.py qui permet d'ajouter un article 
	  	path('post/new/', PostCreateView.as_view(), name='post-create'),

	- créer une classe PostCreateView dans le fichier views.py permet d'ajouter un article et la template post_form.html représente une formulaire d'ajout

16- Modifier un article

	- créer un URL dans le fichier urls.py qui permet de modifier un article 
	  	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	  pk representer l'id de l'article


	- créer une classe PostUpdateView dans le fichier views.py permet de modifier un article


17- Supprimer un article

	- créer un URL dans le fichier urls.py qui permet de supprimer un article 
	 	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

	- créer une classe PostDeleteView dans le fichier views.py permet de supprimer un article et la template post_confirm_delete.html represente un choix de confirmation de suppriession ou non

	- Si la suppression est confirmé, il se derige vers la page home

18- Compte Administrateur

	- j'ai créer une formulaire qui permet à l'administrateur de s'authentifier (hanane, elmeskinehanane)
	
	- lorsque l'administarteur est identifiée, une boutton d'ajout d'article s'ajoute dans la barre ainsi que la possibilite de supprimer et/ou modifier article




















