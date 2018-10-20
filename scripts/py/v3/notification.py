import logging

logger = logging.getLogger('telegram_logger')

class Telegram:
    @staticmethod
    def telegram_notify(message, chat_id, token):
        if chat_id is None or chat_id is "":
            return
        if token is None or token is "":
            return
        try:
            telegram_url = "https://api.telegram.org/bot{}/sendMessage".format(
                token)
            param = {"chat_id": chat_id, "text": message}
            http.post('telegram', telegram_url, params=param)
        except Exception as e:
            logger.error(
                "telegram notify error, msg:{}, exception:{}".format(message, e))
