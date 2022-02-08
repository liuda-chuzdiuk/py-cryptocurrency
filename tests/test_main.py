from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_is_not_substantive(mocked_prediction):
    mocked_prediction.return_value = 105

    assert cryptocurrency_action(105) == "Do nothing"
    assert cryptocurrency_action(100) == "Do nothing"
    assert cryptocurrency_action(110.5263) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_to_buy_more_cryptocurrency(mocked_prediction):
    mocked_prediction.return_value = 2

    assert cryptocurrency_action(1.9029) == "Buy more cryptocurrency"
    assert cryptocurrency_action(1.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_to_sell_cryptocurrency(mocked_prediction):
    mocked_prediction.return_value = 1

    assert cryptocurrency_action(1.0537) == "Sell all your cryptocurrency"
