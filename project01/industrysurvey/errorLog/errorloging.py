import inspect
import logging
from functools import wraps

class CustomFilter(logging.Filter):
    """
    loger用のユーザー定義フィルター
    """

    def filter(self, record):
        """
        呼び出し元のファイル名、関数名、行番号が表示される関数
        これでフィルタリングしないとデコレーターを使用した関数(呼び出し元)にかhんする
        情報ではなく、Log関数の情報が出力される。
        :param record:
        :return True:
        """
        record.real_filename = getattr(record,
                                       'real_filename',
                                       record.filename)
        record.real_funcName = getattr(record,
                                       'real_funcName',
                                       record.funcName)
        record.real_lineno = getattr(record,
                                     'real_lineno',
                                     record.lineno)
        return True


def get_logger():
    """logging.Loggerの作成

        Returns:
            logger (logging.Logger): logging.Loggerのインスタンス
        """

    log_format = '[%(asctime)s] %(levelname)s\t%(real_filename)s' \
                 ' - %(real_funcName)s:%(real_lineno)s -> %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.addFilter(CustomFilter())
    return logger

def log(logger):
    """
    デコレータでLoggerを引数とするためのラッパー関数
    Args: logger(logging.Logger)
    :param logger:
    :return _decoretaorの戻り値:
    """

    def _decorator(func):
        """
        デコレータを使用する関するを引数とする。
        Args; func (fucntion)
        :param func:
        :return Wrapparの戻り値:
        """

        # funcのパラメータを引き継ぐ
        @wraps(func)
        def wrapper(*args,**kwargs):

            func_name = func.__name__
            # loggerで使用するためにfuncに関する情報をdict化
            extra = {
                'real_filename': inspect.getfile(func),
                'real_funcName': func_name,
                'real_lineno': inspect.currentframe().f_back.f_lineno
            }

            logger.info(f'[START] {func_name}', extra=extra)

            try:
                # funcの実行
                return func(*args, **kwargs)
            except Exception as err:
                # funcのエラーハンドリング
                logging.error(err, exc_info=True, extra=extra)
                logging.error(f'[KILLED] {func_name}', extra=extra)
            else:
                logging.info(f'[END] {func_name}', extra=extra)

        return wrapper
    return _decorator