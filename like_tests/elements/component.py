# -*- coding: utf-8 -*-


class Component(object):
    TIMEOUT = 5
    POLL_FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver


class Clickable(Component):
    CLICK = ''

    def click(self):
        self.driver.find_element_by_xpath(self.CLICK).click()

    def hard_click(self):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element_by_xpath(self.CLICK))
