import yfinance as yf
import openai
import json


client = openai.Client()

def retorna_cotacao(ticker, periodo="1mo"):
    ticker_obj = yf.Ticker(f"{ticker}.SA")
    hist = ticker_obj.history(period=periodo)["Close"]
    hist.index = hist.index.strftime("%y-%m-%d")
    hist = round(hist, 2)
    
    # limitador 30 results
    if len(hist) > 30:
        slice_size = int(len(hist)/30)
        hist = hist.iloc[::-slice_size][::-1]
    return hist.to_json()

tools = [
    {
        "type": "function",
            "function": {
                "name": "retorna_cotacao",
                "description": "Retorna cotação da Ibovespa",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "O ticker da acai. Ex: BBSA3, BBDC4"
                        },
                        "periodo": {
                            "type": "string",
                            "description": "Periodo retornado dos dados historicos da cotaçãp \
                                sendo '1mo' equivalente a um mes, '1d' um dia e \
                                    'y1' um ano e 'ytd' equivalente a todos os tempos.",
                            "enum": ["1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "ytd", "max"]
                        }
                    }
                }
            }  
        }
]

funcao_disponivel = {"retorna_cotacao": retorna_cotacao}
mensagens = [{"role": "user", "content": "Qual é a cotação da Vale no ultimo ano?"}]

resposta = client.chat.completions.create(
    messages=mensagens,
    model="gpt-3.5-turbo-0125",
    tools=tools,
    tool_choice="auto"
)

tool_calls = resposta.choices[0].message.tool_calls

if tool_calls:
    mensagens.append(resposta.choices[0].message)
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = funcao_disponivel[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_return = function_to_call(**function_args)
        
        mensagens.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_return
            }
        )
        
        segunda_resposta = client.chat.completions.create(
            messages=mensagens,
            model="gpt-3.5-turbo-0125"
        )
        
        mensagens.append(segunda_resposta.choices[0].message)
        print(segunda_resposta.choices[0].message.content)