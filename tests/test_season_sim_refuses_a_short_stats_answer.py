"""A short stats-API answer for a closed season is asked for again, never kept."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "web"))

from season_sim import fetch  # noqa: E402


def _writer(bodies):
    calls = []

    def get(url, dest, *, required, ttl_hours):
        if dest.exists():
            return True
        body = bodies[min(len(calls), len(bodies) - 1)]
        calls.append(url)
        dest.write_text(json.dumps(body))
        return True

    return get, calls


def test_a_short_answer_is_fetched_again(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch.time, "sleep", lambda s: None)
    full = {"data": [{"id": i} for i in range(3)], "total": 3}
    get, calls = _writer([{"data": [{"id": 1}], "total": 3}, full])
    dest = tmp_path / "skaters_20252026.json"
    assert fetch._get_stats("u", dest, closed=True, ttl_hours=None, get=get)
    assert len(calls) == 2
    assert fetch.stats_file_complete(dest)


def test_an_empty_answer_for_a_closed_season_fails_by_name(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch.time, "sleep", lambda s: None)
    get, calls = _writer([{"data": [], "total": 900}])
    with pytest.raises(fetch.FetchError):
        fetch._get_stats("u", tmp_path / "s.json", closed=True, ttl_hours=None, get=get)
    assert len(calls) == fetch.ATTEMPTS


def test_the_current_season_keeps_what_it_got(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch.time, "sleep", lambda s: None)
    get, _ = _writer([{"data": [], "total": 0}])
    dest = tmp_path / "s.json"
    assert fetch._get_stats("u", dest, closed=False, ttl_hours=6, get=get)
    assert dest.exists()


def test_a_complete_file_is_complete(tmp_path):
    p = tmp_path / "s.json"
    p.write_text(json.dumps({"data": [{"id": 1}], "total": 1}))
    assert fetch.stats_file_complete(p)
    p.write_text("not json")
    assert not fetch.stats_file_complete(p)
