def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(car_info)
    return car
