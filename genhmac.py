import hmac
import dotenv
import os

dotenv.load_dotenv()


def gen_hmac(key, msg):
    return hmac.new(key.encode('utf-8'), msg.encode('utf-8'), 'sha256').hexdigest()


def gen_all_keys(key):
    for i in range(0, 100):
        yield i, gen_hmac(key, str(i))[:5].upper()


def main():
    key = os.getenv('HMAC_KEY')
    print("id;hmac")
    for i, k in gen_all_keys(key):
        print("%d;%s" % (i, k))


if __name__ == '__main__':
    main()
