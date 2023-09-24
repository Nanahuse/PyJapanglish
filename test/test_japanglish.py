# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyJapanglish/blob/main/LICENSE


def test_convert():
    from pyjapanglish import Japanglish

    japanglish = Japanglish()

    assert japanglish.convert("test") == "テスト"

    japanglish.user_dict["test"] = "ホゲホゲ"

    assert japanglish.convert("test") == "ホゲホゲ"

    assert japanglish.convert("japanglish") is not False
    assert japanglish.convert("japanglish", False) is None

    assert japanglish.convert("ホゲホゲ") is None
