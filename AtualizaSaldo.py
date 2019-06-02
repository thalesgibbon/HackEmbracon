import pickle


class AtualizaSaldo(object):
    def __init__(self, user_id, pontos):
        self.status = self.atualiza(user=user_id, pt=pontos)

    def atualiza(self, user, pt):
        user = int(user)
        pt = int(pt)

        with open('db.pkl', 'rb') as handle:
            pkl = pickle.load(handle)

        if user in pkl.keys():
            pkl[user] = pkl[user] + pt
        else:
            pkl[user] = pt

        with open('db.pkl', 'wb') as handle:
            pickle.dump(pkl, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return "ok"


if __name__ == '__main__':
    x = AtualizaSaldo(0, 10)
    print(x.saldo_atual)
