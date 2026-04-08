import os
import dotenv
import yagmail

dotenv.load_dotenv()  # Load environment variables from .env file

yag = yagmail.SMTP(user=os.getenv('APP_EMAIL_FROM'), password=os.getenv('APP_PASSWORD'))

contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]


yag.send('syed.atyab.hussain@gmail.com', 'From Python Final', contents)