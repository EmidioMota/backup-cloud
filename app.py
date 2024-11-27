from flask import Flask, request, jsonify, render_template
from backup_script import fazer_backup

app = Flask(__name__)

# Rota principal com formulário HTML
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Backup Demo</title>
    </head>
    <body>
        <h1>Backup Demo</h1>
        <form action="/backup" method="post">
            <label for="diretorio">Diretório:</label>
            <input type="text" id="diretorio" name="diretorio" value="/app/data">
            <button type="submit">Fazer Backup</button>
        </form>
    </body>
    </html>
    '''

# Endpoint para processar o backup
@app.route('/backup', methods=['POST'])
def backup():
    diretorio = request.form.get('diretorio', '/app/data/')
    fazer_backup(diretorio)
    return jsonify({"message": f"Backup do diretório {diretorio} realizado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
