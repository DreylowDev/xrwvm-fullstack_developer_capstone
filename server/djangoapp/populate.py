from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
            )
        )

    # (name, type, year, index of the car make above)
    car_model_data = [
        # NISSAN
        ("Pathfinder", "SUV", 2023, 0),
        ("Qashqai", "SUV", 2023, 0),
        ("XTRAIL", "SUV", 2023, 0),
        ("Altima", "SEDAN", 2022, 0),
        ("Sentra", "SEDAN", 2021, 0),
        ("Kicks", "SUV", 2022, 0),
        # Mercedes
        ("A-Class", "SUV", 2023, 1),
        ("C-Class", "SUV", 2023, 1),
        ("E-Class", "SUV", 2023, 1),
        ("S-Class", "SEDAN", 2023, 1),
        ("GLC", "SUV", 2022, 1),
        ("CLA", "SEDAN", 2021, 1),
        # Audi
        ("A4", "SUV", 2023, 2),
        ("A5", "SUV", 2023, 2),
        ("A6", "SUV", 2023, 2),
        ("Q5", "SUV", 2022, 2),
        ("Q7", "SUV", 2023, 2),
        ("A3", "SEDAN", 2021, 2),
        # Kia
        ("Sorrento", "SUV", 2023, 3),
        ("Carnival", "SUV", 2023, 3),
        ("Cerato", "SEDAN", 2023, 3),
        ("Sportage", "SUV", 2022, 3),
        ("Rio", "SEDAN", 2021, 3),
        ("Seltos", "SUV", 2023, 3),
        # Toyota
        ("Corolla", "SEDAN", 2023, 4),
        ("Camry", "SEDAN", 2023, 4),
        ("Kluger", "SUV", 2023, 4),
        ("RAV4", "SUV", 2022, 4),
        ("Highlander", "SUV", 2023, 4),
        ("Avensis", "WAGON", 2018, 4),
    ]

    for name, car_type, year, make_index in car_model_data:
        CarModel.objects.create(
            name=name,
            car_make=car_make_instances[make_index],
            type=car_type,
            year=year,
        )
