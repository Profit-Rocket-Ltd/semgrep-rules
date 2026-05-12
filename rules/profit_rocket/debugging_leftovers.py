# pyright: reportMissingImports=false, reportMissingModuleSource=false
# ruff: noqa
# Test fixtures for rules/profit_rocket/debugging_leftovers.yml
# Run with: semgrep --test rules/profit_rocket


def hits_pdb_import():
    # ruleid: profit-rocket.no-pdb-import
    import pdb

    pdb.set_trace()


def hits_ipdb_import():
    # ruleid: profit-rocket.no-pdb-import
    import ipdb

    ipdb.set_trace()


def hits_from_pdb():
    # ruleid: profit-rocket.no-pdb-import
    from pdb import set_trace

    set_trace()


def hits_breakpoint():
    x = 1
    # ruleid: profit-rocket.no-breakpoint-call
    breakpoint()
    return x


def ok_no_debugger():
    # ok: profit-rocket.no-pdb-import
    # ok: profit-rocket.no-breakpoint-call
    import os

    return os.getcwd()


def ok_string_mentions_pdb():
    # ok: profit-rocket.no-pdb-import
    docs = "See pdb docs at https://docs.python.org/3/library/pdb.html"
    return docs
