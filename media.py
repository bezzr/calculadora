def calcular_media():
    print("--- Calculadora de Média ---")
    
    # Lista para armazenar as notas
    notas = []
    
    while True:
        entrada = input("Digite a nota (ou digite 's' para sair e calcular): ")
        
        if entrada.lower() == 's':
            break
            
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Valor inválido! Digite um número ou 's' para sair.")
            
    if not notas:
        print("Nenhuma nota foi informada.")
        return

    # Cálculo da média
    media = sum(notas) / len(notas)
    
    print("\n--- Resultado ---")
    print(f"Total de notas informadas: {len(notas)}")
    print(f"Média final: {media:.2f}")
    
    # Condição de aprovação (exemplo com média 6.0)
    if media >= 6.0:
        print("Situação: **Aprovado(a)!** 🎉")
    else:
        print("Situação: **Reprovado(a).** 📚")

# Executa a função
calcular_media()