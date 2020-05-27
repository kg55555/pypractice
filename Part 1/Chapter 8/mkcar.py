def make_car(model, manufacturer, **kwargs):
    kwargs['model'] = model
    kwargs['manufacturer'] = manufacturer
    return kwargs