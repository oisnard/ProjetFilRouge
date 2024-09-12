cat_code_definition = { 10 : 'Livres',
                        2280 : 'Journaux-Magazines',
                        50 : 'Gaming - Accessoires',
                        1280 : 'Jeux Enfants',
                        2705 : 'Livres',
                        2522 : 'Accessoires Bureautiques',
                        2582 : 'Equipements Jardins',
                        1560 : 'Mobiliers et accessoires',
                        1281 : 'Jeux enfants',
                        1920 : 'Coussins - rideaux - literie accessoires',
                        2403 : 'Livres - Magazines',                     #Similitudes avec 2705, 2280
                        1140 : 'Univers Mangas-Star Wars - porte-clés',
                        2583 : 'Piscine & ses accessoires',              #OK 
                        1180 : 'Jeux Enfants',                           #Similitudes avec 1280, 1281
                        1300  : 'Drones - Maquettes - Accessoires',      #Similitudes pour les accessoires
                        2462 : 'Jeux video',
                        1160 : 'Cartes Jeux',
                        2060 : 'Décoration',                             #Fourre-tout - similitudes avec d'autres cat
                        40 : 'Jeux vidéos & accessoires',                #Très fortes similitudes avec 2462
                        60 : 'Gaming - consoles',                        #Fortes similitudes avec 40, 2462
                        1320 : 'Equipements Bébés',
                        1302 : 'Jeux enfants - camping',                 # Fortes disparités
                        2220 : 'Equipements animalerie',
                        2905 : 'Jeux vidéo à télécharger',               #Designation devrait permettre l'identification
                        2585 : 'Bricolage - outillage - jardinage',      #Similitudes 
                        1940 : 'Nourritures - livres',                   #Problèmes pour identification livres
                        1301 : 'Chaussettes Bébés - Fléchettes - babyfoot'} #Fourre-tout...

list_similitudes = [[10, 2705, 2403, 2280],         # Livres, Magazines
                    [40, 50, 60, 1140, 1160, 1180, 1280, 1281, 1300, 1302, 2462, 2905], #Jeux, jouets
                    [1560, 1920, 2060, 2522],       #Equipements intérieurs : mobiliers, déco, accessoires déco
                    [2583, 2582, 2585, 2220],             #Brico, Jardin Animalerie
                    [1320, 1301],                   # Equipements bébés
                    [1940]]                         # Nourritures + exceptions...
                    


#print(len(cat_code_definition.keys()))

#sum = 0
#for list in list_similitudes:
#    sum = sum + len(list)

#print(sum)
