from rest_framework import throttling


class CustomRateThrottle(throttling.ScopedRateThrottle):
    scope = 'users'
