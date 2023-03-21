from djchoices import DjangoChoices, ChoiceItem


class TypeOfTransport(DjangoChoices):
    auto = ChoiceItem('авто', 'Авто')


class TypeOfEngine(DjangoChoices):
    petrol = ChoiceItem('бензин', 'Бензин')
    propane_butane = ChoiceItem('бензин(пропан-бутан)', 'Бензин(пропан-бутан)')
    methane = ChoiceItem('бензин(метан)', 'Бензин(метан)')
    hybrid = ChoiceItem('бензин(гибрид)', 'Бензин(гибрид)')
    diesel = ChoiceItem('дизель', 'Дизель')
    diesel_hybrid = ChoiceItem('дизель(гибрид)', 'Дизель(гибрид')
    electro = ChoiceItem('электро', 'Электро')


class TypeOfDriveUnit(DjangoChoices):
    front_drive = ChoiceItem('передний привод', 'Передний привод')
    back_drive = ChoiceItem('задний привод', 'Задний привод')
    constant_full_drive = ChoiceItem('постоянный полный привод', 'Постоянный полный привод')
    plug_in_full_drive = ChoiceItem('подключаемый полный привод', 'Подключаемый полный привод')


class TransportAdStatus(DjangoChoices):
    open = ChoiceItem('открыто', 'Открыто')
    close = ChoiceItem('Закрыто', 'Закрыто')

