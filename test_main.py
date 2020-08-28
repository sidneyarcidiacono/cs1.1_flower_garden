"""Import pytest and main."""
import pytest
import main

#TODO: figure out why this doesn't think flower is defined

def test_get_turn_degrees():
    """Test get_turn_degrees for flower class"""
    assert flower.get_turn_degrees() == 60
