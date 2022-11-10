import csv
from .models import Airport
from urllib.request import urlopen
import codecs


def csvFileToModel(type):

    if type == 'file':
        csvfile = open('uploads/airports.csv', "r",
                       newline='', encoding='Latin1')
    else:
        csvfile = urlopen(
            'https://davidmegginson.github.io/ourairports-data/airports.csv')
        csvfile = codecs.iterdecode(csvfile, 'utf-8')
    reader = csv.DictReader(csvfile)
    list_of_dict = list(reader)
    totalrows = len(list_of_dict)

    print('Total:'+str(totalrows))
    print('Loading...')
    objs = [
        Airport(
            id=row['id'],
            ident=row['ident'],
            type=row['type'],
            name=row['name'],
            latitude_deg=row['latitude_deg'],
            longitude_deg=row['longitude_deg'],
            elevation_ft=(None if row['elevation_ft']
                          == '' else (row['elevation_ft'])),
            continent=row['continent'],
            iso_country=row['iso_country'],
            iso_region=row['iso_region'],
            municipality=row['municipality'],
            scheduled_service=row['scheduled_service'],
            gps_code=row['gps_code'],
            iata_code=row['iata_code'],
            local_code=row['local_code'],
            home_link=row['home_link'],
            wikipedia_link=row['wikipedia_link'],
            keywords=row['keywords']

        )
        for row in list_of_dict
    ]
    print('Creating new records ...')
    Airport.objects.bulk_create(objs, ignore_conflicts=True)
    print('Updating ...')
    Airport.objects.bulk_update(objs, [
        'id',
        #'ident',
        'type',
        'name',
        'latitude_deg',
        'longitude_deg',
        'elevation_ft',
        'continent',
        'iso_country',
        'iso_region',
        'municipality',
        'scheduled_service',
        'gps_code',
        'iata_code',
        'local_code',
        'home_link',
        'wikipedia_link',
        'keywords'
    ])

    
    print('Done!')
