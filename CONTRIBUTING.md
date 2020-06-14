# Contributing to bKashWebhook

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

### Table Of Contents
[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Python Styleguide](#python-styleguide)
## Style Guides
#### Git Commit Messages
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings
    
[N.B. Git Commit Messages instruction adopt from Atom project]

#### Python Styleguide
All codebase must adhere to [PEP8](https://www.python.org/dev/peps/pep-0008/)
- Prefer to write well codebase documents 
- Use Type Casting as much as possible
- Prefer to follow standard design pattern
###### Example
```python

# Use this 
def add_two(first: int, second: int) -> int:
    """
    :param first: Example: 1,2 .... 
    :param second: Example: 1,2, ....
    """
    return first + second

# Instate of  
def bad_example(first, second):
    total = first + second
    return total
```
