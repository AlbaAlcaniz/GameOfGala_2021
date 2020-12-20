letter = [
'Querida Gala, \n\nDebido a la gran ayuda que me prestaste justo hace un año, he pensado en pedirte tus servicios una vez más. Así que tengo una misión para ti. ¿Me podrás ayudar?',
'¡Perfecto! Ven a palacio cuando estés lista para que te explique la misión.\nDebido a los acontecimientos de hace un año, hemos aumentado la seguridad en palacio. Para entrar, solo necesitas saber que la piña es azul.\n\nSaludos royales,\nPrincesa Miguelina',
'Debido a motivos de seguridad, esta carta se autodestruirá en'
]

kingdom_map_positions = {
    'Balloon consulting': [18,1,83,161],
    'Hector': [407,127,456,209],
    'Castillo': [446,226,528,338],
    'Laberinto': [458,475,677,558],
    'Villafoto': [212,311,269,406],
    'Sofi': [157,112,210,188],
    'Tren': [554,32,621,122],
    'Abandonada': [30,220,87,320],
}


image_paths = {
    'audio/castle.wav': [],
    'figures/0_2_miguelina.png': [
        '\n¡La princesa Miguelina no despierta!',
        'Sus sueños adolescentes son profundos, pero esto ya pasa de castaño oscuro.',
        'Vamos a consultar la sabiduría alcañicil, a ver si saben qué le pasa.'
    ],
    'figures/0_3_alcanicil.png': [
        'La red telepática de los hermanos Alcañiz nos dice que...',
        '¡Han hechizado a la princesa!\n',
        'Necesitamos encontrar el conjuro para despertarla.'
    ],
    'figures/0_4_letsgo.png': [
        'Los hermanos Alcañiz dicen que ellos nos ayudarán.',
        'A través de la red, nos guiarán en esta aventura por el reino.',
        'Tendremos que visitar a los miembros de la familia...',
        'a cambio de ayudarles en pequeñas misiones, nos darán partes del conjuro',
        '\n¡VAMOS ALLÁ!'
    ],
    'move0': [],
    'audio/1_1_explanation.wav': [],
    'figures/1_1_explanation.png': [
        'Teresa se ha presentado a un concurso de fotografía en VillaFoto',
        '¡pero su foto está llena de cartas!\n',
        'Debes retirar las cartas de encima de la foto para que pueda participar.',
        'Para ello, tienes que encontrar la pareja de cada una de las cartas,',
        'si tocas dos cartas seguidas con el mismo número, éstas desaparecerán.'
    ],
    'memory_game': [],
    'figures/1_3_congrats.png': [
        '¡Muy bien!\nConseguiste sacar las cartas de la foto.',
        'Gracias a ello,\n¡Teresa ha ganado el concurso!'
    ],
    'move1': [],
    'audio/2_1_explanation.wav': [],
    'figures/2_1_explanation.png': [
        'Héctor y María quieren saber la clasificación del fútbol.',
        'Para saber la posición de los equipos, necesitan resolver unas sumas.',
        '¿Los puedes ayudar?\n'
    ],
    'futbol_game': [],
    'figures/2_3_congrats.png': [
        '¡Conseguido!\n',
        'Cómo no, el Valencia va primero.\n',
        'Y el Barça ni aparece en la clasificación de lo malo que es...'
    ],
    'move2': [],
    'audio/3_1_explanation.wav': [],
    'figures/3_1_explanation.png': [
        'El tren del reino se ha estropeado, y Paco y Mari han decidido arreglarlo.',
        'Pero están teniendo problemas para entender las instrucciones del tren.',
        'Completa las series numéricas para ayudarles.\n',
        'Asociando el número que encuentres con su letra del abecedario...',
        'podrás descifrar la siguiente parte del conjuro.\n'
    ],
    'series_game': [],
    'figures/3_3_congrats.png': [
        '¡Conseguido! Ahora el tren del reino vuelve a funcionar perfectamente.',
        'Un tren muy chulo, ¿verdad?\n'
    ],
    'move3': [],
    'audio/4_1_explanation.wav': [],
    'figures/4_1_explanation.png': [
        'Algunas señales de tráfico del reino están mal puestas.',
        'Los yayos no sabían esto, y han decidido no usar el GPS',
        '¡y ahora están perdidos!\n',
        'Se han metido dentro de un laberinto del cual no saben salir.',
        'Sácales de ahí y ve recogiendo las letras que te encuentres por el camino'
    ],
    'labyrinth_game': [],
    'figures/4_3_congrats.png': [
        '¡Bien hecho!\n',
        'Guiaste a los yayos fuera del laberinto y los sacaste del apuro.',
        'Con las letras que dejaron por el camino, ¡desciframos el hechizo!'
    ],
    'move4': [],
    'audio/castle2.wav': [],
    'figures/5_1_miguelina.png': [
        'Vamos a decir el hechizo, a ver si la princesa despierta',
        '\n¡FERNANDUCHO ES UN MIEDICA!',
        '\n...',
        '\n...',
        'Uhm...\nParece que la princesa no despierta...',
        '¿Nos habremos equivocado?\n',
        '¡Gala! Necesitas ver esto, creo que he encontrado el problema...'
        ],
    'figures/5_2_blai.png': [
        '¡Oh no!\n',
        'Blai estaba distrayendo a Fernando y te dio las direcciones mal.',
        'No debimos haber ido al laberinto...\n',
        '¡Al menos ayudamos a los yayos!\n',
        'Vamos a seguir buscando.\n'
    ],
    'move5': [],
    'audio/6_1_explanation.wav': [],
    'figures/6_1_explanation.png': [
        'Parece que ha habido un escape de agua en tu casa.',
        'Las tuberías verdes se han girado y el circuito no está cerrado.',
        'Colócalas bien hasta conectar las dos válvulas redondas.'
    ],
    'pipelines_game': [],
    'figures/6_3_congrats.png': [
        '¡Conseguido!\n',
        'Ahora los papas se pueden relajar tranquilamente en el sofá.'
    ],
    'move6': [],
    'audio/7_1_explanation.wav': [],
    'figures/7_1_explanation.png': [
        'Teresina y Jordi quieren ampliar el negocio haciendo volar su globo en el reino.',
        'Pero están teniendo problemas a la hora de rellenar los permisos.',
        '¿Puedes ayudarles resolviendo el crucigrama?\n'
    ],
    'crossword_game': [],
    'figures/7_3_congrats.png': [
        'Ahora el globo de Teresina y Jordi puede volar tranquilamente por el reino.',
        'Y al ayudarles,\n¡hemos descifrado el hechizo!',
        'A ver si esta vez no hay inconvenientes...\n',
        'Volvamos al castillo a probar si podemos despertar a la princesa.'
    ],
    'move7': [],
    'audio/castle3.wav': [],
    'figures/8_1_miguelina.png': [
        'Vamos a decir el hechizo, a ver si la princesa despierta esta vez',
        '\n¡FERNANDUCHO ES UN MEDIAS NOCHES!',
        '\n...',
        '\n...'],
    'audio/princessrescued.wav': [],
    'figures/8_2_success.png': [
        '\n¡LO CONSEGUIMOS!',
        '\nHemos despertado a la princesa Miguelina.'
    ],
    'figures/8_3_success.png': [
        'Muchas gracias, Gala\n Sin ti no habría sido posible'
    ],
    'figures/8_4_theend.png': [
        '\nFIN'
    ]
}

destinations = [
    ['castle', 'Vayamos primero a VillaFoto, el pueblo de la fotografía', 'fernando'],
    ['photo_village', 'Siguiente parada: casa del tío', 'antonio'],
    ['hector', '¡Rápido! A la estación de tren', 'paco'],
    ['train_station', 'Nos adentramos en el laberinto...', 'fernando'],
    ['labyrinth', '¡Lo tenemos! De vuelta al castillo', 'paco'],
    ['castle', 'Pongamos rumbo a casa de los papas', 'antonio'],
    ['sofi', '¡Ahora toca volar en globo!', 'fernando'],
    ['balloon', '¡Último viaje! Hacia el castillo', 'paco'],
    ['castle','aux']
]