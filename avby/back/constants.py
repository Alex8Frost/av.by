from djchoices import DjangoChoices, ChoiceItem


class TypeOfTransport(DjangoChoices):
    auto = ChoiceItem('auto', 'Авто')


class TypeOfEngine(DjangoChoices):
    petrol = ChoiceItem('petrol', 'Бензин')
    propane_butane = ChoiceItem('propane_butane', 'Бензин(пропан-бутан)')
    methane = ChoiceItem('methane', 'Бензин(метан)')
    hybrid = ChoiceItem('hybrid', 'Бензин(гибрид)')
    diesel = ChoiceItem('diesel', 'Дизель')
    diesel_hybrid = ChoiceItem('diesel_hybrid', 'Дизель(гибрид')
    electro = ChoiceItem('electro', 'Электро')


class TypeOfDriveUnit(DjangoChoices):
    front_drive = ChoiceItem('front_drive', 'Передний привод')
    back_drive = ChoiceItem('back_drive', 'Задний привод')
    constant_full_drive = ChoiceItem('constant_full_drive', 'Постоянный полный привод')
    plug_in_full_drive = ChoiceItem('plug_in_full_drive', 'Подключаемый полный привод')


class TransportAdStatus(DjangoChoices):
    open = ChoiceItem('open', 'Открыто')
    close = ChoiceItem('close', 'Закрыто')


class TransportBody(DjangoChoices):
    all_road_3d = ChoiceItem('all_road_3d', 'внедорожник 3 дв.')
    all_road_5d = ChoiceItem('all_road_5d', 'внедорожник 5 дв.')
    cabriolet = ChoiceItem('cabriolet', 'кабриолет')
    coupe = ChoiceItem('coupe', 'купе')
    light_van = ChoiceItem('light_van', 'легковой фургон')
    limousine = ChoiceItem('limousine', 'лимузин')
    lift_back = ChoiceItem('lift_back', 'лифтбек')
    minivan = ChoiceItem('minivan', 'минивэн')
    pickup = ChoiceItem('pickup', 'пикап')
    sedan = ChoiceItem('sedan', 'седан')
    station_wagon = ChoiceItem('station_wagon', 'универсал')
    hatchback_3d = ChoiceItem('hatchback_3d', 'хэтчбек 3 дв.')
    hatchback_5d = ChoiceItem('hatchback_5d', 'хэтчбек 5 дв.')
    other = ChoiceItem('other', 'другой')


class TransportTransmission(DjangoChoices):
    automatic = ChoiceItem('automatic', 'автоматическая')
    mechanical = ChoiceItem('mechanical', 'механическая')





