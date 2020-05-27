def make_car(model, manufacturer, **kwargs):
    kwargs['model'] = model
    kwargs['manufacturer'] = manufacturer
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
