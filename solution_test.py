from solution import Person, Developer, Roster


def test_use_class_Person():
    person = Person(1, "bal", 23)
    assert isinstance(person, Person)


def test_use_class_Developer():
    dev = Developer(1, "bal", 23, 1000.0, "python")
    assert isinstance(dev, Developer) and isinstance(dev, Person)


def test_use_class_Roster():
    roster = Roster()
    assert isinstance(roster, Roster)


def test_use_method_repr_Person():
    message = Person(1, "bal", 39).__repr__()
    assert message == "Person(id:1, name:bal, age:39)"


def test_use_method_repr_Developer():
    message = Developer(1, "bal", 39, 1000.0, "python").__repr__()
    assert message == "Dev(id:1, name:bal, age:39, salary:1000.0, language:python)"


def test_roster_developerList_empty():
    roster = Roster()
    devList = roster.getDeveloperList()
    assert len(devList) == 0


def test_roster_method_addDeveloper():
    roster = Roster()
    roster.addDeveloper(Developer(1, "bal", 23, 1000.0, "python"))
    devList = roster.getDeveloperList()
    assert len(devList) == 1


def test_roster_method_addDeveloperData():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    devList = roster.getDeveloperList()
    assert len(devList) == 1


def test_roster_method_deleteDeveloper():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    roster.deleteDeveloper(1)
    devList = roster.getDeveloperList()
    assert len(devList) == 0


def test_roster_method_updateDeveloper():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    roster.updateDeveloper(1, "balx", 24, 1100.0, "java")
    message = roster.getDeveloperList()[0].__repr__()
    assert message == "Dev(id:1, name:balx, age:24, salary:1100.0, language:java)"


def test_roster_method_getTotalSalary():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    roster.addDeveloperData(2, "rod", 24, 500.0, "html")
    result = roster.getTotalSalary()
    assert result == 1500.0


def test_roster_method_getDevCountByLanguage():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    roster.addDeveloperData(2, "rod", 24, 500.0, "html")
    result = roster.getDevCountByLanguage()
    assert result == {"python": 1, "html": 1}


def test_roster_method_getTotalSalaryByLanguage():
    roster = Roster()
    roster.addDeveloperData(1, "bal", 23, 1000.0, "python")
    roster.addDeveloperData(2, "rod", 24, 500.0, "html")
    result = roster.getTotalSalaryByLanguage()
    assert result == {"python": 1000.0, "html": 500.0}
