from pathlib import Path

from tempdrive import DriveLetter


def test_drive_letter_init_from_letter() -> None:
    drive = DriveLetter('C')
    assert drive.letter == 'C'
    assert drive.device == 'C:'
    assert drive.path == Path('C:\\')


def test_drive_letter_init_from_device() -> None:
    drive = DriveLetter('D:')
    assert drive.letter == 'D'
    assert drive.device == 'D:'
    assert drive.path == Path('D:\\')


def test_drive_letter_init_from_backslash_path() -> None:
    drive = DriveLetter('E:\\')
    assert drive.letter == 'E'
    assert drive.device == 'E:'
    assert drive.path == Path('E:\\')


def test_drive_letter_init_from_slash_path() -> None:
    drive = DriveLetter('F:/')
    assert drive.letter == 'F'
    assert drive.device == 'F:'
    assert drive.path == Path('F:\\')
