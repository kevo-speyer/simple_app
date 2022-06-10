import flask
import requests
import pandas as pd

app = flask.Flask(__name__)

@app.route("/")
def hello():
    user = flask.request.args.get("user")
    user = user if user else "Guest"
    return f"Hello {user}!\n"

@app.route('/help')
def about():
    return 'WARAP, No help for you!!\n'

@app.route('/sum_nums')
def sum_nums():
    num_1 = flask.request.args.get('num_1')
    num_2 = flask.request.args.get('num_2')
    num_1 = int(num_1) if num_1 else 0
    num_2 = int(num_2) if num_2 else 0
    ret = f"The sum yields: {num_1+num_2}\n"
    return ret

@app.route('/max_dolar_compra')
def dolar_plot():

    def invert_date(date):
        return '-'.join(date.split('-')[::-1])

    from_date = flask.request.args.get('from')
    to_date = flask.request.args.get('to')
    from_date = invert_date(from_date) if from_date else '13-01-2022'
    to_date = invert_date(to_date) if to_date else '13-05-2022'
    
    url = f'https://mercados.ambito.com//dolar/informal/historico-general/{from_date}/{to_date}'
    r = requests.get(url=url)
    df = pd.DataFrame(r.json()[1:])
    df.columns = ['fecha','compra','venta']
    df['fecha'] = df.fecha.apply(invert_date)
    df['compra'] = df.compra.apply(lambda x: float(x.replace(",",".")))
    df['venta'] = df.venta.apply(lambda x: float(x.replace(",",".")))
    
    ret = df[df.compra==df.compra.max()].sort_values(by='fecha',ascending=False).head(1).to_dict()
    max_compra = {k: list(v.values()).pop() for k,v in ret.items()}
    return str(max_compra)


if __name__ == "__main__":
    app.run(debug=True)
