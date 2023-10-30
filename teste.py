from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name)

# Nome da planilha Excel
excel_file = 'emprestimos.xlsx'

@app.route('/')
def formulario():
    return render_template('form.html')

@app.route('/processar', methods=['POST'])
def processar():
    dados = {
        'Nome do Aluno': request.form['nome_aluno'],
        'Nome do Livro': request.form['nome_livro'],
        'Autor do Livro': request.form['autor_livro'],
        'Data do Empréstimo': request.form['data_emprestimo'],
        'Telefone do Aluno': request.form['telefone_aluno']
    }

    # Carregar dados existentes, se houver
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        df = pd.DataFrame()

    # Adicionar os novos dados ao DataFrame e salvar na planilha
    df = df.append(dados, ignore_index=True)
    df.to_excel(excel_file, index=False)

    return "Dados inseridos com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
