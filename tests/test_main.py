"""
Test module for main.py.
Tests the game launcher functionality.
"""

import sys
from pathlib import Path

# Add parent directory to path to import main module
sys.path.insert(0, str(Path(__file__).parent.parent))

import main


def test_show_game_menu(capsys):
    """Test that game menu displays correctly."""
    main.show_game_menu()
    captured = capsys.readouterr()
    assert "ADVENTURE GAME COLLECTION" in captured.out
    assert "Castle Escape" in captured.out


def test_launch_castle_escape_function_exists():
    """Test that launch_castle_escape function exists."""
    assert hasattr(main, "launch_castle_escape")
    assert callable(main.launch_castle_escape)
