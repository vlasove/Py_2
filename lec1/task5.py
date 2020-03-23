n_eng = int(input())
m_deu = int(input())
eng = set()
deu = set()
for _ in range(n_eng):
    eng.add(input())
for _ in range(m_deu):
    deu.add(input())
print(len(eng ^ deu))