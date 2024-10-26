import requests
import random
import time
import os
from dotenv import load_dotenv
import warnings

warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Memuat variabel dari file .env
load_dotenv()

api_endpoints = {
    "keepalive": "https://www.aeropres.in/chromeapi/dawn/v1/userreward/keepalive",
    "getPoints": "https://www.aeropres.in/api/atom/v1/userreferral/getpoint"
}

def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅   Pesan Dikirim Ke Telegram.")
        else:
            print(f"❌ Gagal Kirim Pesan Ke Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Error sending Telegram message: {str(e)}")

def random_delay(min_seconds, max_seconds):
    delay_time = random.randint(min_seconds, max_seconds)
    time.sleep(delay_time)

def fetch_points(headers):
    try:
        response = requests.get(api_endpoints['getPoints'], headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            if data.get("status"):
                reward_point = data["data"]["rewardPoint"]
                referral_point = data["data"]["referralPoint"]
                total_points = (
                    reward_point.get("points", 0) +
                    reward_point.get("registerpoints", 0) +
                    reward_point.get("signinpoints", 0) +
                    reward_point.get("twitter_x_id_points", 0) +
                    reward_point.get("discordid_points", 0) +
                    reward_point.get("telegramid_points", 0) +
                    reward_point.get("bonus_points", 0) +
                    referral_point.get("commission", 0)
                )
                print(f"\nPoints: {total_points}")
                return total_points
            else:
                print(f"Failed to retrieve points: {data.get('message', 'Unknown error')}")
        else:
            print(f"Failed to retrieve points: Status code {response.status_code}")
    except ValueError as ve:
        print(f"Error processing JSON: {str(ve)}")
    except Exception as e:
        print(f"Error during fetching points: {str(e)}")
    return 0

def keep_alive_request(headers, email):
    payload = {
        "username": email,
        "extensionid": "fpdkjdnhkakefebpekbdhillbhonfjjp",
        "numberoftabs": 0,
        "_v": "1.0.8"
    }

    try:
        response = requests.post(api_endpoints["keepalive"], json=payload, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            if 'message' in data:
                print(f"BERHASIL: Bisa untuk {email}: {data['message']}")
                print("""
          .-""""""-.
        .' BERHASIL '.
       /   O      O   \\
      :           `    :
      |        00       |   
      :   ```______```  :
       \               /
        '.          .'
          '-......-'
                """)
                return True
        else:
            print(f"KONEKSI BURUK : GPP lanjut ae untuk {email}: {response.status_code} - {response.text}")
            print("""
          _,--''--._
       ,-'            '-.
     ,'                  '.
    /                      \\
   ;                        ;
   |  GAK BERHASIL, LANJUT AE|
   ;            GPP          ;
    \\                      /
     '.                  .'
       '-.            .-'
          '--......--'
            """)
    except Exception as e:
        print(f"Error during Keep-Alive: {str(e)}")
    return False

def countdown(seconds, message):
    for i in range(seconds, 0, -1):
        print(f"{message} in: {i} seconds...", end='\r')
        time.sleep(1)
    print("\nRestarting...\n")

def countdown_account_delay(seconds):
    for i in range(seconds, 0, -1):
        print(f"Waiting for account processing in: {i} seconds...", end='\r')
        time.sleep(1)
    print("\n")

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("ANAM BACTIAR") 
    print("GITHUB: https://github.com/bactiar291")
    print("BUY COFFEE FOR ME: 0x648dce97a403468dfc02c793c2b441193fccf77b ")
    print("=" * 50 + "\n")

def process_accounts():
    print_header()
    accounts = []
    i = 1
    while os.getenv(f'ACCOUNT_{i}_EMAIL'):
        accounts.append({
            'email': os.getenv(f'ACCOUNT_{i}_EMAIL'),
            'token': os.getenv(f'ACCOUNT_{i}_TOKEN')
        })
        i += 1

    while True:
        total_points = 0

        for account in accounts:
            email = account['email']
            token = account['token']

            headers = {
                "Accept": "*/*",
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            }

            print("_____________----------_____________-----------------______")
            print(f"Processing: {email}...")
            points = fetch_points(headers)
            total_points += points

            if points > 0:
                success = keep_alive_request(headers, email)
                if success:
                    send_telegram_message(f"{email} mendapatkan {points} poin.")
                else:
                    print(f"KONEKSI BURUK : GPP lanjut ae untuk {email}.\n")
            else:
                print(f"No points available for {email}.")
                print("_____________----------_____________-----------------______")

            countdown_account_delay(int(os.getenv("ACCOUNT_DELAY", 15)))

        print(f"All accounts processed. Total points: {total_points}")
        countdown(int(os.getenv("RESTART_DELAY", 60)), "Next process")

if __name__ == "__main__":
    process_accounts()
