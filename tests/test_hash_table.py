import pytest
import sys

sys.path.insert(0, "../src")
from hash_table import HashTable

ht = HashTable()


def test_put_and_get():
    ht.put("First Name", "Taylor")
    ht.put("Last Name", "Liao")
    ht.put("age", 29)

    assert ht.get("First Name") == "Taylor"
    assert ht.get("Last Name") == "Liao"
    assert ht.get("age") == 29


def test_put_and_update():
    ht.put("age", 29)
    ht.put("age", 30)
    ht.put("First Name", "Meggy")
    ht.put("Last Name", "Hsiao")

    assert ht.get("age") == 30
    assert ht.get("First Name") == "Meggy"
    assert ht.get("Last Name") == "Hsiao"


def test_put_and_collide():
    ht.put("age", 29)
    ht.put("gae", 92)
    ht.put("eag", 999)

    assert ht.get("age") == 29
    assert ht.get("gae") == 92
    assert ht.get("eag") == 999
