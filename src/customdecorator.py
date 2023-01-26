#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:59:26 2023

@author: chris
"""

import functools
import time

def timing(decimals=2):
    '''Timing function usable as decorator'''
    # outer function to accept argument for number of decimal points for timer
    def decorator(func):
        # decorator function
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            # wrapper for timing
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time  = round(end_time-start_time, decimals)
            print(f'Function {func.__name__!r} took {run_time} seconds.')
            return value
        return wrap 
    return decorator

def debug(func):
    ''''Print the function signature and return value.'''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature}).")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}.")
        return value
    return wrapper_debug
