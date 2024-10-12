# flags: --minimum-version=3.12


def func[T](a: T, b: T,
            some_very_long_variable_that_should_force_black_to_wrap_like_for_realsies_wrap_like_very_long: T) -> T:
    return a


def func[T](a: T, b: T,
            some_very_long_variable_that_should_force_black_to_wrap: T) -> T:
    return a


# output


def func[T](
    a: T,
    b: T,
    some_very_long_variable_that_should_force_black_to_wrap_like_for_realsies_wrap_like_very_long: T,
) -> T:
    return a


def func[T](
    a: T, b: T, some_very_long_variable_that_should_force_black_to_wrap: T
) -> T:
    return a


