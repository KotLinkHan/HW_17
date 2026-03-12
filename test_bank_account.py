import unittest
from bank_account import BankAccount, InsufficientFunds


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(initial_balance=100)
        self.other_account = BankAccount(initial_balance=50)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_success(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_deposit_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.deposit("100")

    def test_withdraw_success(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFunds):
            self.account.withdraw(200)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_transfer_success(self):
        self.account.transfer(self.other_account, 30)
        self.assertEqual(self.account.get_balance(), 70)
        self.assertEqual(self.other_account.get_balance(), 80)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(InsufficientFunds):
            self.account.transfer(self.other_account, 500)

    def test_transfer_invalid_target(self):
        with self.assertRaises(TypeError):
            self.account.transfer("not_an_account", 10)

if __name__ == '__main__':
    unittest.main()