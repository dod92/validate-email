# use an appropriate path to import
from email_verify import Verifier
from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

# Use socks proxy to connect over SMTP
def is_email_valid(proxy_addr, proxy_port, test_email):
    socks_verifier =  Verifier(
        source_addr='info@kawigraphics.com',
        proxy_type='socks5',
        proxy_addr=proxy_addr,
        proxy_port=proxy_port,
        proxy_username=None,
        proxy_password=None
    )
    results = socks_verifier.verify(test_email)

    print(results)


is_email_valid(env('PROXY_ADDRESS'), env.int('PROXY_PORT'), env('EMAIL_TO_TEST'))