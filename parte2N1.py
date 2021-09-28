def criarUsuario():
    novoUsuario = {}
    novoUsuario["nome"] = input("Digite o nome completo do usuario: ")
    novoUsuario["email"] = input("Digite o email do usuario: ")
    return novoUsuario

def exibirNomesUsuarios(listaOrdem : list):
    for usuarioOrdem in listaOrdem:
        print(usuarioOrdem)

def main():
    listaUsuarios = []
    
    listaUsuarios.append(criarUsuario())
    listaUsuarios.append(criarUsuario())
    listaUsuarios.append(criarUsuario())

    exibirNomesUsuarios(listaUsuarios)

if __name__ == "__main__":
    main()