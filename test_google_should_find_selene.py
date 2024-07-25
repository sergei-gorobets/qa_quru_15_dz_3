from selene import browser, be, have

def test_one():
    browser.open("")
    browser.element('[name="q"]').should(be.blank).type('fdghjklZXCVBNM#$%^&8').press_enter()
    browser.element('[id="search"]').should(be.not_.visible)

def test_two():
    browser.open("")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))