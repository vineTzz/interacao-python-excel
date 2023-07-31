# Importar Pandas e Arquivos #
import pandas as pd

funcionarios_df = pd.read_csv(r'C:\Users\alxia\OneDrive\Área de Trabalho\Integração Python + Excel\CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv(r'C:\Users\alxia\OneDrive\Área de Trabalho\Integração Python + Excel\CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel(r'C:\Users\alxia\OneDrive\Área de Trabalho\Integração Python + Excel\BaseServiçosPrestados.xlsx')

# Retirar Colunas Cargo e Estado Civil #
funcionarios_df = funcionarios_df.drop(['Cargo', 'Estado Civil'], axis=1)

print('-' * 50)
# Qual foi o gasto total com salários de funcionários pela empresa? #
funcionarios_df['Folha Salarial'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VR'] + funcionarios_df['VT']
print(f"Total Folha Salarial Mensal: {funcionarios_df['Folha Salarial'].sum() :,.2f}")

print('-' * 50)

# Qual foi o faturamento da empresa? #
faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamento_mensal = sum(faturamento_df['Valor Contrato Mensal'] * faturamento_df['Tempo Total de Contrato (Meses)'])
print(f"Total Faturamento Mensal: {faturamento_mensal :,.2f}")

print('-' * 50)

# Qual o % de funcionários que já fechou algum contrato? #
qnt_funcionarios_fecharam_contrato = len(servicos_df['ID Funcionário'].unique())
qnt_total_funcionarios = len(funcionarios_df['ID Funcionário'])
percentual_funcionarios = qnt_funcionarios_fecharam_contrato / qnt_total_funcionarios
print(f"Percentual Contratos Fechados: {percentual_funcionarios :.2%}")

print('-' * 50)

# Total de contratos que cada área da empresa já fechou #
contratos_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
total_contratos = contratos_df['Area'].value_counts()
print(f'{total_contratos}')

print('-')

# Total de funcionários por área #
funcionarios_por_area = funcionarios_df['Area'].value_counts()
print(f"{funcionarios_por_area}")

print('-' * 50)

# Qual o ticket médio mensal (faturamento médio mensal) dos contratos? #
faturamento_medio_mensal = clientes_df['Valor Contrato Mensal'].mean()
print(f'Faturamento Médio Mensal: R${faturamento_medio_mensal :,.2f}')

print('-' * 50)