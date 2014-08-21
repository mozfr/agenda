Présentation
============

L'Agenda MozFR [TEST] est une inspiré de l'agendadulibre.qc.ca
(Québec). Puisque ce dernier est disponible sous licence GPL Affero.

Cette version est disponible sous licence GNU Affero General Public License.
C'est une licence qui est plus restritive que la GNU General Public License
dû au fait qu'elle oblige les applications accessibles via le Web à rendre leur
 code source disponible. Le code source est disponible ici. 

L'Agenda MozFR [TEST]

Installation
========

Pour installer l'Agenda MozFR vous n'avez suivre les différentes
étapes suivantes, toutefois, assurez-vous d'avoir Python 2.7.x:

    $ git clone http://gitlab.anthony-maton.eu/anthony/agenda-mozfr.git
    $ cd agenda-mozfr
    $ python bootstrap.py
    $ bin/buildout

Les dépendances seront téléchargées et installées dans le répertoire courant.
Ensuite vous n'avez qui initialiser la base de données (SQLite en
développement):

    $ bin/django syncdb
    $ bin/django migrate
    $ sqlite3 agendadulibre < agenda/events/sql/region.sql
    $ sqlite3 agendadulibre < agenda/events/sql/city.sql
    
Et voilà, et pour lancer l'agenda:

    $ bin/django runserver

Vous n'avez qu'à ouvrir l'url suivante: http://127.0.0.1:8000 dans votre
navigateur !

Installation en production [NON TESTE]
===================

Pour installer l'Agenda en production, on vous conseille de ne pas 
utiliser SQLite3 car ce n'est pas une base de données très robuste pour un 
site web multi-usager. Nous avons donc choisit MySQL afin de faire rouler 
l'agenda en production.

Pour installer l'agenda en production il suffit de spécifier à buildout 
d'utiliser la configuration de production. Le tout compilera localement une
version de nginx et de uwsgi qui serviront l'agenda.

Vous n'avez donc qu'à suivre les étapes suivantes:

    $ git clone http://gitlab.anthony-maton.eu/anthony/agenda-mozfr.git
    $ cd agenda-mozfr
    $ python bootstrap.py
    $ bin/buildout -c production -vvv
    
Vous devez encore une fois initialiser la base de données:

    $ bin/django syncdb
    $ bin/django migrate
    $ mysql agendadulibre < agenda/events/sql/region.sql
    $ mysql agendadulibre < agenda/events/sql/city.sql
    
Ensuite, nous utilisons supervisor afin de faire rouler le tout:

    $ bin/supervisord
    
Vous pouvez toujours vous connecter à supervisor afin d'avoir plus de détails
sur les processus qui roulent:

    $ bin/supervisorctl
    
Vous n'avez qu'à ouvrir l'url suivante: http://127.0.0.1:8000 dans votre
navigateur !


