"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mgithub_star_import` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``github_star_import.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``github_star_import.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
from github3 import login


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    if len(argv) >= 3:
        gh = login(argv[0], password=argv[1])
        slave = gh.user(argv[2])
        for r in slave.starred_repositories():
            owner = r._json_data['repo']['owner']['login']
            reponame = r._json_data['repo']['name']
            print(owner, reponame)
            try:
                argv[3] == '--dry'
            except NameError:
                if not gh.is_starred(owner, reponame):
                    gh.star(owner, reponame)
                    print('*')
    else:
        print("\n" + 'Usage: $ github-star-import github_username github_apikey import_username' + "\n"
              + '   Ex: $ github-star-import username 95ab5c9c26a5b1592d0d97f9b60afc34b6230521 github' + "\n"
              + '--dry: No changes will made in case used.' + "\n")
    return 0
