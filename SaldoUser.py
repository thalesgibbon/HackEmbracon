import pickle


class SaldoUser(object):
    def __init__(self, user_id):
        self.saldo_atual = self.consulta(user=user_id)

    def consulta(self, user):
        user = int(user)

        with open('db.pkl', 'rb') as handle:
            pkl = pickle.load(handle)

        if user in pkl.keys():
            return pkl[user]
        else:
            return 0


if __name__ == '__main__':
    x = SaldoUser(0)
    print(x.saldo_atual)
