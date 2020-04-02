import pytest
from _pytest.capture import capsys
import main


def test_main_menu_E2E(capsys):
    input_values = ["menu", "end"]

    def mock_input(s):
        return input_values.pop(0)

    main.input = mock_input

    main.main()
    captured = capsys.readouterr()
    assert "\"bmi\": to calculate BMI and determine if underweight, normal, or overweight.\n" \
           "\"retire\": calculate retirement age based off current age, annual salary, and percentage saved.\n" \
           "\"menu\": to see all available options\n" \
           "\"end\": to close program\n" in captured.out


def test_main_retire_E2E(capsys):
    input_values = ["retire", "23", "65000", ".2", "1000000", "end"]

    def mock_input(s):
        return input_values.pop(0)

    main.input = mock_input

    main.main()
    captured = capsys.readouterr()
    assert "You will retire at 80 ." in captured.out


def test_main_bmi_E2E(capsys):
    input_values = ["bmi", "180", "6", "2", "end"]

    def mock_input(s):
        return input_values.pop(0)

    main.input = mock_input

    main.main()
    captured = capsys.readouterr()
    assert "BMI: 23.7 \nCategory: Normal" in captured.out
