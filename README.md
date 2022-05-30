# Labs for Innopolis DevOps Engineering Summer 2022 Course

This repository contains solutions for labs provided during the Innopolis DevOps Engineering Summer 2022 Course provided by Nokhrin Ilya

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python3 (versions 3.7+ recommended)
* Packages specified in requirements.txt

### Installing

1. Clone the repository
2. Install dependencies

```
pip3 install -r requirements.txt
```

3. Run main.py

```
python3 main.py
```

4. In browser, open 127.0.0.1:5000 (or localhost:5000)

## Running the tests

To run the tests, execute appropriate `*_tests.py` file. For example, to test `get_time.py` run following command:

```
python3 .\get_time_tests.py
```

### Expected response

This response will be provide if all tests in current version of `get_time_tests.py` run successfully

```
python3 .\get_time_tests.py
..
----------------------------------------------------------------------
Ran 2 tests in 2.515s

OK
```

### Example of failed test response

This response will be provided if API accessibility test fails

```
 python3 .\get_time_tests.py
.F
======================================================================
FAIL: test__get_moscow_time_api__api_responds (__main__.TestLexer)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\get_time_tests.py", line 9, in test__get_moscow_time_api__api_responds
    self.assertFalse(res.ok, "API is not responding")
AssertionError: True is not false : API is not responding

----------------------------------------------------------------------
Ran 2 tests in 0.349s

FAILED (failures=1)
```

## Built With

* [pytz](https://pypi.org/project/pytz/) - Olson tz database to get timezone from location
* [requests](https://requests.readthedocs.io/en/master/) - Lightweight request library to handle API communication
* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Chosen framework

Reasons to use Flask:

* **It's popular**: Flask is one of the most popular web frameworks for Python. Because of that, it has an extensive amount of code examples and well documentation, as well as active community.
* **It's modular**: Flask supports wide variety of modules, which can be used to extend basic Flask functionality.
* **It's lightweight**: As a consequence of its modularity, Flask only comes with basic functionality built-in and is very lightweight as a result.

## Authors

* **Ilya Nokhrin** - [Telegram](https://t.me/IlyaNokhrin) - [Innopolis Mail](mailto:i.nokhrin@innopolis.university)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* [Template used](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)