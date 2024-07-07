from pathlib import Path

from selene import browser, have, command
import os
from selenium.webdriver.common.keys import Keys

import tests


def test_demoqa_practice_form():
    # GIVEN
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Viktoriia')
    browser.element('#lastName').type('Lav')
    browser.element('#userEmail').type('newuser@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('8800222334')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1993')
    browser.element('.react-datepicker__month-select').all('option')[4].click()
    browser.element(f'.react-datepicker__day--0{17}').click()

    browser.element('#subjectsInput').type('Chemistry').click().press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()

    browser.element('#currentAddress').with_(set_value_by_js=True).set_value('144 Broadway, suit 12')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()

    browser.element('#uploadPicture').send_keys(os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), os.path.pardir, 'resources/photo.png')
    ))

    browser.element('#submit').click()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all("td").even.should(have.exact_texts('Viktoriia Lav',
                                                                     'newuser@gmail.com',
                                                                     'Female',
                                                                     '8800222334',
                                                                     '17 May,1993',
                                                                     'Chemistry',
                                                                     'Sports, Reading',
                                                                     'photo.png',
                                                                     '144 Broadway, suit 12',
                                                                     'NCR Gurgaon'))


# noinspection PySingleQuotedDocstring
def test_demoqa_practice_form_different_realization():
    '''
    Other ways to enter birthdate, genre, city, state, subject, uploading a picture, and checks
    '''

    # GIVEN
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Viktoriia')
    browser.element('#lastName').type('Lav')
    browser.element('#userEmail').type('newuser@gmail.com')
    browser.all('[for^=gender-radio]').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('8800222334')

    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('05.17.1993').press_enter()

    browser.element('#subjectsInput').type('m').press_enter()
    browser.element('#subjectsInput').type('ch').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath(
        str(Path(tests.__file__).parent.parent.joinpath('resources/photo.png').absolute())
    ))

    browser.element('#currentAddress').type('144 Broadway, suit 12')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Gurgaon')).click()

    browser.element('#submit').enter()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all("td").should(have.exact_texts(('Student Name', 'Viktoriia Lav'),
                                                                ('Student Email', 'newuser@gmail.com'),
                                                                ('Gender', 'Female'),
                                                                ('Mobile', '8800222334'),
                                                                ('Date of Birth', '17 May,1993'),
                                                                ('Subjects', 'Maths, Chemistry'),
                                                                ('Hobbies', 'Sports, Reading'),
                                                                ('Picture', 'photo.png'),
                                                                ('Address', '144 Broadway, suit 12'),
                                                                ('State and City', 'NCR Gurgaon')))
