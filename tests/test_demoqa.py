from selene import browser, have
import os

def test_demoqa_practice_form():
    # Full all fields
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Viktoriia')
    browser.element('#lastName').type('Lav')
    browser.element('#userEmail').type('newuser@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8800222334')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="1993"]').click()
    browser.element('.react-datepicker__month-select').element('[value="4"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element('#subjectsInput').type('Chemistry').click().press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#currentAddress').type('144 Broadway, suit 12')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.png'))
    browser.element('#submit').click()

    # Test that the form was successfully completed
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
