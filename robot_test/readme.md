# Robot Test Suite

## Background

* each robot file is a test suite
* a test suite contains many test cases
* each test case is a replay of a sequence of commands expressed using robot keywords
* test suites and test cases can have their own setup and tear down logic
* test suites MUST have appropriate tear down logic to leave server database in a consistent state.
* test suites are organized/grouped into directories - any hierarchical grouping is possible, but use common sense to not have arbitrarily deep nestings.
* execution logic can be organized into either python functions/methods in the python library file or using robot keywords (essentially functions/procedures). Keywords can be arbitrarily grouped into high-level keywords. Again, avoid arbitraility deep nestings, because it makes the code harder to read/understand.

## Frequently used commands

Executing all test suites from the root directory:

    robot .

Executing a single test suite (i.e., robot file) in its directory:

    robot mytest.robot

Executing a single test case of a single test suite:

    robot -t "my test case" mytest.robot

Executing a single test suite against a different server:

    robot --variable SERVER:10.0.0.42 mytest.robot

# Resources

* [https://github.com/robotframework/QuickStartGuide](https://github.com/robotframework/QuickStartGuide)
