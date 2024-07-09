import unittest
from password_manager import add_password, get_password, delete_password, list_passwords, load_passwords, save_passwords
import os

def setUp(self):
    # Sample data to be used in tests
    self.test_data = {'test_service': 'test_password'}
    # Encrypt the sample data and write it to storage.json
    self.encrypt_and_write_test_data(self.test_data)

def encrypt_and_write_test_data(self, data):
    # Convert the data dictionary to a JSON string and encode it
    data_str = json.dumps(data).encode()
    # Encrypt the data using your application's encryption logic
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data_str, AES.block_size))
    iv = cipher.iv
    # Prepare the encrypted data for storage
    encrypted_data = {
        'iv': base64.b64encode(iv).decode('utf-8'),
        'ciphertext': base64.b64encode(ct_bytes).decode('utf-8')
    }
    # Write the encrypted data to the storage file
    with open(STORAGE_FILE, 'w') as file:
        json.dump(encrypted_data, file)

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        # Ensure a clean state before each test
        self.test_service = 'test_service'
        self.test_password = 'test_password'
        if os.path.exists('storage.json'):
            os.remove('storage.json')

    def test_add_password(self):
        add_password(self.test_service, self.test_password)
        passwords = load_passwords()
        self.assertIn(self.test_service, passwords)
        self.assertEqual(passwords[self.test_service], self.test_password)

    def test_get_password(self):
        add_password(self.test_service, self.test_password)
        retrieved_password = get_password(self.test_service)
        self.assertEqual(retrieved_password, self.test_password)

    def test_delete_password(self):
        add_password(self.test_service, self.test_password)
        delete_password(self.test_service)
        passwords = load_passwords()
        self.assertNotIn(self.test_service, passwords)

    def test_list_services(self):
        services_to_add = ['service1', 'service2', 'service3']
        for service in services_to_add:
            add_password(service, self.test_password)
        services_list = list_passwords()
        self.assertEqual(set(services_list), set(services_to_add))

    def tearDown(self):
        # Clean up after each test
        if os.path.exists('storage.json'):
            os.remove('storage.json')

if __name__ == '__main__':
    unittest.main()