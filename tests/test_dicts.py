from utils import dicts

data = {"vcs": "mercurial"}


def test_get_val():
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
