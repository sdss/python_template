# SDSS Python template and coding style

**Important: this is a pre-alpha version of this document. Please, look throughout the text and at the end of the document for a list of TODO/missing parts.**

So you want to write some Python code. Congratulations, you've gotten to the right place! This repository has a dual purpose: it provides a template for a basic, but complete, Python package, and includes the coding styles and recommendations for developing code for SDSS. Please, read this document carefully. If you decide to develop your product based on this template, feel free to replace the `README.md` with a description of your project, but keep the `STYLE.md` file as a reminder of the coding conventions.

While this document deals with Python product, and some of the solutions and services suggested are specific for it, much of what is written here is general good advice for developping software in any programming language.

## Python 2 vs Python 3: which one to choose?

SDSS has agreed to transition to Python 3. That means that all new code must *at least* compatible with Python 3. There is, however, a very significant amount of ancillary code that is Python 2-only and that will not be ported to Python 3 for some time.

When deciding what version of Python to write your code on, consider what are its dependencies:

- If your code is standalone, or depends on Python 3-compatible code, write it in Python 3. **You don't need to make sure your code is Python 2-backwards compatible.**
- If your code depends on key packages that are Python 2-only (e.g., `actorcore`, `opscore`, `RO`, `twistedActor`), write your code in Python 2 **but** try to make it as much Python 3-ready as possible, so that when those dependencies are upgraded you can upgrade your code easily.

Whenever you create a new Python file, make sure to add the following lines on the top of the file

```python
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
```

That will force you to use `import`, `print`, and division in a way that is Python 2 and 3-compatible.

Some resources that can be useful to write code that is Python 2 and 3-compatible, and to port code from 2 to 3.

- TODO: link to a web with advice to write code for 2 and 3.
- TODO: description and link to `six.py`.
- TODO: description and link to `2to3`.
