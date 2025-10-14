from enum import Enum


class AllureStories(str, Enum):
    COURSES = 'Curses'
    AUTHORIZATION = 'Authorization'
    DASHBOARD = 'Dashboard'
    REGISTRATION = 'Registration'