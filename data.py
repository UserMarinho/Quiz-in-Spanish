import pandas as pd

questions = [
    ['Con unos zapatos grandes y la cara muy pintada, soy el que hace reír a toda la chiquillada.', 'Futbolista', 'Payaso', 'Panadero', 'Cocinero', 2],
    ['Preparo ricos manjares, mi lugar es la cocina de restaurantes y hoteles. Veamos quién me adivina.', 'Camarero', 'Panadero', 'Cocinero', 'Enfermero', 3],
    ['Riega contento el jardín, amapolas y un jazmín. Cuida la flor con esmero, ¿a quién espero?', 'jardinero', 'Carpintero', 'Electricista', 'Contador', 1],
    ['Recojo frutos sin siembra y mi tractor viene y va, allí por donde trabajo, nadie puede caminar.', 'Arquitecto', 'Pescador', 'Maquinista', 'Agricultor', 4],
    ['Sobre lienzos o en papel, ¡qué bien emplea el color con lápices o pincel!', 'Carpintero', 'Pintor', 'Arquitecto', 'Médico', 2],
    ['Trabajo en el hospital, pero soy médico no soy. Si no lo adivinas, un pinchazo te doy.', 'Recepcionista', 'Farmacêutico', 'Enfermero', 'Terapeuta', 3],
    ['Conduzco por la ciudad, en mi coche te llevo a cualquier lugar, pero después me tendrás que pagar.', 'Bombero', 'Taxista', 'Profesor', 'Panadero', 2],
    ['Tengo chistera y una varita. Si me lo propongo puedo hacer aparecer cositas.', 'Cocinero', 'Bibliotecario', 'Mago', 'Mecánico', 3],
    ['Con madera de pino, de haya o de nogal, construyo los muebles para tu hogar.', 'Masón', 'Dentista', 'Carpintero', 'Jardinero', 3],
    ['Si vas al supermercado, yo te atenderé, pasando por caja te diré lo que te cobraré.', 'Cajero', 'Panadero', 'Mecánico', 'Cocinero', 1],
    ['Con cariño y mucho amor, en el cole te espero, con juegos y actividades con los que aprenderemos.', 'Cajero', 'Actor', 'Profesor', 'Deportivo', 3],
    ['Con mi pluma yo escribo, miles de libros y cuentos, para que tú los disfrutes. ¡Qué gran invento!', 'Jardinero', 'Profesor', 'Músico', 'Escritor', 4],
    ['Trabajo bajo tierra, pico y pala todo el día. Mi segunda casa es la mina. ¿Adivinas?', 'Músico', 'Minero', 'Arquitecto', 'Jardinero', 2],
    ['En los bares estoy y no soy el cocinero. Ayudo a servir las mesas y lo hago con esmero.', 'Dj', 'Abogado', 'Camarero', 'Bailarín', 3],
    ['Sumergido entre las aguas, me gusta trabajar. Con mi bombona de oxígeno me encontrarás.', 'Profesor', 'Buzo', 'Electricista', 'Jardinero', 2],
    ['En televisión trabajo, me gusta comunicar, presento programas, ¿me conoces ya?', 'Médico', 'Carpintero', 'Músico', 'Presentador', 4],
    ['Si tienes una tubería atascada o un grifo roto, me tendrás que llamar, a tu casa iré corriendo para poderlo arreglar.', 'Plomero', 'Médico', 'Buzo', 'Camarero', 1],
    ['A las olimpiadas yo iré y con esfuerzo y mucho trabajo una medalla ganaré.', 'Actor', 'Abogado', 'Deportista', 'Músico', 3],
    ['El pelo arreglo en mi bonito local, si vienes a visitarme te dejaré genial.', 'Deportista', 'Actor', 'Profesor', 'Peluquero', 4],
    ['En la granja trabajo sin cesar, cuido de los animales con gran placer. ¿Quién soy?', 'Arquitecto', 'Músico', 'Granjero', 'Médico', 3],
    ['Soy el guardián del conocimiento, libros y más en mi ambiente. ¿Quién soy?', 'Músico', 'Bombero', 'Granjero', 'Bibliotecario', 4],
    ['Llevo correos de un lugar a otro, en mi moto o bicicleta, siempre soy veloz. ¿Quién soy?', 'Profesor', 'Cartero', 'Arquitecto', 'Mecánico', 2],
    ['En el mar trabajo sin descansar, pescando peces para luego vender. ¿Quién soy?', 'Maestro', 'Arquitecto', 'Escritor', 'Pescador', 4],
    ['Recorro las calles en mi camión, recolectando basura sin cesar. ¿Quién soy?', 'Fotógrafo', 'Recolector', 'Pescador', 'Jardinero', 2],
    ['En el estudio de grabación me encuentras, produciendo música con gran pasión.', 'Maestro', 'Abogado', 'Veterinario', 'Productor', 4],
    ['En el laboratorio realizo experimentos, buscando respuestas a problemas científicos.', 'Pescador', 'Camarero', 'Científico', 'Bombero', 3],
    ['Uso mi cámara para capturar momentos, creando imágenes que recordarás.', 'Dentista', 'Contador', 'Productor', 'Fotógrafo', 4],
    ['Con tijeras y peine trabajo cada día, creando nuevos estilos con gran maestría. ¿Quién soy?', 'Ingeniero', 'Peluquero', 'Chef', 'Abogado', 2],
    ['Dirijo una empresa con gran habilidad, tomando decisiones para prosperar.', 'Empresario', 'Abogado', 'Actor', 'Ingeniero', 1],
    ['Diseño edificios y puentes también, creando estructuras que asombran a quien las ve.', 'Empresario', 'Enfermero', 'Maestro', 'Arquitecto', 4],
    ['Con mi bisturí realizo cirugías, salvando vidas con mis manos cada día. ¿Quién soy?', 'Policía', 'Cirujano', 'Maestro', 'Carpintero', 2],
    ['Conduzco un gran camión de carga, transportando mercancías de una ciudad a otra.', 'Pintor', 'Enfermero', 'Camionero', 'Dentista', 3],
    ['Trabajo en el campo, cultivando vegetales y frutas que todos disfrutamos.', 'Ingeniero', 'Cantante', 'Abogado', 'Agricultor', 4],
    ['En la televisión reporto noticias, informando al público con gran precisión.', 'Periodista', 'Mecánico', 'Chef', 'Jardinero', 1]
]

#pandas dataframe creation
df = pd.DataFrame(questions, columns=['image', 'option 1', 'option 2', 'option 3', 'option 4', 'answer'])
#saving dataframe
df.to_excel('questions.xlsx', index=False)
print('questions ok')
