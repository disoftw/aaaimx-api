from .models import Partner, Project

Projects = [
	{
		"uuid" : "0eacce75-b9c9-4651-aac1-b487867630d4",
		"title" : "Reconocimiento automático de patrones en imágenes tridimensionales basado en técnicas paralelas con OpenMP",
		"start" : "2019-01-01",
		"end" : "2019-12-31",
		"responsible" : "6de07827-0ca2-4b15-bed7-c9ec311eb999",
		"institute" : Partner.objects.get(uuid="52f2a630-893c-4f69-b243-d5eaa75d27c9")
	},
	{
		"uuid" : "12c6ac69-99f4-4ac5-80d7-19759bda0860",
		"title" : "Análisis y procesamiento de datos para el desarrollo de algoritmos de inteligencia artificial enfocados al estudio y reconocimiento de patrones en fenómenos naturales",
		"start" : "2018-01-01",
		"end" : "2018-12-31",
		"responsible" : "d0030f68-a6e0-48c2-a0f2-333105e04366",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	},
	{
		"uuid" : "2c39fff9-6568-4d15-9434-5e2517a9b780",
		"title" : "Caracterización del diseño, construcción y prueba de equipos autogeneradores",
		"start" : "2016-01-01",
		"end" : "2018-12-31",
		"responsible" : "50319dc0-0e86-43da-a1f4-394d222c5f96",
		"institute" : Partner.objects.get(uuid="52f2a630-893c-4f69-b243-d5eaa75d27c9")
	},
	{
		"uuid" : "3d037f34-4603-4023-8a37-8e12274ecdd4",
		"title" : "Sistema de análisis de imágenes radiológicas para diagnóstico por medio de redes neuronales",
		"start" : "2019-01-01",
		"end" : "2019-12-31",
		"responsible" : "d280bf0b-5449-4425-a6c3-fc6cdbaa840c",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	},
	{
		"uuid" : "5ab26328-a435-40a2-9aee-607ca52ca4e8",
		"title" : "Segmentación de regiones basado en atributos de textura de datos bidimensionales utilizado técnicas de procesamiento digital de imágenes e inteligencia artificial",
		"start" : "2018-01-01",
		"end" : "2018-12-31",
		"responsible" : "013ea831-5981-4bef-94a3-7f7a7e10f7af",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	},
	{
		"uuid" : "66225fa9-d0d9-4725-89cf-857ec7e6427a",
		"title" : "Predicción a largo plazo de la actividad solar en el ambiente espacial",
		"start" : "2017-01-01",
		"end" : "2018-07-31",
		"responsible" : "50319dc0-0e86-43da-a1f4-394d222c5f96",
		"institute" : Partner.objects.get(uuid="52f2a630-893c-4f69-b243-d5eaa75d27c9")
	},
	{
		"uuid" : "71c145ab-bf2b-40c0-8789-7547930d0238",
		"title" : "Análisis de sistemas de flujo urbano para el diseño de ciudades inteligentes",
		"start" : "2019-01-01",
		"end" : "2019-12-31",
		"responsible" : "59bfaf34-7342-49c2-875f-3ee41e890d46",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	},
	{
		"uuid" : "9f146cf9-705c-4640-946a-5f575482f720",
		"title" : "Evaluación del fenómeno de El Niño \/ Oscilación Meridional (ENOS) mediante percepción remota, series de tiempo e inteligencia artificial",
		"start" : "2019-07-01",
		"end" : "2022-12-31",
		"responsible" : "50319dc0-0e86-43da-a1f4-394d222c5f96",
		"institute" : Partner.objects.get(uuid="52f2a630-893c-4f69-b243-d5eaa75d27c9")
	},
	{
		"uuid" : "a25f3316-3212-47e2-95c7-48445e9e8e89",
		"title" : "Clasificación, predicción y reconocimiento de patrones en series de tiempo mediante técnicas de aprendizaje automático (machine learning)",
		"start" : "2019-01-01",
		"end" : "2019-12-31",
		"responsible" : "d0030f68-a6e0-48c2-a0f2-333105e04366",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	},
	{
		"uuid" : "e6e8cf36-04c4-465a-8b59-77de2d7f21f1",
		"title" : "Sistema compacto de seguimiento de estación terrena por visión artificial para implementación en un nano-satélite transmitiendo vía comunicaciones ópticas",
		"start" : "2017-01-01",
		"end" : "2018-07-31",
		"responsible" : "c9caf7f6-1fcf-4d4f-ac91-17c3c36eecc2",
		"institute" : Partner.objects.get(uuid="52f2a630-893c-4f69-b243-d5eaa75d27c9")
	},
	{
		"uuid" : "ec12fc0a-8b78-46c6-a045-5bb63df79517",
		"title" : "Análisis y procesamiento de datos para el control inteligente de un sistema de riego automatizado basado en internet de las cosas",
		"start" : "2019-01-01",
		"end" : "2019-12-31",
		"responsible" : "3f85210f-df46-41f4-b905-2ce8d04ed238",
		"institute" : Partner.objects.get(uuid="8862a10a-9e86-43db-b513-d6101cca2e33")
	}
]

for p in Projects:
    try:
        Project(**p).save()
    except Exception as err:
        print(err)
        pass