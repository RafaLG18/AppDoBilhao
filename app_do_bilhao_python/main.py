"""App do Bilhão — visualização do histórico de preços de ações.

Os dados são obtidos via yfinance (Yahoo Finance) e os gráficos são
gerados com Plotly. Execute com:

    streamlit run app_do_bilhao_python/main.py
"""

import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Períodos suportados pelo yfinance (o índice de "5y" é o padrão da barra lateral)
PERIODOS = ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
PERIODO_PADRAO = "5y"
TICKER_PADRAO = "AAPL"
CACHE_TTL_SEGUNDOS = 3600


@st.cache_data(ttl=CACHE_TTL_SEGUNDOS)
def baixar_yahoo(ticker: str, periodo: str) -> pd.DataFrame | None:
    """Baixa o histórico via yfinance e normaliza as colunas.

    Retorna ``None`` quando não há dados (ticker inexistente ou deslistado).
    """
    data = yf.download(ticker, period=periodo, progress=False)
    if data is None or data.empty:
        return None
    # yfinance retorna colunas MultiIndex (Price, Ticker) ao baixar 1 ativo
    if getattr(data.columns, "nlevels", 1) > 1:
        data.columns = data.columns.get_level_values(0)
    return data


def selecionar_parametros() -> tuple[str, str]:
    """Monta a barra lateral e devolve o ticker e o período escolhidos."""
    st.sidebar.title("Selecione o stock")

    periodo = st.sidebar.selectbox(
        "Período", PERIODOS, index=PERIODOS.index(PERIODO_PADRAO)
    )
    ticker = st.sidebar.text_input("stock", TICKER_PADRAO, max_chars=10).strip().upper()
    st.sidebar.caption("Ações da B3 precisam do sufixo .SA (ex.: PETR4.SA).")

    return ticker, periodo


def exibir_historico(ticker: str, data: pd.DataFrame) -> None:
    """Mostra a tabela e o gráfico de fechamento do ativo."""
    st.subheader("Histórico")
    st.dataframe(data)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"], name="Fechamento"))
    fig.update_layout(title=ticker, xaxis_title="Date", yaxis_title="Preço")
    st.plotly_chart(fig)


def main() -> None:
    """Ponto de entrada do app."""
    st.title("Stock History App")

    ticker, periodo = selecionar_parametros()

    if not ticker:
        st.info("Digite um ticker na barra lateral para começar.")
        st.stop()

    try:
        data = baixar_yahoo(ticker, periodo)
    except Exception as erro:
        st.error(f"Não foi possível baixar os dados de '{ticker}': {erro}")
        st.stop()

    # Quando o ticker não existe (ou está deslistado), o retorno vem vazio
    if data is None or data.empty:
        st.warning(
            f"Nenhum dado encontrado para '{ticker}'. "
            "Verifique o ticker (ações da B3 usam o sufixo .SA, ex.: TAEE11.SA)."
        )
        st.stop()

    exibir_historico(ticker, data)


if __name__ == "__main__":
    main()
