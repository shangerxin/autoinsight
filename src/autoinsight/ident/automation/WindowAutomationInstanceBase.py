from abc import ABC, abstractmethod

from .AutomationInstanceBase import AutomationBase


class WindowAutomationInstanceBase(AutomationBase):
    @abstractmethod
    def wait_for_idle(self, *args, **kwargs):
        pass

    @abstractmethod
    def click_input(self, *args, **kwargs):
        pass

    @abstractmethod
    def set_focus(self, *args, **kwargs):
        pass


    # TODO: implement methods
    # select
    # set_focus
    # scroll
    # type
    # toggle
    # rectangle
    # type_keys
    # wait_for_idle
    # double_click_input
    # is_visible
    # is_enable
    # draw_outline
    # client_to_screen
    # capture_as_image
    # maximize
    # minimize
    # window_text
    # close
    # title
