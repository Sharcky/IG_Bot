"""
Desenvolvido 02/03/2021

Autor: MR.Kobay 
Site: http://mrkobay.com/
Para mais codigos contate: programador_enrolado
Redes sociais - Instagram: programador_enrolado -
"""
from time import sleep
from instapy import InstaPy

session = InstaPy(username="USUARIO", password="USV4RI0").login()
session.login()


#Não ira segir usuarios que tenham contas privadas.
#Não ira segir usuarios que não tenham foto de perfil.
#Não ira segir usuarios que tenham contas comerciais. 
#Não ira segir usuarios que tenham contas comerciais nas categorias especificas. 
session.set_skip_users(skip_private=True,
private_percentage=100,
skip_no_profile_pic=False,
no_profile_pic_percentage=100,
skip_business=True,
skip_non_business=False,
business_percentage=100,
skip_business_categories=["vendas", "hotmart", "cursos", "investimento", "vendasonline",  ],
dont_skip_business_categories=[],
skip_bio_keyword=[],
mandatory_bio_keywords=[])

# Ira seguir 50% dos usuarios que curtiram postagens nas categorias maracadas.
session.set_do_follow(True, percentage= 50) 

# Com isso, seu bot não interagirá com postagens de usuários que têm mais de 8.500 seguidores.
session.set_relationship_bounds(enabled=True, max_followers=8500)

#Curte categorias especificas. 25 Likes para cada categoria. 
session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)
session.like_by_tags(["programadorbrasil", 
"programadores", 
"programadora", 
"programadorbr", 
"computador",
"programadorpython"], amount=25) 

#Não ira curtir post com estas categorias.
session.set_dont_like(["proibido", "adulto", "porno"])  

# Comentar em 50% das categorias marcadas. Tres comentarios aleatorios deixados em cada post
session.set_delimit_commenting(enabled=True, max_comments=300, min_comments=20)
session.set_do_comment(True, percentage=50)
session.set_comments(["COMENTARIO", "COMENTARIO", "COMENTARIO"]) 

# Segue os seguidores de outro usuario
session.follow_user_followers(['programador_enrolado', 'programador_enrolado', 'programador_enrolado'], amount=1000, randomize=True, sleep_delay=600)

#Parar de seguir todos os usuarios seguidos pelo bot
session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)

# FINALIZA  A SESSÃO
session.end()

