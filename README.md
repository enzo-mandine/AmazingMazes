La Plateforme_: **Amazing Mazes**

# Un peu d’histoire …
  Dans la mythologie grecque ,le Labyrinthe était une construction complexe et se
  trouvait à Knossos. Il a été construit par l'ingénieur Dédale pour le roi mythique de
  Crète, Minos. La raison pour laquelle il a été construit ,c'était pour enfermer le
  Minotaure, une créature mi-homme mi-taureau. Dédale lui-même a construit le
  labyrinthe d'une façon si minutieuse et compliquée que même lui a réussi avec
  beaucoup de difficulté s'en sortir quand il a achevé son oeuvre.
  La ville d'Athènes avait perdu une bataille contre la Crète et c'est pour cela qu'elle était
  obligée d'envoyer sept jeunes hommes et sept jeunes filles comme sacrifice au
  Minotaure. Thésée, le fils du roi d'Athènes a participé volontairement à l'équipe qui
  tuerait le Minotaure et libérerait la ville d'Athènes de la souveraineté de Crète. La fille du
  roi Minos ,Ariane lui donne une pelote de fil pour lui permettre de retrouver la sortie
  après son exploit. Thésée est entré dans le labyrinthe , a tué le Minotaure et s'est sauvé
  de Crète en emmenant Ariane.
  Ce mythe est un des plus importants de la mythologie grecque . Il a été conservé vivant
  pendant tous ces siècles, parmi les labyrinthes du monde entier!
  La forme la plus connue du labyrinthe est la forme du labyrinthe Crétois. Les sept
  anneaux des sentiers se font facilement en dessinant une croix et quatre points qu'on
  relie jusqu'à former huit cycles concentriques en laissant sept anneaux vides. C'est une
  forme fascinante qui a laissé ses traces dans l'histoire de la Civilisation depuis 5.000
  ans….
  
# Dedale
  Le labyrinthe légendaire de Crète a été audacieusement pensé et dessiné par un
  ingénieur. Cette méthode est néanmoins limitée, c’est pourquoi la création d’un
  générateur automatique vous est demandée.
  
# La première pierre
  Votre programme devra prendre en entrée une taille de Labyrinthe sous forme
  numérique: 10, 100, 500 …. Les labyrinthes étant carres, une seule valeur est nécessaire
  en input.
  Le labyrinthe généré doit être affiché dans un fichier dont le nom doit être, aussi,
  demandé à l’utilisateur.
  L'entrée se situe en haut à gauche et la sortie en bas à droite, dans tous les cas.
  Les murs sont représentés par le caractère ‘ # ‘ et les espaces vides par le caractère ‘ .
  ‘.
  Le labyrinthe doit appartenir à la famille des labyrinthes parfaits. C’est à dire qu’il doit
  exister un chemin, et un seul, reliant deux espaces vides pris aléatoirement dans le
  labyrinthe.
  L’algorithme utilisé doit être le “récursive backtrack” pour cette première version.
  Attention, la taille donnée représente le nombre de couloirs … Par exemple, un labyrinthe
  de taille 5 ressemble à ceci:
  
# La complexité c’est bien
  Si il est un algorithme simple, efficace et esthétique, c’est bien le récursive BackTrack.
  Malheureusement sa faible complexité en terme de résolution n’en fait pas un choix
  intéressant pour la génération de labyrinthes difficiles.
  Pour cette deuxième partie, re-implémentez votre générateur en vous appuyant sur
  l’algorithme de Kruskal.
  
# A l’aveugle
  Afin de tester vos générateurs, vous allez créer différents algorithmes d’explorations.
  En premier lieu, comme pour la génération, servez vous du Récursive Backtracking pour
  relier l'entrée du labyrinthe a sa sortie.
  Vous afficherez le labyrinthe et sa solution dans un fichier dont le nom devra être
  demandé à l’utilisateur.
  Les espaces vides à emprunter pour rejoindre la sortie du labyrinthes doivent être
  représentés par le caractère ‘ o ‘.
  Les espaces vides explorés mais ne participant pas au chemin final doivent être
  représenté par le caractère ‘ * ‘.
  
# Avec ariane
  Implémenter à nouveau votre explorateur de labyrinthes avec l’algorithme AStar (A*).
  Les espaces vides à emprunter pour rejoindre la sortie du labyrinthes doivent être
  représentés par le caractère ‘ o ‘.
  Les espaces vides explorés mais ne participant pas au chemin final doivent être
  représenté par le caractère ‘ * ‘.

# Ascii to JPG
  Ecrivez un programme (ou une fonctionnalite supplementaire a votre generateur /
  explorateur) permettant de visualiser en image vos labyrinthes générés ainsi que leur
  solution et leur parcours d’exploration sous la forme suivante:
  
# Entrer dans la légende …
  Confrontez votre générateur et votre explorateur a des labyrinthes de tailles toujours
  plus grandes … 1 000, 10 000, 100 000 … Quelles conclusions pouvez vous en tirer ?
  Quelles différences en fonction des différents algorithmes utilisés ?

# Source
  https://github.com/enzo-mandine/AmazingMazes/blob/main/Amazing_Mazes.pdf
