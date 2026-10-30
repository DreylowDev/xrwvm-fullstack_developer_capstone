from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      # NISSAN
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"Altima", "type":"SEDAN", "year": 2022, "car_make":car_make_instances[0]},
      {"name":"Sentra", "type":"SEDAN", "year": 2021, "car_make":car_make_instances[0]},
      {"name":"Kicks", "type":"SUV", "year": 2022, "car_make":car_make_instances[0]},

      # Mercedes
      {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"S-Class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"GLC", "type":"SUV", "year": 2022, "car_make":car_make_instances[1]},
      {"name":"CLA", "type":"SEDAN", "year": 2021, "car_make":car_make_instances[1]},

      # Audi
      {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"Q5", "type":"SUV", "year": 2022, "car_make":car_make_instances[2]},
      {"name":"Q7", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A3", "type":"SEDAN", "year": 2021, "car_make":car_make_instances[2]},

      # Kia
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Cerato", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Sportage", "type":"SUV", "year": 2022, "car_make":car_make_instances[3]},
      {"name":"Rio", "type":"SEDAN", "year": 2021, "car_make":car_make_instances[3]},
      {"name":"Seltos", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},

      # Toyota
      {"name":"Corolla", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Camry", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"RAV4", "type":"SUV", "year": 2022, "car_make":car_make_instances[4]},
      {"name":"Highlander", "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Avensis", "type":"WAGON", "year": 2018, "car_make":car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])