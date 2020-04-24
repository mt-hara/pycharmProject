import sys
import logging
import logging.handlers
import logging.config

# ルートロガーの作成。ログレベルをDEBUGに設定
_root_logger = logging.getLogger("")
_root_logger.setLevel(logging.DEBUG)

# フォーマッター作成
# (時刻、ログレベル、モジュール名、関数名、行番号、メッセージ)
_simpleFormatter = logging.Formatter(
    fmt = "%(asctime)s %(levelname)-8s %(module)-18s %(funcName)-10s %(lineno)4s: %(message)s"
    )

# コンソール用ハンドラ作成。標準出力へ出力。ログレベル：DEBUG 書式はsimpleFormatter
_consoleHandler = logging.StreamHandler(sys.stdout)
_consoleHandler.setLevel(logging.DEBUG)
_consoleHandler.setFormatter(_simpleFormatter)

# コンソール用ハンドラをルートロガーに追加
_root_logger.addHandler(_consoleHandler)

# ファイル用ハンドラ作成。ファイル名はlogging.log ログレベル:DEBUG ファイルサイズ：2M backupfile=3 encoding:utf-8
filenames = "C:\\workspace\\pycharmProject\\project01\\industrysurvey\\LogData\\logging.Log"
_fileHandler = logging.handlers.RotatingFileHandler(
    filename=filenames, maxBytes=2000000, backupCount=3, encoding="utf-8"
    )
_fileHandler.setLevel(logging.DEBUG)
_fileHandler.setFormatter(_simpleFormatter)

# ファイル用ハンドラをルートロガーに追加
_root_logger.addHandler(_fileHandler)
