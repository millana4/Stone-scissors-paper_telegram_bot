import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# Initialising logger
logger = logging.getLogger(__name__)

# Function is configuring and starting the bot
async def main():
    # Configuring loggers
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Displaying to console info that bot starts
    logger.info('Starting bot')

    # Loading config into variable
    config: Config = load_config()

    # Initializing bot and dispacher
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    # Parse_mode meams that HTML tags have to work
    dp = Dispatcher()

    # Registering routers in the diapacher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Leaving previous updates and polling starts
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
