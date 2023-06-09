from dotenv import load_dotenv
import os

load_dotenv('.env')
test_var = os.getenv('SECRET_KEY')
print(test_var)
