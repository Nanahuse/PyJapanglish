# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyJapanglish/blob/main/LICENSE

from .cmudict_jp import CMUDICT_JAPANESE
import pyphonixjp


class Japanglish(object):
    def __init__(self, user_dict: dict[str, str] = dict()):
        """
        変換する。
        ユーザー定義辞書はself.user_dictにアクセスして変更可能。

        Args:
            user_dict (dict[str, str], optional): ユーザー定義の辞書。{"英単語","発音"}の構造であること。 Defaults to dict().
        """
        self.user_dict = user_dict

    def convert(self, word: str, use_phonix: bool = True) -> str | None:
        """
        英単語の発音をカナに変換する。

        変換優先度は
        1. ユーザー辞書
        2. 発音辞書
        3. 発音の推定 (if use_phonix == True)

        Args:
            word: 変換する単語。アルファベット以外が含まれるとNoneを返す。
            use_phonix: Trueの場合phonix規則に基づき未知語の発音推定を行う。Falseの場合は未知語にNoneを返す。Defaults to True.

        Returns:
            str | None: 変換した後の文字列。変換にできない場合はNone。
        """
        word_lower = word.lower()

        try:
            return self.user_dict[word_lower]
        except KeyError:
            pass

        try:
            return CMUDICT_JAPANESE[word_lower]
        except KeyError:
            pass

        if use_phonix:
            return pyphonixjp.convert(word_lower)
        else:
            return None
